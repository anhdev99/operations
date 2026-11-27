"""Buoc 4: khung baseline linear probe tren dac trung da trich. Danh gia top-1 va macro-F1 cho 2 kieu split x cac seed.
Chi so chinh: do chenh (random - cluster) cua top-1 tren tap test, trung binh +- do lech chuan qua cac seed.
Ghi baseline_results.csv va baseline_gap.csv.
"""
import argparse
from pathlib import Path

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.preprocessing import StandardScaler

import common
import features


def run(X, y, split, seed):
    tr, te = split == "train", split == "test"
    sc = StandardScaler().fit(X[tr])
    clf = LogisticRegression(max_iter=1000, random_state=seed).fit(sc.transform(X[tr]), y[tr])
    p = clf.predict(sc.transform(X[te]))
    return accuracy_score(y[te], p), f1_score(y[te], p, average="macro", zero_division=0), int(te.sum())


def main(argv=None):
    common.utf8_stdout()
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", required=True)
    ap.add_argument("--splits-dir", required=True, help="thu muc co splits_seed*.csv (tu split.py)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--backend", choices=["tiny", "dinov2"], default="dinov2",
                    help="tiny = thumbnail 16x16 (chi de test); dinov2 = can torch + transformers, tu dung GPU neu co")
    a = ap.parse_args(argv)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    files = sorted(Path(a.splits_dir).glob("splits_seed*.csv"))
    rows0 = common.read_csv(files[0])
    paths = [r["path"] for r in rows0]
    X = features.load_or_extract(a.root, paths, a.backend, out / f"features_{a.backend}.npz")
    res = []
    for f in files:
        seed = int(f.stem.replace("splits_seed", ""))
        rows = common.read_csv(f)
        idx = {r["path"]: r for r in rows}
        assert list(idx) == paths, "cac seed phai dung cung danh sach anh"
        y = np.array([idx[p]["class"] for p in paths])
        for kind in ("random", "cluster"):
            sp = np.array([idx[p][f"split_{kind}"] for p in paths])
            acc, f1, n = run(X, y, sp, seed)
            res.append({"seed": seed, "split": kind, "n_test": n, "top1": round(acc, 6), "macro_f1": round(f1, 6)})
    common.write_csv(out / "baseline_results.csv", res, list(res[0]))

    gap = []
    for m in ("top1", "macro_f1"):
        r = np.array([x[m] for x in res if x["split"] == "random"])
        c = np.array([x[m] for x in res if x["split"] == "cluster"])
        d = r - c
        gap.append({"metric": m, "random_mean": round(float(r.mean()), 6), "cluster_mean": round(float(c.mean()), 6),
                    "gap_mean": round(float(d.mean()), 6), "gap_std": round(float(d.std(ddof=1)), 6) if len(d) > 1 else 0})
    common.write_csv(out / "baseline_gap.csv", gap, list(gap[0]))
    for x in res:
        print(x)
    for g in gap:
        print(g)
    return res, gap


if __name__ == "__main__":
    main()

