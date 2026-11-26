# Brief: Cảm xúc + chatbot (hội thoại đồng cảm)

Issue: RES-4 (con của RES-1). Người soạn: Scholar. Ngày: 2026-11-24.

## Cách khảo sát và giới hạn

- Nguồn đã mở: trang arXiv (abstract), ACL Anthology, README/LICENSE trên GitHub, API Hugging Face (metadata dataset), trang "Indexing" của JMIR.
- Tìm Hugging Face với từ khoá `vietnamese mental health`, `vietnamese counseling`, `vietnamese psychology`, `vietnamese empathetic`: **không có kết quả** (ngày 2026-11-24). Tìm arXiv `vietnamese AND (empathetic OR "emotional support" OR "mental health" OR counseling)`: chỉ ra 3 bài, không bài nào về hội thoại đồng cảm. Đây là bằng chứng *gián tiếp* cho khoảng trống tiếng Việt, chưa phải tổng quan hệ thống (Scopus/Google Scholar bị chặn hoặc giới hạn tần suất 429 trong lượt này).
- Chỉ đọc abstract + README; chưa đọc toàn văn PDF. Số liệu chỉ lấy đúng như abstract/README ghi.

## Tài liệu đã kiểm chứng (dùng chung cho các đề tài)

| Mã | Bài / dataset | Venue, năm | Link |
|---|---|---|---|
| P1 | Rashkin, Smith, Li, Boureau. *Towards Empathetic Open-domain Conversation Models: a New Benchmark and Dataset* (EmpatheticDialogues, 25k hội thoại) | ACL 2019 | https://doi.org/10.48550/arXiv.1811.00207 |
| P2 | Liu, Zheng, Demasi, Sabour, Li, Yu, Jiang, Huang. *Towards Emotional Support Dialog Systems* (ESConv, khung Helping Skills, nhãn chiến lược hỗ trợ) | ACL 2021 | https://doi.org/10.48550/arXiv.2106.01144 |
| P3 | Sharma, Miner, Atkins, Althoff. *A Computational Approach to Understanding Empathy Expressed in Text-Based Mental Health Support* (khung EPITOME: Emotional Reactions / Interpretations / Explorations; 10k cặp post-response) | EMNLP 2020 | https://doi.org/10.18653/v1/2020.emnlp-main.425 |
| P4 | Ho, Nguyen, Nguyen, Pham, Nguyen, Nguyen, Nguyen. *Emotion Recognition for Vietnamese Social Media Text* (UIT-VSMEC, 6.927 câu, 7 nhãn; CNN weighted-F1 59,74%) | PACLING 2019 (Springer CCIS 2020) | https://doi.org/10.48550/arXiv.1911.09339 |
| P5 | Xu, Jiang. *Multi-dimensional Evaluation of Empathetic Dialogue Responses* (prompt GPT-4/Flan đo đồng cảm kém; classifier FlanT5 instruction-tuned tốt hơn) | Findings EMNLP 2024 | https://doi.org/10.18653/v1/2024.findings-emnlp.113 |
| P6 | Luo, Warren, Cheng, Abdul-Muhsin, Banerjee. *Assessing Empathy in LLMs with Real-World Physician-Patient Interactions* (EMRank; dữ liệu Mayo Clinic đã ẩn danh, không công khai) | arXiv 2024 (preprint) | https://doi.org/10.48550/arXiv.2405.16402 |
| P7 | She, Kanashiro Pereira, Cheng, Yahata, Siriaraya, Aramaki. *EmplifAI: Japanese Empathetic Medical Dialogues in 28 Emotion Labels* (280 tình huống, 4.125 hội thoại 2 lượt; so LLM-as-judge với người) | arXiv 2026 (preprint) | https://doi.org/10.48550/arXiv.2601.10033 |
| P8 | Chorna. *SPLIT: Cross-Lingual Empathy and Cultural Grounding in English and Ukrainian LLM Responses* (500 prompt; LLM giảm chất lượng khi sang tiếng Ukraina; người và AI đồng thuận yếu) | arXiv 2026 (preprint) | https://doi.org/10.48550/arXiv.2607.02049 |
| P9 | Guo và cộng sự (16 tác giả). *On Edge in the Dental Chair: Designing VR Support for Moments of Dental Anxiety* (VR, RCT N=24, giảm VAS-A trung bình -12,83) | arXiv 2026 (preprint, cs.HC) | https://doi.org/10.48550/arXiv.2609.15867 |

