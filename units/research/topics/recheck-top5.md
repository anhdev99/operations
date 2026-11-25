# Kiểm lại top 5 đề tài (độc lập)

Ngày: 2026-11-25. Bản cũ: `top5-de-tai.md` (RES-8). Bản kiểm: 5 tệp `verify-t1..t5-*.md` cùng thư mục (mỗi tệp có bảng ✓/⚠/✗, link và trích đoạn gốc).
Người kiểm tự mở nguồn, không dựa vào bản mô tả cũ. Mọi điểm 1-5: Mới / ƯD / KT / CB / NCS.

## Kết quả

| # | Đề tài | Điểm cũ | Điểm sau kiểm | Thay đổi chính | Tệp kiểm |
|---|---|---|---|---|---|
| 1 | Báo cáo panoramic tiếng Việt, detector + VLM nhỏ | 22 | **18-19** (Mới 4→2) | Bài Boulesnane 2026 (Electronics) đã làm gần đúng pipeline | verify-t1-panoramic.md |
| 2 | Chatbot nha khoa neo ontology OHD | 22 | **19** (KT 3→2) | Không bài nào gộp OHD+RAG+tiếng Việt, nhưng thiếu nha sĩ thì không có chuẩn vàng | verify-t2-ohd-chatbot.md |
| 3 | ViEmpath-Dental | 21 | **17** | Có bài đồng cảm cho bệnh nhân lo lắng + fine-tune; không có bác sĩ thì mất nửa câu hỏi | verify-t3-empathy-dental.md |
| 4 | ViText2KG | 21 | **17** | Có LettrIA (ISWC 2025); dịch + chạy LLM chưa đủ; giấy phép dữ liệu gốc ràng buộc | verify-t4-vitext2kg.md |
| 5 | Đau từ video mặt, chéo dataset | 20 | **17** | ErAS-Net đã làm UNBC→BioVid; cần xin dữ liệu | verify-t5-pain-video.md |

## Nhận xét chung

1. Bảng cũ xếp cao hơn thực tế ở cả 5 đề tài (giảm 2-5 điểm). Trích dẫn cốt lõi đều có thật; thứ giảm là tính mới (bài mới xuất hiện) và khả thi (thiếu nha sĩ).
2. Top 5 được chấm trước khi biết tài sản của bạn (dataset cây thuốc, chatbot văn bản trường, chưa có phòng khám). #1-#3 cần nha sĩ.
3. Điểm kiểm cũng chỉ là ước lượng của agent; **tất cả lần kiểm đều bị giới hạn** vì OpenAlex hết hạn mức, arXiv trả 429, Google Scholar và Scopus chưa tra, nhiều bài chỉ đọc abstract. Xem mục "Chưa kiểm" ở từng tệp verify.
4. Danh sách 8 đề tài của RES-14 (`res14-de-xuat-huong-ncs.md`) dựa trên tài sản thật của bạn; Dean tự kiểm trích dẫn chính ở đó nhưng chưa có người phản biện độc lập mức đề tài như lần này.
