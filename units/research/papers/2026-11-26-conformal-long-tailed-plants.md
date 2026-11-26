# Conformal Prediction for Long-Tailed Classification

Đề tài so sánh: **T2 / ViMeLeaf Bài 2** (đuôi dài + conformal). Ngày đọc: 2026-11-26.

## Thông tin
- Tên: *Conformal Prediction for Long-Tailed Classification*
- Tác giả: Tiffany Ding, Jean-Baptiste Fermanian, Joseph Salmon
- Năm: 2025 (arXiv 2025-07-09, v3)
- Nơi đăng: arXiv:2507.06867 — DOI arXiv: 10.48550/arXiv.2507.06867.
- Link: https://arxiv.org/abs/2507.06867

## Vấn đề
Phân loại **đuôi dài** (plant identification được nêu làm motivation): các phương pháp conformal prediction hiện có khi áp vào long-tail buộc người dùng chọn một trong hai: (i) prediction set nhỏ nhưng **class-conditional coverage** kém (loài hiếm bị loại khỏi set), hoặc (ii) set lớn (đảm bảo class-conditional) nhưng **quá cồng kềnh** khó kiểm chứng. Cần trade-off mượt giữa set size và class-conditional coverage.

## Phương pháp
- **Prevalence-adjusted softmax**: conformal score mới, tối ưu **macro-coverage** (trung bình class-conditional coverage trên các lớp) thay vì marginal coverage.
- **Interpolation procedure**: nội suy tuyến tính giữa threshold của marginal conformal và class-conditional conformal → gia số kiểm soát độ lớn set vs độ phủ theo lớp.
- Đảm bảo **marginal coverage** (không class-conditional chặt) nhưng kiểm soát size.

## Dữ liệu và kết quả
- **Pl@ntNet-300K** (1.081 lớp) và **iNaturalist-2018** (8.142 lớp) — 2 dataset ảnh cây/động vật đuôi dài.
- Kết quả (abstract): phương pháp mới cho macro-coverage tốt hơn mà set size hợp lý; so với baseline conformal thường. **Số cụ thể từng bảng chưa đối chiếu lại trong lượt này** (chưa mở HTML/PDF table) — "chưa kiểm chứng" số.

## Hạn chế
- Chỉ mở abstract (không đọc lại bảng kết quả) → số coverage/set size "chưa kiểm chứng".
- Long-tail tổng quát (cây + động vật, Pl@ntNet/iNat), chưa cây **thuốc** Việt Nam/ĐNA.
- Conformal = prediction set (nhiều nhãn khả dĩ), khác "từ chối 0/1" (reject option) — P2 cần ghép cả hai.

## Liên quan ViMeLeaf Bài 2
- **(a) Trùng một phần**: cùng "long-tail + cây + conformal" với P2 (đuôi dài 72 loài <100 ảnh). Nhưng P2 mới ở: (1) **cây thuốc Việt Nam** (không phải Pl@ntNet/iNat), (2) **cặp dễ nhầm có nhãn an toàn**, (3) **OOD điện thoại**, (4) kết hợp conformal với **selective reject + an toàn**.
- **(b) Khoảng trống P2 lấp**: conformal trên dataset cây thuốc Việt + pair-easy-confused + OOD; đo macro-coverage cho loài hiếm (72 loài đuôi) thay vì chỉ marginal.
- **(c) Rủi ro trùng**: **thấp** (khác dataset, khác mục tiêu an toàn). Nhưng **bắt buộc trích** vì cùng "conformal + long-tail + cây".
- **(d) Baseline**: **conformal APS (adaptive prediction set) + RAPS (risk-adaptive)** — chính là 2 cái tên P2 hỏi (Q2: "conformal APS/RAPS"). Bài này + nền 1705.08500 cho P2 lưới: SR, MC-dropout, energy, temperature scaling, Deep Ensemble, conformal APS/RAPS. Đo **AURC + risk@coverage + coverage (conformal)**.

## Dùng được gì
- **Conformal APS / RAPS** làm baseline từ chối cho P2 (đáp ứng Q2).
- **Prevalence-adjusted softmax + macro-coverage** dùng khi P2 muốn đảm bảo 72 loài đuôi không bị bỏ khỏi prediction set.
- Pl@ntNet-300K làm dataset đối chứng (có thể so nếu P2 đủ dữ liệu).
- Xác nhận "long-tail + conformal" là hướng đã có cho cây → P2 phải nêu phần mới (cây thuốc + an toàn + OOD).

## Mức chắc chắn
Đọc **abstract + arXiv metadata** (tác giả, năm, dataset, 2 phương pháp). **Chưa đọc lại bảng kết quả** → số coverage/set size "chưa kiểm chứng". Nếu P2 trích số, mở https://arxiv.org/abs/2507.06867 HTML/PDF trước.

## Ghi chú thêm
- Cùng "bộ baseline từ chối" P2 cần: kết hợp với 2605.08618 (energy/OE) + 1705.08500 (SR/MC-dropout) + 1805.08206 (temperature scaling, chưa đọc lượt này).
- Conformal cho set, selective reject cho 0/1 — P2 nên dùng **cả 2** (set cho "gợi ý top-k", reject cho "không chắc thì từ chối + cảnh báo").
