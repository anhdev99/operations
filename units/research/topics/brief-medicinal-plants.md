# Brief: Hướng nối tiếp cho dataset ảnh cây thuốc nam (RES-16)

Issue: RES-16 (con của RES-14). Người viết: Scholar. Ngày: 2026-11-24.

## Dữ kiện đầu vào (từ Dean, RES-14)

- Dataset của chủ nhóm: **ảnh**, tự thu thập, **100 loài, ~50.000 ảnh**, **nhiều ảnh trùng**. Chủ nhóm **được phép công bố ảnh**.
- Đã có một bài đăng ở "FAIR2025" (nhiều khả năng Hội nghị khoa học quốc gia FAIR - Nghiên cứu cơ bản và ứng dụng CNTT) và luận văn thạc sĩ.
  **Chưa kiểm chứng**: tìm kiếm kỷ yếu FAIR 2025 qua công cụ tự động không ra kết quả; không đoán tên bài.
- Kịch bản "dataset là văn bản" đã bỏ theo chỉ đạo của Dean.

## Cách kiểm chứng

- Bài báo: mở abstract/full text qua arXiv API, Europe PMC (abstract + full text PMC), trang dataset (figshare, Hugging Face).
  OpenAlex/Crossref/Semantic Scholar bị giới hạn truy cập trong lượt này nên phạm vi tìm kiếm **chưa đầy đủ**.
- Nơi công bố: tồn tại xác nhận qua OpenAlex (tra theo ISSN, có trang chủ, APC). **Trạng thái Scopus chưa tra trực tiếp** cho tất cả; chủ nhóm tra Scopus/SJR trước khi nộp.
  Mọi nơi có APC là chi phí, cần board duyệt nếu chọn.
- Số liệu trong brief là số các bài tự báo cáo, Scholar không chạy lại.

## Bức tranh nhanh

- Phân loại ảnh cây thuốc bằng CNN đã bão hoà: nhiều bài báo cáo accuracy 84-93% trên dataset tự thu (Việt Nam, Indonesia, Ấn Độ). "Làm lại phân loại" không đủ mới cho Scopus tốt.
- Hướng mới đang mở: (a) dataset lớn có quy trình làm sạch rõ (TCMP-300 trên Scientific Data), (b) mô hình nền/MLLM cho nhận dạng (đánh giá MLLM năm 2026), (c) few-shot/open-set,
  (d) KG + LLM cho y học cổ truyền (rất dày ở TCM, gần như trống ở Việt Nam).
- Vấn đề "ảnh trùng giữa train và test làm thổi phồng điểm" đã được chứng minh ở CIFAR (Barz & Denzler 2019) nhưng chưa thấy bài nào đo cho dataset cây thuốc (tìm kiếm chưa đầy đủ).

## Tài liệu đã mở và đọc (dùng chung)

