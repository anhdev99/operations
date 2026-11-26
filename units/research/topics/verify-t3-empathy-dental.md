# Phản biện độc lập: Đề tài 3 ViEmpath-Dental

Người kiểm: Critic (độc lập). Ngày: 2026-11-25. Đối tượng: mục 3 của `top5-de-tai.md`.
Quy ước: ✓ = mở được và khớp; ⚠ = tồn tại nhưng phát biểu lệch/thiếu; ✗ = sai. Chỉ ghi điều đã mở và đọc.

## 1. Kiểm từng trích dẫn

| Trích | Kết quả | Căn cứ đã đọc |
|---|---|---|
| EmplifAI, arXiv 2601.10033 | ✓ (⚠ nhỏ về cách gọi) | arXiv API: "EmplifAI: a Fine-grained Dataset for Japanese Empathetic Medical Dialogues in 28 Emotion Labels", She, Pereira, Cheng, Yahata, Siriaraya, Aramaki, 2026-01-15. Trích: "280 medically contextualized situations and 4125 two-turn dialogues, collected through crowdsourcing and expert review". Tiếng Nhật, đúng. ⚠: đây là **dataset** (không phải benchmark) cho bệnh nhân **bệnh mạn tính**, hội thoại chỉ **2 lượt**; có fine-tune LLM-jp-3.1-13b và thấy tăng đồng cảm ("notable improvements in fluency, general empathy, and emotion-specific empathy"), tức ý "LoRA tăng đồng cảm" đã có tiền lệ y khoa. https://arxiv.org/abs/2601.10033 |
| EmpatheticDialogues, 1811.00207 | ✓ | "Towards Empathetic Open-domain Conversation Models: a New Benchmark and Dataset", Rashkin, Smith, Li, Boureau; "25k conversations grounded in emotional situations". Năm trên arXiv 2018; "ACL 2019" là kiến thức sẵn có, tôi chưa mở trang ACL. https://arxiv.org/abs/1811.00207 |
| ESConv, 2106.01144 | ✓ | "Towards Emotional Support Dialog Systems", Liu, Zheng, Demasi, Sabour, Li, Yu (+Jiang, Huang theo README HF), 2021. README HF trích ACL 2021. https://arxiv.org/abs/2106.01144 |
| EPITOME, DOI 10.18653/v1/2020.emnlp-main.425 | ✓ | Crossref: "A Computational Approach to Understanding Empathy Expressed in Text-Based Mental Health Support", Sharma, Miner, Atkins, Althoff, EMNLP 2020. Ý "chỉ tiếng Anh": tôi chưa đọc nội dung bài, chưa kiểm. |
| VR lo âu nha khoa, 2609.15867 | ✓ | "On Edge in the Dental Chair: Designing VR Support for Moments of Dental Anxiety", Zhu Guo et al., 2026-09-14. Trích: "A randomized study (N=24) compared the intervention package with no-intervention VR". ⚠: còn phỏng vấn N=36 và walkthrough N=12; kết quả chỉ nói về "complete package". https://arxiv.org/abs/2609.15867 |

### Dataset (trang Hugging Face, API + README)

| Dataset | Giấy phép HF | Kết quả |
|---|---|---|
| facebook/empathetic_dialogues | `cc-by-nc-4.0` (cardData) | ✓. Chỉ có tệp script `empathetic_dialogues.py` + README, tải dữ liệu bên ngoài; cần kiểm nguồn tải còn sống. Giấy phép NC. https://huggingface.co/datasets/facebook/empathetic_dialogues |
| thu-coai/esconv | `cc-by-nc-4.0` | ✓ về giấy phép. ⚠: README HF **không** có chữ "chỉ nghiên cứu" như bảng viết; chỉ ghi NC. Chưa kiểm repo GitHub. https://huggingface.co/datasets/thu-coai/esconv |
| SEACrowd/uit_vsmec | `unknown` (README: "Unknown (unknown)"; tệp LICENSE chỉ ghi "Unknown (unknown)") | ✓ đúng là không rõ. ⚠ **sai vai trò**: README mô tả "Vietnamese Facebook comments ... emotion labels (enjoyment, sadness, fear, anger, disgust, surprise, other)" tức phân loại cảm xúc bình luận, **không phải hội thoại**. Nguồn tải là Google Sheets/Drive cá nhân, không có điều khoản. Chỉ dùng được làm bộ nhận diện cảm xúc phụ, không làm dữ liệu huấn luyện hội thoại. https://huggingface.co/datasets/SEACrowd/uit_vsmec |

