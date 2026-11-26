"""ViMeLeaf audit (RES-42): per-class/source counts, resolution, format, EXIF/camera/GPS-flag, capture dates.

Run:  python audit_dataset.py [--root E:\\ViMeLeaf_Dataset] [--out audit]   (needs: pip install pillow)
No randomness (no seed): full pass over manifest.csv, deterministic output.
Dataset is read-only: files are only opened for header/EXIF reading. GPS is reduced to a yes/no flag;
no coordinates are ever read into output. Video/HEIC are counted by extension only (no decode).
Not de-duplication (RES-28): dup_group is ignored here.
"""
import argparse, csv, re
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from PIL import Image

HERE = Path(__file__).parent
AUX = {"supplement_v1", "supplement_v2"}  # tập phụ, không công bố
SOURCES = ["raw_angiang", "raw_dongthap", "raw_tayninh", "review_conflict", "supplement_v1", "supplement_v2"]
EXIF_IFD, GPS_IFD, DTO, DT, MAKE, MODEL = 0x8769, 0x8825, 36867, 306, 271, 272


def clean(s):
    return re.sub(r"\s+", " ", str(s).replace("\x00", "")).strip()


def probe(path):
    """-> (w, h, fmt, has_exif, make, model, has_gps, date 'YYYY-MM-DD' or '')"""
    try:
        with Image.open(path) as im:
            w, h, fmt = im.width, im.height, im.format
            ex = im.getexif()
            make, model = clean(ex.get(MAKE, "")), clean(ex.get(MODEL, ""))
            dt = clean(ex.get_ifd(EXIF_IFD).get(DTO, "") or ex.get(DT, ""))
            gps = len(ex.get_ifd(GPS_IFD)) > 0
            m = re.match(r"(\d{4}):(\d\d):(\d\d)", dt)
            date = f"{m[1]}-{m[2]}-{m[3]}" if m and "2000" <= m[1] <= "2030" and m[1] != "0000" else ""
            return w, h, fmt, bool(ex), make, model, gps, date
    except Exception:
        return None


