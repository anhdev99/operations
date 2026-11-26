# P2-01a: tổng hợp selective / conformal / open-set cho nhận dạng ảnh thực vật

Issue: RES-48 (con của RES-36 / RES-27). Người viết: Scholar. Ngày đọc: 2026-11-26.
Phục vụ **ViMeLeaf Bài 2** (RES-38): nhận dạng loài cây thuốc dễ nhầm, đuôi dài, biết từ chối; nộp Computers and Electronics in Agriculture (hạn 2027-04-30).
Bối cảnh: `units/research/papers/brief-vimeleaf-novelty.md` (mục B) và `units/research/topics/vimeleaf-3-paper-series.md`.

## Bài đã đọc trong lượt này (7)

| Slug | Tên | Loại | Link |
|---|---|---|---|
| `2026-11-26-selective-classification-dnn-geifman-el-yaniv.md` | Selective Classification for DNNs (Geifman & El-Yaniv, 2017) | nền | arXiv:1705.08500 |
| `2026-11-26-selectivenet-geifman-el-yaniv.md` | SelectiveNet (Geifman & El-Yaniv, ICML 2019) | nền | arXiv:1901.09192 |
| `2026-11-26-lifeclef-plant-open-world-2016.md` | Plant identification in an open-world (LifeCLEF 2016) | cây, open-set | arXiv:2509.20870 |
| `2026-11-26-ood-detection-plant-pathology.md` | OOD detection for plant pathology (6 methods) | cây, OOD | arXiv:2605.08618 |
| `2026-11-26-conformal-long-tailed-plants.md` | Conformal for long-tailed (Pl@ntNet-300K) | cây, conformal, đuôi dài | arXiv:2507.06867 |
| `2026-11-26-open-world-medicinal-plant-taxonomic.md` | Open-world medicinal plant taxonomic | cây thuốc, open-set | arXiv:2502.17289 |
| `2026-11-26-few-shot-plant-disease-calibration.md` | Few-shot plant disease + calibration | cây, few-shot, calibration | arXiv:2611.16373 |

Mỗi bài: `units/research/papers/<slug>.md` (trích dẫn đầy đủ + DOI, vấn đề, phương pháp, dữ liệu, số chính, hạn chế, liên quan Bài 2). Số "chưa kiểm chứng" (chưa mở lại bảng) được ghi rõ trong từng note.

## Câu 1: thước đo chuẩn (định nghĩa + công thức)

Từ 2 bài nền (1705.08500, 1901.09192) + OOD (2605.08618) + conformal (2507.06867):

- **Risk–coverage curve**: risk R(f, g_θ) là hàm của coverage (tỉ lệ ví dụ được giữ, không từ chối). Selective classifier g_θ chọn ngưỡng α theo confidence-rate κ_f; user đặt **target risk r\*** + độ tin cậy δ; binary-search α để risk ≤ r\* với xác suất ≥ 1−δ (1705.08500, mục 3.5).
- **AURC (area under the risk–coverage curve)**: tích phân đường risk–coverage theo coverage. Thước đo so sánh chất lượng selective classifier (nền 1705.08500; chính thức trong 1901.09192). **P2 nên báo AURC + selective risk @ coverage (vd 80%, 90%)**.
- **E-AURC (expected AURC)**: AURC theo xác suất (hi vọng trên các tập train) — dùng khi muốn bảo đảm thống kê; 1705.08500 đưa "risk control with high probability" (Hoeffding-type), 1901.09192 mở rộng. *(E-AURC định nghĩa chính thức chưa đối chiếu lại công thức trong lượt này → ghi "chưa kiểm chứng" công thức E-AURC cụ thể.)*
- **Selective risk @ coverage**: R(f, g) = E[ loss(f(x), y) · 1[được giữ] ] / P[được giữ]. Báo ở vài mốc coverage (P2: 90% để so với "an toàn khi nhầm").
- **AUROC (OOD)**: diện tích dưới ROC của OOD detector (energy/MSP); **FPR95** = false positive rate ở 95% TPR (2605.08618). Dùng cho "phát hiện OOD" (ảnh điện thoại lạ), không thay AURC.
- **Conformal coverage**: marginal coverage guarantee 1−α (2507.06867); **macro-coverage** = trung bình class-conditional coverage (quan trọng cho 72 loài đuôi P2).

**Khuyến nghị P2**: báo đồng thời **AURC + risk@90% + AUROC OOD + FPR95 + conformal marginal/macro-coverage**. Không chỉ accuracy.

## Câu 2: phương pháp từ chối baseline phổ biến

Lưới baseline P2 nên chạy (ghép từ 7 bài + brief B):