Nhận xét: "dịch EmpatheticDialogues/ESConv sang tiếng Việt" là tạo tác phẩm phái sinh với giấy phép NC; công bố bản dịch phải giữ NC (đúng như đề tài đã cảnh báo).

## 2. Bài bỏ sót làm giảm tính mới

**Giới hạn quan trọng:** API arXiv (`export.arxiv.org`) và OpenAlex trả HTTP 429 liên tục từ máy này sau vài lệnh đầu (kể cả khi chạy chậm, một tiến trình). Tôi **không** hoàn thành được ≥6 truy vấn qua hai API đó. Thay bằng 6 truy vấn WebSearch và mở từng trang arXiv/ClinicalTrials liên quan bằng WebFetch (trang tóm tắt, không phải toàn văn). Kết quả "không thấy" vì vậy yếu hơn so với truy vấn API đầy đủ.

Truy vấn đã chạy (WebSearch): (1) Vietnamese empathetic dialogue dataset LLM 2025; (2) dental anxiety chatbot LLM empathy 2025 2026; (3) Vietnamese mental health chatbot LLM; (4) multilingual medical empathy benchmark LLM; (5) Vietnamese emotional support conversation; (6) LLM empathetic dental/Vietnamese/multilingual dialogue dataset; (7) chatbot dental anxiety MDAS.

Phát hiện (đã mở trang):

1. **Tsai & Yun-Nung Chen, "Balancing Knowledge Delivery and Emotional Comfort in Healthcare Conversational Systems", arXiv 2506.13692, 2025-06-16.** Dùng LLM viết lại hội thoại y khoa thật thành bệnh nhân lo lắng + trả lời trấn an kèm thông tin, rồi fine-tune LLM; "cải thiện đáp ứng cảm xúc mà giữ độ đúng kiến thức". Gần như đúng câu hỏi nghiên cứu "tăng đồng cảm mà không sai thông tin" (trừ nha khoa, tiếng Việt). Ngôn ngữ dữ liệu trang không nêu. https://arxiv.org/abs/2506.13692
2. **Umucu et al., "Empathy by Design: Aligning LLMs for Healthcare Dialogue", arXiv 2512.06097, 2025-12-05.** DPO trên cặp hỗ trợ/quy phạm, báo tăng độ đúng và điểm lấy con người làm trung tâm, hơn baseline và hệ thương mại. https://arxiv.org/abs/2512.06097
3. **Chatbot AI giảm lo âu nha khoa (tóm tắt trên synapsesocial.com, tôi chỉ đọc qua kết quả WebSearch; trang WebFetch bị 429):** bệnh nhân tương tác 10-15 phút **trước điều trị**, đo MDAS trước/sau trên 5 kịch bản nha khoa, giảm có ý nghĩa ở cả 5 (p<0.001). Chưa rõ tác giả, cỡ mẫu, có LLM hay không. Trùng trực tiếp "chatbot trước buổi hẹn" mà đề tài gọi là demo. https://synapsesocial.com/papers/6a0ec9abb7cc3b883f22bcc8 (nguồn thứ cấp, ⚠).
4. **Healthcare 2025, 13(23):3099 (MDPI) và PMC12691705, "Professional Quality and Empathy of Responses Provided by AI and Dentists: A Cross-Sectional Study":** theo kết quả tìm kiếm, ChatGPT-3.5 được chấm đồng cảm 3,23 so với nha sĩ 1,73-2,14. Tôi **không mở được** trang MDPI (403) và PMC (lỗi SSL); chỉ có đoạn tóm tắt của công cụ tìm kiếm. ⚠ Chưa kiểm trực tiếp. Cho thấy "LLM vs nha sĩ về đồng cảm" đã có.
5. **Đã có trên ClinicalTrials.gov NCT07133919, "Effect of AI-Supported Child-Friendly Communication on Dental Anxiety in Pediatric Patients":** chỉ thấy tiêu đề trong kết quả tìm kiếm; trang không tải được nội dung. ⚠ chưa kiểm.
6. **Tiếng Việt, gần nhất:** arXiv 2604.20948 "Can Virtual Agents Care? Designing an Empathetic and Personalized LLM-Driven Conversational Agent" (Toan, Mach, Le, Tuyen; 2026-04-22): agent đồng cảm RAG, nghiên cứu liên văn hoá với sinh viên Việt Nam và Úc; kết quả tốt hơn LLM-only về mạch lạc, độ chính xác cảm nhận, đồng cảm. Trang không nói rõ có chạy tiếng Việt, không có nội dung nha khoa. Không đe doạ trực tiếp nhưng cho thấy nhóm Việt đã làm đồng cảm LLM + đánh giá người. https://arxiv.org/abs/2604.20948
7. **Dataset tiếng Việt liên quan nhưng không phải hội thoại đồng cảm:** ViGoEmotions arXiv 2602.08371 (20.664 bình luận, 27 nhãn cảm xúc, Tran, Pham, Luu, Nguyen, 2026-02-09) — nguồn dữ liệu cảm xúc tiếng Việt mới hơn UIT-VSMEC, nhưng cũng là bình luận; CSConDa 2507.22542 (QA chăm sóc khách hàng).
8. **Đa ngôn ngữ y khoa, không có trục đồng cảm:** GlobMed-Bench 2601.02186 (12 ngôn ngữ, 56 LLM, theo tóm tắt tìm kiếm); HealMed 2608.19981 (9 ngôn ngữ). Chưa mở toàn văn. Không thấy benchmark đồng cảm y khoa đa ngôn ngữ trong các truy vấn đã chạy.
9. Không tìm thấy trong các truy vấn đã chạy: dataset hội thoại đồng cảm tiếng Việt công khai; LLM đồng cảm tiếng Việt cho nha khoa. Đây là "không thấy", không phải "chắc chắn không có".

