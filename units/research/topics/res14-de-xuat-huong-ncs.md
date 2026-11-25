# Đề xuất hướng nghiên cứu NCS từ tài sản sẵn có

Issue: RES-14. Người tổng hợp: Dean. Ngày: 2026-11-25.
Nguồn: `brief-university-docs-chatbot.md` (RES-19, làm lại RES-15), `brief-medicinal-plants.md` (RES-16), `brief-dental-2d-to-3d.md` (RES-17),
phản biện của Critic `review-res14.md` (RES-18, nhánh `agent/RES-18`). Các dữ kiện chủ nhóm trả lời trong RES-14 đều đã đưa vào.

## Quy ước kiểm chứng

- Chỉ dùng bài mà Scholar đã mở (abstract hoặc toàn văn) và Critic không đánh ✗. Critic kết luận: không có lỗi nặng, giữ cả 3 brief (RES-17 sửa cách đo "99%").
- Dean tự kiểm lại các trích dẫn chính ngày 2026-11-25 (arXiv API, Crossref; tiêu đề khớp):
  R2GQA 2409.02840, ViHERMES 2602.07361, "Asking For An Old Friend" 2605.23497, Barz & Denzler 1902.00423,
  NeBLa 2304.04027, X-Splat 2607.02099, PX2Tooth 2411.03725, TCMP-300 (DOI 10.1038/s41597-025-05522-7, Scientific Data), ACM TALLIP DOI 10.1145/3732938.
- **Chưa kiểm chứng**: trạng thái Scopus/SJR của mọi nơi công bố; VNPlant-200; bài FAIR 2025 của chủ nhóm (chưa tìm được tên); quy định đạo đức y sinh Việt Nam.
- Điểm 1-5: Mới, ƯD (ứng dụng), KT (khả thi cho một người), CB (khả năng công bố), NCS (hợp chuỗi bài NCS). Điểm lấy từ brief; Critic giữ nguyên.

## Tài sản của chủ nhóm và ràng buộc

| Tài sản | Dữ kiện | Ràng buộc |
|---|---|---|
| Văn bản trường + chatbot trung tâm | >30.000 tệp PDF/Word; chatbot RAG + Gemini | **Không được công bố** dữ liệu làm benchmark |
| Dataset cây thuốc nam | 100 loài, ~50.000 ảnh tự chụp, nhiều ảnh trùng; đã có bài FAIR 2025 + luận văn ThS | **Được phép công bố ảnh** |
| Răng 2D→3D | Mới là ý tưởng | Chưa có phòng khám hợp tác, chưa có dữ liệu, cần chấp thuận đạo đức |

## Bảng xếp hạng 8 đề tài ứng viên

| # | Đề tài | Brief | Mới | ƯD | KT | CB | NCS | Tổng |
|---|---|---|---|---|---|---|---|---|
| 1 | **EduReg-Time**: hỏi đáp quy chế đào tạo tiếng Việt biết hiệu lực văn bản (đồ thị phiên bản sửa đổi/thay thế) | RES-19 Đ1 | 4 | 5 | 4 | 4 | 5 | **22** |
| 2 | Nhận dạng cây thuốc nam dễ nhầm bằng mô hình nền, ảnh ngoài thực tế, từ chối khi không chắc | RES-16 B | 4 | 4 | 4 | 4 | 5 | **21** |
| 3 | KG cây thuốc nam + GraphRAG tiếng Việt có cảnh báo an toàn, ảnh làm đầu vào | RES-16 C | 4 | 5 | 3 | 4 | 5 | **21** |
| 4 | Ảnh điện thoại trong miệng → răng 3D, đo sai số mm so với scan | RES-17 Đ2 | 4 | 5 | 4 | 4 | 4 | **21** |
| 5 | **VNMedPlant-Clean**: data paper ảnh cây thuốc đã khử trùng, split chống rò rỉ, đo độ thổi phồng accuracy | RES-16 A | 3 | 3 | 5 | 4 | 5 | **20** |
| 6 | Panoramic → răng hàm 3D có bản đồ độ tin cậy, huấn luyện trên cặp mô phỏng từ CBCT công khai | RES-17 Đ1 | 3 | 4 | 4 | 4 | 5 | **20** |
| 7 | Gemini → LLM mở cục bộ: trích dẫn căn cứ và ảo giác trên kho 30k tệp | RES-19 Đ2 | 3 | 5 | 4 | 3 | 4 | **19** |
| 8 | Ghép ảnh điện thoại (thân răng) + panoramic (chân răng) | RES-17 Đ3 | 4 | 4 | 2 | 3 | 5 | **18** |

Điểm số chỉ là một căn cứ. Thứ tự **làm** phụ thuộc phụ thuộc dữ liệu: #5 điểm thấp nhưng là điều kiện của #2 và #3 (chưa khử trùng thì mọi con số sau đều bị phản biện bác).