| # | Bài | Đã đọc | Nội dung dùng được |
|---|---|---|---|
| P1 | Zhang Y. et al., 2025, *TCMP-300*, Scientific Data. DOI 10.1038/s41597-025-05522-7 | full text (PMC12241305) | 52.089 ảnh, 300 loài; ảnh lấy từ Bing, lọc bằng vision foundation model + người duyệt; baseline 89,64%. Dữ liệu figshare CC BY 4.0. |
| P2 | Barz B., Denzler J., 2019, *Do We Train on Test Data? Purging CIFAR of Near-Duplicates*. https://arxiv.org/abs/1902.00423 | abstract | 3,3% (CIFAR-10) và 10% (CIFAR-100) ảnh test có bản trùng trong train; tạo bộ test sạch ciFAIR rồi đánh giá lại. |
| P3 | Jiang Y. et al., 2026, *Benchmarking multimodal LLMs for medicinal plant identification*, Frontiers in Plant Science. DOI 10.3389/fpls.2026.1765281 | abstract | 200 ảnh (dataset riêng), trắc nghiệm 4 lựa chọn; Qwen3-VL-235B 90,50%, GPT-4o 85,00%, Gemma3-27B 65,50%, Llama4Scout 58,50%, DeepSeek-VL2 58,00%. |
| P4 | Zhang T. et al., 2025, *FewMedical-XJAU*, Sensors. DOI 10.3390/s25175499 | abstract | Benchmark few-shot cây thuốc hiếm Tân Cương, nền tự nhiên; thêm text prior vào metric learning. |
| P5 | Tan C. et al., 2026, *Fine-grained few-shot class-incremental identification of medicinal plants (FGDE)*, Frontiers in Plant Science. DOI 10.3389/fpls.2026.1730047 | abstract | Học thêm loài mới từ ít mẫu, chống quên. |
| P6 | Dat T.T. et al., 2021, *Leaf Recognition ... A Testing for Vietnamese Herb*, Computational Intelligence and Neuroscience. DOI 10.1155/2021/5032359 | abstract | Dataset lá cây thuốc Việt tự thu; U-Net tách nền + ensemble EfficientNet/MobileNet. |
| P7 | Nguyen Van Hieu, Ngo Le Huy Hien, 2020, *Automatic Plant Image Identification of Vietnamese species*. https://arxiv.org/abs/2005.02832 | abstract | 28.046 ảnh, 109 loài cây Việt Nam (từ bách khoa trực tuyến + EOL); MobileNetV2 + SVM 83,9%. |
| P8 | Musyaffa M.S.I. et al., 2023, *IndoHerb*. https://arxiv.org/abs/2308.01604 | abstract | Cây thuốc Indonesia, ConvNeXt 92,5%. |
| P9 | Sinha S. et al., 2025, *Open-World Scenarios in Medicinal Plant Classification*. https://arxiv.org/abs/2502.17289 | abstract | Phân loại phân cấp cho loài lạ; độ đúng giảm mạnh từ ngành (83,36%) xuống họ (43,32%). |
| P10 | Stevens S. et al., 2023, *BioCLIP*. https://arxiv.org/abs/2311.18803 · model https://huggingface.co/imageomics/bioclip (MIT) | abstract, trang model | Mô hình nền ảnh sinh vật theo cây phân loại. BioCLIP 2: Gu J. et al., 2025, https://arxiv.org/abs/2505.23883 |
| P11 | Oquab M. et al., 2023, *DINOv2*. https://arxiv.org/abs/2304.07193 | abstract | Đặc trưng ảnh tự giám sát, dùng tốt cho linear probe và tìm ảnh gần trùng. |
| P12 | He J. et al., 2025, *OpenTCM: GraphRAG cho y học cổ truyền Trung Quốc*. https://arxiv.org/abs/2504.20118 | abstract | KG >48.000 thực thể, >152.000 quan hệ từ 68 sách phụ khoa; GraphRAG không fine-tune; điểm chuyên gia 4,378 / 4,045. |
| P13 | Kong S. et al., 2025, *MTCMB*. https://arxiv.org/abs/2506.01252 | abstract | Benchmark TCM 12 tập con, có mục **an toàn**; LLM yếu ở kê đơn và tuân thủ an toàn. |
| P14 | Zhu Y. et al., 2026, *TCMToxDB*, Database (Oxford). DOI 10.1093/database/baag019 | abstract | CSDL độc tính dược liệu TCM (bài thuốc, vị thuốc, hoạt chất). |
| P15 | Joshi S. et al., 2025, *GRAYU*, Frontiers in Pharmacology. DOI 10.3389/fphar.2025.1727224 | abstract | Graph DB Ayurveda: 1.039 bài thuốc, 12.743 cây, 13.480 bệnh. |
| P16 | Baskaran S.P. et al., 2026, *IMPPAT 3.0 (FAIR + IMPPAT-KG)*. https://arxiv.org/abs/2610.07478 | abstract | CSDL cây thuốc Ấn Độ theo nguyên tắc FAIR, có KG và link ảnh cây. |
| P17 | Hou Y.N. et al., 2026, *RAG LLM cho thông tin thảo dược trong chăm sóc ung thư*, JMIR Cancer. DOI 10.2196/86073 | abstract (rất ngắn) | RAG trả lời câu hỏi của nhân viên y tế về thảo dược/thực phẩm bổ sung. |

