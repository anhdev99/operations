# Top 5 đề tài nghiên cứu nên theo đuổi

Issue: RES-8 (con của RES-1). Người tổng hợp: Dean. Ngày: 2026-11-24.
Nguồn: 5 brief của Scholar (`brief-cv-dental.md` RES-2, `brief-kg-rag-medical.md` RES-3, `brief-empathetic-chatbot.md` RES-4,
`brief-ontology-kg.md` RES-5, `brief-cv-emotion.md` RES-6) và phản biện của Critic (`review-briefs.md`, RES-7).

## Quy ước kiểm chứng trong tệp này

- **Chỉ dùng làm căn cứ** các bài/dataset mà Critic đã đánh dấu ✓ (mở được, nội dung khớp) trong `review-briefs.md`.
- Bài Scholar có trích nhưng Critic chưa kiểm lại hoặc đánh ⚠ thì ghi "(chưa kiểm chứng)" và **không dùng để chấm điểm**.
- Nơi công bố: đã xác nhận **tồn tại** (OpenAlex/trang chủ). **Trạng thái Scopus hầu hết chưa tra trực tiếp** (SCImago chặn truy cập tự động);
  chỉ JMIR Formative Research, JMIR Human Factors, JMIR Mental Health có trang indexing ghi Scopus. Chủ nhóm tra lại Scopus/SJR trước khi nộp.
- Thang điểm 1-5 cho mỗi tiêu chí: Mới = tính mới/khoảng trống; ƯD = ứng dụng thực tiễn; KT = khả thi cho một người; CB = khả năng công bố; NCS = hợp hồ sơ NCS.
- Critic giữ nguyên toàn bộ điểm của Scholar (không lỗi nặng). Dean chỉ thay đổi một chỗ: gộp đề tài "Việt hoá OHD" (RES-5) vào đề tài #2 vì trùng phần việc.

---

## Bảng xếp hạng

| # | Đề tài | Nguồn | Mới | ƯD | KT | CB | NCS | Tổng |
|---|---|---|---|---|---|---|---|---|
| 1 | Sinh báo cáo X-quang panoramic tiếng Việt có căn cứ mức răng, VLM nhỏ | RES-2 đề tài 1 | 4 | 5 | 4 | 4 | 5 | **22** |
| 2 | Chatbot nha khoa tiếng Việt neo vào ontology OHD (kèm Việt hoá OHD) | RES-3 đề tài B + RES-5 đề tài 2 | 5 | 5 | 3 | 4 | 5 | **22** |
| 3 | ViEmpath-Dental: hội thoại đồng cảm tiếng Việt cho bệnh nhân lo âu nha khoa | RES-4 đề tài 1 | 5 | 4 | 3 | 4 | 5 | **21** |
| 4 | ViText2KG: benchmark + LLM nhỏ trích KG tiếng Việt tuân thủ ontology | RES-5 đề tài 1 | 4 | 3 | 5 | 4 | 5 | **21** |
| 5 | Đánh giá đau từ video khuôn mặt, mô hình nhẹ, chéo dataset, có độ bất định | RES-6 đề tài 1 | 4 | 5 | 3 | 4 | 4 | **20** |

Xếp #1 trên #2 khi bằng điểm: #1 khả thi hơn (dữ liệu tải tự do, baseline không cần chuyên gia trong 3 tuần đầu) và mảng chạy nhanh nên cần vào sớm.

Năm đề tài phủ đủ năm hướng (CV, chatbot, ontology, cảm xúc, răng hàm mặt) và đều nối vào trục **răng hàm mặt tiếng Việt**:
#4 là máy trích KG → #2 dùng ontology nha khoa → #1 gắn mã khái niệm vào báo cáo ảnh → #3, #5 thêm lớp cảm xúc/đau cho bệnh nhân.

---

## 1. Sinh báo cáo panoramic tiếng Việt có căn cứ mức răng, chạy trên GPU nhỏ