## Điểm chung của cả ba nguồn: "độ tin cậy"

Ba brief độc lập cùng chỉ ra một kiểu lỗi: **hệ thống báo con số đẹp nhưng sai ở chỗ người dùng không thấy**.
- Văn bản trường: chatbot trả lời trôi chảy theo **quy chế đã hết hiệu lực** (lỗi "staleness" và "recency bias" đã được đo cho luật Đức, arXiv 2605.23497; chưa thấy cho văn bản giáo dục tiếng Việt).
- Cây thuốc nam: accuracy 84-93% của các bộ ảnh tự thu có thể bị **thổi phồng do ảnh trùng giữa train và test** (đã chứng minh ở CIFAR, arXiv 1902.00423; chưa thấy ai đo cho cây thuốc). Nhầm loài thuốc có thể gây hại.
- Răng 2D→3D: "99%" không phải chỉ số; từ một ảnh panoramic, mức công bố là IoU 0,68-0,79 hoặc Dice răng ~0,82. Cách trung thực là đo **sai số mm theo vùng + bản đồ độ tin cậy**.

Đây là sợi chỉ để kể câu chuyện hồ sơ NCS: *AI đáng tin cậy cho ứng dụng tiếng Việt: biết căn cứ, biết hiệu lực, biết khi nào không chắc.*

## Khuyến nghị

### Trục luận án chính: hỏi đáp có căn cứ trên tri thức miền chuyên biệt tiếng Việt

Gồm hai miền chủ nhóm đã có dữ liệu, dùng chung một hạ tầng (đồ thị tri thức, RAG/GraphRAG, LLM mở chạy cục bộ, chấm trích dẫn căn cứ, LLM-judge hiệu chỉnh với người):

| Thứ tự | Bài | Đề tài | Vì sao ở vị trí này | Thời gian ước tính |
|---|---|---|---|---|
| 1 | Bài nhanh | **#5 VNMedPlant-Clean** (data paper) | Dữ liệu sẵn, được công bố, tính toán nhẹ (GPU 8 GB); là nền cho #2, #3 | ~6 tuần |
| 2 | Bài lõi 1 | **#1 EduReg-Time** | Điểm cao nhất; công bố được dù kho trường không công bố (bộ đánh giá dựng từ văn bản Bộ GD&ĐT công khai); gắn thẳng vào chatbot đang chạy | 2-3 tháng |
| 3 | Bài lõi 2 | **#3 KG cây thuốc nam + GraphRAG an toàn** | Cùng phương pháp với #1, miền thứ hai; khoảng trống rõ (TCM, Ayurveda đã có KG, Việt Nam chưa thấy) | 2-3 tháng, cần chuyên gia dược duyệt |
| 4 | Bài hệ thống | **#7 triển khai cục bộ trên kho 30k** (hoặc #2 nếu thiên về CV) | Đánh giá triển khai thật: chất lượng, chi phí, quyền riêng tư | 2 tháng, chạy song song với #1 |

Lý do chọn trục này thay vì trục răng hàm mặt: chủ nhóm **đã có dữ liệu và người dùng thật** ở cả hai miền, không phụ thuộc đối tác bên ngoài, và hai miền khác nhau giúp bài có tính tổng quát (một khung, kiểm chứng trên hai miền).

### Hướng răng 2D→3D: dự án song song, không làm trục chính lúc này

- Bắt đầu bằng **#6 (panoramic → 3D có bản đồ tin cậy)** trên dữ liệu công khai (ToothFairy3, CC BY-NC-SA 4.0). #6 nối thẳng với đề tài #1 của RES-1 (báo cáo panoramic tiếng Việt), và panoramic là ảnh phòng khám nào cũng có. #4 (ảnh điện thoại) chạy song song nếu còn sức.
- Sau ~3 tháng mang demo + **gói đề xuất cho phòng khám** (đã soạn sẵn trong `brief-dental-2d-to-3d.md`: phòng khám được gì, cần cung cấp gì, quy trình đạo đức, dữ liệu không rời phòng khám).
- Nếu có phòng khám có CBCT hoặc máy scan trong miệng, hướng này có thể thành **trục NCS thứ hai** hoặc thay trục chính khi đó. Khi chưa có thì không nên đặt cả luận án vào nó.
- Mục tiêu nên viết lại: thay "99%" bằng "≥ X% số răng có sai số bề mặt < Y mm, có bản đồ độ tin cậy". X và Y phải hỏi bác sĩ theo mục đích dùng (tư vấn khác với cắm implant).

## Lộ trình 12 tháng đề xuất

