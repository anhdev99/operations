# Dàn ý chi tiết — Bài 1 ViMeLeaf (data paper)

Issue: RES-47 (con RES-37). Nộp: Computers and Electronics in Agriculture, hạn 2027-01-31.
Nguồn đầu vào: `vimeleaf-p1-cea-structure.md` (RES-40), `brief-vimeleaf-novelty.md` (RES-29), plan RES-37. Số liệu nền RES-30 (trung vị 49 ảnh/tên, 102 tên < 100 ảnh).

## Câu đóng góp chính (gợi ý)

ViMeLeaf là bộ dữ liệu ảnh cây thuốc Việt Nam đầu tiên (62.102 ảnh, ~165 loài, 3 tỉnh An Giang/Tây Ninh/Đồng Tháp) được (1) khử trùng có log nhóm, (2) chia split chống rò rỉ theo nhóm trùng + đợt chụp, và (3) đo được độ thổi phồng accuracy do ảnh trùng — điểm mới so với mọi dataset cây/cây thuốc đã công bố (CWD30, PAGS8, TCMP-300, VNPlant-200...). Không bài nào đo "độ thổi phồng" cho ảnh cây thuốc.

## 1. Abstract
- Quy mô: 62.102 ảnh + 268 video, ~165 loài, 3 tỉnh; 195 thư mục (tên cây địa phương).
- Đóng góp: khử trùng (log 37.980 ảnh gần trùng + 4.188 rác), split chống rò rỉ (theo nhóm trùng + đợt chụp An Giang gốc ↔ bổ sung v1, 30 loài), baseline 3 model × 3 seed, đo chênh lệch accuracy split ngẫu nhiên (trước khử trùng) vs split sạch.
- Kết quả headline: [chỗ trống — số liệu từ RES-28/RES-30: độ thổi phồng accuracy = ? điểm, ghi kèm lệnh tái lập + seed].
- Nơi lưu + giấy phép: [Zenodo — chưa kiểm chứng, chờ board duyệt chi phí], đề xuất CC BY 4.0 (theo PAGS8; CWD30 không ghi → tránh).

## 2. Introduction
- 2.1 Bối cảnh: nhận dạng cây thuốc nam bằng DL; ý nghĩa nông nghiệp/dược liệu; cây thuốc VN ít dataset (trích RES-29: TCMP-300 từ web, VNPlant-200 chưa kiểm chứng, IndoHerb/MedLEA nước khác).
- 2.2 Vấn đề: ảnh trùng trong train/val làm accuracy thổi phồng. Tiền lệ: Barz & Denzler (A8, ciFAIR: test trùng train → accuracy tụt 9-14%); chưa bài nào đo trên dataset cây thuốc.
- 2.3 Khoảng trống (gap): chưa có data paper ảnh cây thuốc VN có split chống rò rỉ theo nhóm trùng (RES-29: tìm arXiv `deduplication + plant` → 0 kết quả phù hợp).
- 2.4 Đóng góp của bài (3 điểm như câu chính).

## 3. Data Collection and Properties (theo CWD30 §III + PAGS8 §2)
### 3.1 Taxonomy & danh mục loài
- ~165 loài từ 195 thư mục tên địa phương; taxonomy kingdom→species (phụ lục, theo CWD30).
- Xung đột nhãn đã biết: Dây giác/Sục sạc (RES-30) → ghi rõ xử lý, metadata 80 loài.
- **Bảng 1** (theo Table 1 PAGS8 / Table I CWD30): thống kê dataset — số ảnh/loài, phân bố (trung vị 49 ảnh/tên, 102/195 tên < 100 ảnh = đuôi dài), so với TCMP-300/VNPlant-200/CWD30 (cột so sánh theo RES-40).
- **Hình 1** (theo Fig. 1 CWD30): ví dụ ảnh, 2-3 ảnh/loài × N loài đại diện. LUẬT: không đưa ảnh vào git → dẫn link Zenodo + thumbnail không có PII.
- **Hình 2**: histogram số ảnh theo loài (đuôi dài).

### 3.2 Data collection (thu thập)
- 3 tỉnh An Giang/Tây Ninh/Đồng Tháp + 2 đợt bổ sung; thiết bị (điện thoại/camera — ghi theo manifest RES-30), thời gian, người thu (ẩn danh theo luật dữ liệu).
- 268 video (cắt khung) — mô tả nguồn.

### 3.3 Data filtering & deduplication (log khử trùng)
- Pipeline RES-26: phát hiện ảnh gần trùng (phash/dhash), log `deleted_near_dups_log.csv` (37.980 ảnh) + rác (4.188).
- **Giữ log "trước khử trùng"** để phần 4-5 đo được độ thổi phồng (điểm mới so với CWD30/PAGS8 — 2 bài này không đo).
- Lọc mờ/nhiễu (theo CWD30 3.C).

