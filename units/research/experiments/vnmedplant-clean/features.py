"""Trich dac trung anh. 'tiny' (thumbnail 16x16, khong can GPU, dung de test) hoac 'dinov2' (can torch + transformers)."""
from pathlib import Path

import numpy as np
from PIL import Image, ImageOps

DINO_MODEL = "facebook/dinov2-small"  # ponytail: ban nho; doi sang -base/-large neu GPU du.


def _tiny(path):
    with Image.open(path) as im:
        im = ImageOps.exif_transpose(im).convert("RGB").resize((16, 16), Image.BILINEAR)
    return np.asarray(im, dtype=np.float32).ravel() / 255.0


def _dinov2(paths, batch=64):
    import torch
    from transformers import AutoImageProcessor, AutoModel

    dev = "cuda" if torch.cuda.is_available() else "cpu"
    proc = AutoImageProcessor.from_pretrained(DINO_MODEL)
    model = AutoModel.from_pretrained(DINO_MODEL).to(dev).eval()
    out = []
    for i in range(0, len(paths), batch):
        ims = []
        for p in paths[i:i + batch]:
            with Image.open(p) as im:
                ims.append(ImageOps.exif_transpose(im).convert("RGB"))
        with torch.no_grad():
            x = proc(images=ims, return_tensors="pt").to(dev)
            out.append(model(**x).last_hidden_state[:, 0].float().cpu().numpy())
    return np.concatenate(out)


def extract(paths, backend):
    if backend == "tiny":
        return np.stack([_tiny(p) for p in paths])
    if backend == "dinov2":
        return _dinov2(paths)
    raise ValueError(f"backend khong hop le: {backend}")


def load_or_extract(root, rel_paths, backend, cache):
    """Cache .npz; dung lai neu danh sach path khong doi. Xoa cache khi du lieu doi."""
    cache = Path(cache)
    rel = np.array(rel_paths)
    if cache.exists():
        z = np.load(cache)
        if np.array_equal(z["paths"], rel):
            return z["feats"]
    feats = extract([Path(root) / p for p in rel_paths], backend)
    np.savez(cache, paths=rel, feats=feats)
    return feats