Dataset đã kiểm chứng (metadata Hugging Face / README):

| Mã | Dataset | Kích thước | Giấy phép / truy cập | Link |
|---|---|---|---|---|
| D1 | EmpatheticDialogues (EN) | 25k hội thoại, 32 nhãn cảm xúc | CC BY-NC 4.0, tải tự do | https://huggingface.co/datasets/facebook/empathetic_dialogues |
| D2 | ESConv (EN) | 1.300 hội thoại, 8 chiến lược; thêm `FailedESConv.json` 196 mẫu âm | CC BY-NC 4.0 (HF); README: "academic research use only" | https://huggingface.co/datasets/thu-coai/esconv , https://github.com/thu-coai/Emotional-Support-Conversation |
| D3 | EPITOME Reddit (EN) | phần Reddit của 10k cặp; 3 tệp csv (ER/IP/EX) có level + rationale | Reddit: public trong repo; phần TalkLife phải xin, phi thương mại. File LICENSE: **chưa kiểm chứng** | https://github.com/behavioral-data/Empathy-Mental-Health |
| D4 | UIT-VSMEC (VI) | 6.927 câu Facebook, 7 nhãn | **Không rõ giấy phép** (SEACrowd ghi "unknown") | https://huggingface.co/datasets/SEACrowd/uit_vsmec |
| D5 | huyleit/vietnamese-social-emotion (VI) | 11.193 mẫu (VSMEC + GoEmotions dịch máy) | ghi MIT nhưng gộp từ D4 (không rõ giấy phép); chất lượng dịch **chưa kiểm chứng** | https://huggingface.co/datasets/huyleit/vietnamese-social-emotion |

Không tìm thấy dataset hội thoại đồng cảm / hỗ trợ cảm xúc tiếng Việt công khai nào.

---

## Đề tài 1. ViEmpath-Dental: benchmark hội thoại đồng cảm tiếng Việt cho lo âu nha khoa

**Câu hỏi nghiên cứu.** LLM mở (7-8B) và LLM thương mại phản hồi đồng cảm bằng tiếng Việt cho bệnh nhân lo âu nha khoa tốt đến đâu so với tiếng Anh, và việc tinh chỉnh nhẹ (LoRA) trên dữ liệu tình huống nha khoa có cải thiện đồng cảm mà không làm sai thông tin y khoa?

**Khoảng trống.**
- P7 (EmplifAI) làm benchmark đồng cảm y khoa cho tiếng Nhật, bệnh mạn tính; không có tiếng Việt, không có nha khoa.
- P8 (SPLIT) cho thấy LLM giảm chất lượng đồng cảm khi chuyển sang ngôn ngữ ít tài nguyên; chỉ làm tiếng Ukraina.
- P1, P2 là tiếng Anh, chủ đề đời sống chung; không có bối cảnh lâm sàng.
- P9 can thiệp lo âu nha khoa bằng VR, không phải hội thoại; giai đoạn trước hẹn (tại nhà) còn để trống.

**Dataset.** Không có sẵn; phải tự xây: (a) 150-300 tình huống lo âu nha khoa viết bởi tác giả + bác sĩ RHM cộng tác (không dùng hội thoại bệnh nhân thật), (b) mở rộng bằng LLM sinh rồi chuyên gia duyệt (như quy trình P7), (c) dùng D1, D2 dịch sang tiếng Việt làm tập phụ để huấn luyện (phi thương mại, phải trích dẫn).

