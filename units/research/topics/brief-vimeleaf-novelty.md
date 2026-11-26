# RES-29: kiểm tính mới cho chuỗi 3 bài ViMeLeaf

Issue: RES-29 (con của RES-27). Người viết: Scholar. Ngày kiểm tra nguồn: 2026-11-26.
Đề xuất được kiểm: `units/research/topics/vimeleaf-3-paper-series.md` (commit 980febf).
Mọi bài/dataset dưới đây đã mở abstract hoặc trang gốc (arXiv, Nature, Crossref) trong lượt này.
Số liệu trích đều lấy từ abstract; không bịa tác giả, năm hay kết quả. Chưa chắc thì ghi "chưa kiểm chứng".

Ghi chú phạm vi: bản thân `units/research/` chưa được đưa vào `develop` (ở state hiện tại trên
`develop`, thư mục này là untracked; commit `f3d3a1a` trên nhánh này thêm nó vào repo).
Do đó các bài đọc TCMaster/`ShenNongDiet` được nhắc trong `experiments/backlog.md` nhưng
không có tệp `papers/*.md` ở `develop`; bản brief này trích thẳng từ arXiv/Crossref thay thế.

## Tóm tắt nhanh

| Bài | Khoảng trống (đã kiểm) | Rủi ro trùng | Ghi chú |
|---|---|---|---|
| 1. Data paper ViMeLeaf | Không thấy data paper ảnh cây thuốc Việt Nam/ĐNA có split chống rò rỉ theo nhóm trùng. TCMP-300 (TC, ảnh từ web) gần nhất nhưng không đo "độ thổi phồng" | Trung bình — phải trích rõ phần mới so với VNPlant-200, TCMP-300, P7 (2005.02832) | Dữ liệu của mình (62k ảnh, 3 tỉnh) khác về nguồn và quy mô ảnh/loài |
| 2. Nhận dạng dễ nhầm + từ chối | Selective prediction / open-set đã có khung lý thuyết chung (ICML 2024, NeurIPS-22, arXiv 2505.15008, 2408.14229); chưa thấy áp dụng cho **cặp loài cây thuốc dễ nhầm + an toàn khi nhầm** | Thấp-trung bình — phần phương pháp là "mượn", mới ở **benchmark cặp dễ nhầm + an toàn** | Cần thêm MLLM (P3, `1765281`) vào so sánh |
| 3. KG cây thuốc + GraphRAG an toàn | Đã có OpenTCM (TC, phụ khoa), ShenNongDiet (TC, dinh dưỡng, có CONTRAINDICATED_FOR), TCMaster (lọc cạnh theo độ tin cậy), BEACON-SP (ontology-grounded, y khoa); **chưa thấy bản tiếng Việt/ĐNA cây thuốc nam, chưa thấy đầu vào là ảnh** | Thấp — khoảng trống rõ; phần mới = tiếng Việt + ảnh làm đầu vào + lọc an toàn cứng có truy vết | ViMeLeaf metadata (66-80 loài) là hạt giống; cần chuyên gia dược duyệt trước |

---

## Bài 1 (data paper): bộ ảnh cây thuốc Việt Nam, khử trùng, split chống rò rỉ

### Công trình gần nhất đã mở