| Tháng | Trục chính | Song song |
|---|---|---|
| 1-2 | #5: khử trùng 50k ảnh, đo tỉ lệ trùng, split chống rò rỉ, baseline 3 seed, datasheet, Zenodo | #1: thu văn bản Bộ GD&ĐT công khai, trích quan hệ sửa đổi/thay thế |
| 3-4 | Nộp #5. #1: đồ thị phiên bản, bộ câu hỏi có mốc thời gian, so 4 cấu hình × 2 LLM | #6: bộ mô phỏng panoramic từ CBCT công khai |
| 5-6 | Nộp #1 (arXiv sớm để giữ ưu tiên) | #7: pipeline nạp kho 30k (OCR, khử trùng, tách điều khoản), chạy nội bộ |
| 7-9 | #3: KG 100 loài + GraphRAG an toàn, chuyên gia dược duyệt | #6 xong demo → đi đề xuất phòng khám |
| 10-12 | Nộp #3; viết #7 hoặc #2 | Nếu có phòng khám: hồ sơ đạo đức, kiểm chứng thật |

## Rủi ro chính

- **Trùng lặp với bài FAIR 2025 / luận văn**: data paper #5 phải trích bài cũ và nêu rõ phần mới (khử trùng, split, đo thổi phồng). Cần tên và nội dung bài cũ.
- **Đối thủ cùng cộng đồng**: ViHERMES (2602.07361) đã có "amendment tracing" cho quy định y tế tiếng Việt; có thể mở rộng sang giáo dục trước. Giảm rủi ro: đăng arXiv bộ dữ liệu #1 sớm.
- **Sau khử trùng còn ít ảnh/loài**: chưa biết tỉ lệ trùng; đo ngay ở tháng 1. Nếu ít, kết quả "độ thổi phồng lớn" lại chính là phát hiện.
- **Chi phí**: nhiều nơi nhận data paper thu APC (Data in Brief ~1.220 USD, Scientific Data ~2.490 USD theo OpenAlex, chưa kiểm lại). Mọi khoản phí cần board duyệt; nếu không có ngân sách, ưu tiên hội nghị Scopus hoặc tạp chí không phí.
- **Scopus chưa tra** cho bất kỳ nơi nào; chủ nhóm tra lại theo danh sách được tính ở cơ sở đào tạo dự kiến.

## Nơi công bố ứng viên (tồn tại đã kiểm; Scopus chưa tra)

- Văn bản trường (#1, #7): ACM TALLIP; KSE (IEEE); ACIIDS (Springer); tham vọng hơn: ICAIL, NLLP Workshop.
- Cây thuốc (#5, #2, #3): Data in Brief; Scientific Data; Ecological Informatics; Frontiers in Plant Science (nơi đăng các bài nhận dạng cây thuốc 2026).
- Răng (#6, #4): Computers in Biology and Medicine; IEEE JBHI; Dentomaxillofacial Radiology.

## Việc tiếp theo cần chủ nhóm quyết định

1. **Chọn trục**: đồng ý trục chính "hỏi đáp có căn cứ trên tri thức tiếng Việt" (văn bản trường + cây thuốc) và răng 2D→3D làm song song? Hay muốn đặt răng làm trục chính?
2. **Bắt đầu #5 ngay?** Nếu đồng ý, Dean tạo issue cho Builder: thống kê trùng lặp và dựng split chống rò rỉ. Cần biết ảnh đang nằm ở đâu trên máy và được phép đặt bản sao làm việc ở thư mục nào (ảnh không đưa vào git).
3. Tên/link bài FAIR 2025 và luận văn; ảnh có metadata (ngày, nơi chụp, thiết bị) không; 100 loài đã có tên khoa học và chuyên gia xác nhận chưa.
4. GPU (loại, VRAM); có ngân sách APC không.
5. Trường có cho dùng log chatbot đã ẩn danh để đánh giá nội bộ không; có cán bộ phòng đào tạo duyệt 100-200 câu hỏi không.

Câu hỏi chi tiết hơn cho từng hướng nằm ở cuối mỗi brief.

## Quyết định của chủ nhóm (2026-11-25)

- **Hướng răng 2D→3D: chưa làm.** Gói đề xuất cho phòng khám vẫn giữ trong brief để dùng sau.
- **Bắt đầu data paper cây thuốc (VNMedPlant-Clean) ngay**: giao Builder ở RES-26. Lượt đầu dựng pipeline khử trùng và split chống rò rỉ, kiểm thử trên dữ liệu giả.
- Thông tin còn thiếu (thư mục ảnh, tên bài FAIR 2025, GPU, ngân sách APC) chủ nhóm sẽ gửi sau. Khi có đường dẫn ảnh thì chạy pipeline trên dữ liệu thật.
- Trục chính theo khuyến nghị: hỏi đáp có căn cứ trên tri thức tiếng Việt, gồm văn bản trường và cây thuốc nam. EduReg-Time là bài lõi tiếp theo.
