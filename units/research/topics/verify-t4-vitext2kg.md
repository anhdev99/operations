# Phản biện độc lập đề tài #4: ViText2KG

Ngày kiểm: 2026-11-25. Đối tượng: mục 4 của `top5-de-tai.md`. Người kiểm: Critic (độc lập, tự mở nguồn gốc).
Ký hiệu: ✓ mở được và khớp; ⚠ tồn tại nhưng có chỗ lệch hoặc chưa đọc hết; ✗ sai/không tìm thấy.

## 0. Giới hạn của lần kiểm này (nói thẳng)

- API arXiv trả HTTP 429 (bị giới hạn tốc độ) với mọi truy vấn tìm kiếm theo từ khoá; chỉ truy vấn theo `id_list` chạy được. Tôi **không** hoàn thành được ≥6 truy vấn arXiv bằng script.
- API OpenAlex trả "Rate limit exceeded – free daily budget used up" nên **không** tra được OpenAlex.
- Thay thế: Crossref API (chạy được), Zenodo API, GitHub API, arXiv `id_list`, và ~10 truy vấn WebSearch + WebFetch trang gốc (arXiv, ACL Anthology, CEUR). Mức bao phủ vì vậy thấp hơn yêu cầu; kết luận "chưa thấy" ở mục 2 chỉ là "chưa thấy trong các truy vấn này".

## 1. Kiểm từng bài / dataset

### 1.1 Text2KGBench — ✓ (có một lệch nhỏ về cách hiểu số liệu)
- Crossref xác nhận DOI 10.1007/978-3-031-47243-5_14: "Text2KGBench: A Benchmark for Ontology-Driven Knowledge Graph Generation from Text", LNCS, *The Semantic Web – ISWC 2023*, tác giả đầu Nandana Mihindukulasooriya. https://doi.org/10.1007/978-3-031-47243-5_14
- arXiv 2308.02357 (nộp 4/8/2023; tác giả Mihindukulasooriya, Tiwari, Enguix, Lata). Trích abstract: "Wikidata-TekGen with 10 ontologies and 13,474 sentences" và "DBpedia-WebNLG with 19 ontologies and 4,860 sentences"; "We define seven evaluation metrics to measure fact extraction performance, ontology conformance, and hallucinations". https://arxiv.org/abs/2308.02357
- **29 ontology = 10 + 19 ✓.**
- **13.474 + 4.860 câu ✓ về con số, nhưng là hai dataset riêng** (tổng 18.334 câu), không phải một tập. Tệp đề tài nên viết rõ "hai dataset" để khỏi bị hiểu là một tập.
- **7 thước đo ✓** (đọc từ bản ar5iv): Precision, Recall, F1 (trích fact); Ontology Conformance (OC); Subject/Relation/Object Hallucination (SH, RH, OH). Baseline gốc: Vicuna-13B và Alpaca-LoRA-13B.
- Lưu ý: OC của bài gốc đo "tỉ lệ bộ ba dùng quan hệ chuẩn của ontology", chưa phải kiểm domain/range. Việc "kiểm domain/range bằng rdflib" là phần **mở rộng** của đề tài, không phải thước đo sẵn có; nên nói rõ như vậy.

### 1.2 Dataset Text2KGBench và giấy phép — ✓ (kèm cảnh báo quan trọng)
- GitHub API: repo `cenguix/Text2KGBench`, giấy phép mã Apache-2.0, push cuối 2024-05-06, 99 sao. https://github.com/cenguix/Text2KGBench
- Zenodo API record 7916716: tiêu đề khớp, `license: cc-by-4.0`, ngày 2023-05-09, một tệp `Text2KGBench.zip` (5,9 MB). https://doi.org/10.5281/zenodo.7916716
- README: badge "Data License: CC BY 4.0"; nhưng dòng chữ lại ghi "Creative Commons Attribution-ShareAlike 4.0 International (CC BY 4.0)". Hai chỗ **mâu thuẫn** (BY vs BY-SA). Metadata Zenodo (máy đọc) ghi CC BY 4.0.
- **Điều quan trọng hơn**: README cuối trang ghi dữ liệu "derived from TekGen corpus (part of the KELM corpus) released under CC BY-SA 2.0 license and WebNLG 3.0 corpus released under CC BY-NC-SA 4.0 license." Nghĩa là:
  - Kết luận về giấy phép: **dữ liệu công bố là CC BY 4.0 (theo Zenodo)**, nhưng phần dẫn xuất từ WebNLG (DBpedia-WebNLG, 19 ontology, 4.860 câu) có thể bị ràng buộc **NC-SA 4.0** (phi thương mại, chia sẻ tương tự), phần TekGen **BY-SA 2.0** (chia sẻ tương tự).
  - Hệ quả: bản dịch tiếng Việt (tác phẩm phái sinh) phải phát hành cùng điều kiện SA, và phần WebNLG không dùng thương mại được. Đây là rủi ro phát hành thật, nặng hơn mô tả "loại CC chưa xác nhận". Chưa kiểm trang gốc WebNLG/KELM, chỉ dựa README.

