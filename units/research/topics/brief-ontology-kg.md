# Brief: Ontology / knowledge graph kết hợp LLM (RES-5)

Người soạn: Scholar · Ngày: 2026-11-24 · Dùng cho: RES-1 (chọn top 5 đề tài)

## Cách kiểm chứng

- arXiv API trả 429 trong lượt này nên tra bằng **OpenAlex** (metadata + abstract) và GitHub API (README, giấy phép, dung lượng repo). Chỉ đọc **abstract + README**, chưa đọc toàn văn; số liệu trích đúng như abstract/README.
- Nơi công bố: đã xác minh tồn tại qua OpenAlex (tên, ISSN-L, nhà xuất bản). **Trạng thái Scopus chưa kiểm chứng trực tiếp**; chủ nhóm tra lại trên Scopus/SJR trước khi nộp.
- Ranh giới với brief KG-RAG y khoa (issue anh em): brief này lo **xây/hoàn thiện ontology và KG** (trích xuất, mở rộng, chuẩn hoá); không đề xuất hệ hỏi đáp RAG.

## Bức tranh nhanh

- **LLM cho ontology learning** đã có benchmark chuẩn: LLMs4OL (challenge tại ISWC 2024, 2025, 2026). Bản 2026 chuyển sang bài toán thật: dựng ontology từ văn bản thô, mở rộng ontology có sẵn (Reuse), suy taxonomy cho miền chưa thấy. Toàn bộ dữ liệu tiếng Anh.
- **Text-to-KG theo ontology**: Text2KGBench (ISWC 2023) là chuẩn; năm 2026 có nhiều bài (ontology-aware prompting, LMKG) báo cải thiện trên nó. Chỉ tiếng Anh.
- **KG completion bằng LLM** (KICGPT, v.v.) và **ontology matching bằng LLM** (OLaLa, LLMs4OM, Agent-OM): rất đông, benchmark tiếng Anh, cần GPU/API lớn để cạnh tranh.
- **Tiếng Việt**: KG tiếng Việt chủ yếu là luật, du lịch, kiểm chứng tin, y học cổ truyền (VietMedKG); trích bộ ba kiểu cũ (NER + POS). Bài LLM gần nhất: KG cây từ SGK Lịch sử (arXiv 2026) nhưng benchmark truy vấn là tổng hợp, không có tập vàng cho trích xuất. **Chưa thấy benchmark text-to-KG theo ontology cho tiếng Việt** (tìm qua OpenAlex; chưa tra Google Scholar → khoảng trống *chưa kiểm chứng đầy đủ*).

---

## Đề tài 1: ViText2KG — benchmark và mô hình nhỏ trích KG tiếng Việt tuân thủ ontology

**Câu hỏi nghiên cứu.** LLM mở cỡ nhỏ (≤8B, 4-bit) trích bộ ba tiếng Việt tuân thủ ontology cho trước tốt tới đâu so với tiếng Anh trên cùng ontology? Prompt có ràng buộc ontology + LoRA nhẹ giảm tỉ lệ ảo giác và vi phạm domain/range bao nhiêu?

**Khoảng trống (bài đã mở):**
1. Mihindukulasooriya N., Tiwari S., Enguix C.F., Lata K., 2023, *Text2KGBench: A Benchmark for Ontology-Driven Knowledge Graph Generation from Text*, ISWC 2023 (LNCS). DOI 10.1007/978-3-031-47243-5_14. Hai tập: Wikidata-TekGen (10 ontology, 13.474 câu), DBpedia-WebNLG (19 ontology, 4.860 câu); 7 thước đo gồm tuân thủ ontology và ảo giác; baseline Vicuna-13B, Alpaca-LoRA-13B. **Chưa làm:** chỉ tiếng Anh.
2. Tiwari B. et al., 2026, *Ontology-Aware Prompting for Knowledge Graph Construction from Text*, Studies on the Semantic Web. DOI 10.3233/ssw260009. Prompt nhiều nhánh + lọc 3 tầng, tăng tới 2,3 lần so với baseline LLM, ảo giác <0,20 phần lớn miền. **Chưa làm:** chỉ tiếng Anh, không xét ngôn ngữ ít tài nguyên.
3. Pappacoda G., Torroni P., 2026, *LMKG: a flexible method for ontology-aware Knowledge Graph Extraction from text*, AKBC 2026. DOI 10.18653/2026.akbc-1.23. Ràng buộc ontology tăng mạnh độ tuân thủ trên Text2KGBench. **Chưa làm:** đơn ngữ tiếng Anh.
4. To H.D., Do P., 2020, *Extracting triples from Vietnamese text to create knowledge graph*, KSE 2020. DOI 10.1109/kse50997.2020.9287471. Trích bộ ba tiếng Việt bằng NER + POS trong câu đơn. **Chưa làm:** không có ontology đích, không có LLM, không có benchmark công khai.
5. Nguyen K.D., Nguyen M.N.H., 2026, *Automated Tree Knowledge Graph Construction using Ontology Expansion and Retrieval from Vietnamese History Textbooks*, arXiv. DOI 10.48550/arXiv.2609.00763. LLM + validator kép, 750 nút / 4.341 cạnh; 1.210 truy vấn tổng hợp. **Chưa làm:** không có tập vàng để đo độ chính xác trích xuất; một miền.

