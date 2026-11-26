# Cấu trúc 3 bài CEA (2023–2025) về dataset/nhận dạng cây — khung cho Bài 1 ViMeLeaf

Issue: RES-40 (con RES-37). Ngày: 2026-11-26. Người làm: Scholar.
Mục đích: lấy mẫu "bài CEA công bố bộ dữ liệu ảnh cây/loài có baseline + split" để dựng dàn ý khung cho **Bài 1 ViMeLeaf** (data paper, nộp CEA hạn 2027-01-31).

Lưu ý đọc: cả 3 bài đều là bài "dataset + benchmark" kiểu IEEE/Elsevier 2 cột (trừ arXiv preprint 1 cột), có bảng thống kê dataset, hình ví dụ, baseline nhiều model. Chưa có bài nào đo **rò rỉ do ảnh trùng** — đúng khoảng trống mà Bài 1 lấp.

---

## Bài 1: CWD30 — dataset benchmark nhận dạng cây trồng/cỏ dại

- **DOI**: https://doi.org/10.1016/j.compag.2024.109737 (CEA vol. 229, 109737, đăng 2025; preprint arXiv:2305.10084, đã đọc PDF đầy đủ)
- **Tác giả/tổ chức**: Ilyas T. et al., Jeonbuk National University + Rural Development Administration (Hàn Quốc)
- **Loại**: bài công bố bộ dữ liệu (219.778 ảnh, 30 loài: 10 cây trồng + 20 cỏ dại) kèm baseline
- **Độ dài**: ~13 trang (IEEE 2 cột), 6 mục chính, nhiều bảng/hình

### Cấu trúc mục (heading)
1. Abstract (nêu quy mô dataset, số loài, baseline)
2. I. Introduction
3. II. Related Works (nhận dạng cây/cỏ, so dataset)
4. III. Data Collection, Preprocessing and Properties
   - A. Taxonomic System Establishment (hệ phân cấp: cây trồng chia EC/FC, cỏ chia grass/broadleaf/sedge; taxonomy đầy đủ kingdom→species trong phụ lục)
   - B. Data Collection (5 nhóm, nhiều thiết bị: Canon SX740/EOS-200D/Android/iPhone/DJI Mavic Pro 2; 2020–2022; xoay nhóm hàng tháng)
   - C. Data Filtering, Labelling and Distribution (5 chuyên gia rà mỗi tháng; xoá ảnh mờ/nhiễu; phân bố 210–12.782 ảnh/loài)
   - D. Data Splits (K-fold K=3; train 74.724 / val 72.526 / test 72.526; tỷ lệ 0.33:0.33:0.34; **split ở mức micro-class**, cân bằng theo lớp nhỏ nhất)
   - E. Viewing Angles and Growth Stages (góc chụp, giai đoạn 8 tuần seedling→trưởng thành; ảnh cả cây, không chỉ lá)
   - F. Comparison with Other Datasets (so sánh với dataset khác)
5. IV. Experiments and Evaluation (AdamW, batch 32, lr 6e-5, cosine decay, 50 epochs, PyTorch, RTX-3090; metric: per-class mean accuracy, F1, mIoU cho segmentation; so sánh scratch vs ImageNet-1K pretrain)
6. V. Results and Discussion (ResNet-101/MobileNetv3-L/EfficientNetv2-M/ViT/SwinViT/MaxViT; MaxViT tốt nhất F1 84.91 / Acc 91.45 với ImageNet; CWD30 pretrained backbone cải thiện task downstream)
7. VI. Conclusion
- Dữ liệu: https://github.com/Mr-TalhaIlyas/CWD30 (link download: cwd-30.github.io/cwd-30/download.html)

### Bảng/hình bắt buộc (mô hình theo)
- Bảng thống kê dataset (số ảnh/loài, so với dataset khác — Table I)
- Bảng phân bố loài (Table II, III; hình radar phân bố theo giai đoạn tăng trưởng)
- Hình ví dụ ảnh (Fig. 1)
- Bảng baseline nhiều kiến trúc (Table IV: F1/Acc, scratch vs ImageNet)
- Hình so tham số/bộ nhớ/đặc trưng (Fig. 9, 10), t-SNE (Fig. 11)

### Thu thập + giấy phép + nơi lưu
- Mô tả thu thập rất chi tiết (nhóm, thiết bị, thời gian, địa điểm, quá trình lọc/ghi nhãn)
- **Giấy phép: không ghi rõ** (chỉ nói "open access"; GitHub repo không có LICENSE nhìn thấy được)
- Nơi lưu: GitHub + trang download riêng

### Metric
Per-class mean accuracy (cân bằng lớp), F1 (vì mất cân bằng), mIoU (segmentation downstream), accuracy.

---

## Bài 2: PAGS8 / Palmer amaranth growth stages (CEA, đã đọc đầy đủ qua arXiv CC-BY + tr. CSU)