### 1.3 Tiwari, DOI 10.3233/ssw260009 — ✓ tồn tại, ✓ liên quan
- Crossref: "Ontology-Aware Prompting for Knowledge Graph Construction from Text", *Studies on the Semantic Web* (sách "Bridging the Gap Between Curated and Induced Semantics"), tác giả đầu Balram Tiwari (Paderborn/Koblenz), 2026-09-02, giấy phép CC BY 4.0. https://doi.org/10.3233/SSW260009
- Trích abstract: "ontology-aware multi-prompt framework ... Tree-of-Thoughts-style reasoning ... schema-constrained OpenIE ... Experiments on Text2KGBench, including DBpedia-WebNLG and Wikidata-TekGen, show improvements of up to 2.3 times over LLM-based baselines, ... hallucination rates below 0.20 in most domains and ontology conformance above 0.90 on most DBpedia-WebNLG domains." Mã: github.com/dice-group/ontology-aware-kg-construction.
- Chỉ tiếng Anh. Là bài không tác giả trùng với Text2KGBench (Sanju Tiwari trong Text2KGBench khác Balram Tiwari: **không** khẳng định cùng người).
- Ý nghĩa: ontology conformance trên DBpedia-WebNLG đã gần trần (>0,90) với LLM lớn + prompt; ranh giới "LLM nhỏ + prompt ràng buộc giảm vi phạm" ở tiếng Anh đã được khai thác.

### 1.4 Pappacoda & Torroni, AKBC 2026 — ✓ tồn tại (⚠ chưa đọc toàn văn)
- ACL Anthology, 11th Workshop on Automated Knowledge Base Construction (AKBC 2026): "LMKG: a flexible method for ontology-aware Knowledge Graph Extraction from text", Gianmarco Pappacoda, Paolo Torroni. ID 2026.akbc-1.24 (trang liệt kê có lệch: link tiêu đề trỏ .23). https://aclanthology.org/volumes/2026.akbc-1/
- Abstract (tóm lược từ trang): pipeline mô-đun, hỗ trợ trích mở và trích ràng buộc ontology; chiến lược "fold"/"enrich" cho văn bản dài; đánh giá trên Text2KGBench, MINE-1, HotpotQA; ontology conditioning cải thiện conformance trên Text2KGBench.
- Chỉ tiếng Anh theo abstract. Chưa đọc toàn văn nên chưa biết mô hình, số liệu.

### 1.5 To & Do, KSE 2020 — ✓ tồn tại (⚠ chưa đọc nội dung)
- Crossref: "Extracting triples from Vietnamese text to create knowledge graph", tác giả To, Do; 2020 12th International Conference on Knowledge and Systems Engineering (KSE), 2020-11-12, DOI 10.1109/KSE50997.2020.9287471. https://doi.org/10.1109/KSE50997.2020.9287471
- Chưa mở được abstract/toàn văn. Chỉ biết tiêu đề: trích bộ ba từ văn bản tiếng Việt, không có dấu hiệu ràng buộc ontology hay LLM (suy từ tiêu đề, chưa xác nhận).
- Bài liên quan cùng nhóm Do: Do et al., "Using BERT and Knowledge Graph for detecting triples in Vietnamese text", Neural Computing and Applications 2022, DOI 10.1007/s00521-022-07439-3 (Crossref ✓, chưa đọc).

### 1.6 Nguyen & Nguyen, arXiv 2609.00763 — ✓ tồn tại, ⚠ KHÔNG đúng loại bài mà đề tài ngụ ý
- arXiv `id_list`: "Automated Tree Knowledge Graph Construction using Ontology Expansion and Retrieval from Vietnamese History Textbooks", Ket Doan Nguyen, Minh N. H. Nguyen, v1 ngày 2026-09-01. https://arxiv.org/abs/2609.00763
- Trích: "the lack of methods for automatic KG construction using ontology expansion for low-resource languages such as Vietnamese"; pipeline trích quan hệ lai 3 pha; KG từ SGK Lịch sử THPT: 750 nút, 4.341 cạnh, ontology 40 → 41 loại; benchmark là **1.210 câu hỏi truy hồi tổng hợp** từ 109 đồ thị con.
- Đây là KG-RAG tiếng Việt, ontology **mở rộng** chứ không cho trước; benchmark của họ đo truy hồi, không đo trích bộ ba. **Không** lấp khoảng trống của ViText2KGBench, nhưng là bài tiếng Việt gần nhất về KG-từ-văn-bản có ontology và nên được trích dẫn.