**Dataset công khai:**
| Tên | Link | Giấy phép / truy cập | Kích thước |
|---|---|---|---|
| Text2KGBench | https://github.com/cenguix/Text2KGBench · Zenodo 10.5281/zenodo.7916716 | Repo Apache-2.0 (GitHub API); abstract ghi "Creative Commons" cho dữ liệu — loại CC cụ thể chưa kiểm chứng | 13.474 + 4.860 câu, 29 ontology; repo ~7 MB |
| VLSP 2020 Relation Extraction | qua VLSP (arXiv:2012.10275 có nhắc) | phải đăng ký với VLSP — **chưa kiểm chứng** điều kiện | chưa kiểm chứng |

**Baseline 1-2 tháng (GPU hạn chế):**
- Tuần 1-3: dịch câu + nhãn ontology DBpedia-WebNLG sang tiếng Việt bằng LLM, giữ nguyên bộ ba vàng (thực thể chuyển ngữ khi cần); người duyệt tay mẫu ~500 câu test để có tập vàng sạch.
- Tuần 4-6: chạy Qwen2.5-7B / Llama-3.1-8B 4-bit, zero/few-shot với prompt ontology (theo Text2KGBench), so tiếng Anh với tiếng Việt; thêm bước kiểm tra domain/range bằng rdflib.
- Tuần 7-8: LoRA trên tập train dịch; đo 7 thước đo của Text2KGBench, 3 seed. GPU 12-16 GB đủ.

**Ứng dụng/demo:** công cụ web cho người làm dữ liệu/giáo viên/cán bộ số hoá: dán văn bản tiếng Việt, chọn ontology, nhận bộ ba có đánh dấu vi phạm ràng buộc, xuất RDF/Neo4j. Là "máy" dùng lại cho Đề tài 2 và 3.

**Nơi công bố (OpenAlex; Scopus cần tra lại):**
- ACM TALLIP (ACM, ISSN-L 2375-4699) — https://tallip.acm.org
- Data & Knowledge Engineering (Elsevier, ISSN-L 0169-023X) — http://www.elsevier.com/locate/datak
- KSE — International Conference on Knowledge and Systems Engineering (IEEE, kỷ yếu có trên IEEE Xplore, ví dụ DOI 10.1109/kse50997.2020.9287471)

**Điểm:**
| Tiêu chí | Điểm | Lý do |
|---|---|---|
| Tính mới | 4 | Benchmark text-to-KG theo ontology cho tiếng Việt chưa thấy; phương pháp thì không mới. |
| Ứng dụng | 3 | Công cụ hạ tầng, hữu ích nhưng người dùng cuối ít thấy trực tiếp. |
| Khả thi một người | 5 | Dữ liệu nhỏ, giấy phép mở, mô hình 7-8B 4-bit chạy GPU vừa. |
| Công bố | 4 | Bài "tài nguyên + benchmark" cho ngôn ngữ ít tài nguyên được TALLIP/KSE đón nhận. |
| Hồ sơ NCS | 5 | Bài nền tự nhiên; Đề tài 2, 3 và brief KG-RAG đều dùng lại. |
| **Tổng** | **21/25** | |

**Rủi ro:** dữ liệu dịch có thể bị chê "nhân tạo" — cần thêm một tập nhỏ văn bản gốc tiếng Việt gán tay; có thể có nhóm VN khác đang làm (chưa tra Google Scholar); giấy phép CC cụ thể của dữ liệu Text2KGBench cần xác nhận.

---

