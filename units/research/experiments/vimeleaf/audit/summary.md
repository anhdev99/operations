# ViMeLeaf audit (RES-42)

Tái lập: `python units/research/experiments/vimeleaf/audit_dataset.py --root E:\ViMeLeaf_Dataset` (không có seed; quét toàn bộ manifest, kết quả tất định). Cần `pip install pillow`. Dữ liệu chỉ đọc; GPS chỉ thống kê có/không, không xuất toạ độ. Không khử trùng (xem RES-28); `dup_group` bị bỏ qua.

Manifest: 62370 tệp = 62102 ảnh + 268 video; 195 thư mục lớp; thiếu trong taxonomy.csv: 0 (-).

## Theo nguồn

| nguồn | vai trò | ảnh | video | số lớp |
|---|---|---:|---:|---:|
| raw_angiang | main | 27093 | 93 | 53 |
| raw_dongthap | main | 6692 | 29 | 22 |
| raw_tayninh | main | 22134 | 40 | 17 |
| review_conflict | review (xung đột) | 2169 | 2 | 2 |
| supplement_v1 | auxiliary (không công bố) | 1577 | 56 | 52 |
| supplement_v2 | auxiliary (không công bố) | 2437 | 48 | 50 |

supplement_v1/v2 là tập phụ, KHÔNG công bố. review_conflict: ảnh ở nhóm xung đột nhãn, chưa quyết định.

## EXIF / GPS / ngày chụp (ảnh đọc được)

| nguồn | ảnh | EXIF % | hãng/máy % | có GPS % | có ngày chụp % | ngày chụp (min..max) |
|---|---:|---:|---:|---:|---:|---|
| raw_angiang | 27093 | 100.0 | 100.0 | 56.2 | 100.0 | 2025-05-26..2025-06-09 |
| raw_dongthap | 6692 | 100.0 | 100.0 | 0.0 | 100.0 | 2025-06-03..2025-06-04 |
| raw_tayninh | 22134 | 100.0 | 100.0 | 100.0 | 100.0 | 2025-06-02..2025-06-03 |
| review_conflict | 2169 | 100.0 | 100.0 | 100.0 | 100.0 | 2025-05-27..2025-05-27 |
| supplement_v1 | 1577 | 0.0 | 0.0 | 0.0 | 0.0 | - |
| supplement_v2 | 2437 | 0.0 | 0.0 | 0.0 | 0.0 | - |

## Hãng máy (top 10 toàn bộ)

| hãng | model | ảnh |
|---|---|---:|
| Apple | iPhone 14 Pro | 39508 |
| samsung | Galaxy M54 5G | 18542 |

## Độ phân giải (megapixel)

| nguồn | <1 | 1-4 | 4-8 | 8-12 | 12-24 | >=24 |
|---|---:|---:|---:|---:|---:|---:|
| raw_angiang | 0 | 2 | 0 | 1480 | 25606 | 0 |
| raw_dongthap | 0 | 0 | 0 | 1 | 6691 | 0 |
| raw_tayninh | 0 | 0 | 0 | 9629 | 12474 | 0 |
| review_conflict | 0 | 0 | 0 | 1 | 2168 | 0 |
| supplement_v1 | 0 | 214 | 1363 | 0 | 0 | 0 |
| supplement_v2 | 0 | 387 | 2050 | 0 | 0 | 0 |

Ảnh không đọc được bằng Pillow: 36 ({'raw_angiang': 5, 'raw_tayninh': 31}). HEIC (36 tệp) Pillow không giải mã nên tính vào số này; ponytail: thêm pillow-heif nếu cần EXIF của HEIC.

## Tệp CSV

images_by_class_source, summary_by_source, format_by_source, resolution_megapixel_by_source, resolution_dims_by_source, exif_by_source, camera_by_source, capture_month_by_source, capture_date_range_by_source (tên lớp nối taxonomy.csv của RES-41).