| # | Bài / dataset | Năm | Link (đã mở) | Ghi chú |
|---|---|---|---|---|
| A1 | Quoc T.N., Hoang V.T., **VNPlant-200**, *Integrated Science in Digital Age 2020* (Springer), 2021, tr. 406-411 | 2021 | Chỉ trích dẫn trong TCMP-300 (P1); **chưa mở được bài gốc, link tải/giấy phép chưa kiểm chứng** | 20.000 ảnh, 200 loài cây thuốc Việt (theo P1) |
| A2 | **TCMP-300**: A Comprehensive TCM Plant Dataset for Plant Recognition, Scientific Data 12, 2025. DOI 10.1038/s41597-025-05522-7 | 2025 | https://www.nature.com/articles/s41597-025-05522-7 (đã mở abstract + references) | 52.089 ảnh, 300 loài, 11,94 GB; ảnh từ web (Bing), lọc bằng VLM + người duyệt; dữ liệu figshare CC BY 4.0 (https://doi.org/10.6084/m9.figshare.29432726). Không thấy mô tả split chống rò rỉ theo nhóm trùng. |
| A3 | **IndoHerb**: Indonesia Medicinal Plants Recognition, arXiv:2308.01604 | 2023-2024 | https://arxiv.org/abs/2308.01604 (đã mở abstract) | Dataset Indonesia tự thu; ConvNeXt 92,5%; không mô tả split chống trùng (theo abstract) |
| A4 | **Automatic Plant Image Identification of Vietnamese species**, arXiv:2005.02832, IJETT 68.4, 2020, DOI 10.14445/22315381/IJETT-V68I4P205S | 2020 | https://arxiv.org/abs/2005.02832 (đã mở abstract) | 28.046 ảnh, 109 loài (từ bách khoa + EOL); MobileNetV2+SVM 83,9%. **Không phải cây thuốc** (cây nói chung) |
| A5 | **MEDIPI / MedLEA**: Statistical ML for Medicinal Plant Leaves Classification, arXiv:2611.04193 | 2026 | https://arxiv.org/abs/2611.04193 (đã mở abstract) | Sri Lanka, 1.099 ảnh, 31 loài; R package MedLEA; chính tác giả báo accuracy tụt 23-50% khi train/test từ dataset khác (tổng quát hoá chéo dataset là vấn đề) |
| A6 | **Local Herb Identification (Nepal)**, arXiv:2505.02147 | 2025 | https://arxiv.org/abs/2505.02147 (đã mở abstract) | Nepal, 12.000 ảnh, 60 loài; DenseNet121 tốt nhất |
| A7 | **Identification of Traditional Medicinal Plant Leaves (self-curated)**, arXiv:2501.09363, DOI 10.1007/978-3-031-83793-7_22 | 2025 | https://arxiv.org/abs/2501.09363 (đã mở abstract) | Ấn Độ (Ayurveda); dùng Indian Medicinal Leaves Dataset, MED117 và dataset tự thu; 99,5%/98,4%/99,7% (tự báo cáo) |
| A8 | **Barz & Denzler 2019**: Do We Train on Test Data? Purging CIFAR of Near-Duplicates, arXiv:1902.00423, DOI 10.3390/jimaging6060041 | 2019/2020 | https://arxiv.org/abs/1902.00423 (đã mở abstract) | CIFAR-10/100: 3,3%/10% ảnh test có bản trùng trong train; tạo bộ test sạch ciFAIR; accuracy tụt 9-14% (tương đối). **Bài gốc của hướng "đo độ thổi phồng do trùng ảnh"** |
| A9 | **Morra & Lamberti 2019**: Benchmarking unsupervised near-duplicate image detection, arXiv:1907.02821, DOI 10.1016/j.eswa.2019.05.002 | 2019 | https://arxiv.org/abs/1907.02821 (đã mở abstract) | Khung benchmark khử trùng không giám sát (MFND, UKBench); dùng làm công cụ so phương pháp khử trùng |

Tìm kiếm arXiv bổ sung (đã chạy, 2026-11-26):
- `all:VNPlant` → 0; `all:"Vietnamese medicinal plant"` → 0; `all:"medicinal plant" AND all:benchmark` → 0;
  `all:"plant image dataset" AND all:deduplicat` → 0; `all:herb dataset` → 22 (không có bộ Việt/ĐNA có split chống rò rỉ).
- `all:"plant species" AND all:"out-of-distribution"` → 0; `all:"plant species" AND all:uncertainty` → 0 (arXiv, lượt này).

### Điểm còn mới (so với các bộ trên)
- **Ảnh tự chụp Việt Nam, 3 tỉnh, ~165 loài**: TCMP-300/IndoHerb/MED117/MedLEA/IndoHerb-2025 đều từ nước khác (TC, ID, SL, NP, IN).
  VNPlant-200 (A1) cùng Việt Nam nhưng chưa mở được bài gốc; theo trích dẫn trong P1 là 20.000 ảnh, 200 loài.
- **Quy mô ảnh/loài**: ViMeLeaf ~62k ảnh / ~165 loài (≈375 ảnh/loài trung vị 247); lớn hơn VNPlant-200, P7 (A4), MedLEA (A5)
  về số ảnh/loài; ngang TCMP-300 (A2) về tổng số ảnh nhưng ảnh tự chụp, không phải web-scrape.
