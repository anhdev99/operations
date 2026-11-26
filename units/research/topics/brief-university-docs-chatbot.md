# Brief: Chatbot hỏi đáp văn bản quy chế trường đại học tiếng Việt (RES-19, làm lại RES-15)

Issue cha: RES-14. Người viết: Scholar. Ngày: 2026-11-25.

## Cách kiểm chứng

- Tìm qua Semantic Scholar API (1 lần, sau đó bị 429), arXiv search, Hugging Face API, Crossref, GitHub API. Tổng khoảng 16 lần tìm/mở.
- Mỗi bài dưới đây đã mở **trang abstract** (arXiv hoặc Crossref). Chỉ R2GQA được đọc gần hết toàn văn (HTML arXiv).
  Các bài khác: thông tin lấy từ abstract, chi tiết phương pháp **chưa kiểm chứng**.
- Venue: tồn tại đã kiểm qua DOI/Crossref/arXiv comment. **Scopus: chưa tra cho venue nào** (Scopus cần đăng nhập). Chủ nhóm tra lại ở https://www.scopus.com/sources trước khi nộp.
- Dữ kiện chủ nhóm đã trả lời được áp dụng: kho trường >30.000 tệp PDF/Word **không công bố**; chatbot hiện tại RAG + Gemini API.
  Do đó đóng góp nằm ở **phương pháp + đánh giá**; bộ đánh giá công khai dựng từ văn bản pháp quy công khai; kho trường chỉ cho số liệu tổng hợp.

## Bài đã mở (dùng chung)

| Mã | Bài | Venue, năm | Link | Đã đọc |
|---|---|---|---|---|
| P1 | Pham Do P.-T., Cao D.-N. D., Tran K. Q., Nguyen K. V. — R2GQA: Retriever-Reader-Generator QA ... Legal Regulations in Higher Education | arXiv, 2024 | https://doi.org/10.48550/arXiv.2409.02840 | Gần toàn văn |
| P2 | Nguyen L. S. T. và cộng sự — ViHERMES: Graph-Grounded Multihop QA Benchmark ... Vietnamese Healthcare Regulations | ACIIDS 2026 (theo arXiv comment), arXiv 2602.07361 | https://arxiv.org/abs/2602.07361 ; code MIT https://github.com/longstnguyen/ViHERMES | Abstract |
| P3 | Prior M., Schultz A., Grabmair M. — Asking For An Old Friend: Temporal Failure Modes in LLM-based Statutory QA | ICAIL 2026 (theo arXiv comment) | https://doi.org/10.48550/arXiv.2605.23497 | Abstract |
| P4 | Le H., Luu N., Nguyen T., Dao T., Dinh S. — Optimizing Answer Generator in Vietnamese Legal QA Systems Using Language Models | ACM TALLIP 24(6), 2025 | https://doi.org/10.1145/3732938 | Abstract (Crossref) |
| P5 | Nguyen D. T. và cộng sự (UIT) — ViLegalExpert: Large-Scale Benchmark for Vietnamese Legal Retrieval and QA | arXiv, 2026 | https://doi.org/10.48550/arXiv.2609.39189 | Abstract |
| P6 | Nguyen T. D. và cộng sự — Benchmarking Vietnamese Legal Knowledge of LLMs (VLegal-Bench) | arXiv, 2025 (v7 2026) | https://doi.org/10.48550/arXiv.2512.14554 | Abstract |

Điểm chính đã kiểm chứng:
- **P1 (gần nhất về miền)**: ViRHE4QA 9.758 cặp hỏi-đáp từ **21 văn bản đào tạo của một trường** (294 "article", trung bình 10,67 trang/văn bản).
  PDF/ảnh được chuyển Word bằng smallpdf hoặc **gõ lại tay**; bảng chuyển thành đoạn văn. Retriever BM25 + bi-encoder, Reader BIO, Generator seq2seq.
  Không xử lý phiên bản/hiệu lực, không đánh giá trích dẫn căn cứ, không dùng LLM sinh (so với RAG chỉ như baseline). Giấy phép bài: CC BY-NC-SA 4.0; dữ liệu "available for research purposes" (giấy phép dữ liệu **chưa kiểm chứng**).
