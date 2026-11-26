# Phản biện độc lập đề tài #2: Chatbot nha khoa tiếng Việt neo OHD (kèm Việt hoá OHD)

Ngày kiểm: 2026-11-25. Người kiểm: Critic (độc lập). Đối tượng: mục 2 của `top5-de-tai.md`.
Ký hiệu: ✓ đúng, đã mở và khớp; ⚠ đúng một phần hoặc chưa chứng minh được; ✗ sai.
Phương pháp: gọi trực tiếp arXiv API, Crossref, GitHub API, OLS4 (EBI), OBO Foundry; WebFetch/WebSearch cho trang HTML.
Nguyên tắc: chỉ ghi điều đã mở và đọc; mục nào chỉ thấy qua kết quả WebSearch (chưa mở bài) thì ghi rõ.

## 1. Kiểm từng bài trích

### 1.1 Medical Graph RAG, arXiv 2408.04187 (arXiv API)
- Tồn tại ✓. "Medical Graph RAG: Towards Safe Medical Large Language Model via Graph Retrieval-Augmented Generation". Tác giả: Junde Wu, Jiayuan Zhu, Yunli Qi, Jingkun Chen, Min Xu, Filippo Menolascina, Vicente Grau. Đăng 2024-08-08 (v2). https://arxiv.org/abs/2408.04187
- Trích abstract: "we create a triple-linked structure that connects user documents to credible medical sources and controlled vocabularies"; "validated on 9 medical Q&A benchmarks, 2 health fact-checking benchmarks".
- "Mã MIT" ✓ (xem 3.2). "Không chuyên nha khoa" ✓ (abstract nói y khoa chung).
- "Chỉ tiếng Anh" ⚠: abstract không nêu ngôn ngữ. README repo mô tả nguồn là MedC-K (S2ORC/PubMed), sách y khoa và UMLS, tức nguồn tiếng Anh, nhưng không có câu nào ghi "chỉ tiếng Anh". Nên viết "nguồn dữ liệu và benchmark đều tiếng Anh" thay cho "chỉ tiếng Anh".
- Lưu ý: MedGraphRAG đã neo tầng thấp nhất vào UMLS (controlled vocabulary). Điểm khác của đề tài là "neo OHD nha khoa + tiếng Việt", không phải "neo ontology" nói chung.

### 1.2 OHD 2020, DOI 10.1186/s13326-020-00222-0 (Crossref)
- Tồn tại ✓. "Structuring, reuse and analysis of electronic dental data using the Oral Health and Disease Ontology"; Duncan, Thyvalikakath, Haendel, Torniai, Hernandez, Song, Acharya, Caplan, Schleyer, Ruttenberg. J. Biomed. Semantics, 2020-08-20, CC BY 4.0.
- Trích: "The OHD contains over 1900 classes and 59 relationships. Most of the classes and relationships were imported from existing OBO Foundry ontologies."
- "Xây thủ công" ⚠: bài không dùng từ "thủ công". Điều đọc được: phần lớn lớp được nhập từ ontology OBO khác. Hệ quả quan trọng: **số lớp riêng của nha khoa nhỏ hơn nhiều so với con số tổng**.
- "Chưa dùng LLM" ⚠ (chỉ suy từ việc abstract không nhắc): chưa đọc toàn văn.
- Mục đích gốc: biểu diễn dữ liệu hồ sơ nha khoa điện tử (EHR) theo BFO/OWL; thử nghiệm là phân tích sống còn của miếng trám composite. Không phải ontology cho hỏi đáp bệnh nhân.

### 1.3 OHD 2026, DOI 10.1186/s13326-026-00350-z (Crossref + OpenAlex)
- Tồn tại ✓. "Representing dental caries and dysbiosis within the oral microbiome in the Oral Health and Disease Ontology"; Duncan, Sabharwal, Diehl, Dutta, Diller, Joachimiak, Chandrasekharan. J. Biomed. Semantics, 2026-04-24. Giấy phép bài báo: CC BY-NC-ND 4.0 (khác giấy phép ontology).
- Trích abstract (OpenAlex): "we added terms and relations to the Oral Health and Disease Ontology (OHD) that more accurately represent how oral microbial dysbiosis influences the development of dental caries."
- Xác nhận: mở rộng bằng rà soát thuật ngữ rồi thêm term/relation; abstract không nhắc LLM ✓ (suy từ vắng mặt, chưa đọc toàn văn). Bài tập trung sâu răng và hệ vi sinh, cho thấy OHD thiên về mô hình khái niệm học thuật.

