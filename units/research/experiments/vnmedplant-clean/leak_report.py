"""Buoc 3: bao cao ro ri. Dem anh test co anh CUNG CUM trong train (va train+val), cho tung kieu split va seed.
Split theo cum phai cho ket qua 0; split ngau nhien cho so > 0 = muc do ro ri.
Ghi leak_report.csv (tong hop) va leak_per_class.csv (split ngau nhien, theo loai).
"""
import argparse
import sys
from collections import Counter
from pathlib import Path

import common


def leak(rows, col):
    """Tra ve (n_test, n_leak_train, n_leak_trainval, {class: (n_test, n_leak)})."""
    train, trval = set(), set()
    for r in rows:
        if r[col] == "train":
            train.add(r["cluster_id"])
        if r[col] in ("train", "val"):
            trval.add(r["cluster_id"])
    n = lt = ltv = 0
    per = {}
    for r in rows:
        if r[col] != "test":
            continue
        n += 1
        a = r["cluster_id"] in train
        lt += a
        ltv += r["cluster_id"] in trval
        c = per.setdefault(r["class"], [0, 0])
        c[0] += 1
        c[1] += a
    return n, lt, ltv, per


def main(argv=None):
    common.utf8_stdout()
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--splits-dir", required=True, help="thu muc co splits_seed*.csv")
    ap.add_argument("--out", help="mac dinh = --splits-dir")
    a = ap.parse_args(argv)
    d = Path(a.splits_dir)
    out = Path(a.out) if a.out else d
    files = sorted(d.glob("splits_seed*.csv"))
    if not files:
        sys.exit(f"khong co splits_seed*.csv trong {d}")
    summ, perc = [], Counter()
    tot = Counter()
    for f in files:
        seed = f.stem.replace("splits_seed", "")
        rows = common.read_csv(f)
        for col in ("split_random", "split_cluster"):
            n, lt, ltv, per = leak(rows, col)
            summ.append({"seed": seed, "split": col.replace("split_", ""), "n_test": n, "n_leak_train": lt,
                         "leak_train_rate": round(lt / n, 6) if n else 0, "n_leak_train_val": ltv,
                         "leak_train_val_rate": round(ltv / n, 6) if n else 0})
            if col == "split_random":
                for c, (nt, nl) in per.items():
                    perc[c] += nl
                    tot[c] += nt
    common.write_csv(out / "leak_report.csv", summ, list(summ[0]))
    common.write_csv(out / "leak_per_class.csv",
                     [{"class": c, "n_test_all_seeds": tot[c], "n_leak_all_seeds": perc[c],
                       "leak_rate": round(perc[c] / tot[c], 6)} for c in sorted(tot)],
                     ["class", "n_test_all_seeds", "n_leak_all_seeds", "leak_rate"])
    print("seed split   n_test  leak_train  rate    leak_train+val  rate")
    for s in summ:
        print(f"{s['seed']:<4} {s['split']:<8} {s['n_test']:>6} {s['n_leak_train']:>10}  {s['leak_train_rate']:.4f}  "
              f"{s['n_leak_train_val']:>14}  {s['leak_train_val_rate']:.4f}")
    return summ


if __name__ == "__main__":
    main()
