# Brief: Chatbot + ontology y khoa (RAG trên knowledge graph)

Issue: RES-3 (con của RES-1). Người viết: Scholar. Ngày kiểm tra nguồn: 2026-11-24.
Mọi bài/dataset dưới đây đã mở trang gốc (arXiv abs/HTML, Hugging Face, GitHub, OLS) trong lượt này.
Chỗ nào chưa xác nhận được ghi rõ "chưa kiểm chứng" và không dùng để chấm điểm.

## 1. Bức tranh nhanh

**Mức bão hoà GraphRAG y khoa (tiếng Anh): cao.**
- Tìm kiếm arXiv ngày 2026-11-24: `GraphRAG` (all fields) 274 kết quả; `medical graph RAG` (abstract) 50;
  `medical knowledge graph retrieval-augmented generation` (abstract) 60. Số đếm lấy từ dòng "Showing 1–25 of N" của arxiv.org/search.
- Đã có framework mạnh, mã nguồn mở: MedGraphRAG (MIT), KG-RAG trên SPOKE (Apache-2.0), MedRAG/MIRAGE benchmark.
- Kết luận: làm thêm "một GraphRAG y khoa tiếng Anh nữa" khó có tính mới. Khoảng trống còn lại nằm ở
  **ngôn ngữ ít tài nguyên (tiếng Việt)** và **chuyên khoa hẹp (nha khoa)**.

**Benchmark hỏi đáp y khoa tiếng Việt: có, nhưng ít.**
- VM14K (2025): 14k câu trắc nghiệm, 34 chuyên khoa. Public 4k + 10k, private 2k.
- ViHealthQA (2022): 10.015 cặp câu hỏi - đoạn trả lời (retrieval QA).
- ViMQ (2021): câu hỏi bệnh nhân có nhãn intent/NER (không phải QA có đáp án). Link dữ liệu: chưa kiểm chứng.
- Chưa tìm thấy benchmark KG-RAG nào cho tiếng Việt (arXiv search `Vietnamese AND "knowledge graph" AND medical`: 0 kết quả).

**Ontology nha khoa có sẵn: có.**
- OHD (Oral Health and Disease Ontology), OBO Foundry, CC-BY-4.0, 1.881 term trên OLS, bản phát hành v2026-11-18 (còn bảo trì).
  Chỉ có nhãn tiếng Anh; không có tiếng Việt.
- SNOMED CT/UMLS: cần tài khoản UTS (license cá nhân, miễn phí nhưng phải đăng ký). Theo luật board, việc đăng ký tài khoản/khoá
  mới cần board duyệt. Đề xuất bên dưới không phụ thuộc UMLS; dùng OHD + PrimeKG.

**Benchmark nha khoa: có cho Anh-Trung, chưa có tiếng Việt.**
- DentalBench (2025): DentalQA 36.597 câu Anh-Trung, 16 phân ngành + DentalCorpus 337,35 triệu token.
- SCMPE (2026): benchmark nha khoa động, thấy RAG giúp tác vụ tĩnh nhưng kém/hại trong hội thoại nhiều lượt.

## 2. Nguồn đã đọc (dùng cho cả 3 đề tài)

