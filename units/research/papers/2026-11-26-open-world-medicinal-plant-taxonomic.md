# A novel approach to navigate the taxonomic hierarchy to address the Open-World Scenarios in Medicinal Plant Classification

Đề tài so sánh: **T2 / ViMeLeaf Bài 2** (open-set cây thuốc). Ngày đọc: 2026-11-26. (Đã mở abstract trong RES-29, xác nhận lại arXiv v4.)

## Thông tin
- Tên: *A novel approach to navigate the taxonomic hierarchy to address the Open-World Scenarios in Medicinal Plant Classification*
- Tác giả: Soumen Sinha, Tanisha Rana, Susmita Ghosh, Rahul Roy (IIT Kharagpur / IIT Delhi)
- Năm: 2025 (arXiv 2025-02-24, v4; **v2/v3 bị rút** theo brief RES-29)
- Nơi đăng: arXiv:2502.17289 — DOI arXiv: 10.48550/arXiv.2502.17289.
- Link: https://arxiv.org/abs/2502.17289

## Vấn đề
Phân loại **thực vật y học (medicinal plant)** theo **phân cấp taxonomic** (phylum→class→order→family→species) dưới kịch bản **open-world**: phải gán nhãn tốt nhất cho cả **loài chưa từng thấy** (unknown species), không chỉ phân loại closed.

## Phương pháp
- **DenseNet121 + Multi-Scale Self-Attention (MSSA)** + **cascaded classifiers** theo phân cấp.
- MSSA: bắt đặc trưng local + global đa tỷ lệ → phân biệt **loài giống nhau** (similar species) và nhận diện loài mới.
- Dùng attention scores để focus vùng quan trọng đa scale.
- Model nhỏ hơn SOTA ~4 lần (dễ deploy).

## Dữ liệu và kết quả (abstract)
- 2 dataset SOTA (có/không có background artifacts), test trên **unknown species**.
- Unknown species accuracy (trung bình): **phylum 83.36%, class 78.30%, order 60.34%, family 43.32%** (suy giảm dần theo độ sâu phân cấp — càng sâu càng kém, như dự kiến).
- Dataset cụ thể (tên bộ SOTA) **không nêu rõ trong abstract** → "chưa kiểm chứng" tên bộ dữ liệu.

## Hạn chế
- **Phân cấp theo phân loại học** (phylum→species), **không phải cặp dễ nhầm có nhãn an toàn** (không đo "nhầm loài nào thì độc/nguy hiểm").
- Dataset SOTA Ấn Độ (không cây thuốc Việt Nam/ĐNA) — "chưa kiểm chứng" bộ dữ liệu.
- Open-world = "loài lạ nhận theo phân cấp", chưa có cơ chế **từ chối kèm cảnh báo độc tính** (B9 automation bias).
- v2/v3 rút, chỉ v4 còn → trích dẫn cẩn thận (ghi "v4").

## Liên quan ViMeLeaf Bài 2
- **(a) Bài open-set cây thuốc gần nhất**: đây là **công trình open-set cây thuốc gần nhất** P2 có (B6 trong brief). P2 **bắt buộc trích** để trả lời "đã ai làm từ chối/open-set cho cây thuốc chưa?" (Q3) → có, bài này, nhưng:
- **(b) Khác biệt / khoảng trống P2 lấp**:
  1. Bài này **phân cấp taxonomic**, P2 làm **cặp dễ nhầm có nhãn an toàn** (micro-level, không phải phylum→species).
  2. Bài này **không đo an toàn khi nhầm** (không cảnh báo độc); P2 có "an toàn khi nhầm" (độc/không dùng được) — nếu có chuyên gia dược.
   3. Dataset **Ấn Độ SOTA**, P2 **Việt Nam/ĐNA** (cây thuốc nam, 3 tỉnh, đuôi dài 102 loài, RES-42).
  4. Bài này **open-set nhận dạng**, P2 thêm **selective reject theo risk–coverage + OOD điện thoại**.
- **(c) Rủi ro trùng**: **thấp–vừa** (cùng "open-set + cây thuốc" nhưng khác: phân cấp vs cặp dễ nhầm, không an toàn vs an toàn, Ấn Độ vs Việt). Trích rõ phần mới.
- **(d) Baseline**: thêm "open-set phân cấp taxonomic" làm baseline so với "cặp dễ nhầm + selective reject". P2 nên so: (1) phân cấp kiểu bài này, (2) flat + MSP/energy, (3) conformal, (4) couple-aware selective (đóng góp P2).

## Dùng được gì
- Trả lời Q3: **có** bài open-set cây thuốc (bài này) — P2 không "lần đầu làm open-set cây thuốc" mà "lần đầu làm **cặp dễ nhầm + an toàn + cây thuốc Việt + OOD + risk–coverage**".
- MSSA (multi-scale self-attention) tham khảo cho nhận diện cặp giống nhau (Dây giác/Sục sạc, lá 3 chét).
- Số đối chứng: unknown-species acc suy giảm theo phân cấp (83.36→43.32) — minh hoạ "càng cụ thể càng khó".

## Mức chắc chắn
Đọc **abstract v4 + arXiv metadata** (tác giả, năm, số unknown-species acc, "4 lần nhỏ hơn SOTA"). **Chưa đọc lại toàn văn bảng/tên dataset** → tên bộ dữ liệu SOTA "chưa kiểm chứng". v2/v3 rút (theo brief RES-29) — chỉ dùng v4.

## Ghi chú thêm
- Cùng brief RES-29 (B6). P2 trích bài này + LifeCLEF (2509.20870) làm 2 tiền lệ open-set cây; phần mới P2 = cặp dễ nhầm + an toàn + Việt + OOD + risk–coverage.