**Câu hỏi nghiên cứu.** Pipeline "detector chuyên biệt + VLM nhỏ (≤4B) đóng băng" có sinh được báo cáo panoramic tiếng Việt có cấu trúc
(vị trí FDI, phát hiện, mức độ) với tỉ lệ ảo giác mức răng thấp hơn VLM fine-tune trực tiếp không? Cần bao nhiêu bằng chứng từ công cụ là đủ?

**Khoảng trống (bài Critic đã xác nhận):**
- Hao J. et al., 2025, MMOral/OralGPT, NeurIPS 2025 — https://arxiv.org/abs/2509.09254. 20.563 ảnh, 1,3 triệu instruction; GPT-4o chỉ 41,45% trên MMOral-Bench. Chỉ tiếng Anh, cần VLM 7B fine-tune.
- Yu Z. et al., 2026, OPGAgent — https://arxiv.org/abs/2603.00462. Đo ảo giác bằng bộ ba (Location, Field, Value); code chưa phát hành; không tiếng Việt.
- Rafid A. et al., 2026, AgenTeeth — https://arxiv.org/abs/2609.17800. VLM đóng băng + bằng chứng từ 7 mô hình chuyên gia, +12,9 đến 23,0 điểm. Chỉ VQA, không sinh báo cáo, không mô hình nhỏ cục bộ.
- Li X. et al., 2026, PanDent — https://arxiv.org/abs/2607.27378. Mô hình "viết trôi chảy nhưng sai vị trí"; dữ liệu đầy đủ chưa phát hành; chỉ tiếng Anh.
- Chỗ trống: **báo cáo tiếng Việt + VLM nhỏ + đo ảo giác mức răng**. Chưa thấy bài nha khoa tiếng Việt (tìm kiếm chưa đầy đủ, cần tra Google Scholar).

**Dataset công khai:**
| Tên | Link | Giấy phép | Ghi chú |
|---|---|---|---|
| DENTEX | https://huggingface.co/datasets/ibrahimhamamci/DENTEX | CC BY-NC-SA 4.0, tải tự do | 11,8 GB; đánh số FDI + 4 chẩn đoán; 1.571 ảnh không nhãn |
| MMOral-OPG-Bench | https://huggingface.co/datasets/OralGPT/MMOral-OPG-Bench | MIT | 100 ảnh, 491 câu đóng + 578 câu mở |
| MMOral-OPG-Training | https://huggingface.co/datasets/OralGPT/MMOral-OPG-Training | gated, điều kiện xin chưa kiểm chứng | không bắt buộc cho baseline |

**Baseline (8 tuần, GPU 8-12 GB).** Tuần 1-3: YOLOv8/v11 hoặc RT-DETR trên DENTEX (FDI + 4 chẩn đoán). Tuần 4-6: đầu ra detector → JSON → VLM 3B 4-bit
viết báo cáo tiếng Việt theo mẫu; so với VLM không có bằng chứng. Tuần 7-8: đo precision/recall mức răng và tỉ lệ ảo giác trên test DENTEX,
dịch MMOral-OPG-Bench sang tiếng Việt cho VQA. 3 seed. Một nha sĩ duyệt mẫu nhỏ báo cáo.

**Ứng dụng/demo.** Web app (Gradio) cho phòng khám nhỏ: tải ảnh panoramic → bản nháp báo cáo tiếng Việt có khung từng răng → nha sĩ sửa, in cho bệnh nhân.

**Nơi công bố (tồn tại, Scopus cần tra):** Dentomaxillofacial Radiology; Journal of Imaging Informatics in Medicine; IEEE Access.

**Rủi ro.** Mảng VLM nha khoa ra bài hằng tháng, có thể bị đi trước; DENTEX NC-SA nên demo chỉ phi thương mại; DENTEX chỉ 4 chẩn đoán nên báo cáo hẹp;
thiếu nha sĩ thẩm định thì bài yếu.

---

## 2. Chatbot nha khoa tiếng Việt neo vào ontology OHD (kèm Việt hoá OHD)

**Câu hỏi nghiên cứu.** (a) LLM có tạo được nhãn/định nghĩa tiếng Việt chấp nhận được cho phần lõi OHD (bệnh, thủ thuật, vật liệu) không?
(b) Neo truy hồi vào OHD tiếng Việt có giảm ảo giác và tăng độ đúng của chatbot tư vấn nha khoa tiếng Việt so với RAG văn bản thường không?