- **DOI**: https://doi.org/10.1016/j.compag.2024.108622 (CEA vol. 217, 1-16, 02/2024; arXiv:2307.15816)
- **Tác giả**: Coleman GRY, Kutugata M, Walsh MJ, Bagavathiannan M (Univ. of Sydney + Texas A&M)
- **Loại**: bài benchmark nhận dạng giai đoạn tăng trưởng 8 lớp của A. palmeri (cỏ dại) trong cotton, so 26 biến thể YOLO; **công bố dataset mở PAGS8**
- **Độ dài**: 27 trang (1 cột)

### Cấu trúc mục (heading)
1. Abstract (nêu kết quả: mAP@[0.5:0.95] 47,34% 8 lớp, 67,05% 1 lớp; CAM; dataset PAGS8 open-access)
2. 1 Introduction (bối cảnh SSWC, phenotyping, CNN/YOLO; chỉ ra gap: ít nghiên cứu nhận dạng giai đoạn tăng trưởng)
3. 2 Materials and Methods
   - 2.1 Field Preparation (thí nghiệm Texas A&M, 2 đợt gieo 2021, hàng cotton 91,5 m, gieo A. palmeri thủ công)
   - 2.2 Image data collection (FLIR BlackFly BFS-70S7C-C 7,1 MP, ba lô tự chế + Jetson Nano, Python script; ghi lại metadata chụp)
   - 2.3 Annotation (LabelImg, PASCAL VOC → YOLO; 1.228 ảnh, 5.026 instances; 8 giai đoạn + phân bố instances + kích thước hộp trong Table 1; chiến lược gộp 8→3 lớp theo đặc trưng/kích thước)
   - 2.4–2.5 Algorithm training (26 biến thể YOLO v3–v8, Table 2 kèm link repo + ngày clone; Colab Pro+ A100; **5-fold stratified Monte Carlo, stratify theo metadata + vị trí đồng ruộng**; 30 epochs; 338 model)
   - 2.6 Class Activation Maps (Grad-CAM)
   - 2.7 Performance Metrics (precision, recall, mAP@[0.5:0.95], mAP@0.5; GFLOPS + hiệu năng/GFLOPS)
   - 2.8 Statistical Analysis (R, ANOVA + Tukey HSD, kiểm định bình thường, Bartlett)
4. 3 Results (3.1 so YOLO families; 3.2–3.3 giai đoạn vs kích thước ảnh; 3.4 số lớp + chiến lược ghi nhãn)
5. 4 Discussion (nên gộp lớp, CAM, hạn chế, cross-dataset)
6. 5 Conclusion
7. References (25–27 trang)
- **Dataset**: PAGS8, "first open-access benchmarking growth stage dataset", link: https://weed-ai.sydney.edu.au/datasets/5c78d067-8750-4803-9cbe-57df8fae55e4 (trang JS, chưa mở được chi tiết trong 60 phút — **chưa kiểm chứng sâu hơn**)

### Bảng/hình bắt buộc
- Table 1: thống kê 8 giai đoạn (số instances, kích thước bounding box ± SE)
- Table 2: 26 biến thể YOLO (repo link, ngày clone)
- Table 3: kết quả baseline đầy đủ (Precision/Recall/mAP0.5/mAP@[0.5:0.95]/GFLOPS/Efficiency, 1 lớp vs 8 lớp)
- Hình: thiết bị chụp (Fig. 1), so hiệu năng YOLO (Fig. 2), CAM

### Thu thập + giấy phép + nơi lưu
- Thu thập mô tả rõ (địa điểm, thiết bị, quy trình, annotation, stratify theo metadata + vị trí)
- **Giấy phép: bản đăng CEA vol. 217 ghi CC BY trên tr. CSU** (bản arXiv preprint CC BY 4.0)
- Nơi lưu: website weed-ai.sydney.edu.au

### Metric
Precision, Recall, mAP@[0.5:0.95], mAP@0.5, GFLOPS, efficiency (mAP/GFLOPS), sai số chuẩn n=5, ANOVA.

**Điểm khác CWD30 và đáng chú ý cho Bài 1**: có **split chống trộn (stratified Monte Carlo theo metadata + vị trí)** — gần nhất với tinh thần "split chống rò rỉ" của ViMeLeaf, nhưng stratify theo metadata/vị trí, không theo nhóm ảnh trùng.

---

## Bài 3: Wheat3D PartNet — dataset 3D point cloud lúa mì (chỉ đọc được metadata + abstract, chưa có PDF đầy đủ)

- **DOI**: https://doi.org/10.1016/j.compag.2025.110697 (CEA vol. 238, 1-20, đăng 11/2025)
- **Tác giả**: Reena R. et al., Edge Hill University + Aberystwyth
- **Loại**: công bố bộ dữ liệu 1.303 mô hình 3D (point cloud) lúa, 3 giống (Paragon, Gladius, Apogee), 2 lớp nhãn (ears/non-ears), tái dựng từ ảnh RGB đa góc, 2 điều kiện (hạn hán/tưới)
- **Truy cập**: PDF publisher bị chặn bot (Cloudflare 403); **chưa kiểm chứng** nội dung phần methods/results — chỉ ghi nhận được abstract + metadata (OA hybrid, CC BY)