- **Khử trùng + split chống rò rỉ có log nhóm**: A2 (TCMP-300) có lọc trùng nhưng bằng VLM+người, ảnh từ web,
  không công bố split theo nhóm trùng/đợt chụp. A8 (Barz & Denzler) chứng minh vấn đề ở CIFAR nhưng
  **không đo trên dataset cây thuốc**. Chưa thấy bài nào đo "độ thổi phồng accuracy" cho ảnh cây thuốc Việt.
- **Đuôi dài**: 72/165 tên < 100 ảnh (dữ kiện từ đề xuất) — điểm khác biệt so với TCMP-300 (300 loài, phân bố không mô tả).

### Rủi ro trùng / việc phải làm
- Trùng một phần với **VNPlant-200** nếu bộ đó đã công bố ảnh cây thuốc Việt. Cần chủ nhóm cung cấp
  tên/link bài FAIR 2025 + luận văn để tách phần mới (chưa kiểm chứng, không dùng để chấm điểm).
- Bài 1 bắt buộc trích và nêu rõ phần mới so với A1-A7; nếu không reviewer sẽ coi là bản 2 của bài cũ.
- Số "độ thổi phồng" phụ thuộc tỉ lệ trùng thực đo (pipeline RES-26, chưa chạy trên dữ liệu thật).

---

## Bài 2: nhận dạng loài dễ nhầm, đuôi dài, biết từ chối

### Công trình gần nhất đã mở

| # | Bài | Năm | Link (đã mở) | Ghi chú |
|---|---|---|---|---|
| B1 | **CCL-SC**: Confidence-aware Contrastive Learning for Selective Classification, ICML 2024, arXiv:2406.04745 | 2024 | https://arxiv.org/abs/2406.04745 (đã mở abstract) | Chọn lựa theo confidence; benchmark CIFAR-10/100, CelebA, ImageNet |
| B2 | **Towards Better Selective Classification**, arXiv:2206.09034 | 2022-2023 | https://arxiv.org/abs/2206.09034 (đã mở abstract) | Chọn theo classification scores + entropy regularizer |
| B3 | **Know When to Abstain**: Optimal Selective Classification with Likelihood Ratios, arXiv:2505.15008 (v3 2026) | 2025 | https://arxiv.org/abs/2505.15008 (đã mở abstract) | Chọn theo Neyman-Pearson; đo trên vision và VLM, **có covariate shift** (liên quan trực tiếp đến OOD điện thoại) |
| B4 | **Holistic Uncertainty Estimation for Open-Set Recognition (HolUE)**, arXiv:2408.14229 | 2024 | https://arxiv.org/abs/2408.14229 (đã mở abstract) | Open-set recognition (thân thế học + cá voi/cá heo); ước lượng bất định "toàn phần" (gallery + embedding) |
| B5 | **Few-shot open-set recognition (meta-learning)**, arXiv:2005.13713 | 2020 | https://arxiv.org/abs/2005.13713 (abstract qua arXiv search; chưa mở trang) | Few-shot + OOS; không cây |
| B6 | **A novel approach to navigate the taxonomic hierarchy ... Open-World Scenarios in Medicinal Plant Classification**, arXiv:2502.17289 (v4) | 2025 | https://arxiv.org/abs/2502.17289 (đã mở abstract; v2/v3 withdrawn) | Phân cấp phylum→species, loài lạ: 83,36% (phylum) → 43,32% (family). **Bài open-set cây thuốc gần nhất** |
| B7 | **Local Foreground Selection aware ... few-shot fine-grained plant species classification**, arXiv:2501.06909 | 2025 | https://arxiv.org/abs/2501.06909 (đã mở abstract) | Few-shot fine-grained cây; 3 dataset cây; không cây thuốc, không an toàn |
| B8 | **Self-Supervised Learning of Plant Image Representations**, arXiv:2604.27538 | 2026 | https://arxiv.org/abs/2604.27538 (đã mở abstract) | SimDINOv2 trên iNaturalist-Plantae; **đánh giá few-shot**, so với Pl@ntCLEF và BioCLIP; cùng hướng "mô hình nền cho cây" |
| B9 | **Selective prediction and automation bias** (user study y khoa), arXiv:2508.07617 | 2025 | https://arxiv.org/abs/2508.07617 (đã mở abstract) | Khi AI từ chối, bác sĩ bỏ sót chẩn đoán/treatment tăng (false negative +18%/+35%); cảnh báo khi thiết kế "từ chối = an toàn" |