**Khoảng trống (bài Critic đã xác nhận):**
- Wu J. et al., 2024, Medical Graph RAG — https://arxiv.org/abs/2408.04187. GraphRAG y khoa mạnh, mã MIT, chỉ tiếng Anh, không chuyên nha khoa.
- Duncan W.D. et al., 2020, OHD, Journal of Biomedical Semantics — DOI 10.1186/s13326-020-00222-0; và 2026, DOI 10.1186/s13326-026-00350-z.
  OHD xây và mở rộng thủ công, chỉ tiếng Anh, chưa dùng LLM.
- Chưa thấy bài dùng OHD làm nguồn cho LLM-RAG (Scholar tìm arXiv `dental AND "knowledge graph"`: chỉ 1 kết quả, không dùng OHD).
- *Tham khảo thêm, chưa kiểm chứng:* DentalBench (arXiv:2508.20416; bài mở được nhưng link tải dữ liệu chưa kiểm chứng),
  SCMPE (arXiv:2601.12974), OntoExtend (DOI 10.3233/ssw260011). Critic chưa xác nhận đủ, nên **không dùng làm căn cứ cho khoảng trống hay điểm** ở trên;
  khoảng trống của #2 chỉ dựa trên MedGraphRAG và hai bài OHD đã xác nhận. Chủ nhóm đọc lại ba bài này trước khi viết phần related work.

**Dataset/tài nguyên công khai:**
| Tên | Link | Giấy phép | Ghi chú |
|---|---|---|---|
| OHD ontology | https://github.com/oral-health-and-disease-ontologies/ohd-ontology · https://obofoundry.org/ontology/ohd.html | CC BY 4.0 | 1.881 term (OLS, bản 2026-11-18) |
| MedGraphRAG code | https://github.com/SuperMedIntel/Medical-Graph-RAG | MIT | baseline GraphRAG |
| Tập đánh giá nha khoa tiếng Việt | chưa có | — | phải tự dựng 300-500 câu; đây là phần tốn công nhất |

**Baseline (8 tuần, GPU 12-16 GB, chỉ suy luận).** Tháng 1: rút ~300-500 lớp lõi OHD, LLM sinh nhãn tiếng Việt ở 3 chế độ (không ngữ cảnh / có cây cha-con / có truy xuất thuật ngữ),
nha sĩ chấm chấp nhận/sửa (≥2 người, đo kappa). Tháng 2: so RAG văn bản vs RAG neo OHD trên 300-500 câu nha khoa tiếng Việt, LLM 7-8B 4-bit;
đo accuracy và tỉ lệ khẳng định trái với ontology.

**Ứng dụng/demo.** Chatbot web/Zalo mini-app cho phòng khám: trả lời câu hỏi bệnh nhân trước/sau điều trị, mỗi câu dẫn khái niệm OHD; kèm từ điển OHD song ngữ tra cứu được.

**Nơi công bố (tồn tại, Scopus cần tra):** SOICT (Springer CCIS, trang chủ ghi Scopus); Journal of Biomedical Semantics (đã đăng chuỗi OHD); JMIR Medical Informatics (OA, có APC — cần board duyệt nếu chọn).

**Rủi ro.** Bắt buộc có nha sĩ chấm; OHD thiên về hồ sơ/billing kiểu Mỹ, có thể thiếu kiến thức cho bệnh nhân; chưa có tập đánh giá tiếng Việt sẵn.

**Vì sao ƯD = 5 mà KT = 3.** Hai tiêu chí đo hai việc khác nhau: ƯD chấm *giá trị khi làm xong* (chatbot tiếng Việt cho bệnh nhân, dẫn khái niệm chuẩn, dùng ngay ở phòng khám);
KT chấm *công sức để làm xong* — tính toán nhẹ (chỉ suy luận) nhưng phải tự dựng 300-500 câu đánh giá và cần ≥2 nha sĩ chấm. Các rủi ro trên đã được tính vào KT = 3, không trừ thêm ở ƯD.
Đây cũng là lý do #2 bằng điểm #1 nhưng xếp sau, và khuyến nghị chỉ làm song song tháng 1 (Việt hoá OHD) chứ không bắt đầu bằng chatbot.