### Cấu trúc mục (dự đoán theo khuôn mẫu 2 bài trên, CHƯA XÁC NHẬN)
Intro → Data acquisition/3D reconstruction → Annotation → Baselines (3D DL models) → Results → Conclusion

### Ghi chú cho Bài 1
- Ít liên quan trực tiếp (3D point cloud, không ảnh 2D; 2 lớp, không nhận dạng loài)
- Giá trị: sample "data paper thuần" trên CEA, CC BY, có data availability
- Nếu cần đọc sâu: cần board/Dean cấp quyền truy cập hoặc đọc tay

---

## Khung đề xuất cho Bài 1 ViMeLeaf (gộp từ 3 bài)

Dựa vào CWD30 (chuẩn "dataset + baseline" CEA) + PAGS8 (split chống trộn + baseline detection), dàn ý khung:

1. **Abstract**: quy mô (62.102 ảnh + 268 video, ~165 loài, 3 tỉnh), đóng góp chính (khử trùng, split chống rò rỉ, đo accuracy thổi phồng), baseline, nơi lưu + giấy phép
2. **1. Introduction**: bối cảnh nhận dạng cây thuốc nam, vấn đề ảnh trùng làm accuracy thổi phồng, gap (chưa có data paper ảnh cây thuốc VN có split chống rò rỉ theo nhóm trùng — theo RES-30: TCMP-300 gần nhất nhưng không công bố split)
3. **2. Data Collection and Properties** (theo CWD30 §III):
   - Thu thập: 3 tỉnh An Giang/Tây Ninh/Đồng Tháp + 2 đợt bổ sung, thiết bị, thời gian
   - Lọc/khử trùng: log 37.980 ảnh gần trùng + 4.188 rác (giữ lại "trước khử trùng" để đo)
   - Phân bố: 195 thư mục → ~165 loài, trung vị 49 ảnh, 102/195 lớp < 100 ảnh (đuôi dài) — **bảng thống kê + hình ví dụ (như Table 1 PAGS8 / Fig. CWD30)**
   - Xung đột nhãn (Dây giác/Sục sạc), metadata 80 loài
   - Split: theo nhóm trùng (log `kept_path`) + theo đợt chụp (An Giang gốc ↔ bổ sung v1, 30 loài) — phần mới so với mọi bài đã đọc
4. **3. Experiments and Evaluation**: baseline 3 model (ResNet/EfficientNet hoặc CNN+ViT kiểu CWD30 Table IV) × 3 seed; so split ngẫu nhiên (trước khử trùng) vs split sạch; đo chênh lệch accuracy = độ thổi phồng
5. **4. Results and Discussion**: bảng baseline, bảng so split, phân tích theo nhóm loài dễ nhầm
6. **5. Data Availability and Licensing**: nơi lưu (Zenodo, chờ duyệt chi phí — ghi "chưa kiểm chứng" nếu chưa có), giấy phép (đề xuất CC BY 4.0 như PAGS8; CWD30 không ghi → tránh), cách tái lập (lệnh + seed theo luật repo)
7. **6. Conclusion**

### Bắt buộc có (so 3 bài)
| Hạng mục | CWD30 | PAGS8 | Wheat3D | → Bài 1 ViMeLeaf |
|---|---|---|---|---|
| Bảng thống kê dataset (số ảnh/loài/phân bố) | ✓ | ✓ (Table 1) | chưa kiểm | ✓ (theo manifest) |
| Hình ví dụ ảnh | ✓ | ✓ | chưa kiểm | ✓ (không đưa ảnh vào git — dẫn Zenodo) |
| Baseline nhiều model + bảng kết quả | ✓ (Table IV) | ✓ (Table 3, 26 YOLO) | chưa kiểm | ✓ (3 model × 3 seed) |
| Split được mô tả | ✓ (K=3, micro-class) | ✓ (5-fold stratified MC) | chưa kiểm | ✓✓ (nhóm trùng + đợt chụp) |
| Thu thập chi tiết (thiết bị, thời gian, lọc nhãn) | ✓ | ✓ | chưa kiểm | ✓ (theo manifest) |
| Giấy phép ghi rõ | ✗ | ✓ (CC BY) | ✓ (CC BY) | ✓ (đề xuất CC BY 4.0) |
| Nơi lưu dữ liệu | ✓ (GitHub) | ✓ (website) | ? | ✓ (Zenodo, chờ duyệt) |
| Metric phù hợp mất cân bằng | ✓ (per-class acc, F1) | mAP@[0.5:0.95] | ? | per-class acc + macro-F1 (đuôi dài 102/195) |
| Đo rò rỉ/trùng ảnh | ✗ | ✗ (chỉ stratify) | ? | **✓ (điểm mới)** |

### Số liệu cần kèm lệnh tái lập (theo luật, chưa chạy trong issue này — việc của Builder)
- 62.102 ảnh / 268 video / 195 thư mục / trung vị 49 / 102 lớp <100 / 37.980 trùng: đọc `E:\ViMeLeaf_Dataset` (manifest.csv, deleted_near_dups_log.csv) — có trong topic `topics/vimeleaf-3-paper-series.md` (RES-29/30 đã đo, chưa kiểm chứng lại ở issue này)
