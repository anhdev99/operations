# Plant identification in an open-world (LifeCLEF 2016)

Đề tài so sánh: **T2 / ViMeLeaf Bài 2** (nhận dạng cây biết từ chối). Ngày đọc: 2026-11-26.

## Thông tin
- Tên: *Plant identification in an open-world (LifeCLEF 2016)*
- Tác giả: Herve Goeau, Pierre Bonnet, Alexis Joly
- Năm: 2016 (CLEF 2016; arXiv đăng lại 2025-09-25, v1)
- Nơi đăng: CLEF 2016 Conference and Labs of the Evaluation Forum (theo arXiv comment: "12 pages, 2 figures, CLEF 2016 ... Evora, Portugal"). arXiv:2509.20870 — DOI arXiv: 10.48550/arXiv.2509.20870.
- Link: https://arxiv.org/abs/2509.20870

## Vấn đề
Cuộc thi LifeCLEF plant identification: nhận dạng ảnh cây ở quy mô lớn (~110k ảnh, 1000 loài Tây Âu, từ nền tảng participatory sensing). Điểm mới 2016: đánh giá dưới dạng **open-set recognition** — hệ phải **bền với các lớp chưa từng thấy** và **tự động từ chối (reject) các hit dương sai do lớp lạ** (không phải chỉ phân loại closed-set).

## Phương pháp
- Tổng quan các hệ tham gia (overview paper): brute-force classification trên lớp train + cơ chế từ chối false positive.
- Không đề xuất 1 thuật toán riêng (bài là overview/evaluation), nên "phương pháp" = tập hợp các tiếp cận tham gia + cách đo open-set.

## Dữ liệu và kết quả
- Dữ liệu: >110K ảnh, 1000 loài, Tây Âu (nền tảng participatory sensing từ 2011).
- Kết quả: bài so sánh các hệ; không có số "đúng/sai" thống nhất trong abstract — "cung cấp phân tích kết quả chính" (đã mở abstract, chưa đọc lại bảng từng hệ — "chưa kiểm chứng" số chi tiết).

## Hạn chế
- Overview → không có số liệu thuật toán riêng để trích.
- 2016: trước era DINOv2/CLIP; các hệ khi đó dựa CNN nhỏ + gallery matching.
- Open-set ở đây = "lớp lạ" (unknown species), chưa phải "cặp dễ nhầm có nhãn an toàn".

## Liên quan ViMeLeaf Bài 2
- **(a) Tiền lệ open-set cây**: đây là **benchmark open-set cây đầu tiên đáng kể** (LifeCLEF 2016) — P2 **phải trích** làm tiền lệ "cây đã có open-set recognition", rồi nêu phần mới: (1) cây **thuốc** (không phải cây tự nhiên tổng quát), (2) **cặp dễ nhầm có nhãn an toàn** (Dây giác/Sục sạc), (3) OOD **ảnh điện thoại**, (4) đường **risk–coverage** (LifeCLEF đo recall/precision open-set, chưa phải risk–coverage + AURC).
- **(b) Khoảng trống P2 lấp**: LifeCLEF 2016 không đo "an toàn khi nhầm" (nhầm loài cây thuốc độc), không có benchmark cặp dễ nhầm, không dữ liệu Việt Nam/ĐNA. P2 lấp đúng chỗ đó.
- **(c) Rủi ro trùng**: **thấp** — khác miền (cây tự nhiên Tây Âu 1000 loài vs cây thuốc Việt ~165 loài + an toàn), khác thước đo (open-set recall/precision vs risk–coverage/AURC). Nhưng bắt buộc trích để reviewer không hỏi "sai khác LifeCLEF?".
- **(d) Baseline**: thêm "open-set gallery + reject" kiểu LifeCLEF làm baseline so với selective prediction (risk–coverage).

## Dùng được gì
- Tiền lệ open-set cây (trích bắt buộc).
- Khái niệm "reject false positive do lớp lạ" = gốc của từ chối open-set mà P2 kế thừa.
- Dataset LifeCLEF (110K/1000 loài) làm đối chứng quy mô nếu P2 cần so.

## Mức chắc chắn
Đọc **abstract + arXiv comment (CLEF 2016)**. **Chưa đọc lại toàn văn bảng kết quả từng hệ** → số cụ thể "chưa kiểm chứng". Dataset số (110K/1000 loài) lấy từ abstract.

## Ghi chú thêm
- Bài cũ (2016) nhưng là cột mốc "cây + open-set"; P2 khác ở an toàn + cây thuốc + risk–coverage + OOD điện thoại.