---

## 3. ViEmpath-Dental: hội thoại đồng cảm tiếng Việt cho bệnh nhân lo âu nha khoa

**Câu hỏi nghiên cứu.** LLM mở 7-8B và LLM thương mại phản hồi đồng cảm bằng tiếng Việt cho bệnh nhân lo âu nha khoa tốt đến đâu so với tiếng Anh,
và LoRA trên tình huống nha khoa có tăng đồng cảm mà không làm sai thông tin y khoa không?

**Khoảng trống (bài Critic đã xác nhận):**
- She et al., 2026, EmplifAI — https://arxiv.org/abs/2601.10033. Benchmark đồng cảm y khoa tiếng Nhật (280 tình huống, 4.125 hội thoại); không tiếng Việt, không nha khoa.
- Rashkin et al., ACL 2019, EmpatheticDialogues — https://arxiv.org/abs/1811.00207; Liu et al., ACL 2021, ESConv — https://arxiv.org/abs/2106.01144. Tiếng Anh, đời sống chung, không bối cảnh lâm sàng.
- Sharma et al., EMNLP 2020, EPITOME — DOI 10.18653/v1/2020.emnlp-main.425. Khung đo đồng cảm, chỉ tiếng Anh.
- Guo et al., 2026, VR cho lo âu nha khoa — https://arxiv.org/abs/2609.15867. Can thiệp bằng VR (RCT N=24), không phải hội thoại; giai đoạn trước hẹn còn trống.
- Không tìm thấy dataset hội thoại đồng cảm tiếng Việt công khai (bằng chứng gián tiếp: tìm HF và arXiv không ra; Critic chấp nhận).

**Dataset công khai:**
| Tên | Link | Giấy phép | Vai trò |
|---|---|---|---|
| EmpatheticDialogues | https://huggingface.co/datasets/facebook/empathetic_dialogues | CC BY-NC 4.0 | dịch làm tập phụ |
| ESConv | https://huggingface.co/datasets/thu-coai/esconv | CC BY-NC 4.0, chỉ nghiên cứu | dịch làm tập phụ, nhãn chiến lược |
| UIT-VSMEC | https://huggingface.co/datasets/SEACrowd/uit_vsmec | **giấy phép không rõ** | chỉ dùng sau khi xác nhận giấy phép |
| Bộ tình huống nha khoa | tự xây | — | 150-300 tình huống do tác giả + bác sĩ RHM viết, LLM mở rộng, chuyên gia duyệt; không dùng hội thoại bệnh nhân thật |

**Baseline (8 tuần, GPU 16-24 GB cho QLoRA).** Zero-shot 3-4 LLM trên cùng bộ tình huống, song song VI/EN; QLoRA 7-8B trên ~2-3k hội thoại
(tình huống tự xây + ESConv dịch); đánh giá người (2-3 người, thang đồng cảm + đúng/sai thông tin) và LLM-as-judge, báo tương quan.

**Ứng dụng/demo.** Chatbot trước buổi hẹn: bệnh nhân kể nỗi sợ (đau, kim, chi phí), bot đáp đồng cảm, giải thích quy trình, nhắc hỏi bác sĩ; tuyên bố là AI, không chẩn đoán.

**Nơi công bố:** JMIR Formative Research (trang indexing ghi Scopus, CiteScore 4,2); JMIR Human Factors (Scopus, CiteScore 5,6); BMC Oral Health (tồn tại, Scopus chưa tra).

**Rủi ro.** Dữ liệu tự sinh có thể thiếu tự nhiên; cần bác sĩ RHM; thử với người thật phải qua hội đồng đạo đức; giấy phép NC chặn thương mại hoá nếu dùng dữ liệu dịch.

---

## 4. ViText2KG: benchmark và LLM nhỏ trích KG tiếng Việt tuân thủ ontology

