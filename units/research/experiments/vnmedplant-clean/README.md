# VNMedPlant-Clean: pipeline khử trùng ảnh và split chống rò rỉ

Đề tài A trong `topics/brief-medicinal-plants.md` (RES-14 / RES-26). Pipeline chạy được và **đã kiểm thử trên dữ liệu giả**.
Chưa chạy trên ảnh thật (chưa có đường dẫn); khi có chỉ cần chạy các lệnh dưới đây.

## Yêu cầu

- Python >= 3.10, thư viện: `numpy>=2.0`, `pillow`, `scikit-learn` (xem `requirements.txt`).
- Tuỳ chọn (chỉ cho `--dino` và `baseline --backend dinov2`): `torch`, `transformers`. Tự dùng GPU nếu `torch.cuda.is_available()`, không thì chạy CPU (chậm với 50k ảnh). **Phần DINOv2 chưa được chạy thử** (máy kiểm thử không cài torch); phần còn lại đã test.
- Cài trong venv của thư mục này, không cài toàn máy:

```powershell
cd units/research/experiments/vnmedplant-clean
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
```

## Chạy trên dữ liệu thật

Cấu trúc ảnh: `<root>/<tên-loài>/*.jpg|png` (tìm cả thư mục con). **Output đặt ngoài git** (ví dụ `D:\vnmedplant-out`).

```powershell
$py = ".\.venv\Scripts\python"; $root = "<đường dẫn ảnh>"; $out = "D:\vnmedplant-out"
& $py dedup.py       --root $root --out $out --phash-thr 8            # thêm --dino --cos-thr 0.95 nếu có torch
& $py split.py       --images $out\images.csv --out $out --seeds 0 1 2
& $py leak_report.py --splits-dir $out
& $py baseline.py    --root $root --splits-dir $out --out $out --backend dinov2
```

| Bước | Đầu ra (trong `--out`) |
|---|---|
| `dedup.py` | `images.csv` (path, class, sha256, phash, cluster_id, keep), `dedup_thresholds.csv` (số ảnh sau và tỉ lệ trùng theo từng ngưỡng pHash/cosine), `dedup_per_class.csv` (ảnh mỗi loài trước/sau), `dedup_summary.json`, `unreadable.csv` (nếu có ảnh hỏng) |
| `split.py` | `splits_seed<S>.csv` (path, class, cluster_id, split_cluster, split_random) |
| `leak_report.py` | `leak_report.csv` (ảnh test có ảnh cùng cụm trong train, theo kiểu split và seed), `leak_per_class.csv` |
| `baseline.py` | `baseline_results.csv` (top-1, macro-F1 mỗi seed x kiểu split), `baseline_gap.csv` (**độ chênh random - cluster**, chỉ số chính) |

## Cách hoạt động

- **Cụm**: hai ảnh được nối nếu SHA-256 bằng nhau, hoặc khoảng cách Hamming pHash <= `--phash-thr` (mặc định 8/64), hoặc (tuỳ chọn) cosine DINOv2 >= `--cos-thr`. Cụm = thành phần liên thông (union-find, `cluster_id` ổn định). `keep=1` đánh dấu một ảnh đại diện mỗi cụm.
- Mặc định chỉ so sánh **trong cùng loài** (nhanh). `--cross-class` so sánh cả giữa các loài, dùng để phát hiện ảnh trùng gắn nhãn khác nhau; với 50k ảnh sẽ chậm hơn nhiều.
- **Ngưỡng**: `dedup_thresholds.csv` cho tỉ lệ trùng theo từng ngưỡng để người duyệt mẫu ngẫu nhiên chọn ngưỡng cuối (chưa có ngưỡng "đúng" cho ảnh thật; 8 chỉ là mặc định).
- **Split**: chia theo cụm trong từng loài (80/10/10 mặc định, `--ratios`), không cụm nào nằm ở hai tập. Split ngẫu nhiên theo ảnh dùng cùng tỉ lệ để so sánh. Cả hai đều dùng cả bản sao trong dữ liệu (muốn bỏ bản sao, thêm `--keep-one`).
- **Seed**: mặc định `--seeds 0 1 2`; split dùng `random.Random("cluster-<seed>")` / `("random-<seed>")`; linear probe dùng `random_state=seed`. Chạy lại cùng đầu vào cho ra cùng CSV (test kiểm tra điều này).
- **Baseline**: logistic regression (chuẩn hoá + linear) trên đặc trưng đóng băng; `--backend tiny` (thumbnail 16x16) chỉ để test khung. Đặc trưng cache ở `features_<backend>.npz` trong `--out`; xoá nếu đổi dữ liệu.

## Kiểm thử (dữ liệu giả)

```powershell
.\.venv\Scripts\python test_pipeline.py
```

`make_fake_data.py` sinh ảnh tổng hợp (không phải ảnh thật) gồm 4 loài x 16 nhóm gốc, có bản sao chính xác, resize 160px, nén JPEG quality 20, crop nhẹ 2% mỗi cạnh. Test khẳng định:
1. mọi biến thể rơi vào đúng cụm của ảnh gốc, hai ảnh gốc khác nhau không bị gom nhầm, đếm đúng số bản sao chính xác;
2. split theo cụm: 0 ảnh test có cụm trong train/val, đủ 3 tập, tái lập theo seed;
3. split ngẫu nhiên có rò rỉ (> 0) trên dữ liệu giả;
4. baseline chạy hết 2 split x 3 seed và ra độ chênh.

Kết quả lần chạy ghi trong issue RES-26: `PASS: tat ca kiem thu`.

## Giới hạn đã biết

- pHash ngưỡng 8 bắt tốt resize/nén JPEG; crop 2% mỗi cạnh bắt được, **crop 4% thì một số cặp vượt ngưỡng 8** (đã đo trên dữ liệu giả). Crop mạnh, xoay, đổi sáng cần `--dino`.
- Số liệu trên dữ liệu giả (độ chênh top-1 giữa hai split) **không có ý nghĩa khoa học**, chỉ chứng minh khung chạy đúng.
- Nối bằng liên thông có thể gom chuỗi ảnh "giống dần" thành cụm lớn (chaining); xem phân bố kích thước cụm khi có dữ liệu thật.
- Chưa có metadata lần chụp/cây; khi có, thêm khoá nhóm đó vào bước cụm.
