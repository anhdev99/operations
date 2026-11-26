# Brief: Dựng mô hình 3D răng hàm từ ảnh 2D (RES-17)

Người soạn: Scholar · Ngày: 2026-11-24 · Dùng cho: RES-14 (Dean tổng hợp)

## Cách kiểm chứng

- Mọi bài dưới đây đã mở trang abstract qua arXiv API (`export.arxiv.org/api/query?id_list=...`) trong lượt này. Chỉ đọc **abstract + README/trang dataset**, chưa đọc toàn văn. Số liệu trích đúng như abstract.
- Dataset: đã mở trang chính thức (Ditto/UNIMORE, trang Teeth3DS+, OSF API, GitHub API). Giấy phép ghi đúng như trang hiển thị.
- Nơi công bố: xác minh tồn tại qua Crossref (`api.crossref.org/journals/<ISSN>`). **Scopus/SJR chưa tra trực tiếp** (OpenAlex hết hạn mức, SCImago chặn truy cập tự động). Chủ nhóm cần tra lại trước khi nộp.
- Văn bản pháp lý Việt Nam (mục đạo đức) **chưa mở trong lượt này**: ghi "chưa kiểm chứng", cần chủ nhóm hoặc phòng khám xác nhận.
- Điểm nối với RES-1/RES-2 (`top5-de-tai.md`, `brief-cv-dental.md`): hai brief đó làm **2D** (báo cáo panoramic tiếng Việt, phát hiện bệnh lý DENTEX, landmark cephalometric). Brief này chỉ làm **2D → 3D**, không trùng.

## Dữ kiện mới từ chủ nhóm (comment Dean, RES-14)

Chủ nhóm **chưa có phòng khám/bệnh viện hợp tác**; mục tiêu là làm demo để **đem đi đề xuất cho một phòng khám**. Vì vậy:
- Giai đoạn 1 của mọi đề tài chỉ dùng **dữ liệu công khai**, kết thúc bằng demo chạy được.
- Có mục "Gói đề xuất cho phòng khám" và bảng "làm được khi không có dữ liệu riêng hay không".

---

## 1. "Độ chính xác 99%" thực tế là bao nhiêu?

"99%" không phải một chỉ số. Mỗi bài đo khác nhau, và các số công bố cho **tái tạo 3D từ một ảnh 2D** còn xa 99%:

| Bài toán | Bài (đã mở) | Chỉ số công bố (theo abstract) |
|---|---|---|
| Panoramic → răng 3D | X2Teeth, Liang 2021 | IoU 0,681 |
| Panoramic → răng 3D (point cloud) | PX2Tooth, Ma 2024 | IoU 0,793 (499 cặp PX-CBCT) |
| Panoramic → khối CBCT | HyDAR-Pano3D, Yue 2026 | PSNR 25,76 dB; SSIM 85,70%; Dice giải phẫu tổng 83,83%; Dice răng 82,4%; ống thần kinh răng dưới 72,2% |
| 10 ảnh trong miệng → mô hình hàm trên | Cho 2026 | "accuracy" 77,49% (tỉ lệ đỉnh khớp láng giềng gần nhất trong ngưỡng 0,035, đơn vị chuẩn hoá) |
| **So sánh:** phân đoạn răng trên CBCT (có 3D thật) | Hao 2022 (DDMA) | Dice 93,99%, IoU 88,68% |
| **So sánh:** phân đoạn răng trên scan 3D trong miệng | 3DTeethSeg'22 (trang leaderboard) | TSA (F1 trung bình) tốt nhất 0,9859 |

Nhận xét:
- 98-99% chỉ thấy ở bài toán **có sẵn dữ liệu 3D** (phân đoạn CBCT/scan). Từ **một ảnh 2D**, mức công bố là IoU 0,68-0,79 hoặc Dice ~0,82 cho răng; chân răng và ống thần kinh kém hơn thân răng.
- Không có bài nào trong danh sách trên báo cáo sai số theo **mm** trong abstract (X-Splat có đề xuất thước đo hình học BA-ASD nhưng abstract không ghi số). Sai số mm là chỗ trống đáng đo.