**Câu hỏi nghiên cứu.** LLM mở ≤8B (4-bit) trích bộ ba tiếng Việt tuân thủ ontology cho trước tốt tới đâu so với tiếng Anh trên cùng ontology?
Prompt có ràng buộc ontology + LoRA nhẹ giảm ảo giác và vi phạm domain/range bao nhiêu?

**Khoảng trống (bài Critic đã xác nhận):**
- Mihindukulasooriya et al., ISWC 2023, Text2KGBench — DOI 10.1007/978-3-031-47243-5_14. Chuẩn đánh giá text-to-KG theo ontology (29 ontology, 7 thước đo gồm tuân thủ ontology và ảo giác). Chỉ tiếng Anh.
- Các bài 2026 cải thiện trên Text2KGBench (Tiwari, DOI 10.3233/ssw260009; Pappacoda & Torroni, AKBC 2026) và bài KG tiếng Việt (To & Do, KSE 2020; Nguyen & Nguyen, arXiv:2609.00763)
  **(chưa kiểm chứng — Critic chưa mở được)**, không dùng để chấm.
- Chưa thấy benchmark text-to-KG theo ontology cho tiếng Việt (tìm OpenAlex; chưa tra Google Scholar).

**Dataset công khai:**
| Tên | Link | Giấy phép | Ghi chú |
|---|---|---|---|
| Text2KGBench | https://github.com/cenguix/Text2KGBench · Zenodo 10.5281/zenodo.7916716 | repo Apache-2.0; dữ liệu "Creative Commons", **loại CC cụ thể chưa xác nhận** | 13.474 + 4.860 câu |

**Baseline (8 tuần, GPU 12-16 GB).** Dịch câu + nhãn ontology DBpedia-WebNLG sang tiếng Việt, giữ bộ ba vàng; duyệt tay ~500 câu test.
Chạy Qwen2.5-7B / Llama-3.1-8B 4-bit zero/few-shot với prompt ontology, so VI với EN; kiểm tra domain/range bằng rdflib; LoRA trên tập train dịch;
đo 7 thước đo Text2KGBench, 3 seed. Nên thêm một tập nhỏ văn bản gốc tiếng Việt gán tay để tránh chê "dữ liệu dịch".

**Ứng dụng/demo.** Công cụ web: dán văn bản tiếng Việt, chọn ontology, nhận bộ ba có đánh dấu vi phạm ràng buộc, xuất RDF/Neo4j. Dùng lại cho #2 (đổ văn bản nha khoa vào OHD).

**Nơi công bố:** ACM TALLIP (tồn tại, OpenAlex); KSE (IEEE Xplore); Data & Knowledge Engineering. Scopus cần tra.

**Rủi ro.** Ứng dụng gián tiếp (công cụ hạ tầng); có thể nhóm VN khác đang làm; giấy phép CC của dữ liệu cần xác nhận trước khi phát hành bản dịch.

---

## 5. Đánh giá đau từ video khuôn mặt: mô hình nhẹ, chéo dataset, có độ bất định

**Câu hỏi nghiên cứu.** Mô hình video mặt ≤5M tham số chạy CPU/điện thoại có giữ được độ chính xác phát hiện đau khi chuyển từ BioVid sang UNBC-McMaster không?
Thêm ước lượng độ bất định ("không chắc thì hỏi lại bệnh nhân") giảm bao nhiêu cảnh báo sai?

**Khoảng trống (bài Critic đã xác nhận):**
- Gkikas et al., 2024, Frontiers in Pain Research — DOI 10.3389/fpain.2024.1372814. BioVid, video + nhịp tim, 82,74% nhị phân, 9,62M tham số; một dataset, không đo bất định.
- Fernandez Rojas et al., AI4Pain 2024, ACIIW 2024 — DOI 10.1109/aciiw63320.2024.00012. Baseline video mặt chỉ 40,1% (3 lớp); các kỳ sau bỏ nhánh video → benchmark video mặt bị bỏ ngỏ.
- AlAbdouli et al., 2026, AlamViT, Mathematics — DOI 10.3390/math14183376. 3,11M tham số; tự ghi chưa đo trên thiết bị biên, chưa train-một-test-kia.
- Pittara et al., 2025, Scientific Reports — DOI 10.1038/s41598-025-21987-3. Chỉ khung đỉnh, không video, không chéo dataset.

