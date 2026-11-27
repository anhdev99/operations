"""Kiem thu tren du lieu gia. Chay: python test_pipeline.py  (hoac: python -m pytest, khong bat buoc)."""
import tempfile
from pathlib import Path

import baseline
import common
import dedup
import leak_report
import make_fake_data
import split


def test_all():
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        root, out = tmp / "data", tmp / "out"
        truth, kinds = make_fake_data.make(root, n_classes=4, n_groups=16, seed=0)

        s = dedup.main(["--root", str(root), "--out", str(out), "--phash-thr", "8"])
        rows = common.read_csv(out / "images.csv")
        cid = {r["path"]: r["cluster_id"] for r in rows}
        assert len(rows) == len(truth)

        # 1) dedup bat dung: anh cung goc -> cung cum; anh khac goc -> khac cum
        by_gid = {}
        for p, g in truth.items():
            by_gid.setdefault(g, set()).add(cid[p])
        assert all(len(v) == 1 for v in by_gid.values()), "co bien the khong bi gom vao cum goc"
        assert len({next(iter(v)) for v in by_gid.values()}) == len(by_gid), "hai goc khac nhau bi gom nham"
        # 2) tung loai bien the deu bat duoc, ban sao chinh xac cung sha256
        sha = {r["path"]: r["sha256"] for r in rows}
        assert kinds["exact"] and all(len({sha[p], sha[p.replace("_copy", "_orig")]}) == 1
                                      for p in kinds["exact"] if p.replace("_copy", "_orig") in sha)
        assert s["n_clusters"] == len(by_gid)
        assert s["n_exact_dup"] == len(kinds["exact"])

        # 3) split theo cum khong ro ri; split ngau nhien co ro ri
        split.main(["--images", str(out / "images.csv"), "--out", str(out), "--seeds", "0", "1", "2",
                    "--ratios", "0.5", "0.25", "0.25"])
        for seed in (0, 1, 2):
            sp = common.read_csv(out / f"splits_seed{seed}.csv")
            where = {}
            for r in sp:
                where.setdefault(r["cluster_id"], set()).add(r["split_cluster"])
            assert all(len(v) == 1 for v in where.values()), "cum nam o nhieu tap"
            assert {r["split_cluster"] for r in sp} == {"train", "val", "test"}
        # tai lap theo seed
        a = (out / "splits_seed0.csv").read_text(encoding="utf-8")
        split.main(["--images", str(out / "images.csv"), "--out", str(tmp / "out2"), "--seeds", "0",
                    "--ratios", "0.5", "0.25", "0.25"])
        assert a == (tmp / "out2" / "splits_seed0.csv").read_text(encoding="utf-8"), "seed khong tai lap"

        rep = leak_report.main(["--splits-dir", str(out)])
        assert all(r["n_leak_train"] == 0 for r in rep if r["split"] == "cluster")
        assert sum(r["n_leak_train"] for r in rep if r["split"] == "random") > 0, "split ngau nhien phai ro ri tren du lieu gia"

        # 4) baseline chay duoc (backend tiny), cho ra do chenh
        res, gap = baseline.main(["--root", str(root), "--splits-dir", str(out), "--out", str(out), "--backend", "tiny"])
        assert len(res) == 6 and gap[0]["metric"] == "top1"
    print("PASS: tat ca kiem thu")


if __name__ == "__main__":
    test_all()
