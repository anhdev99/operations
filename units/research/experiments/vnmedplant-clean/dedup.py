"""Buoc 1: khu trung. Quet <root>/<loai>/**/*.jpg|png, gom anh thanh cum (union-find).

Canh noi 2 anh: SHA-256 bang nhau (trung chinh xac), hoac pHash Hamming <= --phash-thr,
hoac (tuy chon, --dino) cosine DINOv2 >= --cos-thr. Mac dinh chi so sanh trong cung loai;
--cross-class de bat ca anh trung giua cac loai (nghi sai nhan).
"""
import argparse
import hashlib
import json
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np
from PIL import Image, ImageOps

import common
import features

EXTS = {".jpg", ".jpeg", ".png"}
_DCT = None


def _dct_matrix(n=32):
    k = np.arange(n)[:, None]
    m = np.cos(np.pi * (2 * np.arange(n)[None, :] + 1) * k / (2 * n))
    m[0] *= 1 / np.sqrt(2)
    return m * np.sqrt(2 / n)


def phash(path):
    """pHash 64 bit (DCT 32x32 -> khoi 8x8 thap tan, nguong = median). Tra ve int."""
    global _DCT
    if _DCT is None:
        _DCT = _dct_matrix()
    with Image.open(path) as im:
        im.draft("L", (64, 64))  # ponytail: giai ma JPEG thu nho cho nhanh; doi neu can bit-chinh-xac.
        g = ImageOps.exif_transpose(im).convert("L").resize((32, 32), Image.LANCZOS)
    a = np.asarray(g, dtype=np.float64)
    low = (_DCT @ a @ _DCT.T)[:8, :8].ravel()
    bits = low > np.median(low)
    return int("".join("1" if b else "0" for b in bits), 2)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for blk in iter(lambda: f.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()


def scan(root):
    root = Path(root)
    items = []
    for cdir in sorted(p for p in root.iterdir() if p.is_dir()):
        for p in sorted(cdir.rglob("*")):
            if p.is_file() and p.suffix.lower() in EXTS:
                items.append((p.relative_to(root).as_posix(), cdir.name))
    return items


class UF:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            self.p[max(a, b)] = min(a, b)  # goc = chi so nho nhat -> cluster_id on dinh


def clusters(n, edges):
    uf = UF(n)
    for a, b in edges:
        uf.union(int(a), int(b))
    roots = [uf.find(i) for i in range(n)]
    ids = {r: k for k, r in enumerate(sorted(set(roots)))}
    return [ids[r] for r in roots]


def groups(classes, cross):
    if cross:
        return [np.arange(len(classes))]
    d = {}
    for i, c in enumerate(classes):
        d.setdefault(c, []).append(i)
    return [np.array(v) for v in d.values()]


def phash_edges(h, grp, maxd):
    """Tra ve (i, j, hamming) cho moi cap trong grp co hamming <= maxd. h: uint64."""
    out = []
    for k in range(len(grp) - 1):
        i = grp[k]
        rest = grp[k + 1:]
        d = np.bitwise_count(h[rest] ^ h[i])
        for j, dv in zip(rest[d <= maxd], d[d <= maxd]):
            out.append((i, j, int(dv)))
    return out


def cos_edges(f, grp, mincos, chunk=2048):
    out = []
    for s in range(0, len(grp), chunk):
        a = grp[s:s + chunk]
        sim = f[a] @ f[grp].T
        ii, jj = np.nonzero(sim >= mincos)
        for x, y in zip(ii, jj):
            i, j = a[x], grp[y]
            if i < j:
                out.append((i, j, float(sim[x, y])))
    return out


def main(argv=None):
    common.utf8_stdout()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", required=True, help="thu muc anh: <root>/<loai>/*.jpg|png")
    ap.add_argument("--out", required=True, help="thu muc output (nen NGOAI git)")
    ap.add_argument("--phash-thr", type=int, default=8, help="nguong Hamming dung de gom cum (mac dinh 8)")
    ap.add_argument("--phash-list", type=int, nargs="+", default=[0, 2, 4, 6, 8, 10, 12],
                    help="cac nguong Hamming de thong ke ti le trung")
    ap.add_argument("--dino", action="store_true", help="them canh cosine tren dac trung DINOv2 (can torch, transformers)")
    ap.add_argument("--cos-thr", type=float, default=0.95)
    ap.add_argument("--cos-list", type=float, nargs="+", default=[0.90, 0.92, 0.95, 0.97, 0.99])
    ap.add_argument("--cross-class", action="store_true", help="so sanh ca giua cac loai (cham hon)")
    ap.add_argument("--workers", type=int, default=8)
    a = ap.parse_args(argv)

    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    items = scan(a.root)
    if not items:
        sys.exit(f"Khong thay anh trong {a.root} (can dang <root>/<loai>/*.jpg|png)")
    root = Path(a.root)

    def one(it):
        p = root / it[0]
        try:
            return sha256(p), phash(p)
        except Exception as e:  # anh hong: ghi lai, khong dung ca pipeline
            return None, str(e)

    with ThreadPoolExecutor(a.workers) as ex:
        res = list(ex.map(one, items))
    bad = [(it[0], r[1]) for it, r in zip(items, res) if r[0] is None]
    if bad:
        common.write_csv(out / "unreadable.csv", [{"path": p, "error": e} for p, e in bad], ["path", "error"])
        print(f"CANH BAO: {len(bad)} anh khong doc duoc, bo qua (xem unreadable.csv)")
    keep_idx = [i for i, r in enumerate(res) if r[0] is not None]
    items = [items[i] for i in keep_idx]
    shas = [res[i][0] for i in keep_idx]
    ph = np.array([res[i][1] for i in keep_idx], dtype=np.uint64)
    paths = [it[0] for it in items]
    classes = [it[1] for it in items]
    n = len(paths)

    sha_edges = []
    first = {}
    for i, s in enumerate(shas):
        if s in first:
            sha_edges.append((first[s], i))
        else:
            first[s] = i

    grps = groups(classes, a.cross_class)
    pe = [e for g in grps for e in phash_edges(ph, g, max(a.phash_list + [a.phash_thr]))]

    ce = []
    if a.dino:
        f = features.extract([root / p for p in paths], "dinov2")
        f = f / np.linalg.norm(f, axis=1, keepdims=True)
        ce = [e for g in grps for e in cos_edges(f, g, min(a.cos_list + [a.cos_thr]))]

    main_edges = sha_edges + [(i, j) for i, j, d in pe if d <= a.phash_thr] + [(i, j) for i, j, c in ce if c >= a.cos_thr]
    cid = clusters(n, main_edges)
    seen = set()
    keep = []
    for c in cid:
        keep.append(0 if c in seen else 1)
        seen.add(c)

    rows = [{"path": paths[i], "class": classes[i], "sha256": shas[i], "phash": f"{int(ph[i]):016x}",
             "cluster_id": cid[i], "keep": keep[i]} for i in range(n)]
    common.write_csv(out / "images.csv", rows, ["path", "class", "sha256", "phash", "cluster_id", "keep"])

    stat = [{"method": "sha256", "threshold": "exact", "n_before": n,
             "n_after": len(set(clusters(n, sha_edges)))}]
    for t in sorted(set(a.phash_list)):
        stat.append({"method": "phash", "threshold": t, "n_before": n,
                     "n_after": len(set(clusters(n, sha_edges + [(i, j) for i, j, d in pe if d <= t])))})
    if a.dino:
        for t in sorted(set(a.cos_list)):
            stat.append({"method": "dinov2_cos", "threshold": t, "n_before": n,
                         "n_after": len(set(clusters(n, sha_edges + [(i, j) for i, j, c in ce if c >= t])))})
    for s in stat:
        s["dup_rate"] = round(1 - s["n_after"] / n, 6)
    common.write_csv(out / "dedup_thresholds.csv", stat, ["method", "threshold", "n_before", "n_after", "dup_rate"])

    before, after = Counter(classes), Counter(c for c, k in zip(classes, keep) if k)
    per = [{"class": c, "n_before": before[c], "n_after": after[c],
            "dup_rate": round(1 - after[c] / before[c], 6)} for c in sorted(before)]
    common.write_csv(out / "dedup_per_class.csv", per, ["class", "n_before", "n_after", "dup_rate"])

    summary = {"root": str(a.root), "n_images": n, "n_classes": len(before), "n_unreadable": len(bad),
               "phash_thr": a.phash_thr, "dino": a.dino, "cos_thr": a.cos_thr if a.dino else None,
               "cross_class": a.cross_class, "n_clusters": len(set(cid)), "n_exact_dup": len(sha_edges),
               "dup_rate": round(1 - len(set(cid)) / n, 6)}
    (out / "dedup_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    print("method      threshold  n_after  dup_rate")
    for s in stat:
        print(f"{s['method']:<11} {s['threshold']!s:<9} {s['n_after']:>8}  {s['dup_rate']:.4f}")
    return summary


if __name__ == "__main__":
    main()