### 1.4 "1.881 term" (OLS4)
- ✓ có điều kiện. https://www.ebi.ac.uk/ols4/api/ontologies/ohd trả `numberOfTerms: 1881`, `numberOfProperties: 273`, `numberOfIndividuals: 33`, version `2026-11-18`. Số 1.881 gồm cả lớp nhập từ ontology khác (theo 1.2), nên không đồng nghĩa "1.881 thuật ngữ nha khoa". Chưa đếm số lớp gốc OHD.

### 1.5 DentalBench, arXiv 2508.20416 (arXiv API + bản HTML)
- Tồn tại ✓. "DentalBench: Benchmarking and Advancing LLMs Capability for Bilingual Dentistry Understanding"; Hengchuan Zhu, Yihuan Xu, Yichen Li, Zijie Meng, Zuozhu Liu; 2025-08-28.
- Trích: "DentalQA, an English-Chinese question-answering (QA) benchmark with 36,597 questions spanning 4 tasks and 16 dental subfields"; "DentalCorpus ... 337.35 million tokens ... supporting both supervised fine-tuning (SFT) and retrieval-augmented generation (RAG)".
- Bản HTML: không nhắc ontology, không dựng KG (chỉ có "knowledge graph" trong tên một tài liệu tham khảo), không nhắc tiếng Việt, không thấy liên kết mã/dữ liệu hay giấy phép. WebSearch cũng không tìm ra repo.
- **Không làm mất khoảng trống.** Là benchmark Anh-Trung và RAG văn bản; dùng được làm tham chiếu thiết kế và baseline "RAG văn bản", không dùng được cho tiếng Việt.

### 1.6 SCMPE, arXiv 2601.12974 (arXiv API + trang abs; PDF nhị phân không trích được chữ, bản HTML 404)
- Tồn tại ✓. "Bridging the Knowledge-Action Gap by Evaluating LLMs in Dynamic Dental Clinical Scenarios"; Hongyang Ma, Tiantian Gu, Huaiyuan Sun, ..., Zhihui Tang; 2026-01-19.
- Trích abstract: "While RAG mitigates hallucinations in static tasks, its efficacy in dynamic workflows is limited and heterogeneous, sometimes causing degradation."
- Abstract không nhắc ontology/KG. Ngôn ngữ benchmark và kho RAG: **không biết** (chỉ đọc abstract).
- **Không làm mất khoảng trống**; làm động cơ rõ hơn (RAG văn bản yếu ở hội thoại động) nhưng cũng báo trước rằng cải thiện nhờ truy hồi có thể nhỏ.

### 1.7 OntoExtend, DOI 10.3233/ssw260011 (Crossref)
- Tồn tại ✓. "OntoExtend: A Framework for Requirement-Driven and Scalable Ontology Extension with LLMs"; Lippolis, Saeedizade, Schmid, Blattner, Keskisärkkä, Gangemi, Blomqvist, Nuzzolese. Studies on the Semantic Web, 2026-09-02, CC BY 4.0.
- Trích: "It uses retrieval-augmented generation (RAG) over relevant input ontologies and requirements in the form of competency questions to propose grounded extensions." Đánh giá trên ontology Onto-DESIDE và ontology công nghiệp Bosch.
- Là **mở rộng** ontology bằng LLM, không dịch/Việt hoá, không y khoa. **Không làm mất khoảng trống Việt hoá**; chỉ là tài liệu phương pháp (LLM + RAG trên ontology có sẵn).

## 2. Bài bỏ sót
Hạn chế: OpenAlex API trả "Rate limit exceeded ... daily budget" nên **không chạy được truy vấn OpenAlex nào cho phần này**. Thay bằng 8 truy vấn arXiv API và 5 truy vấn WebSearch.

Truy vấn arXiv đã chạy: (1) RAG AND dental; (2) ontology AND retrieval-augmented AND LLM AND medical; (3) ontology AND translation AND multilingual AND LLM; (4) Vietnamese AND medical; (5) Vietnamese AND dental (0 kết quả từ 2025); (6) Vietnamese AND ontology; (7) dental AND ontology AND LLM (0 kết quả); (8) "knowledge graph" AND dental (bị lỗi 429, không có kết quả).

Bài đã xác nhận tồn tại qua arXiv API và đọc abstract (đầu 650 ký tự):

