# Beyond Toy Benchmarks: A Systematic Evaluation of OOD Detection Methods For Plant Pathology Classification

Đề tài so sánh: **T2 / ViMeLeaf Bài 2** (từ chối/OOD cho ảnh cây). Ngày đọc: 2026-11-26.

## Thông tin
- Tên: *Beyond Toy Benchmarks: A Systematic Evaluation of OOD Detection Methods For Plant Pathology Classification*
- Tác giả: Devesh Shah
- Năm: 2026 (arXiv 2026-05-09, v1)
- Nơi đăng: arXiv:2605.08618 — DOI arXiv: 10.48550/arXiv.2605.08618. Code: https://github.com/deveshshah1/Out_Of_Distribution_Exploration
- Link: https://arxiv.org/abs/2605.08618 , toàn văn HTML: https://arxiv.org/html/2605.08618

## Vấn đề
OOD detection (tạo tín hiệu từ chối khi gặp ảnh ngoài phân bố) cho **nghiệp vụ cây** (foliar disease) trên dataset thực (Plant Pathology 2021, fine-grained), thay vì benchmark nhỏ CIFAR. Câu hỏi: 6 họ phương pháp OOD (post-hoc scoring, auxiliary objective, energy-based, constrained optimization) hoạt động thế nào trên dữ liệu cây + near-OOD (loài hoa trông giống lá bệnh)?

## Phương pháp (6 phương pháp, cùng backbone ResNet-18 fine-tune)
- **E1 MSP (baseline)**: score S(x) = −max_c p̂_c (max softmax prob; Hendrycks & Gimpel).
- **E3 OOD-class auxiliary**: thêm lớp thứ 6 "OOD" + loss BCE (train có nhãn OOD) — giả định nặng (đòi OOD được gán nhãn), coi là **upper bound**, không fair.
- **E4 Outlier Exposure (OE)**: fine-tune với loss CE trên ID + λ·loss_OE trên dữ liệu OOD (Hendrycks et al. 2018).
- **E5a Post-hoc Energy**: thay MSP bằng free energy E(x;f) = −T·log Σ_c exp(f_c(x)/T) (Liu et al. 2020), không retrain.
- **E5b Energy Fine-Tuning**: thêm loss energy margin (m_in/m_out theo trung vị energy val ID/OOD) → **tốt nhất trong các phương pháp fair**.
- **WOODS/SCONE (constrained optimization)**: tối ưu có ràng buộc trên dữ liệu "wild" (ID+OOD trộn, không nhãn). Ghi chú: **không ổn định training** khi scale lên dataset cỡ vừa (tìm kiếm mới, ít được báo cáo trong văn học).

## Dữ liệu và kết quả
- **Plant Pathology 2021** (Thapa et al. 2021; gốc Kaggle FGVC8, lá táo, foliar disease). Lọc về **5 lớp đơn nhãn phổ biến nhất → 15.675 ảnh**. Split 64/16/20 + 15% train hold-out làm wild.
- OOD sets: **Stanford Cars** (far), **DTD** (far), **Flowers102** (near — gần giống nhất, failure mode thực tế: hoa vs lá bệnh).
- Thước đo: **balanced accuracy** (ID) + **AUROC / FPR95** (OOD, từng set).
- Kết quả (Table 2): **E3 gần như hoàn hảo** (AUROC cao, FPR95 thấp) mọi set nhưng là upper bound (cần OOD có nhãn). Trong các phương pháp fair, **E5b (energy fine-tuning) tốt nhất**, cải thiện trên MSP baseline mà giữ ID accuracy; lợi ích đến từ cả **tái cấu trúc embedding + calibration hàm scoring** (mục 4–5).