def write(path, header, rows):
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def pct(a, b):
    return f"{100 * a / b:.1f}" if b else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=r"E:\ViMeLeaf_Dataset")
    ap.add_argument("--out", default=str(HERE / "audit"))
    ap.add_argument("--workers", type=int, default=16)
    a = ap.parse_args()
    root, out = Path(a.root), Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    man = list(csv.DictReader(open(root / "manifest.csv", encoding="utf-8-sig")))
    tax = {r["folder"]: r for r in csv.DictReader(open(HERE / "taxonomy.csv", encoding="utf-8-sig"))}
    imgs = [r for r in man if r["media_type"] == "image"]
    print(f"manifest {len(man)} rows, {len(imgs)} images")

    with ThreadPoolExecutor(a.workers) as ex:
        res = list(ex.map(lambda r: probe(root / r["path"]), imgs, chunksize=64))

    # counts per class x source (images + videos)
    cls = defaultdict(Counter)
    for r in man:
        cls[r["class"]][r["source"]] += 1 if r["media_type"] == "image" else 0
    vid = Counter((r["source"]) for r in man if r["media_type"] == "video")
    miss_tax = sorted(c for c in cls if c not in tax)
    rows = []
    for c, cnt in sorted(cls.items()):
        t = tax.get(c, {})
        rows.append([c, t.get("scientific_name", ""), t.get("family", ""), t.get("match_status", "")]
                    + [cnt[s] for s in SOURCES] + [sum(cnt.values())])
    write(out / "images_by_class_source.csv",
          ["folder", "scientific_name", "family", "taxonomy_match"] + SOURCES + ["total_images"], rows)

    per = defaultdict(lambda: Counter())
    fmt_c, res_c, mp_c = Counter(), Counter(), Counter()
    exif_c, cam_c, month_c = defaultdict(Counter), Counter(), Counter()
    dates = defaultdict(list)
    bad = Counter()
    for r, p in zip(imgs, res):
        s = r["source"]
        per[s]["images"] += 1
        ext = r["path"].rsplit(".", 1)[-1].lower()
        if p is None:
            bad[s] += 1
            fmt_c[(s, ext, "UNREADABLE")] += 1
            continue
        w, h, f, e, mk, md, g, d = p
        fmt_c[(s, ext, f)] += 1
        res_c[(s, max(w, h), min(w, h))] += 1
        mpx = w * h / 1e6
        mp_c[(s, "<1" if mpx < 1 else "1-4" if mpx < 4 else "4-8" if mpx < 8 else "8-12" if mpx < 12 else "12-24" if mpx < 24 else ">=24")] += 1
        x = exif_c[s]
        x["with_exif"] += e
        x["with_make_model"] += bool(mk or md)
        x["with_gps_flag"] += g
        x["with_capture_date"] += bool(d)
        if mk or md:
            cam_c[(s, mk, md)] += 1
        if d:
            dates[s].append(d)
            month_c[(s, d[:7])] += 1

    by_source = []
    for s in SOURCES:
        n_cls = sum(1 for c in cls if cls[c][s])
        by_source.append([s, "auxiliary (không công bố)" if s in AUX else "review (xung đột)" if s == "review_conflict" else "main",
                          per[s]["images"], vid[s], n_cls])
    write(out / "summary_by_source.csv", ["source", "tier", "images", "videos", "classes"], by_source)

    write(out / "format_by_source.csv", ["source", "ext", "pil_format", "count"],
          [[*k, v] for k, v in sorted(fmt_c.items())])
    mp_order = ["<1", "1-4", "4-8", "8-12", "12-24", ">=24"]
    write(out / "resolution_megapixel_by_source.csv", ["source", "megapixel_bucket", "count"],
          [[s, b, mp_c[(s, b)]] for s in SOURCES for b in mp_order if mp_c[(s, b)]])
    write(out / "resolution_dims_by_source.csv", ["source", "long_side", "short_side", "count"],
          [[s, l, sh, v] for (s, l, sh), v in sorted(res_c.items(), key=lambda kv: (kv[0][0], -kv[1]))])
    ex_rows = []
    for s in SOURCES:
        n, x = per[s]["images"] - bad[s], exif_c[s]
        ex_rows.append([s, per[s]["images"], bad[s]] + [v for k in ("with_exif", "with_make_model", "with_gps_flag", "with_capture_date")
                        for v in (x[k], pct(x[k], n))])
    write(out / "exif_by_source.csv", ["source", "images", "unreadable", "with_exif", "with_exif_pct", "with_make_model", "with_make_model_pct",
                                       "with_gps_flag", "with_gps_flag_pct", "with_capture_date", "with_capture_date_pct"], ex_rows)
    write(out / "camera_by_source.csv", ["source", "make", "model", "count"],
          [[*k, v] for k, v in sorted(cam_c.items(), key=lambda kv: (kv[0][0], -kv[1]))])
    write(out / "capture_month_by_source.csv", ["source", "month", "count"], [[*k, v] for k, v in sorted(month_c.items())])
    dr = [[s, min(d), max(d), len(d)] for s in SOURCES if (d := dates[s])]
    write(out / "capture_date_range_by_source.csv", ["source", "min_date", "max_date", "n_with_date"], dr)

    # summary.md
    tot = len(imgs)
    allx = Counter()
    for s in SOURCES:
        allx.update(exif_c[s])
    L = ["# ViMeLeaf audit (RES-42)", "",
         "Tái lập: `python units/research/experiments/vimeleaf/audit_dataset.py --root E:\\ViMeLeaf_Dataset` (không có seed; quét toàn bộ manifest, kết quả tất định). "
         "Cần `pip install pillow`. Dữ liệu chỉ đọc; GPS chỉ thống kê có/không, không xuất toạ độ. Không khử trùng (xem RES-28); `dup_group` bị bỏ qua.", "",
         f"Manifest: {len(man)} tệp = {tot} ảnh + {sum(vid.values())} video; {len(cls)} thư mục lớp; thiếu trong taxonomy.csv: {len(miss_tax)} ({', '.join(miss_tax) or '-'}).", "",
         "## Theo nguồn", "", "| nguồn | vai trò | ảnh | video | số lớp |", "|---|---|---:|---:|---:|"]
    L += [f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} |" for r in by_source]
    L += ["", "supplement_v1/v2 là tập phụ, KHÔNG công bố. review_conflict: ảnh ở nhóm xung đột nhãn, chưa quyết định.", "",
          "## EXIF / GPS / ngày chụp (ảnh đọc được)", "",
          "| nguồn | ảnh | EXIF % | hãng/máy % | có GPS % | có ngày chụp % | ngày chụp (min..max) |", "|---|---:|---:|---:|---:|---:|---|"]
    drd = {r[0]: r for r in dr}
    for r in ex_rows:
        L.append(f"| {r[0]} | {r[1]} | {r[4]} | {r[6]} | {r[8]} | {r[10]} | {drd[r[0]][1] + '..' + drd[r[0]][2] if r[0] in drd else '-'} |")
    L += ["", "## Hãng máy (top 10 toàn bộ)", "", "| hãng | model | ảnh |", "|---|---|---:|"]
    cm = Counter()
    for (s, mk, md), v in cam_c.items():
        cm[(mk, md)] += v
    L += [f"| {mk} | {md} | {v} |" for (mk, md), v in cm.most_common(10)]
    L += ["", "## Độ phân giải (megapixel)", "", "| nguồn | " + " | ".join(mp_order) + " |", "|---|" + "---:|" * len(mp_order)]
    L += [f"| {s} | " + " | ".join(str(mp_c[(s, b)]) for b in mp_order) + " |" for s in SOURCES]
    L += ["", f"Ảnh không đọc được bằng Pillow: {sum(bad.values())} ({dict(bad)}). HEIC (36 tệp) Pillow không giải mã nên tính vào số này; "
          "ponytail: thêm pillow-heif nếu cần EXIF của HEIC.", "",
          "## Tệp CSV", "", "images_by_class_source, summary_by_source, format_by_source, resolution_megapixel_by_source, resolution_dims_by_source, "
          "exif_by_source, camera_by_source, capture_month_by_source, capture_date_range_by_source (tên lớp nối taxonomy.csv của RES-41)."]
    (out / "summary.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("done ->", out)


if __name__ == "__main__":
    main()