**Chưa kiểm chứng (không dùng để chấm điểm):**
- VNPlant-200 (Quoc T.N., Hoang V.T., *Integrated Science in Digital Age 2020*, Springer, 2021, tr. 406-411): chỉ đọc qua trích dẫn trong P1 (20.000 ảnh, 200 loài cây thuốc Việt). Chưa mở bài gốc, chưa xác nhận link tải/giấy phép.
- VietMed-MCQ (https://arxiv.org/abs/2601.03792): 3.190 câu trắc nghiệm y học cổ truyền Việt Nam; **tác giả đã rút bài** trên arXiv. Không dùng.
- Bài FAIR 2025 của chủ nhóm: chưa tìm được.

## Dataset công khai để so sánh / bổ sung

| Tên | Link | Giấy phép | Quy mô | Ghi chú |
|---|---|---|---|---|
| TCMP-300 | https://doi.org/10.6084/m9.figshare.29432726 | CC BY 4.0 | 52.089 ảnh, 300 loài, 11,94 GB | Có thể có loài trùng với cây thuốc nam; dùng để pretrain hoặc kiểm tra chéo |
| Vietnamese Medicinal Herb VQA | https://huggingface.co/datasets/gdllelf/vietnamese-medicinal-herb-vqa | CC BY-NC 4.0 | 3.791 ảnh, 29.161 cặp hỏi-đáp tiếng Việt (train 3.032/23.211; val 379/2.998; test 380/2.952) | Không có bài báo kèm; dùng làm benchmark VQA tiếng Việt phụ |
| VNPlant-200 | chưa kiểm chứng link | chưa kiểm chứng | 20.000 ảnh, 200 loài (theo P1) | Đối chứng Việt Nam gần nhất; cần mở bài gốc |
| Wikidata | https://query.wikidata.org | CC0 | 11.109 taxon có `P366` (công dụng) = `Q188840` (cây thuốc); 11.081 trong số đó có nhãn tiếng Việt | Truy vấn chạy ngày 2026-11-24 (xem Phụ lục) |
| GBIF | https://api.gbif.org | theo từng bộ, phần lớn CC BY/CC0 | ví dụ *Artemisia vulgaris* (ngải cứu, taxonKey 3120946): chỉ **10** bản ghi có ảnh ở Việt Nam | Cho thấy dữ liệu ảnh cây thuốc Việt Nam trên GBIF rất mỏng, là lý do đóng góp |

Kết luận so sánh: bộ của chủ nhóm (100 loài, ~50k ảnh, tự chụp) **ngang TCMP-300 về số ảnh** và lớn hơn VNPlant-200, P7 về số ảnh/loài.
Giá trị thật phụ thuộc số ảnh **còn lại sau khử trùng**. Đây là việc phải làm đầu tiên, bất kể chọn đề tài nào.

---
## Đề tài A. VNMedPlant-Clean: bộ ảnh cây thuốc nam đã khử trùng, benchmark chống rò rỉ và đánh giá lại mô hình

**Câu hỏi nghiên cứu.** Bao nhiêu phần trăm ảnh trong bộ 50k là trùng hoặc gần trùng, và khi chia train/test chống rò rỉ (theo nhóm ảnh gần trùng, theo cây/lần chụp)
thì accuracy của các mô hình phân loại phổ biến giảm bao nhiêu so với chia ngẫu nhiên?

**Khoảng trống.**
- P2 (Barz & Denzler 2019): chứng minh ảnh trùng train-test làm sai lệch so sánh mô hình, nhưng trên CIFAR, không phải dữ liệu thực vật.
- P1 (TCMP-300, 2025): có lọc bằng foundation model + người duyệt, nhưng ảnh lấy từ web, không phải ảnh tự chụp; không báo cáo split chống rò rỉ theo nhóm.
- P6, P7, P8 (dataset Việt Nam/Indonesia): báo cáo accuracy 83,9-92,5% với split không mô tả cơ chế chống trùng (theo abstract). Chưa ai đo con số này bị thổi phồng bao nhiêu.
- Chỗ trống: **data paper ảnh cây thuốc Việt Nam tự chụp, có quy trình khử trùng công bố được, split cố định chống rò rỉ, đo "độ thổi phồng"**.

**Dữ liệu.**
- Của chủ nhóm: toàn bộ 50k ảnh / 100 loài là dữ liệu chính. Bài FAIR 2025 + luận văn là "phiên bản 1"; bản này là "phiên bản 2 đã làm sạch", trích dẫn bài cũ.
- Bổ sung: TCMP-300 (CC BY 4.0) để kiểm tra chéo các loài trùng tên khoa học; Wikidata/GBIF để gắn ID chuẩn cho 100 loài (FAIR thật sự: định danh bền vững).

**Quy trình chuẩn bị data paper.**
1. Khử trùng: trùng chính xác bằng hash tệp (SHA-256); gần trùng bằng perceptual hash (pHash, ngưỡng Hamming) + cosine trên đặc trưng DINOv2 (P11). Gom thành cụm, người duyệt mẫu ngẫu nhiên ở các ngưỡng để chọn ngưỡng.
2. Làm sạch nhãn: đối chiếu tên Việt - tên khoa học - Wikidata QID - GBIF taxonKey; dùng độ bất đồng giữa nhiều mô hình để khoanh ảnh nghi sai nhãn, **chuyên gia dược liệu xác nhận**.
3. Split cố định: chia theo **cụm gần trùng** (và theo lần chụp/địa điểm nếu có metadata), không bao giờ để một cụm nằm ở hai tập. Công bố file split.
4. Datasheet (theo mẫu "Datasheets for Datasets", chưa mở bài gốc trong lượt này): nguồn, thiết bị, thời gian, địa điểm (làm mờ nếu loài quý hiếm), người gán nhãn, giấy phép.
5. Lưu trữ có DOI: **Zenodo** (DOI miễn phí) làm bản gốc; mirror lên **Hugging Face** (có Croissant metadata) và tuỳ chọn Kaggle.
6. Giấy phép đề xuất: **CC BY 4.0** (giống TCMP-300, đa số tạp chí data paper chấp nhận). Chọn CC BY-NC 4.0 nếu chủ nhóm muốn giữ quyền thương mại, đánh đổi là ít người dùng hơn.

**Baseline (6 tuần, GPU 8 GB đủ).** Tuần 1-2: khử trùng + thống kê (tỉ lệ trùng, phân bố ảnh/loài trước-sau). Tuần 3-4: ResNet-50, EfficientNet-B0, ConvNeXt-T, ViT-S fine-tune
+ linear probe DINOv2/BioCLIP, mỗi mô hình 2 kiểu split (ngẫu nhiên vs chống rò rỉ), 3 seed. Tuần 5-6: viết datasheet, đóng gói, đăng Zenodo.
Chỉ số: top-1, macro-F1 (do mất cân bằng), **độ chênh accuracy giữa hai kiểu split** (chỉ số chính của bài), tỉ lệ trùng theo từng ngưỡng.

**Ứng dụng/demo.** Trang Hugging Face dataset + notebook tải và chạy baseline; dùng bởi nhóm nghiên cứu khác, giảng viên dạy CV, sinh viên.
Không phải demo người dùng cuối, nhưng là nền cho đề tài B, C.

**Nơi công bố (tồn tại đã xác nhận qua OpenAlex; Scopus chưa tra):**
- Data in Brief (Elsevier, OA, APC ~1.220 USD theo OpenAlex) — https://www.journals.elsevier.com/data-in-brief
- Scientific Data (Nature, OA, APC ~2.490 USD) — https://www.nature.com/sdata/ (nơi đăng TCMP-300; khó hơn, cần đóng góp kỹ thuật rõ)
- Ecological Informatics (Elsevier) — https://www.journals.elsevier.com/ecological-informatics (nếu viết bản nặng phương pháp: đo thổi phồng do trùng ảnh)
APC là chi phí: cần board duyệt nếu chọn nơi có phí.

**Điểm.**
| Tiêu chí | Điểm | Lý do |
|---|---|---|
| Tính mới | 3 | Data paper ảnh cây thuốc đã có nhiều; mới ở phần đo rò rỉ do trùng ảnh và ảnh tự chụp Việt Nam |
| Ứng dụng thực tiễn | 3 | Tài nguyên cho nghiên cứu, chưa phải sản phẩm cho người dùng cuối |
| Khả thi một người | 5 | Dữ liệu đã có, được phép công bố, tính toán nhẹ |
| Khả năng công bố | 4 | Data in Brief nhận data paper có quy trình rõ; tăng giá trị nhờ số đo "thổi phồng" |
| Hợp hồ sơ NCS | 5 | Là bài 1 tự nhiên, mọi bài sau dùng lại bộ split này |
| **Tổng** | **20** | |

**Rủi ro.** Sau khử trùng còn quá ít ảnh/loài (chưa biết tỉ lệ trùng); trùng lặp nhiều với bài FAIR 2025 nếu bài đó đã công bố ảnh (cần xem điều khoản tự đạo văn của tạp chí);
nhãn chưa có chuyên gia xác nhận thì phản biện sẽ hỏi.

---

## Đề tài B. Nhận dạng cây thuốc nam dễ nhầm bằng mô hình nền: few-shot, ngoài phân phối và từ chối khi không chắc

**Câu hỏi nghiên cứu.** Trên split chống rò rỉ của đề tài A, mô hình nền (BioCLIP, DINOv2) với linear probe/few-shot so với CNN fine-tune thế nào,
đặc biệt ở **cặp loài dễ nhầm** và ảnh điện thoại ngoài thực tế? Cơ chế từ chối (abstain) khi không chắc giảm được bao nhiêu nhầm lẫn nguy hiểm?

**Khoảng trống.**
- P3 (Jiang 2026): MLLM lớn đạt 58-90,5% trên 200 ảnh dạng trắc nghiệm, dataset riêng không công khai; không đo loài dễ nhầm, không đo từ chối, không có mô hình nhỏ chạy cục bộ.
- P4 (FewMedical-XJAU 2025), P5 (FGDE 2026): few-shot cây thuốc Trung Quốc, không có loài Việt Nam, không gắn nhầm lẫn với độc tính.
- P9 (Sinha 2025): open-set theo cây phân loại, accuracy mức họ chỉ 43,32%; cho thấy nhận loài lạ còn yếu.
- P10 (BioCLIP): mô hình nền sinh vật, chưa thấy đánh giá trên cây thuốc Việt Nam (tìm kiếm chưa đầy đủ).
- Chỗ trống: **benchmark cặp loài dễ nhầm có ý nghĩa an toàn + ảnh điện thoại thực địa + đánh giá từ chối**, cho cây thuốc Việt Nam.

**Dữ liệu.**
- Của chủ nhóm: bộ đã làm sạch (đề tài A). Từ ma trận nhầm lẫn chọn 10-20 cặp loài hay nhầm; chuyên gia dược liệu đánh dấu cặp nào **nhầm thì nguy hiểm** (một loài có độc/không dùng được).
- Thu thêm (một người, 2-4 tuần): **tập OOD** 20-30 ảnh/loài × 30-50 loài, chụp điện thoại ở chợ, vườn, nhà thuốc; ghi thiết bị, nền, bộ phận (lá/hoa/thân/dược liệu khô). Chuẩn chụp: 1 ảnh toàn cây, 1 lá mặt trên, 1 lá mặt dưới, 1 hoa/quả nếu có, thước hoặc nền xám.
- Bổ sung: TCMP-300 (pretrain/so sánh chéo), Vietnamese Medicinal Herb VQA (CC BY-NC 4.0; kiểm tra phụ VQA tiếng Việt).

**Baseline (8 tuần, GPU 8-12 GB).** Tuần 1-2: embedding BioCLIP/DINOv2/CLIP đóng băng + linear probe, k-shot (1/5/10) bằng prototype. Tuần 3-4: fine-tune ConvNeXt-T/ViT-S làm đối chứng.
Tuần 5-6: thu ảnh OOD, đo tụt độ đúng. Tuần 7-8: calibration (temperature scaling) + selective prediction. 3 seed, cố định split.
Chỉ số: top-1/macro-F1; accuracy trên cặp dễ nhầm; ECE; đường risk-coverage (AURC); **tỉ lệ nhầm nguy hiểm ở mức coverage 90%**.

**Ứng dụng/demo.** Web app (Gradio) hoặc app điện thoại: người bán/người dùng chụp lá → top-3 loài + độ tin cậy; nếu rơi vào cặp nguy hiểm hoặc không chắc thì **từ chối và nhắc hỏi dược sĩ**.
Người dùng: sinh viên dược, cán bộ trạm y tế, người trồng dược liệu.

**Nơi công bố (tồn tại đã xác nhận qua OpenAlex; Scopus chưa tra):**
- Plant Methods (BMC, OA, APC ~3.090 USD) — https://plantmethods.biomedcentral.com/ (đã đăng bài nhận dạng cây thuốc bằng DL)
- Frontiers in Plant Science (OA, APC ~3.801 USD) — https://journal.frontiersin.org/journal/plant-science (nơi đăng P3, P5)
- Ecological Informatics — https://www.journals.elsevier.com/ecological-informatics ; hoặc SOICT (Springer CCIS, đã ghi ở `top5-de-tai.md`) nếu muốn hội nghị không phí đăng tạp chí.

**Điểm.**
| Tiêu chí | Điểm | Lý do |
|---|---|---|
| Tính mới | 4 | Kết hợp loài dễ nhầm có nhãn an toàn + OOD điện thoại + từ chối; chưa thấy cho cây thuốc Việt |
| Ứng dụng thực tiễn | 4 | App nhận dạng có cảnh báo dùng ngay được; chưa phải thiết bị y tế |
| Khả thi một người | 4 | Tính toán nhẹ; cần 2-4 tuần thu ảnh OOD và chuyên gia đánh dấu cặp nguy hiểm |
| Khả năng công bố | 4 | Có câu chuyện rõ (mô hình nền vs CNN, độ an toàn); venue cây trồng nhận nhiều bài loại này |
| Hợp hồ sơ NCS | 5 | Bài 2 dùng trực tiếp dữ liệu bài 1, dẫn sang bài 3 |
| **Tổng** | **21** | |

**Rủi ro.** Dataset có thể không chứa nhiều cặp loài nguy hiểm thật (100 loài chọn theo tiện thu thập); cần chuyên gia; mô hình nền tốt đến mức bài toán "đã giải" trên tập sạch,
khi đó trọng tâm phải dồn vào OOD và từ chối.

---

## Đề tài C. Tri thức cây thuốc nam: KG liên kết Wikidata/GBIF và trợ lý hỏi đáp tiếng Việt có cảnh báo an toàn, nhận ảnh làm đầu vào

**Câu hỏi nghiên cứu.** Một KG nhỏ cho 100 loài (tên Việt, tên khoa học, bộ phận dùng, công dụng, độc tính/chống chỉ định, loài dễ nhầm, liên kết QID/GBIF)
dùng trong GraphRAG có giảm câu trả lời sai/thiếu cảnh báo an toàn của LLM nhỏ tiếng Việt so với RAG văn bản thường không?

**Khoảng trống.**
- P12 (OpenTCM 2025): GraphRAG cho TCM rất mạnh nhưng tiếng Trung, phụ khoa, không có đầu vào ảnh.
- P13 (MTCMB 2025): LLM yếu ở tuân thủ an toàn trong TCM; benchmark tiếng Trung.
- P14 (TCMToxDB 2026), P15 (GRAYU 2025), P16 (IMPPAT 3.0 2026): CSDL/KG độc tính và cây thuốc cho Trung Quốc, Ấn Độ; IMPPAT gắn nhãn FAIR. Chưa thấy tương đương cho cây thuốc Việt Nam.
- P17 (JMIR Cancer 2026): RAG cho câu hỏi thảo dược, tiếng Anh, không KG.
- Chỗ trống: **KG cây thuốc nam liên kết định danh chuẩn + chatbot tiếng Việt có kiểm tra an toàn + ảnh làm lối vào**.

**Dữ liệu.**
- Của chủ nhóm: 100 loài là danh sách thực thể gốc; mô hình đề tài B nhận ảnh → loài → truy vấn KG.
- Bổ sung: Wikidata (CC0; 11.081 taxon cây thuốc có nhãn tiếng Việt, xem Phụ lục) để lấy tên khoa học, tên gọi khác, liên kết; GBIF backbone để chuẩn hoá tên.
- Nguồn công dụng/độc tính tiếng Việt: Dược điển Việt Nam, sách cây thuốc chuẩn (chủ nhóm chọn; **chưa kiểm chứng giấy phép**, chỉ trích dẫn/tóm tắt, không chép nguyên văn).
- Tập đánh giá: tự dựng 300-500 câu hỏi tiếng Việt (công dụng, liều, chống chỉ định, phân biệt loài), có câu "bẫy an toàn"; ≥2 người có chuyên môn dược chấm.

**Baseline (8 tuần, GPU 12-16 GB, chỉ suy luận).** Tháng 1: schema nhỏ (Loài, Bộ phận, Công dụng, Độc tính, Chống chỉ định, Loài dễ nhầm) trong RDF hoặc Neo4j; LLM trích bộ ba từ tài liệu, người duyệt; gắn QID/GBIF.
Tháng 2: so 3 cấu hình trên LLM 7-8B 4-bit: không RAG / RAG văn bản / GraphRAG + luật cảnh báo cứng (loài có độc thì luôn chèn cảnh báo).
Chỉ số: accuracy theo chuyên gia, **tỉ lệ thiếu cảnh báo an toàn**, tỉ lệ khẳng định trái KG, độ phủ trích dẫn nguồn.

**Ứng dụng/demo.** Chatbot web/Zalo: chụp ảnh hoặc gõ tên cây → thẻ thông tin (tên, công dụng, độc tính, loài dễ nhầm, nguồn) + hỏi đáp; luôn kèm "tham khảo, không thay chỉ định của thầy thuốc".
Người dùng: sinh viên y dược, người dân, phòng chẩn trị YHCT. Dùng lại hạ tầng chatbot chủ nhóm đang làm cho trường (tài sản 1).

**Nơi công bố (tồn tại đã xác nhận qua OpenAlex; Scopus chưa tra):**
- Database: The Journal of Biological Databases and Curation (OUP, OA, APC ~2.729 USD) — https://academic.oup.com/database (nơi đăng TCMToxDB)
- Journal of Biomedical Semantics (BMC, APC ~1.590 USD) — http://www.jbiomedsem.com/
- SOICT (Springer CCIS) hoặc IEEE Access — http://ieeexplore.ieee.org/servlet/opac?punumber=6287639 (APC ~2.075 USD)

**Điểm.**
| Tiêu chí | Điểm | Lý do |
|---|---|---|
| Tính mới | 4 | KG + GraphRAG cho cây thuốc Việt chưa thấy; phương pháp mượn từ TCM |
| Ứng dụng thực tiễn | 5 | Dùng ngay cho người dân/sinh viên, nối với chatbot trường đang làm |
| Khả thi một người | 3 | Tính toán nhẹ nhưng cần chuyên gia dược duyệt KG và chấm 300-500 câu |
| Khả năng công bố | 4 | Hướng KG-LLM y học cổ truyền đang được nhận nhiều |
| Hợp hồ sơ NCS | 5 | Bài 3-4 khép chuỗi ảnh → loài → tri thức → tư vấn an toàn |
| **Tổng** | **21** | |

**Rủi ro.** Thiếu chuyên gia dược thì không chấm được an toàn; nguồn tri thức tiếng Việt có bản quyền; chatbot sức khoẻ cần câu miễn trừ trách nhiệm rõ và không tư vấn liều điều trị.

---

## Tổng hợp

| Đề tài | Mới | ƯD | KT | CB | NCS | Tổng |
|---|---|---|---|---|---|---|
| A. VNMedPlant-Clean: data paper + benchmark chống rò rỉ | 3 | 3 | 5 | 4 | 5 | **20** |
| B. Nhận dạng loài dễ nhầm bằng mô hình nền, OOD, từ chối | 4 | 4 | 4 | 4 | 5 | **21** |
| C. KG cây thuốc nam + GraphRAG có cảnh báo an toàn | 4 | 5 | 3 | 4 | 5 | **21** |

**Khuyến nghị thứ tự: A → B → C** (không theo điểm). A điểm thấp nhất nhưng là điều kiện của B và C: chưa khử trùng thì mọi con số của B đều có thể bị phản biện bác.
A làm xong trong ~6 tuần, ra bài sớm nhất. Chuỗi NCS: A (dữ liệu) → B (nhận dạng an toàn) → C (tri thức + trợ lý) → bài 4 tuỳ chọn: đánh giá người dùng thực tế của demo C.

**Điểm nối với trục răng hàm mặt (RES-1).** Không trùng đề tài. Dùng chung phương pháp: kiểm tra rò rỉ dữ liệu (A) áp dụng được cho dataset ảnh nha khoa;
GraphRAG có cảnh báo (C) cùng khung với đề tài #2 "chatbot nha khoa neo OHD" trong `top5-de-tai.md`. Một người làm cả hai trục sẽ dàn mỏng; nên chọn một trục chính.

## Đã cân nhắc nhưng loại

1. **Chỉ làm lại phân loại ảnh với mô hình mới hơn**: bão hoà (P6-P8, P1 đều >83%), không đủ mới cho Scopus tốt.
2. **Fine-tune VLM/MLLM riêng cho cây thuốc Việt (kiểu ShizhenGPT, https://arxiv.org/abs/2508.14706)**: cần dữ liệu và GPU lớn hơn nhiều so với một người; dùng MLLM có sẵn làm đối chứng trong B là đủ.
3. **Benchmark trắc nghiệm YHCT tiếng Việt từ tài liệu tổng hợp**: bài gần nhất (VietMed-MCQ) đã bị rút; hướng này không dùng tài sản ảnh của chủ nhóm, chỉ nên làm như phần đánh giá trong C.

## Câu hỏi cần chủ nhóm trả lời

1. Tên chính xác, link/DOI bài FAIR 2025 và luận văn? Bài cũ đã công bố ảnh chưa, chia train/test thế nào, accuracy báo cáo bao nhiêu? (để tránh trùng lặp và để đo "độ thổi phồng").
2. Ảnh có metadata không: ngày chụp, địa điểm, thiết bị, người chụp, bộ phận cây (lá/hoa/dược liệu khô)? Ảnh trùng sinh ra từ đâu (chụp liên tiếp, augment, tải web)?
3. 100 loài đã có **tên khoa học** và chuyên gia dược liệu xác nhận nhãn chưa? Có thể nhờ ai (khoa Dược, viện dược liệu) duyệt nhãn và chấm câu trả lời an toàn?
4. Trong 100 loài có những cặp nào người dùng hay nhầm, có loài độc hoặc chống chỉ định đáng chú ý không?
5. Có ngân sách APC không (Data in Brief ~1.220 USD; nhiều tạp chí 2-4k USD)? Nếu không, ưu tiên hội nghị Scopus (SOICT) hoặc tạp chí không phí — Dean tra thêm.

## Phụ lục: lệnh tái lập số liệu Wikidata/GBIF (chạy 2026-11-24)

```sparql
# Wikidata Query Service: taxon có "has use" = medicinal plant, có nhãn tiếng Việt (kết quả 11081; bỏ dòng FILTER: 11109)
SELECT (COUNT(DISTINCT ?t) AS ?n) WHERE {
  ?t wdt:P31 wd:Q16521; wdt:P366 wd:Q188840 .
  ?t rdfs:label ?l . FILTER(LANG(?l)="vi")
}
```

```text
GBIF: https://api.gbif.org/v1/species/match?name=Artemisia%20vulgaris  -> usageKey 3120946
      https://api.gbif.org/v1/occurrence/search?taxonKey=3120946&country=VN&mediaType=StillImage&limit=0  -> count 10
```
Số liệu Wikidata/GBIF thay đổi theo thời gian; chạy lại trước khi đưa vào bài.