| Baseline | Nguồn | Ghi chú cho P2 |
|---|---|---|
| **MSP** (max softmax, S(x)=−max_c p̂c) | 2605.08618 (E1), nền | baseline rẻ nhất, luôn chạy |
| **Energy** E(x;f)=−T·log Σ exp(f_c/T) | 2605.08618 (E5a/E5b), Liu 2020 | fair-nhất trong 2605.08618; E5b = energy fine-tune |
| **Temperature scaling** (calibrate softmax) | 1805.08206 (chưa đọc lượt này, Geifman); ODIN (Liang 2017) được nhắc trong 2605.08618 | cần mở thêm 1805.08206 trước khi trích số |
| **MC dropout** (var over dropout) | 1705.08500 (SR + MC-dropout) | baseline nền |
| **Deep Ensemble** (variance over ensemble) | nền (chưa đọc bài riêng trong lượt này; được nêu trong 1705.08500 "ensemble techniques") | thêm nếu P2 có thời gian; chi phí cao |
| **Conformal APS** (adaptive prediction set) | 2507.06867 | prediction set (top-k gợi ý), marginal guarantee |
| **Conformal RAPS** (risk-adaptive) | 2507.06867 | kiểm soát size set + macro-coverage (72 loài đuôi) |
| **Outlier Exposure (OE)** | 2605.08618 (E4) | cần OOD data; P2 có thể dùng "cặp dễ nhầm" làm OOD aux |
| **OOD-class auxiliary** | 2605.08618 (E3) | upper bound, đòi OOD có nhãn — chỉ làm reference |
| **WOODS / SCONE (constrained, wild data)** | 2605.08618 | **không ổn định ở dataset vừa** (2605.08618) → P2 bỏ qua hoặc thử sau |
| **Calibration local evidence (linear probe + patch)** | 2611.16373 | baseline few-shot cho 72 loài đuôi |
| **Reject option tích hợp (SelectiveNet-style)** | 1901.09192 | so với threshold-naive (MSP/energy) |

**Khuyến nghị P2 (trật tự chạy)**: MSP → energy (post-hoc + fine-tune) → temperature scaling → MC dropout → conformal APS/RAPS → (nâng cao) SelectiveNet-style reject. Bỏ WOODS/SCONE (không ổn định, chi phí). Deep Ensemble chỉ nếu so sánh cần.

## Câu 3: đã có ai làm từ chối/open-set cho cây thuốc / cặp dễ nhầm chưa?

- **Cây (tổng quát), open-set**: **LifeCLEF 2016** (2509.20870) — benchmark open-set cây đầu tiên (110K ảnh/1000 loài, Tây Âu). Từ chối false positive do lớp lạ.
- **Cây thuốc, open-set (phân cấp)**: **2502.17289** — open-world medicinal plant theo phân cấp taxonomic (phylum→species), unknown-species acc 83.36% (phylum) → 43.32% (family). **Không cặp dễ nhầm có nhãn an toàn, không cây Việt/ĐNA, không cảnh báo độc.**
- **Cây, OOD detection (6 methods)**: **2605.08618** — plant pathology (bệnh lá táo, 5 lớp), MSP/energy/OE/WOODS/SCONE, AUROC/FPR95. **Bệnh, không loài; 5 lớp, không đuôi dài; không an toàn.**
- **Cây, conformal + đuôi dài**: **2507.06867** — Pl@ntNet-300K/iNaturalist (cây + động vật), conformal macro-coverage. **Tổng quát, không cây thuốc, không cặp dễ nhầm.**
- **Cây, few-shot + calibration**: **2611.16373** — PlantVillage/Cassava/Pear (bệnh cây), CLIP + local evidence calibration. **Bệnh, không loài; không selective.**
- **Cặp dễ nhầm cây thuốc có nhãn an toàn + OOD điện thoại + risk–coverage (AURC)**: **chưa thấy** (tìm arXiv: `all:"medicinal plant" AND all:"selective classification"` → 0; `all:"plant" AND all:"open-set"` → LifeCLEF + CropVLM, không cặp dễ nhầm an toàn; `all:"plant species" AND all:"out-of-distribution"` → 0). Đây đúng khoảng trống P2 lấp.

**Kết luận Q3**: có người làm open-set/OOD/selective cho **cây nói chung** và **cây thuốc phân cấp**, nhưng **chưa ai làm "từ chối cho cặp loài cây thuốc dễ nhầm (Dây giác/Sục sạc) có nhãn an-toàn-khi-nhầm + OOD điện thoại + đường risk–coverage (AURC) trên dữ liệu Việt Nam/ĐNA"**. P2 mới ở đúng giao điểm đó.