- **P2**: multihop QA trên quy định y tế; abstract nêu rõ có kiểu phụ thuộc "amendment tracing", truy hồi đồ thị theo đơn vị pháp lý. **Đây là đối thủ gần nhất về phương pháp**; khác miền (y tế, không phải giáo dục).
- **P3**: 312 câu hỏi luật Đức nhạy thời gian; hai lỗi: "post-cutoff staleness" và "recency bias"; RAG có lọc phiên bản theo ngày cải thiện rõ. Chỉ tiếng Đức, chỉ LLM thương mại (OpenAI, Anthropic, DeepSeek).
- **P4**: fine-tune LLM nhỏ cho sinh câu trả lời pháp luật tiếng Việt, nhấn mạnh triển khai GPU hạn chế. Không nói tới hiệu lực văn bản hay trích dẫn (theo abstract).
- **P5**: 172K câu hỏi thật, 34 lĩnh vực, bằng chứng do chuyên gia kiểm. **P6**: 10.450 mẫu, có tác vụ RAG. Cả hai là luật chung, không riêng giáo dục, không có trục thời gian rõ ràng (theo abstract).

Kết luận khoảng trống chung: QA quy chế đại học tiếng Việt đã có (P1) nhưng **tĩnh, một trường, nhỏ**. Hỏi đáp **nhận biết hiệu lực** đã có cho luật Đức (P3) và có dấu vết trong y tế Việt Nam (P2), **chưa thấy cho văn bản giáo dục/đào tạo tiếng Việt**, và chưa thấy so sánh LLM mở cục bộ với API trên kho thật hàng chục nghìn tệp.

## Dataset công khai (đã mở trang)

| Tên | Link | Giấy phép | Kích thước | Dùng cho |
|---|---|---|---|---|
| vietnamese-legal-documents (thu từ thuvienphapluat.vn) | https://huggingface.co/datasets/vohuutridung/vietnamese-legal-documents (bản gốc ghi trong citation: th1nhng0/vietnamese-legal-documents) | CC BY 4.0 (thẻ dataset); văn bản quy phạm là công khai theo Luật Tiếp cận thông tin | 518.255 văn bản, 1924–2026, metadata có `document_number`, `legal_type`, `issuing_authority`, `issuance_date` | Lọc văn bản Bộ GD&ĐT (thông tư, quy chế đào tạo) để dựng chuỗi sửa đổi/thay thế |
| ViRHE4QA (P1) | https://arxiv.org/abs/2409.02840 (link dữ liệu trong bài) | chưa kiểm chứng ("research purposes") | 9.758 QA, 21 văn bản | Baseline QA quy chế tĩnh, so sánh trực tiếp |
| ViHERMES (P2) | https://github.com/longstnguyen/ViHERMES | MIT (GitHub API) | chưa kiểm chứng số câu | Baseline truy hồi đồ thị, tái dùng pipeline sinh multihop |
| Vietnamese-Legal-QA-RAG | https://huggingface.co/datasets/NamSyntax/Vietnamese-Legal-QA-RAG | Apache-2.0 (metadata HF) | 420 dòng | Kiểm tra nhanh pipeline RAG; chỉ đọc metadata, nội dung chưa kiểm |
| vietnamese-legal-ocr | https://huggingface.co/datasets/niits/vietnamese-legal-ocr | MIT (metadata HF) | 9.579 ảnh **tổng hợp** | Chỉ để thử OCR; không thay được scan thật |

Lưu ý: thuvienphapluat.vn có điều khoản sử dụng riêng; thẻ dataset tự tuyên bố CC BY 4.0. Trước khi phát hành benchmark, nên lấy văn bản gốc từ Cổng văn bản pháp luật / Công báo của Chính phủ và ghi nguồn (chưa kiểm chứng điều khoản tái phân phối của thuvienphapluat).