**Baseline (1-2 tháng, GPU hạn chế).**
- Zero-shot: 3-4 LLM (một model mở 7-8B hỗ trợ tiếng Việt chạy 4-bit + 1-2 API) trên cùng bộ tình huống, VI và EN song song.
- LoRA/QLoRA 7-8B trên ~2-3k hội thoại (tình huống tự xây + D2 dịch): vừa 1 GPU 16-24 GB.
- Đánh giá: người (2-3 người, thang đồng cảm + đúng/sai thông tin) + LLM-as-judge, báo cáo tương quan.

**Ứng dụng / demo.** Chatbot web/Zalo-mini-app trước buổi hẹn nha khoa: bệnh nhân nói nỗi sợ (đau, kim tiêm, chi phí), bot đáp đồng cảm, giải thích quy trình, nhắc hỏi bác sĩ. Phòng khám dùng làm kênh tiếp nhận; không chẩn đoán.

**Nơi công bố.**
- JMIR Formative Research (ISSN 2561-326X) — trang Indexing ghi Scopus, CiteScore 4,2 (2025): https://formative.jmir.org/about-journal/indexing-and-impact-factor
- JMIR Human Factors — trang Indexing ghi Scopus, CiteScore 5,6: https://humanfactors.jmir.org/about-journal/indexing-and-impact-factor
- BMC Oral Health (ISSN 1472-6831, BioMed Central): https://bmcoralhealth.biomedcentral.com/ — tồn tại; chỉ số Scopus **chưa kiểm chứng** trong lượt này (trang bị chặn).

**Điểm.**
| Tiêu chí | Điểm | Lý do |
|---|---|---|
| Tính mới | 5 | Không tìm thấy dataset/benchmark đồng cảm tiếng Việt; nha khoa chưa ai làm hội thoại. |
| Ứng dụng | 4 | Demo trước hẹn dùng được ở phòng khám; cần bác sĩ duyệt nội dung. |
| Khả thi 1 người | 3 | Tự xây dữ liệu + đánh giá người tốn công; cần ít nhất 1 bác sĩ RHM. |
| Công bố | 4 | Paper dataset + benchmark hợp JMIR/LRE; tiếng Việt là điểm bán. |
| Hợp hồ sơ NCS | 5 | Chuỗi tự nhiên: dataset, đánh giá, mô hình, thử nghiệm người dùng. |
| **Tổng** | **21/25** | |

**Rủi ro.** Dữ liệu tự sinh có thể thiên lệch, thiếu tự nhiên; cần thoả thuận với bác sĩ; nếu thử với người thật phải qua hội đồng đạo đức; giấy phép NC của D1/D2 chặn thương mại hoá.

---

## Đề tài 2. Đo đồng cảm tự động cho tiếng Việt: chuyển giao EPITOME và độ tin cậy của LLM-as-judge

**Câu hỏi nghiên cứu.** Có thể đo mức đồng cảm (ER/IP/EX theo P3) của phản hồi tiếng Việt bằng (a) classifier đa ngôn ngữ huấn luyện trên dữ liệu tiếng Anh + dịch, hoặc (b) LLM-as-judge, với độ đồng thuận với người đủ cao không?

**Khoảng trống.**
- P3 đưa khung và dữ liệu EPITOME, chỉ tiếng Anh.
- P5 cho thấy prompt LLM (kể cả GPT-4) đo đồng cảm kém, classifier fine-tune tốt hơn; chỉ tiếng Anh, dữ liệu customer service nội bộ.
- P8 thấy người và AI đồng thuận yếu về đồng cảm khi đổi ngôn ngữ; không có tiếng Việt.
- P6 đề xuất EMRank nhưng dữ liệu không công khai.