## Khoảng trống mà P2 lấp được

1. **Cặp dễ nhầm có nhãn an toàn**: chưa có benchmark "cặp loài cây thuốc dễ nhầm + mức nguy hiểm nếu nhầm" (độc/không dùng được). P2 bắt đầu từ Dây giác/Sục sạc (conflict ngày trong ViMeLeaf). *Cần chuyên gia dược gán nhãn nguy hiểm; nếu không, thu hẹp claim thành "đường risk–coverage trên cặp đã chọn, chưa gán an toàn" (theo brief B).*
2. **Cây thuốc Việt Nam/ĐNA + đuôi dài 72 loài**: các bài trên (LifeCLEF Tây Âu, 2502.17289 Ấn Độ, 2605.08618 bệnh táo, 2507.06867 tổng quát, 2611.16373 bệnh) đều không cây thuốc Việt/ĐNA, không đuôi dài 72 loài <100 ảnh.
3. **OOD ảnh điện thoại (covariate shift)**: 2505.15008 (Know When to Abstain, brief B3) cùng hướng "selective + covariate shift" nhưng chưa cây. P2 đo OOD điện thoại (ảnh chụp thực địa) so với lab.
4. **Ghép selective + an toàn (automation bias)**: brief B9 (2508.07617) cảnh báo "từ chối làm người dùng bỏ qua cảnh báo" (false negative +18%/+35% y khoa). P2 phải **đo hiệu ứng người dùng**, không chỉ AURC — nếu không reviewer hỏi "từ chối có làm bỏ lỡ cảnh báo độc không?".

## Phương pháp nên dùng làm baseline (tóm tắt)

- **Backbone**: DINOv2/CLIP (theo brief) + linear probe (2611.16373).
- **Từ chối**: MSP → energy (post-hoc + fine-tune, 2605.08618) → temperature scaling (1805.08206) → MC dropout (1705.08500) → conformal APS/RAPS (2507.06867, macro-coverage cho 72 loài) → SelectiveNet-style (1901.09192, nâng cao).
- **Thước đo**: AURC + selective risk@90% (1705.08500/1901.09192) + AUROC OOD + FPR95 (2605.08618) + conformal marginal/macro-coverage (2507.06867).
- **OOD set near**: dùng "cặp dễ nhầm" (Dây giác↔Sục sạc) làm near-OOD (kiểu Flowers102 trong 2605.08618).
- **An toàn**: gán nhãn nguy hiểm (chuyên gia dược) → đo risk khi nhầm đúng cặp nguy hiểm; thêm user study (B9) nếu có đối tượng.

## Chưa kiểm chứng / việc tiếp theo

- **Temperature scaling** (1805.08206) và **Deep Ensemble**: chưa đọc bài riêng trong lượt này → mở trước khi trích số (liên quan Q2 "temperature scaling, Deep Ensemble").
- **E-AURC công thức chính thức**: chưa đối chiếu lại → xác nhận trước khi dùng.
- **Số từng bảng** của 2507.06867, 2611.16373, 2502.17289, 1901.09192: chưa mở lại table → "chưa kiểm chứng" (ghi trong từng note).
- **MLLM cây (P3, Jiang 2026, DOI 10.3389/fpls.2026.1765281)**: chưa mở lại (brief ghi) → đối chứng MLLM cho P2, ghi "chưa kiểm chứng lại".
- **Chuyên gia dược** gán nhãn cặp nguy hiểm: chưa có → blocker cho claim "an toàn khi nhầm" (theo brief B). Nếu thiếu, P2 thu hẹp thành "risk–coverage trên cặp, chưa an toàn".
- **Notion "Bài đã đọc"**: chưa thêm dòng (thiếu token Notion trong biến môi trường được cấp; ghi trong comment issue).

## Ghi chú phương pháp (không đổi hướng P2)

P2 giữ đúng như đề xuất (bài 2 = "Nhận dạng loài dễ nhầm, đuôi dài, biết từ chối"); review này **không đổi hướng**, chỉ: (1) chốt lưới baseline (MSP/energy/temperature/MC-dropout/conformal APS+RAPS), (2) chốt thước đo (AURC + risk@90% + AUROC/FPR95 + conformal coverage), (3) xác nhận khoảng trống còn nguyên (cặp dễ nhầm + an toàn + cây thuốc Việt + OOD điện thoại), (4) bắt buộc trích 7 bài trên + B3/B9 (brief). Rủi ro trùng: thấp–vừa, đã chỉ ra cách phân biệt trong từng note.