---

## Đề tài 1. EduReg-Time: hỏi đáp quy chế đào tạo tiếng Việt có nhận biết hiệu lực văn bản

**Câu hỏi nghiên cứu.** RAG có mô hình hoá quan hệ sửa đổi/thay thế/bãi bỏ ở mức điều-khoản-điểm (đồ thị phiên bản) có giảm câu trả lời dựa trên quy định đã hết hiệu lực so với RAG thường và GraphRAG không có trục thời gian không?
Mức giảm này khác nhau thế nào giữa Gemini (API) và LLM mở 7-8B chạy cục bộ?

**Khoảng trống.**
- P1 dựng QA quy chế đại học nhưng coi 21 văn bản là tĩnh; không có câu hỏi "theo quy chế hiện hành", "khoá nhập học 2019 áp dụng quy chế nào".
- P3 chứng minh lỗi "staleness" và "recency bias" là thật và lọc phiên bản theo ngày giúp nhiều, nhưng cho luật Đức, chỉ LLM thương mại, 312 câu.
- P2 có "amendment tracing" cho quy định y tế tiếng Việt; chưa thấy cho giáo dục, và (theo abstract) không tách câu hỏi theo **mốc thời gian áp dụng** (khoá, năm học).
- Văn bản trường đại học có đặc thù chồng lớp: thông tư Bộ GD&ĐT, rồi quy chế trường "căn cứ" thông tư, rồi quyết định sửa đổi của trường; người hỏi thường là sinh viên khoá cũ chịu quy chế cũ. Đây là chỗ P3 không có.

**Dữ liệu.**
- Công khai (để công bố): lọc từ vietnamese-legal-documents các văn bản do Bộ GD&ĐT ban hành về đào tạo đại học (quy chế đào tạo, tuyển sinh, công tác sinh viên, chuẩn chương trình) cùng các văn bản sửa đổi/thay thế chúng.
  Trích quan hệ "sửa đổi, bổ sung", "thay thế", "bãi bỏ", "hết hiệu lực kể từ" bằng luật (regex trên phần "Điều khoản thi hành") + LLM kiểm, người duyệt mẫu.
  Sinh 500-1.000 câu hỏi có **mốc thời gian** theo ba loại kiểu P3 (sau sửa đổi, trước sửa đổi, nhiều điều khoản) cộng loại riêng: "căn cứ chéo" (quy chế trường dẫn thông tư).
  Người duyệt: chủ nhóm + 1 cán bộ phòng đào tạo, đo đồng thuận trên mẫu 100 câu.
- Nội bộ (không công bố): áp đúng pipeline lên kho 30.000 tệp của trường; báo cáo số liệu tổng hợp (tỷ lệ văn bản có quan hệ thay thế, tỷ lệ câu trả lời dùng bản hết hiệu lực trước/sau).
  Đặt câu hỏi thử từ log chatbot hiện tại **đã ẩn danh** (xem câu hỏi cho chủ nhóm).

**Baseline 1-2 tháng, GPU hạn chế.**
- Tháng 1: đồ thị phiên bản (node = điều/khoản, cạnh = sửa đổi/thay thế/căn cứ, thuộc tính = ngày hiệu lực) lưu SQLite/Neo4j; bộ câu hỏi công khai.
- Tháng 2: so 4 cấu hình × 2 LLM: (a) RAG BM25+dense, (b) RAG + lọc metadata ngày, (c) GraphRAG kiểu P2 không thời gian, (d) đồ thị phiên bản + lọc theo mốc áp dụng.
  LLM: Gemini (API đang dùng) và một LLM mở 7-8B 4-bit chạy cục bộ (ví dụ họ Qwen hoặc Llama; tên/phiên bản cụ thể chốt khi làm, chưa đánh giá ở đây). Embedding đa ngôn ngữ chạy CPU/GPU nhỏ.