**Dataset (đau thực nghiệm trên tình nguyện viên, không phải bệnh nhân):**
| Tên | Link | Truy cập | Ghi chú |
|---|---|---|---|
| BioVid Heat Pain (Part A) | https://www.nit.ovgu.de/BioVid.html | phi thương mại; **người ký phải có vị trí cơ hữu ở viện/trường** | 8.700 mẫu, 87 người, 5 lớp |
| UNBC-McMaster Shoulder Pain | https://www.jeffcohn.net/Resources/ | giảng viên/nhà nghiên cứu xin; cấm thương mại | kích thước chưa kiểm chứng |
| AI4Pain 2024 | trang ai4pain.github.io trả 404 | **chưa kiểm chứng** cách tải | không dựa vào trong kế hoạch |

**Baseline (8 tuần, GPU nhỏ).** Cắt mặt (MediaPipe/OpenFace) + backbone FER nhẹ đóng băng + head thời gian nhỏ (1D-conv/GRU), BioVid LOSO;
train BioVid test UNBC và ngược lại; MC-dropout/temperature scaling, báo ECE; xuất ONNX/TFLite int8, đo FPS trên laptop CPU và 1 điện thoại; 3 seed.

**Ứng dụng/demo.** App theo dõi đau chạy cục bộ trên máy tính bảng cạnh ghế nha/giường hậu phẫu, hiện chỉ số đau + độ không chắc; demo chỉ trên tình nguyện viên, không quay bệnh nhân khi chưa có phê duyệt đạo đức.

**Nơi công bố (tồn tại, Scopus cần tra):** Frontiers in Pain Research; IEEE Access; IEEE Transactions on Affective Computing (mục tiêu cao).

**Về phán quyết "Cần sửa" của Critic (RES-7).** Phán quyết này nói về *rủi ro truy cập dữ liệu và link AI4Pain 404*, không phải sai trích dẫn hay sai điểm:
Critic giữ nguyên điểm của Scholar (Mới 4, các tiêu chí khác không đề nghị đổi). Rủi ro truy cập đã được tính vào KT = 3, nên tổng vẫn 20.
Dean giữ #5 trong danh sách **có điều kiện**: chỉ theo đuổi khi đã ký được form BioVid/UNBC; nếu không ký được, thay #5 bằng "Phát hiện răng bất thường ít nhãn trên DENTEX" (RES-2 đề tài 2, 19 điểm, dữ liệu tải tự do) —
hai mục 20 điểm trong "Vì sao không chọn" đã được gộp vào #2 nên không dùng làm phương án thay.

**Rủi ro.** **Không lấy được BioVid/UNBC thì đề tài không chạy được** — chủ nhóm là giảng viên nên có thể tự ký, cần gửi form ngay nếu chọn;
đau nhiệt ở tay khác đau nha khoa thật; độ chính xác đa mức thấp (~40-55%) khiến demo kém thuyết phục.

---

## Vì sao không chọn