| # | Bài | Tác giả, năm | Venue | Link |
|---|-----|--------------|-------|------|
| P1 | Medical Graph RAG: Towards Safe Medical LLM via Graph RAG | Junde Wu, Jiayuan Zhu, ... Vicente Grau, 2024 | arXiv (preprint) | https://arxiv.org/abs/2408.04187 |
| P2 | Biomedical knowledge graph-optimized prompt generation for LLMs (KG-RAG, SPOKE) | Karthik Soman, ... Sergio E. Baranzini, 2023 | arXiv (preprint) | https://arxiv.org/abs/2311.17330 |
| P3 | Exploring the Role of KG-Based RAG in Japanese Medical QA with Small-Scale LLMs | Yingjian Chen, ... Irene Li, 2025 | arXiv (preprint) | https://arxiv.org/abs/2504.10982 |
| P4 | Benchmarking Retrieval-Augmented Generation for Medicine (MIRAGE/MedRAG) | Guangzhi Xiong, Qiao Jin, Zhiyong Lu, Aidong Zhang, 2024 | arXiv (preprint) | https://arxiv.org/abs/2402.13178 |
| P5 | VM14K: First Vietnamese Medical Benchmark | Thong Nguyen, ... Minh Tran, 2025 | arXiv (preprint) | https://arxiv.org/abs/2506.01305 |
| P6 | SPBERTQA (giới thiệu ViHealthQA) | Nhung Thi-Hong Nguyen, ... Ngan Luu-Thuy Nguyen, 2022 | KSEM 2022 (theo dataset card) | https://arxiv.org/abs/2206.09600 |
| P7 | ViMQ: A Vietnamese Medical Question Dataset | Ta Duc Huy, ... Steven Q. H. Truong, 2021 | ICONIP 2021, DOI 10.1007/978-3-030-92310-5_76 | https://arxiv.org/abs/2304.14405 |
| P8 | DentalBench: Bilingual Dentistry Understanding | Hengchuan Zhu, Yihuan Xu, Yichen Li, Zijie Meng, Zuozhu Liu, 2025 | arXiv (preprint) | https://arxiv.org/abs/2508.20416 |
| P9 | Bridging the Knowledge-Action Gap ... Dynamic Dental Clinical Scenarios (SCMPE) | Hongyang Ma, ... Zhihui Tang, 2026 | arXiv (preprint) | https://arxiv.org/abs/2601.12974 |
| P10 | Knowledge-Guided LLM for Pediatric Dental Record Understanding and Safe Antibiotic Recommendation | Zihan Han, Junyan Ge, Caifeng Li, 2025 | arXiv (preprint) | https://arxiv.org/abs/2512.09127 |
| P11 | Unlocking EHRs: A Hybrid Graph RAG Approach (MediGRAF) | Samuel Thio, Matthew Lewis, Spiros Denaxas, Richard JB Dobson, 2025 | Frontiers in Digital Health vol. 8, 2026 (journal_ref arXiv) | https://arxiv.org/abs/2602.00009 |

Ghi chú: chỉ đọc abstract + trang arXiv; chưa đọc toàn văn. Số liệu trích trong brief đều lấy từ abstract.
VietMed-MCQ (arXiv 2601.03792) đã bị tác giả rút lại, không dùng.

## 3. Dataset / tài nguyên công khai đã kiểm tra

| Tên | Link | Giấy phép / truy cập | Kích thước |
|-----|------|----------------------|-----------|
| VM14K (VietnameseMedBench) | https://huggingface.co/datasets/venera-ai/VietnameseMedBench ; code https://github.com/Venera-AI/VM14K-Megarepo | HF không gated; dataset card **không ghi license**; repo code MIT | 14k MCQ (public 4k + 10k, private 2k) theo P5 |
| ViHealthQA | https://huggingface.co/datasets/tarudesu/ViHealthQA | Không gated; card ghi "only used for research purposes", **không ghi license**; cảnh báo có thể lẫn thông tin cá nhân, cần lọc | 10.015 (train 7.009 / val 993 / test 2.013), kiểm qua datasets-server |
| OHD ontology | https://obofoundry.org/ontology/ohd.html ; https://github.com/oral-health-and-disease-ontologies/ohd-ontology | CC-BY-4.0 | 1.881 term (OLS, bản 2026-11-18) |
| PrimeKG | https://github.com/mims-harvard/PrimeKG | Repo MIT; license phần dữ liệu: chưa kiểm chứng | chưa kiểm chứng |
| DentalBench (DentalQA + DentalCorpus) | https://arxiv.org/abs/2508.20416 | **Link tải dữ liệu: chưa kiểm chứng** (không thấy trong HTML paper) | 36.597 câu; 337,35M token (theo P8) |
| MedGraphRAG code | https://github.com/SuperMedIntel/Medical-Graph-RAG | MIT | - |
| KG-RAG code | https://github.com/BaranziniLab/KG_RAG | Apache-2.0 | - |
| MedRAG toolkit / MIRAGE | https://github.com/Teddy-XiongGZ/MedRAG ; https://github.com/Teddy-XiongGZ/MIRAGE | GitHub báo NOASSERTION (cần đọc file LICENSE) | 7.663 câu (MIRAGE, theo P4) |
| UMLS / SNOMED CT | https://www.nlm.nih.gov/research/umls/index.html | Cần license UTS cá nhân; cần board duyệt trước khi đăng ký | - |

Không dataset nào ở trên là dữ liệu bệnh nhân. Không dùng MIMIC (P11) vì cần credential PhysioNet.

