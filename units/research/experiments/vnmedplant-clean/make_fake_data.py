"""Sinh du lieu GIA (anh tong hop, khong phai anh that). Moi loai co 'goc' la mot anh nhieu ngau nhien co cau truc
rieng cua loai; bien the: ban sao chinh xac, resize, nen JPEG thap, crop nhe, va anh doc lap (khong trung).
Tra ve ground truth: {ten_tep: id_nhom_goc}.
"""
import argparse
import json
import shutil
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter


def base_image(rng, size=256):
    """Anh nhieu thap tan (blob) mau ngau nhien -> pHash on dinh, moi goc khac han nhau."""
    small = rng.integers(0, 256, (8, 8, 3), dtype=np.uint8)
    return Image.fromarray(small).resize((size, size), Image.BICUBIC).filter(ImageFilter.GaussianBlur(2))


def make(root, n_classes=4, n_groups=12, seed=0):
    rng = np.random.default_rng(seed)
    root = Path(root)
    if root.exists():
        shutil.rmtree(root)
    truth = {}  # path tuong doi -> group id; kind -> list path
    kinds = {"exact": [], "resize": [], "jpeg": [], "crop": []}
    for c in range(n_classes):
        d = root / f"loai_{c:02d}"
        d.mkdir(parents=True)
        for g in range(n_groups):
            gid = f"{c}-{g}"
            im = base_image(rng)
            name = f"g{g:02d}_orig.png" if g % 2 else f"g{g:02d}_orig.jpg"
            im.save(d / name, quality=95) if name.endswith("jpg") else im.save(d / name)
            truth[f"{d.name}/{name}"] = gid
            if g % 4 == 0:  # ban sao chinh xac, ten khac
                shutil.copy(d / name, d / f"g{g:02d}_copy{Path(name).suffix}")
                truth[f"{d.name}/g{g:02d}_copy{Path(name).suffix}"] = gid
                kinds["exact"].append(f"{d.name}/g{g:02d}_copy{Path(name).suffix}")
            if g % 4 == 1:  # resize
                p = d / f"g{g:02d}_resize.jpg"
                im.resize((160, 160), Image.LANCZOS).save(p, quality=90)
                truth[f"{d.name}/{p.name}"] = gid
                kinds["resize"].append(f"{d.name}/{p.name}")
            if g % 4 == 2:  # nen JPEG manh
                p = d / f"g{g:02d}_jpeg.jpg"
                im.save(p, quality=20)
                truth[f"{d.name}/{p.name}"] = gid
                kinds["jpeg"].append(f"{d.name}/{p.name}")
            if g % 4 == 3:  # crop nhe 2% moi canh
                p = d / f"g{g:02d}_crop.jpg"
                m = int(256 * 0.02)
                im.crop((m, m, 256 - m, 256 - m)).save(p, quality=90)
                truth[f"{d.name}/{p.name}"] = gid
                kinds["crop"].append(f"{d.name}/{p.name}")
    return truth, kinds


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--classes", type=int, default=4)
    ap.add_argument("--groups", type=int, default=12)
    ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args()
    t, k = make(a.out, a.classes, a.groups, a.seed)
    (Path(a.out).parent / "truth.json").write_text(json.dumps({"truth": t, "kinds": k}), encoding="utf-8")
    print(f"{len(t)} anh gia -> {a.out}")

