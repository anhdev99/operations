# Conformal Prediction for Long-Tailed Classification (Ding, Fermanian, Salmon 2025)

- **Tác giả / năm / nơi:** Tiffany Ding, Jean-Baptiste Fermanian, Joseph Salmon (2025).
- **Trích dẫn:** arXiv:2507.06867 (v3 09/07/2025). DOI https://doi.org/10.48550/arXiv.2507.06867 · link đã mở: https://arxiv.org/abs/2507.06867 (abstract).

## Bài toán
Classification có phân bố **long-tail** (nhiều lớp hiếm), ví dụ **plant identification** (Pl@ntNet-300K, iNaturalist). Cần prediction set (nhiều nhãn + độ tin cậy) mà vừa (i) **class-conditional coverage tốt** (không bỏ sót lớp hiếm) vừa (ii) **size hợp lý** (người dùng kiểm tra được ít ứng viên). Method conformal hiện tại ở long-tail bắt chọn nhị phân: set nhỏ → bỏ lớp hiếm, hoặc set lớn → khó kiểm tra.

## Phương pháp
- Đưa vào **marginal coverage guarantee** để **trả dần (smooth trade-off)** giữa size set và class-conditional coverage.
- (1) **prevalence-adjusted softmax**: conformal score function mới, tối ưu **macro-coverage** (trung bình coverage theo từng lớp thay vì theo ảnh).
- (2) **Interpolation procedure**: linear interpolate ngưỡng conformal score giữa marginal và class-conditional → gia số từ 2 đầu.
- Chạy trên **Pl@ntNet-300K (1.081 lớp)** và **iNaturalist-2018 (8.142 lớp)** — 2 dataset long-tail thật.

## Số liệu chính (theo abstract)
- 2 dataset benchmark (Pl@ntNet-300K 1081 lớp; iNat-2018 8142 lớp); "demonstrate methods" — số exact (coverage/size per threshold) không ở abstract, chưa kiểm chứng; cần đọc bảng.
- Điểm cốt lõi: cho **đường risk-coverage theo class-conditional** thay vì chỉ một điểm.

## Hạn chế
- Pl@ntNet-300K/iNat là ảnh cây tổng quát (toàn cây, hoa, lá, rễ...) chụp ngoài thực địa + herbarium; **không phải ảnh lá cây thuốc Việt Nam** (ViMeLeaf). Cần chuyển kỹ thuật sang ViMeLeaf.
- Chỉ đánh giá prediction set (abstain/risk-control), **không gắn "an toàn khi nhầm"** (độc tính) — phần đó là đóng góp của Bài 2.

## Dùng được gì cho Bài 2 (trung tâm câu hỏi 2 + 3)
- **Trả lời (2) "có bài đo calibration/từ chối của MLLM/mô hình không?":** Đây là khung **conformal** cho prediction set long-tail — dùng làm so sánh với MLLM (Jiang, tệp mllm-...) vì MLLM raw **không có** guarantee kiểu này.
- **Trả lời (3) "kỹ thuật đuôi dài nào phổ biến":** 3 hướng chính (khớp với task):
  - **logit adjustment / prevalence-adjusted** (bài này: prevalence-adjusted softmax) — hiệu chỉnh theo tỉ lệ lớp.
  - **balanced / dual-margin** (xem TaxoNet, 2512.18994, dưới đây).
  - **re-sampling** (over-sample hiếm / under-sample phổ biến).
- **Kế hoạch cho Bài 2:** áp dụng **prevalence-adjusted softmax + interpolation** làm lớp "từ chối có guarantee" cho backbone BioCLIP/DINOv2 trên ViMeLeaf; so với threshold-naive. Chỉ số: **AURC (diện tích dưới đường risk-coverage)** + **tỉ lệ nhầm nguy hiểm ở coverage 90%** (mục tiêu an toàn). Ghi "chưa kiểm chứng" nếu chưa chạy lại trên ViMeLeaf.

## Phụ: kỹ thuật đuôi dài long-tail + fine-grained plant (đọc thêm, trả lời (3))
- **TaxoNet — Dual-Margin Embedding for Fine-Grained Long-Tailed Plant Taxonomy** (Cheng Yaw Low, Heejoon Koo, Jaewoo Park, Meeyoung Cha, 2025), arXiv:2512.18994. Link: https://arxiv.org/abs/2512.18994. Khung embedding + **mục tiêu dual-margin** (margin khác nhau theo tần suất lớp) để chỉnh decision boundary dưới mất cân bằng; đánh giá open-world trên Google Auto-Arborist, iNaturalist (Plantae), NAFlora-Mini (herbarium); "consistently outperform" baseline gồm **foundation model multimodal**. → bổ sung cho (3): dual-margin nằm cùng họ với logit adjustment (hiệu chỉnh theo prevalence) nhưng ở không gian embedding.
- **Digital Taxonomist** (de Lutio et al., 2021), arXiv:2106.03774. Link: https://arxiv.org/abs/2106.03774. Multimodal deep model (ảnh + spatial/temporal/ecological context + taxonomic hierarchy) nhận dạng loài từ ảnh community-scientist; "performance gained over 6 points" so classifier ảnh-only → tiền lệ "gộp ngữ cảnh + phân cấp giúp long-tail plant", khớp việc ViMeLeaf gộp nhiều khung hình video lúc suy luận.