## Đề tài 2: Việt hoá và mở rộng Ontology Răng hàm mặt (OHD) bằng LLM có người duyệt

**Câu hỏi nghiên cứu.** LLM có tạo được nhãn/định nghĩa tiếng Việt đúng chuẩn cho OHD và đề xuất khái niệm mới từ văn bản nha khoa tiếng Việt công khai, với tỉ lệ được nha sĩ chấp nhận bao nhiêu? Cung cấp từ vựng chuẩn lúc sinh (truy xuất) có tốt hơn sửa sau sinh không?

**Khoảng trống (bài đã mở):**
1. Duncan W.D. et al., 2020, *Structuring, reuse and analysis of electronic dental data using the Oral Health and Disease Ontology*, Journal of Biomedical Semantics. DOI 10.1186/s13326-020-00222-0. OHD mã nguồn mở làm khung dữ liệu nha khoa. **Chưa làm:** chỉ tiếng Anh, xây thủ công.
2. Duncan W.D. et al., 2026, *Representing dental caries and dysbiosis within the oral microbiome in the OHD*, Journal of Biomedical Semantics. DOI 10.1186/s13326-026-00350-z. Mở rộng OHD bằng cách rà các thuật ngữ/ontology có sẵn rồi thêm lớp và quan hệ. **Chưa làm:** abstract không nhắc LLM hỗ trợ mở rộng.
3. Lippolis A.S. et al., 2026, *OntoExtend: A Framework for Requirement-Driven and Scalable Ontology Extension with LLMs*, Studies on the Semantic Web. DOI 10.3233/ssw260011. RAG trên ontology + competency question, kỹ sư đánh giá "cần sửa nhẹ đến vừa". **Chưa làm:** không thử miền y/nha, không đa ngôn ngữ.
4. Vizcaino M. et al., 2026, *semantic-swingers at LLMs4OL 2026 ...: the Seen-Unseen Gap in LLM Ontology Learning*, Open Conference Proceedings. DOI 10.52825/ocp.v11i.3681. Nút thắt là **hình thức bề mặt** của tên khái niệm; chỉ truy xuất hoặc fine-tune mới cải thiện, mô hình mở 9B fine-tune thắng API trả phí. **Liên quan:** khi Việt hoá, vấn đề bề mặt còn nặng hơn — chưa ai đo.

**Dataset công khai:**
| Tên | Link | Giấy phép / truy cập | Kích thước |
|---|---|---|---|
| OHD ontology | https://github.com/oral-health-and-disease-ontologies/ohd-ontology · bản phát hành Zenodo 10.5281/zenodo.23092415 (2026-11-18) | CC BY 4.0 (GitHub API) | repo ~36 MB; số lớp chưa đếm |
| LLMs4OL 2026 (Task B Reuse) | https://github.com/sciknoworg/LLMs4OL-Challenge | MIT (GitHub API) | repo ~63 MB; nhiều miền tiếng Anh |
| Văn bản nha khoa tiếng Việt công khai (giáo trình mở, trang Bộ Y tế) | chưa chọn | **chưa kiểm chứng** bản quyền | — |

**Baseline 1-2 tháng:**
- Tuần 1-2: tải OHD, rút lớp + nhãn + định nghĩa (rdflib/ROBOT); chọn ~300 lớp cốt lõi (răng, bệnh, thủ thuật).
- Tuần 3-5: LLM 7-8B sinh nhãn + định nghĩa tiếng Việt, 3 chế độ: không ngữ cảnh / có cây cha-con / có truy xuất thuật ngữ. Nha sĩ cộng tác chấm chấp nhận/sửa trên mẫu.
- Tuần 6-8: chạy kiểu OntoExtend với 20-30 competency question từ thực hành nha khoa VN, đề xuất lớp mới; kiểm tra nhất quán bằng reasoner (HermiT qua owlready2). Chấm theo tỉ lệ chấp nhận, lỗi cấu trúc.

**Ứng dụng/demo:** từ điển ontology nha khoa song ngữ tra cứu được (web), dùng để chuẩn hoá ghi chú khám/phiếu điều trị tiếng Việt; cũng là lớp ngữ nghĩa cho brief CV dental (Đề tài 1 RES-2: báo cáo panoramic tiếng Việt có mã khái niệm).