| arXiv | Nội dung | Ảnh hưởng |
|---|---|---|
| 2512.09127 (Han, Ge, Li; 2025-12) | KG-LLM nha nhi: KG + RAG + kiểm an toàn, đề xuất kháng sinh | Gần nhất: KG + RAG nha khoa đã có. Không dùng OHD, không tiếng Việt, hẹp (nha nhi, kháng sinh). Thu hẹp "Mới" (Scholar trước chỉ thấy 1 kết quả). |
| 2610.36335 (OA-RAG; Yang, Chen, Gao; 2026-10) | Agent RAG dựa ontology, kết hợp suy luận hình thức và LLM, nhắm y sinh | "RAG neo ontology" đã có ở mức chung; chỉ đọc abstract, cần đọc toàn văn trước khi tuyên bố mới. |
| 2605.27378 (OralAgent; 2026-04) | Agent nha khoa đa phương thức, 368 giáo trình nha khoa làm kho truy xuất | RAG văn bản nha khoa đã có hệ thống đầy đủ; dùng làm tham chiếu baseline. |
| 2507.19537 (WOKIE; Kraus, Blumenröhr, Tonne; 2025-07) | LLM dịch thesaurus SKOS, 15 ngôn ngữ, mã mở | Việt hoá ontology bằng LLM có tiền lệ (nhân văn số, không y khoa). Cần đối chiếu phương pháp. |
| 2509.15640 (Vo, Le, Le; 2025-09) | Prompt LLM dịch y khoa Anh-Việt, thêm từ điển Meddict | Rất liên quan: là baseline cho chế độ "có truy xuất thuật ngữ". |
| 2608.29890 (En-ViMedNER; 2026-08) | Kho song song Anh-Việt có nhãn UMLS semantic type | Có thể dùng làm đánh giá tự động thuật ngữ y khoa Việt. Chưa xem giấy phép. |
| 2603.22642 (Anyaegbuna et al.; 2026-03) | LLM hàng đầu dịch 22 tài liệu y khoa sang 8 ngôn ngữ gồm tiếng Việt | LLM dịch y khoa cấp tài liệu đạt ngữ nghĩa cao (abstract: LaBSE > 0.92); không phải cấp thuật ngữ nha khoa. |
| 2506.01305 (VM14K; 2025-06) | Benchmark y khoa Việt 14.000 câu trắc nghiệm, 34 chuyên khoa | Không riêng nha khoa; chưa kiểm có nha khoa không. |
| 2601.03792 (VietMed-MCQ; 2026-01) | MCQ y học cổ truyền Việt, sinh bằng RAG | Chỉ cho thấy xu hướng; không nha khoa. |
| 2611.11426 (Vietnamese Legal Ontology; 2026-11) | Ontology pháp luật Việt cho hỏi đáp có trích dẫn | Hướng "ontology + QA tiếng Việt" đang có ở lĩnh vực khác; không y khoa. |

Chỉ thấy qua WebSearch, **chưa mở bài**: mini-review "Retrieval augmented generation in dentistry" (PMC12916606, Frontiers in Dental Medicine 2026); báo cáo "Integrating Ontologies and LLM RAG" (johnbeve.github.io/LLMO-FOIS); arXiv 2605.24636 (GlobalDentBench). Không dùng làm căn cứ.

Kết luận mục 2: **chưa thấy** bài nào kết hợp (a) ontology nha khoa như OHD, (b) RAG LLM, (c) tiếng Việt; arXiv không có kết quả "Vietnamese AND dental" từ 2025. Nhưng tìm không toàn diện (không có OpenAlex, Scopus, PubMed, Google Scholar), nên chỉ nên viết "chưa thấy", không viết "chưa có".

## 3. Tài nguyên
### 3.1 OHD
- Repo https://github.com/oral-health-and-disease-ontologies/ohd-ontology ✓: GitHub API cho license CC-BY-4.0, đẩy lần cuối 2026-11-20, 15 sao, chưa lưu trữ. Có `ohd.owl`, `ohd.obo`, `ohd.json`, `ohd-base.*`, `ohd-full.*`, `ohd-non-classified.*`.
- OLS4: 1.881 term, 273 property, 33 individual, version 2026-11-18 ✓ (khớp bản mô tả).
- Trang OBO Foundry https://obofoundry.org/ontology/ohd.html tồn tại; không trích được trường giấy phép từ trang, nên giấy phép lấy từ GitHub.
- Cảnh báo: số term gồm lớp nhập khẩu (1.2); chưa đo số lớp cốt lõi dùng được cho chatbot bệnh nhân.