- **Chỉ số**: độ đúng câu trả lời (người chấm + LLM-as-judge có hiệu chỉnh với người, như P3); **tỷ lệ dùng bản hết hiệu lực** (stale rate); tỷ lệ "recency bias" trên câu hỏi lịch sử; Recall@k mức điều khoản; độ đúng trích dẫn (số hiệu văn bản + điều).

**Ứng dụng/demo.** Sinh viên và chuyên viên phòng đào tạo hỏi "khoá K2020 được học vượt tối đa bao nhiêu tín chỉ?"; chatbot trả lời kèm số hiệu văn bản, điều khoản, **ngày hiệu lực**, và cảnh báo khi có bản mới hơn.
Gắn thẳng vào chatbot trường đang chạy (thay bước truy hồi).

**Nơi công bố.**
- ACM TALLIP (ACM Transactions on Asian and Low-Resource Language Information Processing), ISSN 2375-4699 — tồn tại đã kiểm qua Crossref (P4 đăng ở đây). Scopus: chưa tra.
- KSE (International Conference on Knowledge and Systems Engineering, IEEE) — tồn tại đã kiểm qua DOI 10.1109/KSE68178.2025.* của các bài ALQAC 2025. Scopus: chưa tra.
- ACIIDS (Springer) — tồn tại: P2 nhận ở ACIIDS 2026; Crossref thấy kỷ yếu "Recent Challenges in Intelligent Information and Database Systems" (Springer CCIS). Scopus: chưa tra.
- Tham vọng hơn: ICAIL hoặc NLLP Workshop (P3 ở ICAIL 2026; NLLP 2026 có DOI 10.18653/2026.nllp-1.*). Scopus: chưa tra.

**Điểm.**
| Tiêu chí | Điểm | Lý do |
|---|---|---|
| Tính mới | 4 | Trục thời gian cho QA giáo dục tiếng Việt chưa thấy; nhưng P3 và P2 đã có ý tưởng gần, phải phân biệt rõ. |
| Ứng dụng thực tiễn | 5 | Lỗi trả lời theo quy chế cũ là lỗi thật, gây hậu quả cho sinh viên; gắn được vào chatbot đang chạy. |
| Khả thi một người | 4 | Văn bản công khai có sẵn metadata ngày; phần khó là trích quan hệ sửa đổi và duyệt câu hỏi. |
| Khả năng công bố | 4 | Benchmark + phương pháp + so sánh API/cục bộ đủ cho TALLIP/KSE; rủi ro nếu ViHERMES mở rộng sang giáo dục trước. |
| Hợp hồ sơ NCS | 5 | Là bài 1 của chuỗi: benchmark có thời gian → phương pháp truy hồi → đánh giá triển khai (Đề tài 2) → mâu thuẫn văn bản. |
| **Tổng** | **22/25** | |

**Rủi ro chính.** Trích quan hệ sửa đổi tự động sai ở văn bản cấp trường (ghi chú "thay thế" không theo mẫu); bộ câu hỏi nhỏ bị chê; P2/P5 (cùng cộng đồng UIT/HCMUT) có thể ra bản giáo dục trước. Giảm rủi ro: đăng arXiv bộ dữ liệu sớm.

---

## Đề tài 2. Từ Gemini sang LLM cục bộ: đánh giá trích dẫn căn cứ và ảo giác của chatbot quy chế trên kho 30.000 tệp

**Câu hỏi nghiên cứu.** Trên kho văn bản hành chính thật quy mô 30k tệp, một pipeline cục bộ (OCR tiếng Việt + khử trùng lặp/gom phiên bản + truy hồi phân tầng văn bản→điều→khoản + LLM mở 7-8B) đạt bao nhiêu phần chất lượng của RAG + Gemini, xét **độ đúng trích dẫn căn cứ** và tỷ lệ ảo giác, với chi phí và rủi ro dữ liệu là bao nhiêu?