## Hạn chế
- E3 (upper bound) đòi OOD có nhãn — hiếm đạt được trong thực tế.
- WOODS/SCONE không ổn định ở dataset vừa (mục 4) — khó dùng.
- Chỉ 5 lớp, apple foliar (một cây, một loại bệnh) — chưa cây thuốc, chưa đuôi dài 72 loài, chưa cặp dễ nhầm.
- Không đo selective risk–coverage (AURC) — chỉ AUROC/FPR95 (detection) chứ chưa "từ chối theo coverage".

## Liên quan ViMeLeaf Bài 2
- **(a) Trùng một phần**: bài này làm OOD detection cho **cây (foliar disease)** — cùng "cây + OOD" với P2. Nhưng: (1) **foliar disease (bệnh lá)**, không phải **loài cây thuốc**; (2) **5 lớp**, không đuôi dài/cặp dễ nhầm; (3) thước đo **AUROC/FPR95 (detection)**, chưa **risk–coverage/AURC (selective)**; (4) không "an toàn khi nhầm".
- **(b) Khoảng trống P2 lấp**: (1) chuyển OOD/selective từ bệnh lá → **loài cây thuốc** (66-80/165 loài, đuôi 72); (2) thêm **cặp dễ nhầm có nhãn an toàn** (Dây giác/Sục sạc); (3) đo **AURC + risk@coverage** thay vì chỉ AUROC; (4) OOD **ảnh điện thoại** (covariate shift); (5) "an toàn khi nhầm" (b9 automation bias). P2 mới rõ.
- **(c) Rủi ro trùng**: **vừa**. Cùng "cây + OOD" nhưng khác (bệnh vs loài, 5 lớp vs đuôi dài, detection vs selective, không an toàn). **Bắt buộc trích bài này + nêu khác biệt**; nếu P2 chỉ làm AUROC OOD cho cây thì trùng phần lớn.
- **(d) Baseline nên dùng làm lưới cho P2**: **MSP (E1) + Energy (Liu et al. 2020, E5a/E5b) + Outlier Exposure (E4) + WOODS/SCONE (constrained)** — chính là "phương pháp từ chối phổ biến" P2 hỏi (Q2). Thêm SR/MC-dropout (1705.08500) + temperature scaling (1805.08206) + conformal (2507.06867). Đo **AUROC OOD + FPR95 + AURC/risk@coverage**.

## Dùng được gì
- Lưới 6 OOD methods (MSP, OOD-class, OE, energy post-hoc, energy fine-tune, WOODS/SCONE) làm **baseline từ chối** cho P2 (đáp ứng Q2).
- Công thức **energy E(x;f) = −T·log Σ exp(f_c/T)** (trích được).
- Cách dựng OOD sets gần/xa (Flowers102 = near-OOD cho cây) — P2 làm tương tự với "cặp dễ nhầm" làm near-OOD.
- Cảnh báo: constrained optimization (WOODS/SCONE) không ổn định ở dataset vừa → P2 có thể bỏ qua 2 cái này, giữ MSP/energy/OE.
- Số đối chứng: E5b năng nhất (fair) giữ ID acc; E3 upper bound.

## Mức chắc chắn
Đọc **toàn văn HTML arXiv** (mục 1–5, công thức E1–E10, Table 1–2, OOD sets). Số (15.675 ảnh, 5 lớp, split 64/16/20, AUROC/FPR95 định nghĩa, E3 upper bound, E5b fair-nhất) khớp giữa abstract + bảng. "E5b số cụ thể từng set" (giá AUROC chính xác) đọc qua table layout, **chưa ghi từng số từng OOD set** (table 2 là inline-block, số khó trích chính xác) — nếu P2 cần số chính xác, mở lại PDF table 2. Venue: preprint (không thấy journal).

## Ghi chú thêm
- Tác giả cá nhân (Devesh Shah), code public. Bài **detection** (AUROC/FPR95), không phải **selective** (AURC) — P2 cần thêm AURC/risk–coverage (nền 1705.08500/1901.09192) để so fair.
- Flowers102 làm near-OOD cho lá = mô hình tốt cho "cặp dễ nhầm" P2 (loài hoa/loài lá giống nhau).
