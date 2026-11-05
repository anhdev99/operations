---
name: morning-brief
description: Use when the user asks for the morning summary, today's overview, "hôm nay có gì", "tóm tắt sáng", or starts the day in the operations repo. Gathers teaching calendar, work due, PRs and mentions across the four roles into one HTML page.
---

# Morning brief

Gom tình hình 4 nơi vào một trang HTML để bạn đọc trong ~5 phút. **Chỉ đọc**, không ghi gì ra hệ thống ngoài.

## Quy trình

1. Chạy `python3 scripts/collect.py` (từ gốc repo). Đây là toàn bộ dữ liệu tự động: OpenProject và GitHub theo từng nơi, kèm `status` của từng nguồn.
2. Đọc `teaching/term-calendar.html` (lịch giảng dạy) và `shared/week-calendar.html` (khung giờ cố định). Lấy hôm nay và 7 ngày tới. Nếu bảng còn dòng ví dụ "Chưa nhập" thì ghi rõ chưa có lịch.
3. Dựng trang: `python3 scripts/collect.py | python3 scripts/render_brief.py > shared/morning-brief.html`. Script này dựng cảnh báo nguồn, từng nơi (OpenProject, GitHub) và mục chưa phân nơi.
4. Thay dấu `<!-- CALENDAR -->` trong `shared/morning-brief.html` bằng phần lịch bạn đọc ở bước 2: lịch dạy hôm nay, khối giờ cố định, 7 ngày tới, và **cảnh báo trùng giờ** nếu có. Nếu bảng còn dòng ví dụ "Chưa nhập" thì ghi "Chưa có lịch".
5. Nhìn lại trang: việc quá hạn và việc đến hạn ≤ 3 ngày phải dễ thấy; thiếu thì sửa HTML.
6. Báo lại đường dẫn tệp và tóm tắt 3–5 dòng trong chat.

## Luật

- Mỗi mục chỉ gồm **tiêu đề, hạn, nhãn và link**. Không chép nội dung ticket, mô tả hay tin nhắn (nguyên tắc tách bạch dữ liệu giữa các nơi).
- Phần của từng nơi nằm riêng một khối; không gộp nội dung nơi này vào nơi khác.
- Nguồn lỗi hoặc chưa cấu hình phải hiện ra trong trang, không được bỏ im.
- Không nói "xong" nếu `collect.py` chưa chạy thành công; báo đúng lỗi nếu có.
- Ngày tháng lấy từ `generated_at`, không đoán.