**Nơi công bố (OpenAlex; Scopus cần tra lại):**
- Journal of Biomedical Semantics (BioMed Central, ISSN-L 2041-1480) — http://www.jbiomedsem.com/
- Semantic Web (IOS Press, ISSN-L 1570-0844)
- ACM TALLIP (như trên)

**Điểm:**
| Tiêu chí | Điểm | Lý do |
|---|---|---|
| Tính mới | 4 | OHD tiếng Việt + mở rộng bằng LLM chưa thấy; ngách hẹp, ít cạnh tranh. |
| Ứng dụng | 4 | Chuẩn hoá thuật ngữ nha khoa VN, nối trực tiếp với hướng răng hàm mặt và chatbot. |
| Khả thi một người | 3 | Kỹ thuật nhẹ, nhưng **bắt buộc** có nha sĩ chấm; văn bản VN công khai cần lọc bản quyền. |
| Công bố | 4 | JBMS đã đăng chuỗi bài OHD, hợp đúng mạch. |
| Hồ sơ NCS | 5 | Nối 3 hướng của nhóm (ontology, răng hàm mặt, chatbot) thành chuỗi. |
| **Tổng** | **20/25** | |

**Rủi ro:** phụ thuộc chuyên gia nha khoa; OHD thiên về hồ sơ điều trị Mỹ, có khái niệm không khớp thực hành VN; tiêu chí "đúng" của nhãn tiếng Việt dễ bị chê chủ quan — cần ≥2 người chấm và đo đồng thuận (kappa).

---

## Đề tài 3: Đồ thị khái niệm + quan hệ tiên quyết cho học liệu tiếng Việt bằng LLM

**Câu hỏi nghiên cứu.** LLM nhỏ có trích được khái niệm và dự đoán quan hệ tiên quyết giữa các khái niệm từ học liệu tiếng Việt (giáo trình đại học) đủ tốt để sắp lộ trình học không? Chuyển giao từ dữ liệu tiếng Anh (LectureBank) sang tiếng Việt mất bao nhiêu?

**Khoảng trống (bài đã mở):**
1. Li I., Fabbri A.R., Tung R.R., Radev D., 2019, *What Should I Learn First: Introducing LectureBank for NLP Education and Prerequisite Chain Learning*, AAAI 2019. DOI 10.1609/aaai.v33i01.33016674. 1.352 bài giảng, 208 chủ đề gán tay quan hệ tiên quyết. **Chưa làm:** chỉ tiếng Anh, trước thời LLM.
2. Bai Y. et al., 2025, *Prerequisite Relation Learning: A Survey and Outlook*, ACM Computing Surveys. DOI 10.1145/3733593. Tổng quan phương pháp và đánh giá. Dùng làm khung so sánh.
3. Xiao K. et al., 2026, *LECDPR: LLM Enhancement and Concept-Document Interactive Modeling for Prerequisite Relation Prediction*, IJCAI 2026. DOI 10.24963/ijcai.2026/567. LLM chưng cất mô tả khái niệm, vượt 10 baseline trên UCD, LectureBank, MOOC; có code. **Chưa làm:** không tiếng Việt; không dựng khái niệm từ đầu.
4. Liang D. et al., 2026, *Course Knowledge Graph Construction with Large Language Models: Method and System Implementation*, International Conference on Artificial Intelligence, Digital Media and Education (ACM). DOI 10.1145/3839592.3839617. Ontology khoá học + LLM, 93,33% nút hợp lệ (lấy mẫu tay). **Chưa làm:** abstract không nêu ngôn ngữ, không tiếng Việt; chỉ đánh giá lấy mẫu, không có tập vàng tiên quyết.

**Dataset công khai:**
| Tên | Link | Giấy phép / truy cập | Kích thước |
|---|---|---|---|
| LectureBank | https://github.com/Yale-LILY/LectureBank | GitHub không khai báo giấy phép — **chưa kiểm chứng** điều kiện dùng lại | 7.499 tài nguyên (alldata.tsv), taxonomy 320 chủ đề, 208 chủ đề có nhãn tiên quyết |
| Học liệu tiếng Việt | giáo trình mở của trường chủ nhóm dạy / OER — chưa chọn | **chưa kiểm chứng**; SGK phổ thông có bản quyền NXB | — |