**Đề xuất cách đặt mục tiêu đúng** (thay "99%"):
1. Báo cáo theo **từng răng và từng vùng** (thân răng / chân răng / xương / ống thần kinh), không gộp.
2. Chỉ số chính: Dice/IoU từng răng; **ASSD và Hausdorff 95% tính bằng mm**; sai số chiều dài chân răng (mm); với ảnh trong miệng: Chamfer (mm) và sai số vị trí tâm răng (mm) so với scan 3D.
3. Mục tiêu dạng "≥ X% số răng có sai số bề mặt < 1 mm" — ngưỡng cụ thể phải hỏi bác sĩ (dùng để xem/tư vấn khác với dùng để cắm implant). **Ngưỡng 1 mm là ví dụ, chưa kiểm chứng theo hướng dẫn lâm sàng.**
4. Kèm **bản đồ độ tin cậy**: chỗ nào mô hình không chắc thì tô màu, để bác sĩ biết không được dựa vào. Đây là cách trung thực thay cho con số 99%.
5. Nói rõ với phòng khám: mô hình 3D từ ảnh 2D là **để xem và tư vấn**, không thay CBCT cho phẫu thuật.

---

## 2. Dữ liệu công khai (đã mở trang)

| Tên | Link | Giấy phép / truy cập | Kích thước | Dùng cho |
|---|---|---|---|---|
| ToothFairy3 | https://ditto.ing.unimore.it/toothfairy3/ | CC BY-NC-SA 4.0; cần tạo tài khoản | 532 khối CBCT (NIfTI, Hounsfield), 77 lớp nhãn (răng theo FDI, xương hàm, ống thần kinh, xoang, tuỷ/chân răng, implant...); 2 máy chụp | Mô phỏng panoramic từ CBCT → cặp 2D-3D tổng hợp (Đề tài 1, 3) |
| ToothFairy2 | https://ditto.ing.unimore.it/toothfairy2/ | CC BY-NC-SA 4.0; cần tài khoản; trang ghi "không còn cập nhật, dùng ToothFairy3" | 480 khối, 42 lớp | Thay thế nếu cần |
| Teeth3DS+ | https://crns-smartvision.github.io/teeth3ds · dữ liệu https://osf.io/xctdy/ | OSF công khai; giấy phép ghi "Other" (không rõ loại) — **chưa kiểm chứng điều khoản cụ thể** | 1.800 scan trong miệng của 900 bệnh nhân (hàm trên/dưới riêng), 23.999 răng có nhãn FDI, ~30.000 landmark (theo mô tả OSF) | Render ảnh "giả chụp điện thoại" → cặp ảnh-mesh (Đề tài 2, 3) |
| STS 2023 (2D panoramic + 3D CBCT) | bài https://arxiv.org/abs/2407.13246 | Theo abstract là challenge MICCAI 2023 trên Tianchi; điều kiện tải **chưa kiểm chứng** | chưa kiểm chứng | Panoramic thật để thử khoảng cách miền (không ghép cặp) |
| DENTEX (đã kiểm chứng ở RES-2) | https://huggingface.co/datasets/ibrahimhamamci/DENTEX | CC BY-NC-SA 4.0 | ~2.300 ảnh panoramic có nhãn + 1.571 không nhãn | Panoramic thật, không có 3D: dùng để thử chuyển miền ảnh thật → ảnh mô phỏng |

**Không tìm thấy** dataset công khai nào ghép cặp **panoramic thật ↔ CBCT** cùng bệnh nhân, hay **ảnh điện thoại thật ↔ scan 3D** cùng bệnh nhân. Các bộ ghép cặp thật trong bài (PX2Tooth 499 cặp, HiCT 500 cặp, DentalSplat/Dental3R 950 ca) đều là dữ liệu riêng. Đây chính là thứ cần phòng khám.

Tất cả bộ CBCT trên là **phi thương mại (NC-SA)** → demo và bài báo được, sản phẩm thương mại thì không.

---