## 4. Nơi công bố đã kiểm tra tồn tại

- **SOICT 2026** (https://soict.org/): trang chủ ghi proceedings Springer CCIS, index Scopus. Hội nghị trong nước, hợp bài đầu.
- **KSEM** (Knowledge Science, Engineering and Management), Springer LNCS: venue của ViHealthQA (P6). Trang Springer
  https://link.springer.com/conference/ksem trả về 200 nhưng bị chặn bot; năm/hạn nộp 2027: chưa kiểm chứng.
- **JMIR Medical Informatics** (https://medinform.jmir.org, ISSN 2291-9694): đã mở trang editorial board; open access, **có phí APC**.
- **BMC Medical Informatics and Decision Making** (https://bmcmedinformdecismak.biomedcentral.com/, ISSN 1472-6947): OpenAlex xác nhận; OA, có APC.
- **Journal of Biomedical Informatics** (Elsevier, ISSN 1532-0464): OpenAlex xác nhận; không bắt buộc OA.
- Trạng thái Scopus của các tạp chí: Scimago chặn truy cập tự động nên **chưa kiểm chứng trực tiếp** trong lượt này. Dean nên tra Scopus Sources trước khi chốt.
- Lưu ý chi phí: APC là tiền, cần board duyệt nếu chọn tạp chí OA bắt buộc.

---

## Đề tài A. KG-RAG cho hỏi đáp y khoa tiếng Việt với LLM nhỏ

**Câu hỏi nghiên cứu.** KG-RAG dùng knowledge graph y sinh tiếng Anh (PrimeKG/OHD) kèm ánh xạ thuật ngữ Việt-Anh có cải thiện
độ chính xác của LLM mở cỡ nhỏ (≤8B) trên câu hỏi y khoa tiếng Việt so với RAG văn bản thường không? Khi nào KG giúp, khi nào hại?

**Khoảng trống.**
- P3 làm đúng câu hỏi này cho tiếng Nhật và thấy KG-RAG "chỉ có tác động hạn chế" với LLM nhỏ, nhạy với chất lượng truy hồi;
  tác giả mời làm cho ngôn ngữ ít tài nguyên khác. Chưa có ai làm cho tiếng Việt.
- P1, P2, P4 chỉ đánh giá tiếng Anh.
- P5 (VM14K) chỉ đo LLM trần, không thử RAG/KG-RAG.

**Dataset.** VM14K (đánh giá MCQ), ViHealthQA (corpus + đánh giá retrieval), PrimeKG (KG), OHD cho phần răng.

**Baseline 1-2 tháng, GPU hạn chế.**
- LLM: Qwen2.5-7B hoặc Llama-3.1-8B bản 4-bit (chạy được trên 1 GPU 12-16 GB, chỉ suy luận, không fine-tune).
- So sánh 4 cấu hình: không RAG / BM25+dense RAG trên ViHealthQA / KG-RAG (theo cách P2: trích thực thể, lấy láng giềng 1-hop, prune bằng embedding) / lai.
- Chỉ số: accuracy trên tập VM14K public theo chuyên khoa và mức khó; seed cố định; báo cáo lỗi truy hồi.
- Tái dùng mã KG_RAG (Apache-2.0) và MedGraphRAG (MIT).

**Ứng dụng/demo.** Chatbot web hỏi đáp sức khoẻ tiếng Việt, mỗi câu trả lời hiện các bộ ba KG làm bằng chứng. Người dùng: sinh viên y,
người dân tra cứu. Có disclaimer, không chẩn đoán.

**Nơi công bố.** SOICT (CCIS), KSEM (LNCS); bản mở rộng sang BMC Med Inform Decis Mak.

**Điểm.**
| Tiêu chí | Điểm | Lý do |
|---|---|---|
| Tính mới | 4 | Chưa có KG-RAG tiếng Việt; nhưng thiết kế là "P3 cho tiếng Việt" nên mới ở mức áp dụng. |
| Ứng dụng | 3 | Demo hỏi đáp chung, cạnh tranh với chatbot thương mại. |
| Khả thi một người | 5 | Dữ liệu và mã đều mở, chỉ suy luận, không gán nhãn. |
| Công bố | 4 | Kết quả âm/dương đều viết được (P3 công bố kết quả "hạn chế"). |
| Hồ sơ NCS | 4 | Bài 1 tự nhiên của chuỗi; dẫn sang B và C. |
| **Tổng** | **20/25** | |

**Rủi ro.** Ánh xạ thuật ngữ Việt-Anh là nút thắt (không có UMLS tiếng Việt); VM14K không ghi license; kết quả có thể âm như P3.

---

## Đề tài B. Chatbot nha khoa tiếng Việt neo vào ontology OHD

**Câu hỏi nghiên cứu.** Neo truy hồi vào ontology nha khoa (OHD, bổ sung nhãn tiếng Việt) có giảm ảo giác và tăng độ đúng
của chatbot tư vấn nha khoa tiếng Việt so với RAG văn bản thường không, đặc biệt ở câu hỏi về thủ thuật và vật liệu?

**Khoảng trống.**
- P8 (DentalBench) chỉ Anh-Trung, dùng corpus văn bản, không dùng ontology.
- P9 cho thấy RAG văn bản trong nha khoa giúp tác vụ tĩnh nhưng không ổn định ở hội thoại; chưa thử RAG có cấu trúc.
- P10 dùng KG nha khoa nhưng trên 32.000 hồ sơ nhi khoa không công khai, tiếng Anh/Trung, không tái lập được.
- OHD tồn tại từ lâu nhưng chưa thấy bài nào dùng OHD làm nguồn cho LLM-RAG (tìm arXiv `dental AND "knowledge graph"`: chỉ 1 kết quả là P10).

**Dataset.** OHD (CC-BY-4.0, 1.881 term); câu hỏi nha khoa trong VM14K (lọc theo chuyên khoa; **có chuyên khoa răng hàm mặt hay không: chưa kiểm chứng**);
DentalQA nếu tải được (chưa kiểm chứng) để dịch một tập con.

**Baseline 1-2 tháng.**
- Tháng 1: dịch nhãn OHD sang tiếng Việt bằng LLM + rà tay phần lõi (~300-500 term về bệnh, thủ thuật, vật liệu); đưa vào Neo4j/NetworkX.
- Tháng 2: so sánh RAG văn bản vs RAG neo ontology (truy hồi theo khái niệm + quan hệ) trên 300-500 câu nha khoa tiếng Việt; LLM 7-8B 4-bit.
- Đánh giá: accuracy MCQ + tỉ lệ khẳng định sai so với ontology (tự động kiểm tra bộ ba).

**Ứng dụng/demo.** Chatbot trên web/Zalo mini-app cho phòng khám răng: trả lời câu hỏi bệnh nhân trước/sau điều trị, giải thích thủ thuật,
mỗi câu dẫn khái niệm OHD. Nha sĩ dùng làm công cụ giáo dục bệnh nhân.

**Nơi công bố.** SOICT (CCIS); JMIR Medical Informatics; Journal of Biomedical Informatics (bản mở rộng có đánh giá chuyên gia).

**Điểm.**
| Tiêu chí | Điểm | Lý do |
|---|---|---|
| Tính mới | 5 | Ontology nha khoa + LLM-RAG + tiếng Việt: chưa thấy ai làm. |
| Ứng dụng | 5 | Khớp trực tiếp mảng răng hàm mặt của chủ nhóm, demo cho phòng khám rõ ràng. |
| Khả thi một người | 3 | Phải dịch/rà ontology và dựng tập đánh giá; cần ít nhất 1 nha sĩ rà. |
| Công bố | 4 | Có cả đóng góp tài nguyên (OHD-vi) lẫn phương pháp. |
| Hồ sơ NCS | 5 | Trục chính của chuỗi bài: tài nguyên, phương pháp, đánh giá người dùng, mở rộng đa phương thức (ảnh X-quang). |
| **Tổng** | **22/25** | |

**Rủi ro.** OHD thiên về hồ sơ/billing kiểu Mỹ, có thể thiếu kiến thức lâm sàng cho bệnh nhân; thiếu tập đánh giá tiếng Việt sẵn có;
cần chuyên gia nha khoa rà (không có thì chất lượng đánh giá yếu).

---

## Đề tài C. ViDentQA: benchmark hỏi đáp nha khoa tiếng Việt cho đánh giá RAG/KG-RAG

**Câu hỏi nghiên cứu.** LLM mở và thương mại làm tốt đến đâu với câu hỏi nha khoa tiếng Việt, và RAG/KG-RAG thu hẹp khoảng cách
so với tiếng Anh được bao nhiêu?

**Khoảng trống.**
- P8 có benchmark nha khoa nhưng chỉ Anh-Trung; P5 có benchmark y khoa tiếng Việt nhưng gộp chung chuyên khoa, không có phần RAG.
- P9 chỉ ra cần đánh giá theo kịch bản, nhưng chỉ tiếng Trung/Anh (theo abstract; ngôn ngữ cụ thể: chưa kiểm chứng).

**Dataset nguồn.** Tập con nha khoa của VM14K (nếu có), dịch có rà tập con DentalQA (nếu license cho phép, chưa kiểm chứng),
câu hỏi sinh từ OHD + tài liệu công khai, lọc nhất quán như P5 làm.

**Baseline 1-2 tháng.** Dựng 1.000-2.000 câu MCQ + 100 câu mở; đánh giá 6-8 LLM (mở chạy local 4-bit; thương mại chỉ nếu board cấp API);
3 cấu hình: trần / RAG văn bản / KG-RAG từ đề tài B.

**Ứng dụng/demo.** Leaderboard công khai; dùng làm bộ kiểm thử trước khi đưa chatbot nha khoa (đề tài B) vào phòng khám.

**Nơi công bố.** SOICT; KSEM; dạng data paper: BMC Med Inform Decis Mak.

**Điểm.**
| Tiêu chí | Điểm | Lý do |
|---|---|---|
| Tính mới | 4 | Benchmark nha khoa tiếng Việt đầu tiên (theo tìm kiếm hiện tại), nhưng là bài tài nguyên. |
| Ứng dụng | 3 | Gián tiếp: phục vụ đánh giá, không phải sản phẩm cuối. |
| Khả thi một người | 3 | Gán nhãn/rà câu hỏi tốn công; cần chuyên gia xác nhận đáp án. |
| Công bố | 4 | Benchmark ngôn ngữ ít tài nguyên dễ được nhận và được trích dẫn. |
| Hồ sơ NCS | 4 | Bổ trợ tốt cho B (đóng vai bộ đánh giá chung của chuỗi). |
| **Tổng** | **18/25** | |

**Rủi ro.** Nguồn câu hỏi bản quyền không rõ (đề thi, sách); license VM14K/DentalQA chưa rõ; nếu chỉ dịch thì reviewer coi là ít mới.

---

## 5. Tổng hợp và gợi ý chuỗi bài

| Đề tài | Mới | Ứng dụng | Khả thi | Công bố | NCS | Tổng |
|---|---|---|---|---|---|---|
| B. Chatbot nha khoa neo ontology OHD | 5 | 5 | 3 | 4 | 5 | **22** |
| A. KG-RAG y khoa tiếng Việt, LLM nhỏ | 4 | 3 | 5 | 4 | 4 | **20** |
| C. ViDentQA benchmark | 4 | 3 | 3 | 4 | 4 | **18** |

Chuỗi gợi ý: A (nhanh, dữ liệu sẵn, bài 1) rồi C (tập đánh giá nha khoa) rồi B (phương pháp + demo) rồi mở rộng B sang ảnh X-quang (giao CV).
A và C có thể chạy song song vì dùng chung pipeline.

## 6. Đã cân nhắc nhưng loại

- **GraphRAG y khoa tiếng Anh tổng quát**: đã bão hoà (MedGraphRAG, KG-RAG, MIRAGE và hàng chục biến thể), một người khó vượt SOTA.
- **KG-RAG trên hồ sơ bệnh án (EHR) như MediGRAF (P11)**: cần MIMIC/dữ liệu bệnh nhân, vi phạm ưu tiên dữ liệu công khai và cần credential.
- **Dựa vào SNOMED CT/UMLS làm xương sống**: cần license UTS (khoá mới, phải board duyệt) và không có tiếng Việt; để dành, chỉ thêm khi board cấp.

## 7. Việc còn mở (chưa kiểm chứng)

- VM14K có chuyên khoa răng hàm mặt không, bao nhiêu câu; license dữ liệu VM14K.
- Link tải và license DentalQA/DentalCorpus.
- Trạng thái Scopus hiện hành của JMIR Med Inform, BMC MIDM, JBI (tra Scopus Sources).
- Hạn nộp SOICT 2026/2027 và KSEM 2027.