## 2. Bài bỏ sót (đã mở/đọc ở mức abstract hoặc metadata)

| Bài | Nguồn | Liên quan |
|---|---|---|
| Text2KGBench-LettrIA (Lettria + EURECOM), ISWC 2025 workshops, CEUR Vol-4041 paper 3. Viết lại chú thích 4.860 câu DBpedia-WebNLG, >14.000 bộ ba, 19 ontology | https://ceur-ws.org/Vol-4041/paper3.pdf (PDF đọc không ra chữ; tóm lược lấy từ trang EURECOM/WebSearch) ⚠ | **Rủi ro lớn**: kết luận "mô hình mở nhỏ fine-tune vượt mô hình đóng lớn zero/few-shot" trùng ý LoRA nhỏ của đề tài, ở tiếng Anh. Nên dùng LettrIA thay bản gốc làm nguồn dịch (nhãn sạch hơn). Chưa xác nhận giấy phép (chỉ thấy link CC BY 4.0). |
| OSKGC (Waseda), CEUR Vol-4041 paper 1: benchmark ontology phân cấp | https://ceur-ws.org/Vol-4041/paper1.pdf ⚠ chưa mở | Đối thủ benchmark tiếng Anh |
| Loconte, Hospedales, Cornelio, "Better Later Than Sooner", arXiv 2605.29168 (EMNLP 2026 Findings) | https://arxiv.org/abs/2605.29168 ✓ | Sửa vi phạm ontology sau trích; trang không nhắc Text2KGBench |
| Ilves, Barbu, Übi, "LLMs for KG Extraction: A Schema-Constrained Evaluation Framework", KG-LLM @ LREC26 | https://aclanthology.org/2026.kallm-1.21/ ✓ | Schema adherence, Mistral 7B, DocRED (tiếng Anh) |
| Mai et al., VLSP 2020 RelEx (phân loại 4 loại quan hệ tin tức tiếng Việt) | https://aclanthology.org/2020.vlsp-1.17/ ✓ (qua tìm kiếm) | Benchmark RE tiếng Việt, không theo ontology; dữ liệu phải xin phép qua VLSP |
| Vietnamese OIE (vnOIE), arXiv 1801.07804 | https://arxiv.org/abs/1801.07804 ⚠ chỉ thấy qua tìm kiếm | Trích mở dựa luật, không LLM |
| Vuong et al. KG án lệ Việt, arXiv 2309.09069; Bui & Quan KG giáo dục HCMUT, arXiv 2404.09296 | tìm kiếm ⚠ | KG tiếng Việt, ứng dụng, không benchmark ontology |
| VHE (PACLIC 2024), trích sự kiện lịch sử tiếng Việt, có đánh giá LLM | tìm kiếm ⚠ | Gần về "IE tiếng Việt + LLM" |
| KG-RAG pháp lý tiếng Việt, doi 10.3233/FAIA260735 | tìm kiếm ⚠ chưa mở | Ontology + KG tiếng Việt |
| arXiv 2609.31663 "LLM-Guided Ontology-Driven KG Construction" | ✓ mở nhưng **đã bị rút (withdrawn)**, dữ liệu tiếng Pháp riêng | **Không trích dẫn** |

Kết luận về khoảng trống: trong phạm vi tra được, **chưa thấy** benchmark text-to-KG theo ontology cho tiếng Việt, cũng chưa thấy bản đa ngữ/dịch của Text2KGBench. Bốn bài "chưa kiểm chứng" nay đã tồn tại, **không làm mất khoảng trống** (hai bài tiếng Anh, hai bài tiếng Việt nhưng khác tác vụ). Nhưng khoảng trống này hẹp và dễ lấp bởi một nhóm khác chỉ cần dịch dataset, và độ bao phủ tìm kiếm của tôi thấp (mục 0).

## 3. Đánh giá thẳng