### Điểm còn mới (so với các bài trên)
- B1-B5: khung **phương pháp** (selective/open-set) đã có; **chưa thấy bài nào dùng cho cây thuốc + an toàn khi nhầm**.
- B6 là bài open-set cây thuốc gần nhất, nhưng: (a) phân cấp theo phân loại học (phylum→species), không phải **cặp dễ nhầm có nhãn an toàn**;
  (b) dataset là bộ SOTA Ấn Độ (không nêu tên cây thuốc Việt/ĐNA); (c) không có cơ chế từ chối kèm cảnh báo độc tính.
- **B7+B8**: few-shot cây và mô hình nền (DINOv2/BioCLIP) cho cây đã có (B8 chính là hướng "foundation model cây"
  cùng thời). Điểm mới còn lại: **bộ benchmark cặp dễ nhầm (bắt đầu từ Dây giác/Sục sạc trong ViMeLeaf) + đường risk–coverage + ảnh điện thoại OOD + từ chối ở mức "cặp nguy hiểm"**.
- **B9**: từ chối không tự động an toàn cho người dùng (bỏ sót tăng); bài 2 phải **đo** hiệu ứng này trên người dùng
  (chủ nhóm hoặc đối tượng), không chỉ đo AURC. Nếu không, reviewer sẽ hỏi "từ chối có làm người dùng bỏ qua cảnh báo không?".

### Rủi ro trùng / việc phải làm
- MLLM nhận dạng cây (P3 trong brief-medicinal-plants: Jiang 2026, DOI 10.3389/fpls.2026.1765281,
  200 ảnh trắc nghiệm, Qwen3-VL-235B 90,5%) **chưa mở lại trong lượt này** (lượt trước). Trích vào bài 2 như đối chứng MLLM,
  ghi "chưa kiểm chứng lại" nếu chưa đọc lại abstract.
- Duôi dài (72 loài <100 ảnh): chưa thấy benchmark cây thuốc ĐNA công bố; nếu không thu thêm ảnh, bài chỉ có 72/165 loài đuôi.
- Cần **chuyên gia dược** đánh dấu cặp nào nhầm thì nguy hiểm (độc/không dùng được); không có thì "an toàn khi nhầm" không đo được.
- B3 (Neyman-Pearson + covariate shift) nên so trực tiếp vì cùng đo OOD; nếu chỉ so threshold-naive thì bị chê phương pháp cũ.

---

## Bài 3: KG cây thuốc + GraphRAG có lọc an toàn

### Công trình gần nhất đã mở