## Đề tài 1: Panoramic → mô hình răng hàm 3D có bản đồ độ tin cậy, huấn luyện hoàn toàn trên cặp mô phỏng từ CBCT công khai

**Câu hỏi nghiên cứu.** Mô hình tái tạo 3D từ một ảnh panoramic, huấn luyện chỉ trên ảnh panoramic mô phỏng từ CBCT công khai, đạt sai số bề mặt bao nhiêu mm theo từng răng và từng vùng (thân/chân răng, ống thần kinh)? Độ bất định dự đoán có khớp với sai số thật (calibration) để bác sĩ biết vùng nào không tin được không?

**Khoảng trống (bài đã mở):**
1. Park S. et al., 2023, *NeBLa: Neural Beer-Lambert for 3D Reconstruction of Oral Structures from Panoramic Radiographs*, AAAI 2024 (theo README repo). https://arxiv.org/abs/2304.04027 · code MIT https://github.com/sihwa-park/nebla. Mô phỏng panoramic (SimPX) từ CBCT theo định luật Beer-Lambert, **không cần cặp PX-CBCT thật**. **Chưa làm:** không báo bất định; repo chỉ có lớp mô hình lõi, không có pipeline đầy đủ.
2. Szczepanski T. et al., 2026, *X-Splat: Gaussian Splatting for 3D CBCT Generation from Single Panoramic Radiograph*, arXiv. https://arxiv.org/abs/2607.02099. Huấn luyện trên cặp tổng hợp từ **ToothFairy3**, đề xuất thước đo hình học dựa trên phân đoạn. **Chưa làm:** code "sẽ phát hành khi được nhận" (README); không đo bất định; không thử trên panoramic thật ghép cặp.
3. Yue Y. et al., 2026, *HyDAR-Pano3D*, arXiv. https://arxiv.org/abs/2605.20827. Dice răng 82,4%, ống thần kinh 72,2%. **Chưa làm:** không có bản đồ tin cậy; cần 3 dataset lớn.
4. Ma W. et al., 2024, *PX2Tooth: Reconstructing the 3D Point Cloud Teeth from a Single Panoramic X-ray*, arXiv. https://arxiv.org/abs/2411.03725. IoU 0,793 trên 499 cặp riêng. **Chưa làm:** dữ liệu riêng, không công khai; không báo sai số mm.

