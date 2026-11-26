# SelectiveNet: A Deep Neural Network with an Integrated Reject Option

Đề tài so sánh: **T2 / ViMeLeaf Bài 2**. Ngày đọc: 2026-11-26. Bài nền (foundational).

## Thông tin
- Tên: *SelectiveNet: A Deep Neural Network with an Integrated Reject Option*
- Tác giả: Yonatan Geifman, Ran El-Yaniv
- Năm: 2019 (arXiv 2019-01-26, v4)
- Nơi đăng: arXiv:1901.09192 — DOI arXiv: 10.48550/arXiv.1901.09192. **arXiv comment: "Accepted to ICML 2019"** (đã đọc trong arXiv API).
- Link: https://arxiv.org/abs/1901.09192

## Vấn đề
Các cơ chế từ chối hiện có dựa **ngưỡng trên confidence** của mạng pre-trained (post-hoc). SelectiveNet thay vào đó: **train end-to-end một kiến trúc có sẵn reject option**, tối ưu đồng thời classification + rejection trên miền covered (không phải threshold post-hoc).

## Phương pháp
- Kiến trúc: thêm nhánh "reject" vào DNN; loss tổng hợp = loss phân loại (trên miền covered) + loss cho việc từ chối, train cùng lúc.
- Tối ưu "over the covered domain" → đường **risk–coverage trade-off** tốt hơn ngưỡng-naive.
- So sánh: "consistently improved risk–coverage trade-off ... new state-of-the-art for deep selective classification".

## Dữ liệu và kết quả
- Nhiều dataset classification + regression (CIFAR, ImageNet, UCI theo bài). Kết quả: SOTA risk–coverage lúc đó (abstract; chưa mở lại bảng số cụ thể trong lượt này — "chưa kiểm chứng" số từng bảng).

## Hạn chế
- Train end-to-end cần sửa kiến trúc + mất thời gian train so với post-hoc threshold (nhanh hơn cho thử baseline).
- Số liệu cụ thể từng dataset chưa đối chiếu lại (chưa mở HTML/PDF bảng kết quả trong lượt này).

## Liên quan ViMeLeaf Bài 2
- **(a) Trùng với giả thuyết P2**: SelectiveNet làm selective classification **tổng quát**, không cây, không an toàn. P2 không trùng; mượn ý tưởng "reject option tích hợp".
- **(b) Khoảng trống P2 lấp**: P2 = benchmark cặp cây thuốc dễ nhầm + đường risk–coverage + OOD điện thoại + (có thể) reject option tích hợp cho mạng cây (DINOv2/CLIP adapter). SelectiveNet cho hướng "từ chối được train cùng, không phải threshold hậu-giám" nếu P2 muốn so với threshold-naive.
- **(c) Rủi ro trùng**: thấp. P2 phải trích SelectiveNet + 1705.08500 như nền, rồi nêu phần mới (miền cây thuốc + an toàn + OOD).
- **(d) Baseline**: thêm "SelectiveNet-style end-to-end reject" làm 1 baseline so với SR/MC-dropout/energy/conformal (post-hoc).

## Dùng được gì
- Hướng "reject option tích hợp vào loss" làm baseline nâng cao cho P2 (nếu so với ngưỡng-naive).
- Xác nhận **AURC / risk–coverage** là cách so sánh chuẩn (nối tiếp 1705.08500).

## Mức chắc chắn
Đọc **abstract + arXiv comment** (ICML 2019) + danh mục. **Chưa mở lại toàn văn/bảng kết quả** trong lượt này → số "SOTA risk–coverage" ghi "chưa kiểm chứng chi tiết từng bảng". Cần mở https://arxiv.org/abs/1901.09192 HTML/PDF trước khi trích số cụ thể.

## Ghi chú thêm
- Cùng "bộ ba nền" với 1705.08500 + 1805.08206. P2 nên trích đủ khi định nghĩa AURC + lưới baseline.