| # | Bài | Năm | Link (đã mở) | Ghi chú |
|---|---|---|---|---|
| C1 | **OpenTCM**: GraphRAG cho TCM (phụ khoa), arXiv:2504.20118 (v4) | 2025 | https://arxiv.org/abs/2504.20118 (đã mở abstract) | KG >48k thực thể, >152k quan hệ từ 68 sách; GraphRAG không fine-tune; điểm chuyên gia 4,378/4,045 |
| C2 | **ShenNongDiet**: KG+RAG cho thuốc-độc TCM, Chinese Medicine 21:214, 2026, DOI 10.1186/s13020-026-01505-x | 2026 | https://doi.org/10.1186/s13020-026-01505-x (đã mở abstract qua Crossref) | Neo4j: 3.376 bài thuốc, 2.110 nguyên liệu, 38.669 quan hệ; có **CONTRAINDICATED_FOR** theo nhóm người; RAG hybrid (graph 0,2 + vector 0,8) + LoRA Qwen3-8B; Hit@1 84%, MRR 0,878. **Bài gần nhất về "GraphRAG + chống chỉ định"** |
| C3 | **TCMaster**: Confidence-aware querying cho KG TCM, arXiv:2609.25712 | 2026 | https://arxiv.org/abs/2609.25712 (đã mở abstract) | KG ~221k thực thể, ~723k cạnh; mỗi cạnh có provenance confidence; lọc theo ngưỡng bỏ 39,3% đường đi kém chất lượng; +20 điểm accuracy TCMbench QA. **Bài gần nhất về "lọc cạnh KG theo độ tin cậy"** |
| C4 | **BEACON-SP**: Ontology-grounded GraphRAG cho đánh giá rủi ro tự tử, arXiv:2610.09026 | 2026 | https://arxiv.org/abs/2610.09026 (đã mở abstract) | KG bệnh nhân + ontology (Three-Step Theory, IMV, SDOH); benchmark 1.500 câu, 100 bệnh nhân; GraphRAG tốt hơn vector-RAG (76,4% trường hợp được ưu tiên). **Y khoa lâm sàng, không cây thuốc** |
| C5 | **MED-COPILOT**: GraphRAG + similar-patient, arXiv:2603.00460 | 2026 | https://arxiv.org/abs/2603.00460 (đã mở abstract) | KG từ WHO/NICE guidelines + 36k ca bệnh (MIMIC-IV/Synthea); không cây thuốc |
| C6 | **IMPPAT 3.0**: FAIR database + KG cây thuốc Ấn Độ (Ayurveda), arXiv:2610.07478 | 2026 | https://arxiv.org/abs/2610.07478 (đã mở abstract) | CSDL + IMPPAT-KG (thực thể cây, phytochemical, bài thuốc, link ảnh cây, clinical trial, patent); không GraphRAG, không an toàn |
| C7 | **Empowering GraphRAG with Knowledge Filtering and Integration (GraphRAG-FI)**, arXiv:2503.13804 | 2025 | https://arxiv.org/abs/2503.13804 (đã mở abstract) | Hai-stage filtering (loại cạnh/đường đi nhiễu) + logits-based integration; benchmark KG QA chung, không y khoa |
| C8 | **Do We Still Need GraphRAG?** (RAGSearch), arXiv:2604.09666 | 2026 | https://arxiv.org/abs/2604.09666 (đã mở abstract) | So sánh agentic search + dense RAG với GraphRAG; GraphRAG vẫn lợi thế ở multi-hop, kém hơn về chi phí offline |
| C9 | **When to use Graphs in RAG** (GraphRAG-Bench), arXiv:2506.05690 (v3) | 2025-2026 | https://arxiv.org/abs/2506.05690 (đã mở abstract) | Benchmark khi nào GraphRAG thắng RAG (fact retrieval, complex reasoning, summarization, creative) |
| C10 | **Vietnamese RAG benchmark tổng quát** (arXiv:2403.01616, PACLIC-IR benchmark 2503.07470) | 2024-2025 | https://arxiv.org/abs/2403.01616, https://arxiv.org/abs/2503.07470 (đã mở abstract) | Benchmark RAG/embedding tiếng Việt tổng quát; **không có KG, không cây thuốc** |
| C11 | **VietMed-MCQ** (đã rút), arXiv:2601.03792 | 2026 | https://arxiv.org/abs/2601.03792 (đã mở abstract + note rút) | 3.190 MCQ y học cổ truyền Việt; **bị rút** (tác giả sửa lại, "not a final representation"). **Không dùng** |

Tìm kiếm arXiv bổ sung (đã chạy):
- `all:"Vietnamese" AND all:"knowledge graph"` → 0; `all:"Vietnamese" AND all:"knowledge graph" AND all:medical` → 0;
  `all:"Vietnamese" AND all:"knowledge graph" AND all:"question answering"` → 0;
  `all:"Vietnamese" AND all:RAG` → 6 (không bài nào về KG cây thuốc).
- `all:"herb" AND all:"knowledge graph"` (mở rộng: `all:"medicinal plant" AND all:"knowledge graph"`) → chỉ C6 (IMPPAT 3.0)
  và một bài NLP trên văn bản Ayurveda (2608.28608, không GraphRAG, không an toàn).
- `all:"GraphRAG" AND all:medical` → C4, C5, C1, C7, C8 (không cây thuốc Việt/ĐNA).

### Điểm còn mới (so với các bài trên)
- **Ngôn ngữ + miền**: OpenTCM (C1), ShenNongDiet (C2), TCMaster (C3) đều TCM Trung Quốc; C6 (IMPPAT) là Ấn Độ (Ayurveda).
  Chưa thấy KG + GraphRAG cây thuốc **Việt Nam/ĐNA**, chưa thấy bản tiếng Việt (tìm `all:"Vietnamese" AND all:"knowledge graph" AND all:medicine` → 0).
- **Đầu vào là ảnh**: C1 (OpenTCM), C2 (ShenNongDiet), C3 (TCMaster) chỉ có văn bản làm đầu vào.
  Chưa thấy hệ thống "ảnh cây → nhận dạng → truy vấn KG → trả lời có cảnh báo".