**Baseline 1-2 tháng:**
- Tuần 1-2: tái lập LECDPR hoặc baseline đơn giản (embedding + MLP) trên LectureBank.
- Tuần 3-5: chọn 2-3 học phần chủ nhóm đang dạy, LLM trích khái niệm + đề xuất cặp tiên quyết; chủ nhóm và 1 đồng nghiệp gán vàng ~300 cặp.
- Tuần 6-8: so zero-shot LLM / dịch-rồi-dự đoán / LoRA trên LectureBank chuyển sang tiếng Việt; đo F1, AUC, đồng thuận người gán.

**Ứng dụng/demo:** giảng viên tải đề cương/slide, nhận bản đồ khái niệm có mũi tên tiên quyết, sửa trực tiếp; sinh viên xem lộ trình ôn tập. Dùng ngay trong lớp chủ nhóm dạy.

**Nơi công bố (OpenAlex; Scopus cần tra lại):**
- Education and Information Technologies (Springer, ISSN-L 1360-2357) — https://www.springer.com/journal/10639
- Knowledge-Based Systems (Elsevier, ISSN-L 0950-7051) — https://www.journals.elsevier.com/knowledge-based-systems
- KSE (IEEE, như trên)

**Điểm:**
| Tiêu chí | Điểm | Lý do |
|---|---|---|
| Tính mới | 3 | Tiếng Việt mới, nhưng bài toán tiên quyết đã đông và LLM hoá nhanh. |
| Ứng dụng | 4 | Dùng trong lớp thật, có người dùng sẵn (sinh viên của chủ nhóm). |
| Khả thi một người | 4 | Tự gán nhãn được vì là chuyên môn mình dạy; thiếu dataset VN công khai. |
| Công bố | 3 | Hợp tạp chí giáo dục-công nghệ; khó lên venue mạnh nếu tập vàng nhỏ. |
| Hồ sơ NCS | 3 | Tách khỏi mạch y tế/răng hàm mặt; chỉ nối được qua Đề tài 1 (máy trích KG). |
| **Tổng** | **17/25** | |

**Rủi ro:** tập vàng do chính người nghiên cứu gán dễ bị nghi thiên lệch; giấy phép LectureBank chưa rõ; công bố dữ liệu tiếng Việt cần học liệu có giấy phép mở.

---

## Tổng hợp

| # | Đề tài | Mới | Ứng dụng | Khả thi | Công bố | NCS | Tổng |
|---|---|---|---|---|---|---|---|
| 1 | ViText2KG: trích KG tiếng Việt tuân thủ ontology, LLM nhỏ | 4 | 3 | 5 | 4 | 5 | **21** |
| 2 | Việt hoá + mở rộng OHD (răng hàm mặt) bằng LLM | 4 | 4 | 3 | 4 | 5 | **20** |
| 3 | Đồ thị khái niệm + tiên quyết cho học liệu tiếng Việt | 3 | 4 | 4 | 3 | 3 | **17** |

Khuyến nghị: chuỗi 1 → 2 (bài 1 benchmark + mô hình trích KG tiếng Việt; bài 2 áp vào ontology nha khoa; bài 3 dùng ontology đó làm lớp ngữ nghĩa cho KG-RAG/báo cáo panoramic ở các brief anh em). Đề tài 3 là phương án nếu không có nha sĩ cộng tác.

## Đã cân nhắc nhưng loại

- **KG completion bằng LLM** (vd. KICGPT, Findings EMNLP 2023, DOI 10.18653/v1/2023.findings-emnlp.580): rất đông, benchmark FB15k/WN18RR tiếng Anh, cạnh tranh cần GPU/API lớn, khó có điểm mới cho một người.
- **Ontology matching bằng LLM** (OLaLa DOI 10.1145/3587259.3627571; LLMs4OM DOI 10.1007/978-3-031-78952-6_3; Agent-OM DOI 10.14778/3712221.3712222): đã có nhiều nhóm mạnh và benchmark OAEI tiếng Anh; ứng dụng thực tiễn ở VN mờ.
- **KG y học cổ truyền Việt Nam**: VietMedKG (TALLIP 2025, DOI 10.1145/3744740, code MIT) đã làm, và trùng với brief KG-RAG y khoa.

## Việc cần chủ nhóm làm trước khi chốt

1. Tra Scopus/SJR cho các tạp chí trên; tra Google Scholar "knowledge graph" + "tiếng Việt" + "LLM" để xác nhận khoảng trống Đề tài 1.
2. Xác nhận giấy phép dữ liệu Text2KGBench (Zenodo) và LectureBank.
3. Tìm 1-2 nha sĩ cộng tác chấm (bắt buộc cho Đề tài 2).
