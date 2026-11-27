"""Buoc 2: chia train/val/test theo cum (khong cum nao o 2 tap), phan tang theo loai, co seed.
Dong thoi tao split ngau nhien theo anh (cung ti le, cung phan tang) de so sanh.
Ghi splits_seed<S>.csv: path, class, cluster_id, split_cluster, split_random.
"""
import argparse
import random
from collections import defaultdict
from pathlib import Path

import common

NAMES = common.SPLITS


def cluster_split(rows, ratios, rng):
    """rows: list dict. Tra ve {path: split}. Moi loai chia rieng, cum lon xep truoc, chon tap thieu nhieu nhat so voi muc tieu."""
    by_cls = defaultdict(lambda: defaultdict(list))
    for r in rows:
        by_cls[r["class"]][r["cluster_id"]].append(r["path"])
    out = {}
    for cls in sorted(by_cls):
        cl = list(by_cls[cls].values())
        rng.shuffle(cl)
        cl.sort(key=len, reverse=True)  # sort on dinh: hoa giua cac cum bang nhau van la thu tu ngau nhien
        total = sum(len(c) for c in cl)
        target = [total * r for r in ratios]
        cur = [0, 0, 0]
        for c in cl:
            k = max(range(3), key=lambda i: (target[i] - cur[i]) / target[i] if target[i] else -1)
            cur[k] += len(c)
            for p in c:
                out[p] = NAMES[k]
    return out


def random_split(rows, ratios, rng):
    by_cls = defaultdict(list)
    for r in rows:
        by_cls[r["class"]].append(r["path"])
    out = {}
    for cls in sorted(by_cls):
        ps = sorted(by_cls[cls])
        rng.shuffle(ps)
        n = len(ps)
        n_val, n_test = round(n * ratios[1]), round(n * ratios[2])
        if n >= 3:
            n_val, n_test = max(n_val, 1), max(n_test, 1)
        for i, p in enumerate(ps):
            out[p] = "test" if i < n_test else "val" if i < n_test + n_val else "train"
    return out


def main(argv=None):
    common.utf8_stdout()
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--images", required=True, help="images.csv tu dedup.py")
    ap.add_argument("--out", required=True)
    ap.add_argument("--seeds", type=int, nargs="+", default=[0, 1, 2])
    ap.add_argument("--ratios", type=float, nargs=3, default=[0.8, 0.1, 0.1], metavar=("TRAIN", "VAL", "TEST"))
    ap.add_argument("--keep-one", action="store_true", help="chi dung anh dai dien moi cum (keep=1) cho CA HAI kieu split")
    a = ap.parse_args(argv)
    if abs(sum(a.ratios) - 1) > 1e-6:
        raise SystemExit("ratios phai co tong = 1")

    rows = common.read_csv(a.images)
    if a.keep_one:
        rows = [r for r in rows if r["keep"] == "1"]
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    fields = ["path", "class", "cluster_id", "split_cluster", "split_random"]
    for s in a.seeds:
        sc = cluster_split(rows, a.ratios, random.Random(f"cluster-{s}"))
        sr = random_split(rows, a.ratios, random.Random(f"random-{s}"))
        common.write_csv(out / f"splits_seed{s}.csv",
                         [{"path": r["path"], "class": r["class"], "cluster_id": r["cluster_id"],
                           "split_cluster": sc[r["path"]], "split_random": sr[r["path"]]} for r in rows], fields)
        print(f"seed {s}: {len(rows)} anh -> {out / f'splits_seed{s}.csv'}")


if __name__ == "__main__":
    main()