- **Lọc an toàn cứng có truy vết**: C2 có CONTRAINDICATED_FOR + RAG hybrid (trộn mềm, graph weight 0,2),
  **không mô tả lọc cứng trước khi sinh** (chưa kiểm chứng). C3 chỉ lọc cạnh theo độ tin cậy (θ), không phải "an toàn".
  C7 lọc nhiễu chung (không y khoa). Chưa thấy bài nào **gắn cờ/loại ứng viên vi phạm chống chỉ định trước khi sinh + đường đi KG làm bằng chứng** (chính là E2 trong `experiments/backlog.md`).
- **Benchmark an toàn tiếng Việt**: chưa thấy (C11 rút). ViMeLeaf metadata (66-80 loài, có tính vị/liều dùng) là hạt giống,
  cần chuyên gia dược duyệt + gộp câu hỏi an toàn (30-40% tập test, như E2).

### Rủi ro trùng / việc phải làm
- **Bắt buộc trích C1, C2, C3, C7** và nêu phần mới (tiếng Việt + ảnh + lọc an toàn cứng). Không trích C2 thì reviewer
  sẽ hỏi "khác gì so với ShenNongDiet".
- C11 (VietMed-MCQ) bị rút: không trích như công trình đã công bố; nếu cần dẫn "đã có người làm benchmark MCQ y học cổ
  truyền Việt" thì ghi "arXiv:2601.03792 (rút, chưa công bố)".
- C4 (BEACON-SP) chứng minh ontology-grounded GraphRAG được cho y khoa nặng (tự tử); dùng làm tiền lệ, không đối thủ.
- C8/C9 (GraphRAG-Bench, RAGSearch) cho thấy GraphRAG không luôn thắng; bài 3 nên **đo khi nào lọc an toàn cứng thắng**,
  không chỉ chạy 1 cấu hình và báo kết quả đẹp.
- Cần **chuyên gia dược** duyệt KG (66-80 loài) + chấm tập đánh giá an toàn; không có thì không đo được "an toàn".
- Dữ liệu y tế: chỉ dùng nguồn công khai (Dược điển, sách tra cứu đã xuất bản); không đưa dữ liệu bệnh nhân.

---

## Việc cần làm tiếp (theo thứ tự, dưới 60 phút còn lại của lượt)

1. **Bài 1**: trích phần mới so với A1-A7 vào đề xuất; ghi rõ "VNPlant-200 chưa kiểm chứng, cần mở bài gốc trước khi nộp".
2. **Bài 2**: thêm MLLM (P3) + B3 (Neyman-Pearson/covariate shift) + B9 (automation bias khi từ chối) vào phần phương pháp;
   xác nhận có chuyên gia dược đánh dấu cặp nguy hiểm; nếu không, thu hẹp claim "an toàn khi nhầm" thành "đường risk-coverage
   trên cặp đã chọn, chưa gán nhãn nguy hiểm".
3. **Bài 3**: trích C1, C2, C3, C7; ghi rõ "lọc an toàn cứng trước khi sinh + truy vết đường đi" là phần mới so với C2/C3;
   xác nhận chuyên gia dược duyệt KG; dựng 30-40% câu an toàn trong tập đánh giá (E1/E2 đã có kế hoạch trong backlog).
4. **Cả 3 bài**: không dùng C11 (VietMed-MCQ) làm công trình đã công bố; nếu chủ nhóm có tên/link bài FAIR 2025,
   thêm vào A1 cùng VNPlant-200 làm "bản 1 cần trích".
5. Cập nhật đề xuất `vimeleaf-3-paper-series.md` với các mục "chưa kiểm chứng" ở trên, rồi Critic phản biện (RES-27 mục 3).

## Chưa kiểm chứng (không dùng để chấm điểm, ghi lại để làm sau)

- VNPlant-200 (A1): chỉ đọc qua trích dẫn trong P1 (TCMP-300); chưa mở được bài gốc, chưa xác nhận link tải/giấy phép/quy mô ảnh/loài thật.
- Bài FAIR 2025 + luận văn ThS của chủ nhóm: chưa có tên/link; chưa kiểm chứng.
- P3 (Jiang 2026 MLLM cây thuốc, DOI 10.3389/fpls.2026.1765281): đã trích trong brief-medicinal-plants, chưa mở lại abstract trong lượt này.
- Trạng thái Scopus của Data in Brief, Scientific Data, Ecological Informatics, Frontiers in Plant Science: chưa tra trực tiếp (SCImago chặn truy cập tự động).