**Khoảng trống.**
- P4 cho thấy LLM nhỏ fine-tune làm được QA pháp luật tiếng Việt với tài nguyên ít, nhưng (theo abstract) trên dữ liệu luật sạch, không xét OCR, trùng lặp, phiên bản, và không chấm trích dẫn.
- P1 phải **gõ lại tay** văn bản dạng ảnh và đổi bảng thành đoạn văn cho 21 văn bản; cách này không mở rộng tới 30k tệp. Chưa thấy bài đo ảnh hưởng của lỗi OCR/bảng lên QA quy chế tiếng Việt.
- P5, P6 là benchmark kiến thức/hỏi đáp; không đánh giá hệ thống triển khai thật với người dùng thật và chi phí vận hành.

**Dữ liệu.**
- Nội bộ: 30k tệp trường (không công bố). Đo: tỷ lệ tệp cần OCR, tỷ lệ trùng lặp gần (MinHash), số cụm phiên bản; chỉ báo cáo số tổng hợp.
  Bộ câu hỏi nội bộ 300-500 câu lấy từ log chatbot đã ẩn danh + câu do cán bộ viết; nhãn đáp án + văn bản/điều khoản căn cứ.
- Công khai (để người khác tái lập): cùng pipeline chạy trên tập con Bộ GD&ĐT của vietnamese-legal-documents và trên ViRHE4QA (P1) để có số so sánh mở.
  OCR: thử trên bản PDF scan công khai của văn bản Bộ GD&ĐT (tự tải, chưa kiểm chứng số lượng sẵn có); vietnamese-legal-ocr chỉ dùng để kiểm tra nhanh vì là ảnh tổng hợp.

**Baseline 1-2 tháng, GPU hạn chế.**
- Tháng 1: pipeline nạp: trích văn bản (PDF số → text; PDF ảnh → OCR mã nguồn mở hỗ trợ tiếng Việt), tách cấu trúc Chương/Điều/Khoản/Điểm bằng regex, MinHash khử trùng lặp, gom phiên bản theo số hiệu + tiêu đề.
- Tháng 2: ma trận đánh giá: {chunk cố định, chunk theo điều khoản, truy hồi phân tầng} × {Gemini, LLM mở 7-8B 4-bit, LLM mở 3-4B}.
- **Chỉ số**: độ đúng câu trả lời (người chấm trên mẫu, LLM-judge hiệu chỉnh); **citation precision/recall** (trích đúng văn bản + điều); tỷ lệ câu không có căn cứ (ảo giác); Recall@k; độ trễ; chi phí/1.000 câu (API vs điện + phần cứng); tỷ lệ "từ chối đúng" khi kho không có câu trả lời.
- Thêm (tháng 3, tuỳ chọn): đánh giá người dùng thật A/B trên chatbot trường với log ẩn danh, cần chấp thuận của trường.

**Ứng dụng/demo.** Bản chatbot chạy hoàn toàn trong mạng trường (không gửi văn bản nội bộ ra API ngoài), cùng giao diện hiện có; bảng so sánh chất lượng/chi phí để lãnh đạo trường chọn cấu hình.
Bộ công cụ nạp kho (OCR + khử trùng lặp + tách điều khoản) dùng lại được cho trường khác.

**Nơi công bố.**
- ACM TALLIP — như trên (P4 là tiền lệ cùng chủ đề "LLM nhỏ cho QA pháp luật tiếng Việt"). Scopus: chưa tra.
- KSE (IEEE) — như trên. Scopus: chưa tra.
- ACIIDS (Springer) — như trên. Scopus: chưa tra.

**Điểm.**
| Tiêu chí | Điểm | Lý do |
|---|---|---|
| Tính mới | 3 | Đóng góp chủ yếu là đánh giá thực nghiệm trên kho thật; phương pháp từng phần đã biết. |
| Ứng dụng thực tiễn | 5 | Giải đúng vấn đề của trường: chi phí API, quyền riêng tư, chất lượng trích dẫn. |
| Khả thi một người | 4 | Chủ nhóm đã có kho và chatbot; OCR 30k tệp tốn thời gian nhưng không cần GPU lớn. |
| Khả năng công bố | 3 | Bài "đánh giá triển khai" khó vào venue mạnh nếu không công bố dữ liệu; cần phần công khai (ViRHE4QA + văn bản Bộ) để tái lập. |
| Hợp hồ sơ NCS | 4 | Là bài hệ thống/triển khai trong chuỗi; ghép với Đề tài 1 thành chương "từ phương pháp tới triển khai". |
| **Tổng** | **19/25** | |

