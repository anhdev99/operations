# Selective Classification for Deep Neural Networks

Đề tài so sánh: **T2 / ViMeLeaf Bài 2** (nhận dạng cây thuốc nam dễ nhầm, đuôi dài, biết từ chối). Ngày đọc: 2026-11-26. Bài nền (foundational).

## Thông tin
- Tên: *Selective Classification for Deep Neural Networks*
- Tác giả: Yonatan Geifman, Ran El-Yaniv (Blavatnik National Center for Research, Technion)
- Năm: 2017 (arXiv 2017-05-23, v2)
- Nơi đăng: arXiv:1705.08500 — DOI arXiv: 10.48550/arXiv.1705.08500 (quy ước, chưa mở trang DOI). **Venue CVPR 2017** (rộng rãi biết; arXiv không có comment xác nhận, chưa kiểm chứng trang CVPR).
- Link: https://arxiv.org/abs/1705.08500 , toàn văn HTML: https://arxiv.org/html/1705.08500

## Vấn đề
Áp dụng **selective classification / reject option** (bài từ chối khi không chắc) vào DNN: cho một mạng đã train, sinh một bộ chọn lựa (selective classifier) mà người dùng đặt **mức rủi ro mong muốn** (target risk r*) và **độ tin cậy** δ; ở test, bộ này từ chối đủ ví dụ để bảo đảm rủi ro ≤ r* với xác suất ≥ 1−δ. Câu hỏi: dùng tín hiệu confidence-rate nào cho DNN?

## Phương pháp
- **Confidence-rate function** κ_f: X→R⁺ gán mỗi ảnh một điểm "tin cậy"; hai lựa chọn:
  - **SR (selective response)**: κ_f(x) = max_c f(x|c) = max softmax response (mục 4.2). Dùng chính xác theo ranking, không đòi xác suất tuyệt đối.
  - **MC-dropout**: uncertainty = phương sai của nhiều lần feed-forward có dropout ở lớp FC cuối (Gal & Ghahramani), κ_f(x) = −Var(p).
- **Thuật toán** (mục 3.5): input f, κ_f, δ, r*, tập train S_m. Binary search ngưỡng α theo κ_f để tìm selection function g_θ(x|κ_f) = f(x) nếu κ_f(x) ≥ α, từ chối nếu < α. Đảm bảo risk control với xác suất ≥ 1−δ (hàm số theo Hoeffding/empirical process).
- **Thước đo**: đường **risk–coverage** (risk là hàm của coverage = tỉ lệ ví dụ được giữ). "Area under the risk–coverage curve" (AURC) là đại lượng so sánh chất lượng (mục 4; thuật ngữ AURC chính thức hoá sau trong SelectiveNet 1901.09192).
- So sánh: SR và MC-dropout cho đường risk–coverage gần trùng trên CIFAR (Fig 2).

## Dữ liệu và kết quả
- CIFAR-10/100, MNIST, ImageNet.
- Số nổi bật (abstract): **2% error top-5 ImageNet được bảo đảm với xác suất 99.9%, ở ~60% test coverage**.
- Trên CIFAR, SR và MC-dropout "cực kỳ hiệu quả" (mục 5).

## Hạn chế
- Confidence-rate (softmax response / MC-dropout) **không ideal** — chỉ cho ranking hợp lý, không phải xác suất đúng (mục 4.1).
- Bảo đảm risk là **với xác suất** (không deterministc), phụ thuộc cỡ mẫu train m.
- Chưa có cơ chế conformal/calibration cho coverage (đó là hướng về sau).

## Liên quan ViMeLeaf Bài 2
- **(a) Định nghĩa thước đo**: bài này đặt nền **risk–coverage curve** + khái niệm AURC (area under risk–coverage) — chính là thước đo chuẩn cho P2. P2 nên báo **AURC + risk@coverage** (vd risk ở 80%/90% coverage) chứ không chỉ accuracy.
- **(b) Baseline từ chối**: SR (max softmax) và **MC-dropout** là 2 baseline "nền" nên chạy cho P2; thêm **energy** (từ 2605.08618) và **temperature scaling** (từ Geifman 1805.08206, chưa đọc trong lượt này).
- **(c) Khoảng trống còn P2 lấp**: bài này trên CIFAR/ImageNet (vision tổng quát), **không cây thuốc, không cặp dễ nhầm, không an toàn khi nhầm, không dữ liệu đuôi dài cây**. P2 mới ở (1) benchmark cặp loài cây thuốc dễ nhầm (Dây giác/Sục sạc), (2) risk–coverage trên tập đó, (3) OOD ảnh điện thoại.
- **(d) Nên thêm baseline**: SR + MC-dropout + energy + temperature scaling + conformal (2507.06867) làm lưới so sánh; đo AURC, risk@coverage, AUROC OOD (2605.08618).

## Dùng được gì
- Công thức risk–coverage + AURC làm thước đo chính P2.
- Thuật toán binary-search ngưỡng confidence theo target risk (mục 3.5) — tái lập được ngay cho bộ DINOv2/CLIP P2.
- SR + MC-dropout làm 2 baseline từ chối.
- Số đối chứng: 2% top-5 error @ 60% coverage (ImageNet) làm anchor "từ chối giảm rủi ro" cho P2.

## Mức chắc chắn
Đọc **toàn văn HTML arXiv** (mục 1–5, Fig 1–2, công thức 3, 6). Abstract khớp: CIFAR/ImageNet, 2% top-5 @ 99.9% prob / ~60% coverage. **Venue CVPR 2017 chưa kiểm chứng** (arXiv không có comment; cần mở trang CVPR/DBLP). MC-dropout theo Gal & Ghahramani (ref 9). AURC: bài dùng thuật ngữ "area under risk–coverage", ký hiệu AURC chính thức trong SelectiveNet.

## Ghi chú thêm
- Cùng tác giả với 1901.09192 (SelectiveNet) và 1805.08206 (bias-reduced uncertainty / temperature scaling). Ba bài này tạo nên "bộ ba nền" của hướng selective prediction; P2 nên trích đủ 3 khi định nghĩa thước đo + baseline.
- "chưa kiểm chứng": trang CVPR 2017 cho bài này.