Chỗ trống cụ thể: **pipeline nhẹ, tái lập hoàn toàn trên dữ liệu công khai + đo sai số mm theo vùng + bất định có hiệu chuẩn**. Bài liên quan khác đã mở: Oral-3D (https://arxiv.org/abs/2003.08413), Oral-3Dv2 (https://arxiv.org/abs/2303.12123), X2Teeth (https://arxiv.org/abs/2108.13004), Occudent (https://arxiv.org/abs/2311.16524), ViT-NeBLa (https://arxiv.org/abs/2506.13195), K-U-KAN (https://arxiv.org/abs/2605.25163), HiCT (https://arxiv.org/abs/2604.00792), 3DPX (https://arxiv.org/abs/2409.18701) — mảng đông, nên điểm mới phải nằm ở **đo lường và độ tin cậy**, không phải kiến trúc mới.

**Dữ liệu.** Chủ nhóm chưa có dữ liệu riêng. Giai đoạn 1: ToothFairy3 (532 CBCT) → tự viết bộ mô phỏng panoramic (chiếu tia theo cung hàm hình móng ngựa, Beer-Lambert, như NeBLa/X-Splat mô tả) → cặp (ảnh 2D, nhãn 3D theo răng). Thử định tính trên panoramic thật của DENTEX (không có 3D, chỉ xem). Giai đoạn 2 (cần phòng khám): 50-100 cặp PX-CBCT thật để đo khoảng cách sim→thật.

**Baseline 1-2 tháng (GPU 12-16 GB):**
- Tuần 1-2: bộ mô phỏng panoramic từ CBCT (numpy/torch, có seed); kiểm tra bằng mắt + so histogram với DENTEX.
- Tuần 3-5: mô hình 2D → khối 3D độ phân giải thấp (U-Net 2D encoder + decoder 3D, hoặc dự đoán độ sâu theo tia như K-U-KAN/NeBLa); xuất nhãn theo răng. Downsample khối về 128³ để vừa GPU.
- Tuần 6-7: bất định bằng MC-dropout hoặc ensemble 3-5 mô hình nhỏ; đo calibration (ECE) giữa bất định và sai số.
- Tuần 8: đánh giá: Dice/IoU từng răng, ASSD & HD95 (mm), sai số chiều dài chân răng; chia train/test theo bệnh nhân và theo máy chụp (Set A/B vs Set C của ToothFairy3); 3 seed.

**Ứng dụng/demo.** Web (Gradio + trình xem 3D) cho nha sĩ: tải ảnh panoramic → xem hàm 3D xoay được, từng răng tô màu theo độ tin cậy, đo nhanh chiều dài chân răng. Dùng để **giải thích cho bệnh nhân** và sàng lọc trước khi quyết định chụp CBCT.

**Nơi công bố (Crossref đã xác nhận tồn tại; Scopus chưa tra):**
- Computers in Biology and Medicine (Elsevier, ISSN 0010-4825) — https://api.crossref.org/journals/0010-4825
- IEEE Journal of Biomedical and Health Informatics (IEEE, ISSN 2168-2194) — https://api.crossref.org/journals/2168-2194
- Dentomaxillofacial Radiology (Oxford University Press, ISSN 0250-832X) — https://api.crossref.org/journals/0250-832X

**Điểm:**
| Tiêu chí | Điểm | Lý do |
|---|---|---|
| Tính mới | 3 | Mảng có ≥10 bài; mới ở đo mm theo vùng + bất định có hiệu chuẩn, không ở kiến trúc. |
| Ứng dụng | 4 | Hình 3D xoay được rất dễ thuyết phục phòng khám; nhưng chỉ để xem/tư vấn, không dùng phẫu thuật. |
| Khả thi một người | 4 | Dữ liệu công khai đủ; CBCT 3D tốn GPU, phải hạ độ phân giải; tự viết bộ mô phỏng mất 2 tuần. |
| Công bố | 4 | Kết quả tái lập trên dữ liệu công khai + câu chuyện "trung thực về độ chính xác" hợp tạp chí ứng dụng. |
| Hồ sơ NCS | 5 | Chuỗi tự nhiên: bài 1 sim công khai → bài 2 kiểm chứng trên dữ liệu phòng khám → bài 3 nối báo cáo panoramic tiếng Việt (RES-2) với hình 3D. |
| **Tổng** | **20/25** | |

**Rủi ro:** khoảng cách ảnh mô phỏng ↔ panoramic thật lớn (NeBLa phải thêm bước dịch ảnh); X-Splat/HyDAR có thể công bố code và vượt xa; CBCT công khai có ít ca mất răng/răng lệch kiểu người Việt; NC-SA cấm thương mại.

---

## Đề tài 2: Ảnh điện thoại trong miệng (3-5 góc chuẩn chỉnh nha) → mô hình răng 3D, đánh giá theo mm so với scan 3D

**Câu hỏi nghiên cứu.** Từ 3-5 ảnh trong miệng chụp bằng điện thoại theo quy trình chỉnh nha (chính diện, hai bên má, mặt nhai), mô hình răng 3D dựng được sai bao nhiêu mm so với scan trong miệng, theo từng răng? Dùng mesh khuôn mẫu theo răng (template) có ổn định hơn 3DGS/NeRF không ghép mẫu khi chỉ có ít góc chụp?

**Khoảng trống (bài đã mở):**
1. Xu C. et al., 2024, *TeethDreamer: 3D Teeth Reconstruction from Five Intra-oral Photographs*, MICCAI 2024 (theo mô tả repo). https://arxiv.org/abs/2407.11419 · code MIT https://github.com/ShanghaiTech-IMPACT/TeethDreamer. Dùng diffusion sinh thêm góc nhìn rồi dựng bề mặt. **Chưa làm:** abstract không công bố dữ liệu huấn luyện; mô hình diffusion lớn, nặng GPU.
2. Miao Y. et al., 2025, *DentalSplat: Dental Occlusion Novel View Synthesis from Sparse Intra-Oral Photographs*, arXiv. https://arxiv.org/abs/2511.03099. 3DGS từ 3 ảnh, 950 ca lâm sàng + 195 ca video. **Chưa làm:** đánh giá theo **chất lượng ảnh góc mới** (novel view synthesis), không đo sai số hình học mm so với scan; dữ liệu riêng.
3. Miao Y. et al., 2025, *Dental3R: Geometry-Aware Pairing for Intraoral 3D Reconstruction from Sparse-View Photographs*, arXiv. https://arxiv.org/abs/2511.14315. Pipeline không cần tư thế camera + 3DGS. **Chưa làm:** như trên, đo bằng chất lượng ảnh, không đo mm; dữ liệu riêng.
4. Cho J. et al., 2026, *Deep Learning-based 3D Oral Cavity Reconstruction Using 2D Intraoral Images*, arXiv. https://arxiv.org/abs/2606.05998. Huấn luyện trên **Teeth3DS** (950 mẫu hàm trên), 10 ảnh, "accuracy" 77,49%. **Chưa làm:** chỉ số tự đặt (ngưỡng chuẩn hoá 0,035), không mm, không theo răng; chính tác giả ghi điểm dự đoán phân bố không đều.

Chỗ trống cụ thể: **benchmark công khai, tái lập được, đo theo mm từng răng** cho "ít ảnh trong miệng → 3D" (bài 4 cho thấy Teeth3DS dùng được, nhưng làm còn thô).

**Dữ liệu.** Giai đoạn 1: Teeth3DS+ (1.800 scan, nhãn FDI từng răng) → render ảnh giả điện thoại theo 3-5 góc chuẩn (pyrender/pytorch3d, thêm màu men răng, đèn flash, mờ, banh môi) → cặp (ảnh, mesh, nhãn răng). Giai đoạn 2 (cần phòng khám): 30-50 bệnh nhân có **cả ảnh điện thoại và scan trong miệng cùng buổi** để đo trên dữ liệu thật.

**Baseline 1-2 tháng (GPU 8-12 GB):**
- Tuần 1-2: bộ render từ Teeth3DS+ (có seed, cố định góc theo quy trình chỉnh nha).
- Tuần 3-5: baseline A: mesh trung bình từng răng (từ Teeth3DS+) + mạng dự đoán vị trí/xoay/tỉ lệ từng răng từ ảnh (nhẹ). Baseline B: tái tạo kiểu Cho 2026 (MobileNetV2 + attention) để so.
- Tuần 6-7: thử thêm baseline TeethDreamer (code MIT) nếu chạy vừa GPU; nếu không, ghi rõ không chạy được.
- Tuần 8: Chamfer (mm), sai số tâm răng (mm), sai số trục răng (độ), F-score@1 mm; theo nhóm răng (cửa/nanh/cối); 3 seed; chia theo bệnh nhân.

**Ứng dụng/demo.** Ứng dụng web/điện thoại cho **chỉnh nha theo dõi từ xa**: bệnh nhân tự chụp 3-5 ảnh theo hướng dẫn → bác sĩ xem mô hình 3D và so với lần khám trước. Cho phòng khám nhỏ không có máy scan trong miệng.

**Nơi công bố (Crossref đã xác nhận; Scopus chưa tra):**
- Journal of Dentistry (Elsevier, ISSN 0300-5712) — https://api.crossref.org/journals/0300-5712
- IEEE Access (IEEE, ISSN 2169-3536) — https://api.crossref.org/journals/2169-3536
- Computers in Biology and Medicine (như trên)

**Điểm:**
| Tiêu chí | Điểm | Lý do |
|---|---|---|
| Tính mới | 4 | Các bài 3DGS đo chất lượng ảnh; chưa thấy benchmark công khai đo mm theo răng (tìm arXiv, chưa rà Google Scholar). |
| Ứng dụng | 5 | Điện thoại thay máy scan cho theo dõi chỉnh nha; phòng khám nhỏ hiểu ngay giá trị. |
| Khả thi một người | 4 | Teeth3DS+ tải tự do, render + mạng nhẹ vừa GPU nhỏ; khoảng cách ảnh render ↔ ảnh thật là phần khó. |
| Công bố | 4 | Benchmark + baseline tái lập là loại bài tạp chí ứng dụng nhận tốt. |
| Hồ sơ NCS | 4 | Chuỗi: benchmark tổng hợp → kiểm chứng trên dữ liệu phòng khám → app theo dõi chỉnh nha; ít nối với RES-2 hơn Đề tài 1. |
| **Tổng** | **21/25** | |

**Rủi ro:** giấy phép Teeth3DS+ ghi "Other" chưa rõ có cho tạo dữ liệu phái sinh không; ảnh render khác xa ảnh thật (nước bọt, phản chiếu, môi che); scan trong miệng không có chân răng nên mô hình chỉ có **thân răng**; nhóm DentalSplat/Dental3R có 950 ca thật có thể ra bài đo mm trước.

---

## Đề tài 3: Ghép ảnh trong miệng (thân răng) với panoramic (chân răng) thành mô hình răng đầy đủ

**Câu hỏi nghiên cứu.** Kết hợp thân răng 3D dựng từ ảnh điện thoại (Đề tài 2) với hình chân răng lấy từ panoramic có dựng được răng đầy đủ thân + chân với sai số chân răng thấp hơn dùng panoramic đơn lẻ không?

**Khoảng trống (bài đã mở):**
1. Yang Y. et al., 2022, *ToothInpaintor: Tooth Inpainting from Partial 3D Dental Model and 2D Panoramic Image*, arXiv. https://arxiv.org/abs/2211.15502. Dùng **scan 3D một phần + panoramic** dựng răng đầy đủ có chân. **Chưa làm:** đầu vào là scan trong miệng (máy đắt), không phải ảnh điện thoại; dữ liệu từ phòng khám, không công khai.
2. Hao J. et al., 2022, *AI-enabled Automatic Multimodal Fusion of CBCT and Intraoral Scans* (DDMA), arXiv. https://arxiv.org/abs/2203.05784. Ghép CBCT + scan, 503 CBCT và 28.559 scan. **Chưa làm:** cần CBCT; dữ liệu riêng.
3. Miao Y. et al., 2025, *Silhouette-to-Contour Registration: Aligning Intraoral Scan Models with Cephalometric Radiographs*, arXiv. https://arxiv.org/abs/2511.14343 (chỉ thấy tiêu đề trong kết quả tìm, **chưa đọc abstract** — không dùng để chấm).

**Dữ liệu.** Giai đoạn 1 chỉ làm được **một phần**: ToothFairy3 có cả thân và chân răng → cắt lấy "thân răng" giả làm scan, mô phỏng panoramic → ghép lại. Không có dữ liệu công khai nào có **ảnh điện thoại + panoramic + 3D** cùng bệnh nhân. Giai đoạn 2 **bắt buộc phòng khám**: bệnh nhân có ảnh trong miệng + panoramic + (CBCT hoặc scan) cùng đợt.

**Baseline:** chỉ nên làm sau Đề tài 1 và 2 (dùng lại hai mô hình đó + bước đăng ký hình học theo nhãn FDI). Chỉ số: sai số chiều dài chân răng (mm), góc trục răng, Dice răng đầy đủ.

**Ứng dụng/demo.** Lập kế hoạch chỉnh nha không cần CBCT: thấy chân răng khi dời răng.

**Nơi công bố:** Medical Image Analysis (Elsevier, ISSN 1361-8415, Crossref) nếu kết quả mạnh; Journal of Dentistry (như trên). Scopus chưa tra.

**Điểm:**
| Tiêu chí | Điểm | Lý do |
|---|---|---|
| Tính mới | 4 | Ảnh điện thoại + panoramic chưa thấy ai ghép (ToothInpaintor dùng scan). |
| Ứng dụng | 4 | Có giá trị cho chỉnh nha, nhưng cần hai loại ảnh. |
| Khả thi một người | 2 | Phụ thuộc Đề tài 1 và 2 xong trước; phần chính cần dữ liệu phòng khám. |
| Công bố | 3 | Tốt nếu có dữ liệu thật; chỉ dữ liệu mô phỏng thì yếu. |
| Hồ sơ NCS | 5 | Là bài kết của chuỗi (1 + 2 → 3). |
| **Tổng** | **18/25** | |

**Rủi ro:** không có dữ liệu công khai cho phần chính; nếu không có phòng khám thì không ra bài.

---

## Tổng hợp

| # | Đề tài | Mới | Ứng dụng | Khả thi | Công bố | NCS | Tổng | Không có dữ liệu riêng? |
|---|---|---|---|---|---|---|---|---|
| 2 | Ảnh điện thoại → răng 3D, đo mm so với scan | 4 | 5 | 4 | 4 | 4 | **21** | **Làm được** bài 1 (Teeth3DS+); bài kiểm chứng thật cần phòng khám |
| 1 | Panoramic → 3D có bản đồ tin cậy, sim từ CBCT | 3 | 4 | 4 | 4 | 5 | **20** | **Làm được** bài 1 (ToothFairy3); kiểm chứng sim→thật cần phòng khám |
| 3 | Ghép ảnh điện thoại + panoramic → răng đầy đủ | 4 | 4 | 2 | 3 | 5 | **18** | **Bắt buộc có đối tác** |

Khuyến nghị: bắt đầu với **Đề tài 1** dù điểm thấp hơn 1 điểm, vì (a) nối thẳng với đề tài #1 của RES-1 (báo cáo panoramic tiếng Việt) — cùng loại ảnh, cùng phòng khám, cùng demo; (b) panoramic là ảnh phòng khám nào cũng có sẵn trong lưu trữ, xin dữ liệu hồi cứu dễ hơn yêu cầu chụp mới. Đề tài 2 chạy song song nếu còn sức (dữ liệu nhẹ hơn). Đề tài 3 là bài kết sau khi có phòng khám.

---

## Gói đề xuất cho phòng khám

**Mang theo khi đi đề xuất (cuối giai đoạn 1, ~3 tháng):** demo web chạy trên laptop: tải panoramic → hàm 3D có tô màu độ tin cậy; tải 3-5 ảnh điện thoại → mô hình răng 3D; bảng sai số mm trên dữ liệu công khai, ghi rõ giới hạn (không thay CBCT).

**Phòng khám được gì:**
- Công cụ giải thích cho bệnh nhân bằng hình 3D từ ảnh đã có, miễn phí trong thời gian nghiên cứu.
- Đánh giá độc lập công cụ trên chính bệnh nhân của họ; đồng tác giả cho bác sĩ tham gia gán nhãn/đánh giá.
- Báo cáo panoramic tiếng Việt (nếu gộp với đề tài RES-2).

**Cần phòng khám cung cấp (ước lượng, chưa kiểm chứng với phòng khám):**
| Loại | Thiết bị | Số ca hợp lý | Ghi chú |
|---|---|---|---|
| Panoramic + CBCT cùng bệnh nhân, chụp gần nhau (hồi cứu) | Máy panoramic + CBCT | 50-100 ca để **kiểm chứng** (không đủ để huấn luyện lại; huấn luyện đã làm trên dữ liệu công khai) | Có máy CBCT là điều kiện của Đề tài 1 giai đoạn 2 |
| Ảnh điện thoại 3-5 góc + scan trong miệng cùng buổi (tiến cứu) | Máy scan trong miệng, banh môi, gương, điện thoại | 30-50 bệnh nhân | Cần cho Đề tài 2 giai đoạn 2 |
| 1 bác sĩ đánh giá | — | 2-4 giờ/tháng | Chấm hình 3D có dùng được không (thang Likert) |

Cơ sở cho con số: bài công bố dùng 499-500 cặp để **huấn luyện** (PX2Tooth, HiCT); nghiên cứu này chỉ dùng dữ liệu phòng khám để **kiểm chứng**, nên vài chục ca là đủ để báo cáo khoảng tin cậy. Số mẫu chính xác cần tính lại theo độ rộng khoảng tin cậy mong muốn — **chưa tính**.

**Quy trình đạo đức và dữ liệu** (khung chung; quy định Việt Nam cụ thể **chưa kiểm chứng**, cần phòng khám/trường xác nhận):
1. Xin chấp thuận của **hội đồng đạo đức trong nghiên cứu y sinh** (của trường chủ nhóm hoặc bệnh viện đối tác) trước khi lấy bất kỳ dữ liệu nào.
2. **Đồng ý tham gia bằng văn bản** của bệnh nhân với ca tiến cứu (Đề tài 2); với dữ liệu hồi cứu (Đề tài 1), hội đồng quyết định có miễn đồng ý hay không.
3. **Ẩn danh tại phòng khám**: xoá thông tin cá nhân trong header DICOM, đổi mã bệnh nhân; ảnh điện thoại cắt chỉ còn vùng miệng, không có mặt.
4. **Dữ liệu không rời phòng khám**: chạy mô hình trên máy đặt tại phòng khám; chỉ mang ra **chỉ số tổng hợp** (Dice, mm). Không đưa ảnh vào repo, comment, log.
5. Thoả thuận sử dụng dữ liệu (DUA) ghi rõ mục đích, thời hạn, huỷ dữ liệu sau nghiên cứu, quyền công bố.

**Mốc thời gian:**
| Tháng | Việc | Cần phòng khám? |
|---|---|---|
| 1-3 | Giai đoạn 1: dữ liệu công khai, demo, bản thảo bài 1 | Không |
| 3-4 | Đi đề xuất, ký thoả thuận, nộp hồ sơ đạo đức | Có (ký) |
| 4-6 | Chờ duyệt đạo đức; nộp bài 1 | — |
| 6-9 | Thu/ẩn danh dữ liệu tại phòng khám, chạy kiểm chứng | Có |
| 9-12 | Bài 2 (kiểm chứng thật); bắt đầu Đề tài 3 | Có |

---

## Đã cân nhắc nhưng loại

- **Tái tạo CBCT đầy đủ độ phân giải bằng diffusion (kiểu HiCT, https://arxiv.org/abs/2604.00792):** mô hình video diffusion + 500 cặp riêng, vượt GPU và dữ liệu của một người.
- **Cephalometric → 3D:** tìm arXiv `cephalometric AND 3D AND reconstruction` chỉ ra bài landmark trên ảnh chiếu từ CBCT (https://arxiv.org/abs/2608.16535, chỉ thấy tiêu đề), không có hướng dựng răng 3D từ ảnh sọ nghiêng; ảnh sọ nghiêng chồng hai bên hàm, ít thông tin răng. Để landmark 2D ở RES-2 đề tài 3.
- **Tự thu thập dữ liệu ngay từ đầu:** chưa có phòng khám, chưa có chấp thuận đạo đức → giai đoạn 1 chỉ dùng dữ liệu công khai.

## Câu hỏi cần chủ nhóm trả lời

1. "Bác sĩ xem và lên hướng xử lý" là chuyên khoa nào: chỉnh nha (cần thân + vị trí răng, hợp Đề tài 2), implant/nhổ răng khôn (cần chân răng, ống thần kinh, hợp Đề tài 1), hay chỉ tư vấn bệnh nhân?
2. Phòng khám nhắm tới có máy gì: panoramic, CBCT, máy scan trong miệng? (Quyết định đề tài nào kiểm chứng được.)
3. Trường của chủ nhóm có hội đồng đạo đức nghiên cứu y sinh không, hay phải nhờ bệnh viện?
4. GPU cụ thể (loại, bộ nhớ)? CBCT 3D cần ≥12 GB.
5. Có chấp nhận giấy phép phi thương mại (NC-SA) cho giai đoạn 1 không, hay mục tiêu cuối là sản phẩm bán cho phòng khám?