**Rủi ro chính.** Reviewer chê không tái lập được vì kho nội bộ; xin chấp thuận dùng log người dùng có thể chậm; LLM mở tụt chất lượng tiếng Việt xa so với Gemini khiến kết luận chỉ là "chưa đủ tốt" (vẫn công bố được nếu đo kỹ).

---

## Tổng hợp

| Đề tài | Mới | Ứng dụng | Khả thi | Công bố | NCS | Tổng |
|---|---|---|---|---|---|---|
| 1. EduReg-Time (QA nhận biết hiệu lực) | 4 | 5 | 4 | 4 | 5 | **22** |
| 2. Gemini → LLM cục bộ, trích dẫn + ảo giác, kho 30k | 3 | 5 | 4 | 3 | 4 | **19** |

Khuyến nghị: làm **Đề tài 1 làm lõi** (bài công bố được với dữ liệu công khai), Đề tài 2 chạy song song trên kho trường vì dùng chung pipeline nạp và tách điều khoản.
Chuỗi NCS gợi ý (3-4 bài): (1) benchmark + đồ thị phiên bản (Đề tài 1) → (2) truy hồi phân tầng có thời gian, LLM cục bộ (Đề tài 2) → (3) phát hiện mâu thuẫn giữa quy chế trường và thông tư Bộ → (4) đánh giá với người dùng thật.

Điểm nối với `top5-de-tai.md` (RES-1): trục răng hàm mặt dùng RAG neo ontology cho chatbot nha khoa (#2). Hai hướng **dùng chung hạ tầng đánh giá** (citation precision/recall, LLM-judge hiệu chỉnh với người, LLM 7-8B 4-bit cục bộ) nhưng không trùng dữ liệu hay câu hỏi nghiên cứu. Không đề xuất gộp.

## Đã cân nhắc nhưng loại

- **Phát hiện mâu thuẫn giữa văn bản làm đề tài riêng ngay**: chưa tìm được bài tiếng Việt đã đọc để làm khoảng trống có căn cứ; để làm bài 3 của chuỗi sau khi đồ thị phiên bản (Đề tài 1) có sẵn.
- **Benchmark QA pháp luật tiếng Việt chung**: đã có P5 (172K câu) và P6 (10.450 mẫu); một người không cạnh tranh được về quy mô.
- **Fine-tune LLM riêng cho quy chế trường**: P4 đã làm cho luật chung; với dữ liệu nội bộ không công bố, bài khó tái lập. Giữ làm cấu hình phụ trong Đề tài 2.

## Câu hỏi cần chủ nhóm trả lời

1. Trường có cho phép dùng **log câu hỏi chatbot đã ẩn danh** để làm bộ đánh giá nội bộ và báo cáo số tổng hợp trong bài không? Ai ký chấp thuận?
2. Trong 30k tệp, ước lượng bao nhiêu phần là **PDF scan/ảnh** và bao nhiêu có bảng? Kho có lưu ngày hiệu lực/số hiệu dạng metadata hay chỉ trong nội dung?
3. Có cán bộ phòng đào tạo nào chịu **duyệt 100-200 câu hỏi** (đáp án + căn cứ + mốc thời gian) để đo đồng thuận không?
4. Máy chạy cục bộ có GPU gì (VRAM bao nhiêu)? Chi phí Gemini hiện tại mỗi tháng (để so sánh chi phí)?
5. Chủ nhóm có ràng buộc venue (danh sách tạp chí Scopus Q nào được tính cho hồ sơ NCS ở cơ sở đào tạo dự kiến) không?