Hệ quả cho tính mới: ba mảnh (đồng cảm y khoa + fine-tune, chatbot lo âu nha khoa, so sánh LLM vs nha sĩ về đồng cảm) đã có riêng lẻ. Phần còn lại là **tổ hợp tiếng Việt + nha khoa + so VI/EN + so mở/thương mại**. Mới ở mức tổ hợp, không phải mới về phương pháp. "Mới = 5" là cao.

## 3. Tính thực tế

- **Không có bác sĩ RHM cộng tác**: đề tài tự nêu "tình huống do tác giả + bác sĩ RHM viết", "chuyên gia duyệt" và "đúng/sai thông tin" (cần người có chuyên môn). Thiếu họ thì (a) bộ tình huống không có độ tin cậy lâm sàng, (b) không chấm được mục "không làm sai thông tin y khoa", đó là nửa câu hỏi nghiên cứu. Có thể thay bằng đối chiếu hướng dẫn công khai, nhưng tạp chí JMIR/BMC sẽ vẫn đòi chuyên gia.
- **Đánh giá người + đạo đức**: nếu chỉ dùng tình huống tự viết và để 2-3 người chấm (không bệnh nhân thật), nhiều nơi coi là không phải nghiên cứu trên người, nhưng vẫn cần giấy xác nhận miễn/không áp dụng của hội đồng/đơn vị. Chưa kiểm quy định cụ thể của cơ sở của chủ nhóm. Thử với bệnh nhân thật (hướng demo "chatbot trước buổi hẹn") chắc chắn cần hội đồng đạo đức và cơ sở nha khoa: ngoài tầm với 8 tuần.
- **Tác động**: đề tài tự thừa nhận dữ liệu tự sinh kém tự nhiên và giấy phép NC chặn thương mại hoá. Cộng thêm tiền lệ #1-#3 ở trên khiến phần đóng góp chủ yếu là "áp dụng sang tiếng Việt/nha khoa". Ứng dụng thực tế phụ thuộc đúng vào thứ chủ nhóm đang thiếu (bác sĩ, cơ sở).
- **Kỹ thuật**: 8 tuần, QLoRA 7-8B trên 2-3k hội thoại, GPU 16-24 GB: làm được về kỹ thuật. Chưa biết chủ nhóm có GPU không (CLAUDE.md của research ghi chưa biết). Chất lượng 7-8B tiếng Việt chưa kiểm.
- LLM-as-judge cho đồng cảm tiếng Việt chưa có xác nhận độ tin cậy; đề tài cần báo tương quan với người (bước cần người).