### 3.2 MedGraphRAG
- Link trong bản mô tả `SuperMedIntel/Medical-Graph-RAG` đã bị chuyển hướng (HTTP 301) sang `ImprintLab/Medical-Graph-RAG`: giấy phép MIT ✓, 845 sao, đẩy lần cuối 2025-10-18. arXiv ghi `MedicineToken/Medical-Graph-RAG`, cũng chuyển hướng. Nên sửa link.
- README dùng PubMed web, MedC-K, UMLS (cần đăng ký tài khoản UMLS, có điều khoản riêng); một số dữ liệu sách không phát hành vì giấy phép. Chưa chạy thử mã.

## 4. Tác động của việc không có nha sĩ cộng tác
- Đề tài cần ≥2 nha sĩ chấm nhãn tiếng Việt (chấp nhận/sửa, kappa) và chấm tập 300-500 câu. Không có nha sĩ thì **cả hai câu hỏi nghiên cứu (a) và (b) đều thiếu chuẩn vàng**; LLM tự chấm LLM không thay được, và bài báo y khoa khó chấp nhận làm kết quả chính.
- Điểm: KT 3 → 2 (không chỉ nặng công mà phụ thuộc người ngoài chưa có). ƯD 5 → 4: demo "cho phòng khám" cần nha sĩ/phòng khám thử nghiệm; hiện chưa có đối tác.
- Lối thoát (đề xuất, chưa kiểm tính khả thi): (i) tuyển 2 nha sĩ qua trường/hội nha khoa trước khi mở repo; (ii) giai đoạn 1 chỉ làm phần đo tự động: đối chiếu nhãn Việt với Meddict/UMLS (bài 2509.15640, 2608.29890) và back-translation, chưa cần nha sĩ; (iii) hoãn chấm của nha sĩ sang giai đoạn 2, chỉ cam kết khi đã có người; (iv) câu hỏi bệnh nhân phải tự soạn tổng hợp, không dùng dữ liệu bệnh nhân thật.
- Rủi ro công bố: tạp chí y khoa (JMIR Med Inform, JBMS) sẽ đòi đánh giá chuyên gia; nếu chỉ chấm tự động thì nhắm hội nghị công nghệ (SOICT) và hạ mức tuyên bố lâm sàng.

## 5. Kết luận
**Giữ nhưng sửa điểm và hạ hạng; không loại.**

| Tiêu chí | Cũ | Mới | Lý do |
|---|---|---|---|
| Mới | 5 | 4 | Đã có KG-LLM nha nhi (2512.09127), OA-RAG ontology y sinh (2610.36335), WOKIE dịch thesaurus bằng LLM, Meddict cho dịch Anh-Việt. Tổ hợp OHD + tiếng Việt vẫn chưa thấy nhưng không còn là khoảng trống trắng. |
| ƯD | 5 | 4 | Không có nha sĩ/phòng khám để thử; OHD thiên về EHR, không phải tri thức dành cho bệnh nhân. |
| KT | 3 | 2 | Phụ thuộc nha sĩ chấm chưa có; chưa có tập đánh giá tiếng Việt nha khoa. |
| CB | 4 | 4 | Giữ; JBMS và SOICT tồn tại, nhưng cần đánh giá chuyên gia. |
| NCS | 5 | 5 | Giữ. |
| Tổng | 22 | 19 | Thấp hơn #3, #4 (21) và #5 (20); Dean cần tính lại bảng xếp hạng. |

Điều chỉnh khuyến nghị nếu giữ: (1) Việt hoá lõi OHD bằng chấm tự động và đối chiếu từ điển trước; (2) tìm 2 nha sĩ trước khi làm chatbot; (3) thu hẹp phạm vi hỏi đáp theo một bệnh (ví dụ sâu răng, khớp bài OHD 2026) để ontology thực sự dùng được.

## 6. Chưa kiểm được
- OpenAlex hết hạn mức ngày: chưa chạy truy vấn OpenAlex nào cho phần bỏ sót. Truy vấn arXiv "knowledge graph AND dental" bị 429.
- Chưa đọc toàn văn bài nào; nhận định nội dung chỉ dựa trên abstract (OHD 2020/2026, MedGraphRAG, SCMPE, OntoExtend, OA-RAG) hoặc bản HTML (DentalBench).
- Chưa biết ngôn ngữ và kho RAG của SCMPE; chưa thấy repo/giấy phép dữ liệu DentalBench.
- Chưa đếm số lớp gốc OHD; giấy phép OHD lấy từ GitHub, chưa đối chiếu OBO Foundry.
- Chưa mở PMC12916606, GlobalDentBench 2605.24636, báo cáo LLMO-FOIS; chưa kiểm Scopus/SJR nơi công bố.
- Chưa chạy MedGraphRAG hay thử Việt hoá mẫu OHD bằng LLM nên chưa biết chất lượng thực.