| Đề tài | Điểm | Lý do loại |
|---|---|---|
| KG-RAG y khoa tiếng Việt chung, LLM nhỏ (RES-3 A) | 20 | Khoảng trống dựa trên bài tiếng Nhật (arXiv:2504.10982) và VM14K (arXiv:2506.01305) mà Critic chưa xác nhận; ứng dụng cạnh tranh với chatbot thương mại. Giữ làm cấu hình baseline bên trong #2. |
| Việt hoá + mở rộng OHD đứng riêng (RES-5 đề tài 2) | 20 | Trùng phần việc với #2; đã gộp làm tháng 1 của #2. |
| Phát hiện răng bất thường ít nhãn trên DENTEX (RES-2 đề tài 2) | 19 | Kỹ thuật bán giám sát đã quen (tính mới 3), demo yếu nếu đứng riêng. Dùng được như bài kỹ thuật phụ cho #1. |
| Chatbot hỗ trợ cảm xúc có chiến lược + lớp an toàn (RES-4 đề tài 3) | 19 | Ghép module đã có ở tiếng Anh (mới 3); nên làm sau #3 như bài hệ thống. |
| Landmark cephalometric bền vững giữa máy chụp (RES-2 đề tài 3) | 18 | Bài toán lâu đời, khó nối chuỗi với các hướng còn lại; là phương án dự phòng nhanh ra bài (Aariz CC BY 4.0, Critic ✓). |
| ViDentQA benchmark (RES-3 C), đo đồng cảm tiếng Việt (RES-4 đề tài 2) | 18 | Bài tài nguyên/đo lường, ứng dụng gián tiếp; sẽ phát sinh tự nhiên khi làm #2 và #3. |
| Engagement người học trực tuyến (RES-6 đề tài 2) | 18 | Nhãn benchmark nhiễu nặng, xa mạch y tế/răng hàm mặt, vấn đề riêng tư. |
| Đồ thị tiên quyết cho học liệu tiếng Việt (RES-5 đề tài 3) | 17 | Tách khỏi mạch y tế; LectureBank chưa rõ giấy phép. |
| FER nén cho thiết bị biên (RES-6 đề tài 3) | 15 | FER bão hoà, câu hỏi gốc đã có bài 2023. |

Các hướng Scholar đã loại sớm (Critic không phản đối): GraphRAG y khoa tiếng Anh, phân đoạn răng CBCT/panoramic thuần, FER ảnh tĩnh, nhận diện cảm xúc đa phương thức kiểu MER, KG completion và ontology matching bằng LLM.

---

## Khuyến nghị: bắt đầu từ đâu

**Bắt đầu với #1 (báo cáo panoramic tiếng Việt), chạy song song phần tháng 1 của #2 (Việt hoá OHD).**

Lý do:
1. **Vào được ngay, không chờ ai**: DENTEX tải tự do, 3 tuần đầu (detector) không cần chuyên gia, GPU 8-12 GB đủ. Các đề tài khác hoặc cần dựng dữ liệu từ đầu (#2, #3) hoặc chờ xin dữ liệu (#5).
2. **Mảng chạy nhanh**: VLM nha khoa có bài mới mỗi tháng; chậm 6 tháng có thể mất khoảng trống tiếng Việt.
3. **Demo mạnh nhất** cho mục tiêu ứng dụng: nha sĩ thấy ngay giá trị.
4. **Là trục của chuỗi NCS**: #1 (ảnh → báo cáo) + #2 (ontology + chatbot) gặp nhau ở báo cáo có mã khái niệm OHD và chatbot giải thích kết quả X-quang cho bệnh nhân; #3 thêm lớp đồng cảm. Chuỗi 3-4 bài: detector/báo cáo VI → OHD-vi + chatbot neo ontology → hội thoại đồng cảm → đánh giá ở phòng khám.

Phương án dự phòng: nếu **không tìm được nha sĩ cộng tác**, làm #4 (ViText2KG) — khả thi 5, không cần chuyên gia y khoa, vẫn nối lại được với #2 sau.
#5 chỉ nên chọn nếu chủ nhóm ký được form BioVid/UNBC sớm.

## Việc chủ nhóm cần làm trước khi mở repo

1. **Tìm 1-2 nha sĩ/bác sĩ RHM cộng tác** (cần cho #1, #2, #3) — đây là điều kiện chung lớn nhất.
2. Tra Google Scholar "nha khoa" + "tiếng Việt" + "AI" để xác nhận khoảng trống của #1 và #2.
3. Tra Scopus/SJR cho các tạp chí đã nêu.
4. Xác nhận giấy phép: loại CC của dữ liệu Text2KGBench (#4), UIT-VSMEC (#3, nếu dùng).
5. Nếu cân nhắc #5: gửi form BioVid và yêu cầu UNBC-McMaster ngay.
6. Mở repo private trong org `anhdev99-research-lab` cho đề tài đã chọn (nhánh `develop` + `main`).