## 4. Kết luận và điểm

**Kết luận: SỬA, hạ điểm; không loại. Giữ trong top 5 nhưng không còn là hướng ưu tiên khi chưa có bác sĩ RHM.**

| Tiêu chí | Cũ | Mới | Lý do |
|---|---|---|---|
| Mới | 5 | 4 | Mới ở mức tổ hợp VI + nha khoa + VI/EN; đã có tiền lệ cho từng mảnh (2506.13692, 2512.06097, chatbot MDAS, ChatGPT vs nha sĩ) |
| ƯD | 4 | 4 | Nhu cầu có thật, nhưng ứng dụng bệnh nhân thật cần cơ sở và đạo đức |
| KT | 3 | 2 | Không có bác sĩ RHM, đánh giá người, đạo đức; tự tạo dữ liệu |
| CB | 4 | 3 | Tạp chí y khoa số sẽ đòi chuyên gia + người đánh giá; mới ở mức tổ hợp |
| NCS | 5 | 4 | Hợp mảng, nhưng dễ dừng ở "đã dịch/áp dụng" |
| **Tổng** | **21** | **17** | |

Cách cứu (nếu giữ): (1) bỏ phần thử với người thật và demo bệnh nhân; (2) đổi trọng tâm sang **bộ tình huống + benchmark đồng cảm VI/EN** (đánh giá zero-shot, đo VI-EN gap), QLoRA là phần phụ; (3) tìm một bác sĩ RHM duyệt tối thiểu 150 tình huống và 100 cặp trả lời (vài giờ, làm cố vấn, ghi cảm ơn/đồng tác giả); (4) cắt UIT-VSMEC khỏi danh sách dữ liệu huấn luyện; (5) dùng ESConv/EmpatheticDialogues chỉ để đối chiếu, không công bố bản dịch ngoài NC; (6) so sánh trực tiếp với 2506.13692 làm baseline phương pháp.

Chiếu theo bảng chung, 17 điểm thấp hơn #4 (21) và #5 (20): đề tài này tụt xuống hạng 5 nếu Dean cập nhật bảng.

## 5. Điều CHƯA kiểm được

- Truy vấn API arXiv/OpenAlex bị 429, chưa làm đủ ≥6 truy vấn qua hai API; kết quả tìm kiếm dựa WebSearch (thứ cấp) và trang tóm tắt arXiv. Nên chạy lại bằng API sau khi hết giới hạn, đặc biệt tìm 2025-2026 với "Vietnamese empathetic", "dental anxiety LLM".
- Không mở được trang MDPI Healthcare 13(23):3099, PMC12691705, PMC12939114, synapsesocial (429), ClinicalTrials NCT07133919 (không có nội dung). Các con số 3,23 vs 1,73-2,14 và kết quả MDAS p<0.001 chỉ là bản tóm tắt tìm kiếm.
- Chưa đọc toàn văn EmplifAI, EPITOME, 2506.13692, 2512.06097, 2604.20948 (chỉ tóm tắt), nên chưa kiểm ngôn ngữ dữ liệu của 2506.13692 và việc 2604.20948 có chạy tiếng Việt không.
- Chưa kiểm: ACL 2019 cho EmpatheticDialogues; ESConv "chỉ nghiên cứu" ở GitHub; nguồn tải dữ liệu của EmpatheticDialogues còn sống không; Scopus/SJR của JMIR FR/HF/BMC Oral Health; quy định đạo đức của cơ sở chủ nhóm; GPU; chất lượng 7-8B mở trên tiếng Việt.
- Chưa kiểm tồn tại hay không có dataset hội thoại đồng cảm tiếng Việt trên HF (chỉ WebSearch; không gọi HF search API).