Đúng, đề tài hiện là "dịch benchmark + chạy LLM nhỏ + LoRA". Với bài Scopus Q2-Q3, **chưa đủ** nếu chỉ vậy:
1. Tài nguyên dịch tự động bị coi là mỏng nếu không có đánh giá chất lượng; reviewer hỏi ngay "khác gì dịch máy WebNLG".
2. LoRA trên tập train dịch + prompt ontology là kỹ thuật chuẩn; LettrIA, Tiwari, LMKG đã làm tương tự ở tiếng Anh. Phần mới chỉ là ngôn ngữ.
3. Tiếng Việt khác biệt thật ở: tên riêng/thực thể không có ranh giới từ, tên quan hệ ontology giữ tiếng Anh hay dịch, chuẩn hoá thực thể (dấu, biến thể phiên âm). Nếu khai thác được thì mới là khoa học.

Cần thêm để không mỏng (chọn ≥2):
- **Phân tích lỗi có hệ thống VI so với EN**: phân loại lỗi (ranh giới thực thể, nhầm quan hệ, vi phạm domain/range, ảo giác thực thể), kiểm tách ảnh hưởng của chất lượng dịch với ảnh hưởng của ngôn ngữ (so bản dịch máy chưa sửa với bản duyệt tay ~500 câu, đo chênh).
- **Phương pháp mới nhẹ**: giải mã ràng buộc ontology (constrained decoding / grammar theo domain-range) hoặc bước sửa vi phạm sau trích (như hướng Loconte), so với prompt đơn thuần; báo cáo ablation.
- **Tập gốc tiếng Việt gán tay** (không dịch), chia theo nhiều miền, có thoả thuận gán nhãn (kappa). Đây là phần giá trị nhất, đã được đề tài gợi ý nhưng nên là **trung tâm**, không phải phụ.
- **Cross-lingual transfer**: train EN, test VI; train VI dịch, test VI gốc; có/không đa ngữ (Qwen so với mô hình VN) để có câu hỏi nghiên cứu nghiêm túc.
- **Giấy phép sạch**: dựng từ nguồn cho phép (ưu tiên phần TekGen BY-SA hoặc LettrIA nếu giấy phép cho phép), tránh vướng NC của WebNLG.

## 4. Kết luận: SỬA điểm, GIỮ có điều kiện (hạ hạng)

| Tiêu chí | Cũ | Mới | Lý do |
|---|---|---|---|
| Mới | 4 | 3 | Khoảng trống còn (chưa thấy VI), nhưng chỉ mới về ngôn ngữ; LettrIA/Tiwari/LMKG đã chiếm phần phương pháp EN; tìm kiếm mỏng |
| ƯD | 3 | 3 | Giữ: công cụ hạ tầng gián tiếp |
| KT | 5 | 4 | Dịch + duyệt tay 500 câu + vướng giấy phép NC-SA/SA; phần dịch rẻ nhưng chất lượng và pháp lý không "dễ nhất" |
| CB | 4 | 3 | Mỏng nếu không có phân tích lỗi/phương pháp; Q2-Q3 cần thêm mục 3 |
| NCS | 5 | 4 | Hợp hướng ontology/KG, nhưng là đóng góp tài nguyên hơn là học thuật cốt lõi |
| **Tổng** | 21 | **17** | Rớt xuống dưới đề tài #5 (20) |

Khuyến nghị: không loại; giữ như **mảng hạ tầng cho #2** (trích văn bản nha khoa vào OHD) và chỉ nâng thành bài độc lập khi đã có ít nhất tập gốc tiếng Việt + phân tích lỗi VI/EN. Đổi cách phát biểu: không phải "benchmark dịch" mà "đánh giá tuân thủ ontology xuyên ngôn ngữ với LLM nhỏ, kèm tập gốc tiếng Việt".

## 5. Điều CHƯA kiểm được

- Toàn văn To & Do (KSE 2020), Do et al. (NCA 2022), LMKG, Tiwari (chỉ đọc abstract/metadata); số liệu kết quả của họ.
- Toàn văn LettrIA (PDF không trích được chữ): giấy phép dữ liệu, mô hình đã fine-tune, ngôn ngữ.
- Giấy phép gốc của WebNLG 3.0 và KELM/TekGen (chỉ dựa dòng ghi trong README).
- Trạng thái Scopus/SJR của TALLIP, KSE, DKE; xác suất nhóm VN khác đang làm.
- Truy vấn arXiv theo từ khoá (429) và OpenAlex (hết hạn mức): danh sách bài bỏ sót chưa đủ ≥6 truy vấn arXiv + OpenAlex như yêu cầu; Google Scholar chưa tra.