**Dataset.** D3 (Reddit EPITOME, có nhãn level + rationale) dịch sang tiếng Việt; tập test 300-500 cặp dịch + hiệu chỉnh tay và gán nhãn lại bởi 2 người Việt (đo Cohen's kappa). D4/D5 làm tác vụ phụ nhận diện cảm xúc.

**Baseline.**
- Classifier: XLM-R base / PhoBERT (cần kiểm tra giấy phép) fine-tune multi-task như P3; chạy được trên 1 GPU 8-12 GB.
- LLM-as-judge zero/few-shot với rubric EPITOME.
- So sánh: train-EN-test-VI, translate-train, translate-test; báo F1 + tương quan với người.

**Ứng dụng / demo.** Công cụ chấm đồng cảm cho câu trả lời tiếng Việt: dùng làm bộ lọc/reward cho chatbot ở Đề tài 1, 3; hoặc phản hồi luyện kỹ năng giao tiếp cho sinh viên RHM/điều dưỡng (gõ câu trả lời, nhận điểm + gợi ý).

**Nơi công bố.**
- Language Resources and Evaluation (Springer, ISSN 1574-020X): https://link.springer.com/journal/10579 — tồn tại (OpenAlex); Scopus **chưa kiểm chứng** trong lượt này.
- PACLIC (ACL Anthology, có kỳ 2025): https://aclanthology.org/venues/paclic/ — tồn tại; Scopus **chưa kiểm chứng**.
- JMIR Human Factors (Scopus, đã kiểm chứng ở trên) nếu nhấn mạnh ứng dụng đào tạo.

**Điểm.**
| Tiêu chí | Điểm | Lý do |
|---|---|---|
| Tính mới | 4 | Đo đồng cảm tiếng Việt chưa thấy; nhưng phương pháp là chuyển giao chuẩn. |
| Ứng dụng | 3 | Là công cụ hạ tầng; giá trị thực tế gián tiếp. |
| Khả thi 1 người | 4 | Dữ liệu có sẵn, model nhỏ; chỉ cần gán nhãn test ~500 cặp. |
| Công bố | 3 | Đủ cho hội nghị khu vực; khó lên tạp chí mạnh nếu thiếu phần ứng dụng. |
| Hợp hồ sơ NCS | 4 | Là bài "đo lường" làm nền cho chuỗi Đề tài 1 và 3. |
| **Tổng** | **18/25** | |

**Rủi ro.** Dịch làm lệch nhãn đồng cảm (khác văn hoá, xưng hô); giấy phép file D3 chưa rõ; nội dung Reddit về sức khoẻ tâm thần nhạy cảm.

---

## Đề tài 3. Chatbot hỗ trợ cảm xúc có điều khiển chiến lược + nhận diện cảm xúc, an toàn cho bệnh nhân tiếng Việt

**Câu hỏi nghiên cứu.** Ghép (1) nhận diện cảm xúc người dùng tiếng Việt, (2) chọn chiến lược hỗ trợ theo ESConv (hỏi, phản ánh cảm xúc, trấn an, thông tin...) và (3) lớp an toàn chuyển người thật khi có tín hiệu nguy cơ, có làm phản hồi LLM đồng cảm và an toàn hơn so với prompt trực tiếp?

**Khoảng trống.**
- P2 chứng minh chiến lược hỗ trợ quan trọng, nhưng dữ liệu tiếng Anh và chủ đề đời sống (trầm cảm, chia tay, công việc...), không có bệnh nhân y khoa.
- P4 nhận diện cảm xúc tiếng Việt ở mức câu mạng xã hội, chưa gắn vào hội thoại hay sinh phản hồi.
- P7, P8 đánh giá phản hồi đơn lượt; ít bàn chiến lược nhiều lượt và cơ chế chuyển tiếp an toàn.

**Dataset.** D2 (ESConv, nhãn chiến lược) dịch sang tiếng Việt; D4/D5 cho bộ nhận diện cảm xúc; bộ tình huống nha khoa của Đề tài 1 (nếu có) làm test miền.

**Baseline.**
- Bộ nhận diện cảm xúc: PhoBERT/XLM-R trên D4 (tham chiếu weighted-F1 59,74% của P4).
- Bộ dự đoán chiến lược: classifier nhỏ trên ESConv dịch.
- Sinh: LLM 7-8B 4-bit với prompt có cảm xúc + chiến lược; so với prompt thường; đánh giá bằng người + bộ chấm Đề tài 2.
- An toàn: danh sách từ khoá + classifier nguy cơ; luôn có thông điệp chuyển tới người thật.

**Ứng dụng / demo.** Trợ lý chăm sóc khách hàng/bệnh nhân cho phòng khám (trước và sau điều trị), hoặc kênh lắng nghe cho sinh viên; chạy cục bộ để không gửi dữ liệu ra ngoài.

**Nơi công bố.**
- JMIR Formative Research (Scopus, đã kiểm chứng) — bài thử nghiệm khả thi.
- JMIR Mental Health (Scopus, CiteScore 11,4; đã kiểm chứng: https://mental.jmir.org/about-journal/indexing-and-impact-factor) — nếu hướng sức khoẻ tâm thần, yêu cầu cao.
- Vietnam Journal of Computer Science (World Scientific, ISSN 2196-8896) — tồn tại (OpenAlex); Scopus **chưa kiểm chứng** (trang bị 403).

**Điểm.**
| Tiêu chí | Điểm | Lý do |
|---|---|---|
| Tính mới | 3 | Ghép module là hướng đã có ở tiếng Anh; mới chủ yếu ở tiếng Việt + miền bệnh nhân. |
| Ứng dụng | 5 | Demo chatbot chạy được ngay, dễ trình diễn cho phòng khám. |
| Khả thi 1 người | 4 | Toàn bộ dùng dữ liệu công khai + model nhỏ; phần khó là đánh giá người. |
| Công bố | 3 | Cần đánh giá người dùng tốt mới vượt mức "system paper". |
| Hợp hồ sơ NCS | 4 | Là bài "hệ thống" cuối chuỗi sau Đề tài 2 và 1. |
| **Tổng** | **19/25** | |

**Rủi ro.** Chatbot nói sai thông tin y khoa hoặc đáp không phù hợp với người có nguy cơ tự hại; thử với người dùng thật cần chấp thuận đạo đức; dịch ESConv có thể mất sắc thái chiến lược.

---

## Rủi ro đạo đức chung

- Không dùng hội thoại bệnh nhân thật; mọi tình huống do tác giả/bác sĩ viết hoặc LLM sinh rồi duyệt.
- Chatbot phải tuyên bố là AI, không chẩn đoán, có lối chuyển tới nhân viên y tế/đường dây nóng.
- D1, D2 là CC BY-NC 4.0: chỉ dùng nghiên cứu phi thương mại; thương mại hoá demo phải dùng dữ liệu tự xây.
- Đánh giá với người (kể cả sinh viên) nên xin chấp thuận hội đồng đạo đức của trường trước khi chạy.

## Chuỗi bài gợi ý cho hồ sơ NCS

Đề tài 2 (đo lường) -> Đề tài 1 (dataset + benchmark nha khoa) -> Đề tài 3 (hệ thống) -> bài thử nghiệm người dùng ở phòng khám (JMIR Formative Research).

## Tóm tắt điểm

| Đề tài | Mới | Ứng dụng | Khả thi | Công bố | NCS | Tổng |
|---|---|---|---|---|---|---|
| 1. ViEmpath-Dental benchmark | 5 | 4 | 3 | 4 | 5 | **21** |
| 3. Chatbot chiến lược + an toàn | 3 | 5 | 4 | 3 | 4 | **19** |
| 2. Đo đồng cảm tiếng Việt | 4 | 3 | 4 | 3 | 4 | **18** |

## Đã cân nhắc nhưng loại

- **Nhận diện cảm xúc đa phương thức (giọng nói/khuôn mặt) bệnh nhân nha khoa**: cần quay video/ghi âm bệnh nhân thật, vướng quy tắc dữ liệu y tế và tốn GPU.
- **Chỉ nhận diện cảm xúc văn bản tiếng Việt (cải tiến F1 trên UIT-VSMEC)**: đã có nhiều công trình và bản phái sinh trên Hugging Face (≥15 repo VSMEC), khoảng trống nhỏ, không có demo hội thoại.
- **Chatbot trị liệu tâm lý (CBT) tự động cho trầm cảm**: rủi ro an toàn cao, cần chuyên gia lâm sàng giám sát, vượt sức một người.