### 3.4 Data splits (split chống rò rỉ — điểm khác biệt chính)
- Split theo **nhóm trùng** (log `kept_path`) + theo **đợt chụp** (An Giang gốc ↔ bổ sung v1, 30 loài) — theo RES-40 "phần mới so với mọi bài đã đọc".
- So sánh: CWD30 K-fold micro-class (không theo nhóm trùng), PAGS8 stratified Monte Carlo theo metadata/vị trí (không theo nhóm trùng).
- Tỷ lệ train/val/test: [chỗ trống — RES-30/RES-28, ghi seed + lệnh tái lập].

## 4. Experiments and Evaluation (theo CWD30 §IV + PAGS8 §2.4)
### 4.1 Baseline
- 3 model (ResNet-50/EfficientNet-B0 + 1 kiến trúc theo CWD30 Table IV: CNN hoặc ViT; ghi repo link + phiên bản như PAGS8 Table 2), 3 seed mỗi model.
- Hyperparameter theo CWD30 (AdamW, batch 32, lr, cosine decay, 50 epochs, PyTorch) — [chỗ trống: config thực từ RES-28].
- Scratch vs ImageNet pretrain (theo CWD30).
### 4.2 Thiết kế đo thổi phồng
- Chạy baseline trên (a) split ngẫu nhiên **trước khử trùng** (chứa trùng) và (b) split **sạch** (chống rò rỉ).
- Chênh lệch accuracy = độ thổi phồng. Metric phù hợp đuôi dài (102/195): per-class mean accuracy + macro-F1 (theo RES-40), không chỉ overall accuracy.
- [Chỗ trống: kết quả từ RES-28/RES-30 + lệnh tái lập + seed theo luật repo].
### 4.3 Phân tích
- Theo nhóm loài dễ nhầm (Dây giác/Sục sạc), theo giai đoạn/điều kiện chụp nếu có.

## 5. Results and Discussion
- **Bảng 2** (theo Table IV CWD30 / Table 3 PAGS8): kết quả baseline 3 model × 3 seed (F1/accuracy, scratch vs pretrain).
- **Bảng 3**: so sánh split trước khử trùng vs split sạch → chênh lệch accuracy per model.
- **Hình 3**: đường cong accuracy theo tỉ lệ ảnh trùng (nếu có số liệu tỉ lệ — chưa kiểm chứng).
- Discussion: so CWD30/PAGS8 (không có split chống trùng → baseline của họ cũng có thể bị thổi phồng), so TCMP-300 (A2: lọc trùng bằng VLM+người, không công bố split theo nhóm), so Barz & Denzler (A8: CIFAR, tụt 9-14% tương đối).
- Giới hạn: 3 tỉnh (không toàn quốc), đuôi dài 102/195 loài, video chưa khai thác hết.

## 6. Data Availability and Licensing (theo RES-40 bảng so sánh)
- Nơi lưu: Zenodo [chờ duyệt chi phí — ghi "chưa kiểm chứng"], manifest + log khử trùng + split files công khai.
- Giấy phép: đề xuất CC BY 4.0 (PAGS8 có, CWD30 thiếu → ghi rõ tránh như họ).
- Tái lập: lệnh + seed (luật repo: mọi số liệu kèm lệnh tái lập + seed; pipeline RES-26, baseline RES-28).

## 7. Conclusion
- Tóm 3 đóng góp; khuyến nghị: split chống rò rỉ theo nhóm trùng nên là tiêu chuẩn cho dataset ảnh cây; hướng tới Bài 2 (cặp dễ nhầm + từ chối) và Bài 3 (KG + GraphRAG an toàn).

## References (đã kiểm chứng trong RES-29/RES-40, trích bắt buộc)
- A8 Barz & Denzler 2019 (ciFAIR, arXiv:1902.00423) — điểm gốc "đo thổi phồng do trùng".
- A9 Morra & Lamberti 2019 (arXiv:1907.02821) — công cụ khử trùng.
- A2 TCMP-300 (DOI 10.1038/s41597-025-05522-7) + A1 VNPlant-200 (ghi "chưa kiểm chứng" nếu chưa mở bài gốc).
- CWD30 (DOI 10.1016/j.compag.2024.109737), PAGS8 (DOI 10.1016/j.compag.2024.108622).
- A3-A7 (IndoHerb, P7, MedLEA, Nepal, Indian self-curated) — so sánh dataset cây thuốc.

## Chỗ trống số liệu (issue nào cung cấp)
| Dữ liệu | Issue nguồn | Trạng thái |
|---|---|---|
| Chênh lệch accuracy (split trước/sau khử trùng) | RES-28 (chạy thử) | chưa kiểm chứng — Builder chạy kèm seed |
| Phân bố ảnh/loài chính xác | RES-30 (manifest) | đã có: trung vị 49, 102/195 <100 |
| Config baseline 3 model | RES-28 | chưa kiểm chứng |
| Zenodo DOI | Board duyệt chi phí | chưa kiểm chứng |
