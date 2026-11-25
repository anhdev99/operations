# Nghiên cứu khoa học

Nơi này chỉ tập trung vào **nghiên cứu**: đọc tài liệu, chọn đề tài, làm thí nghiệm, viết bài. Chưa gắn với cơ sở đào tạo, người hướng dẫn hay hạn nộp hồ sơ; khi có thì ghi thêm, không chặn việc nghiên cứu.
Định hướng: nghiên cứu để **ứng dụng thực tiễn** (có demo/sản phẩm chạy được), và công bố bài báo, làm nền cho hồ sơ NCS sau này.

## Năm hướng

1. Ontology (biểu diễn tri thức, knowledge graph, suy luận)
2. Cảm xúc (emotion recognition / affective computing)
3. Computer vision
4. Chatbot (LLM, RAG, hội thoại)
5. Y tế, mảng răng hàm mặt (ảnh X-quang/CBCT, hỗ trợ chẩn đoán, hỏi đáp lâm sàng)

Điểm giao nên ưu tiên: CV + răng hàm mặt; chatbot + ontology y khoa (RAG trên knowledge graph); cảm xúc + chatbot (hội thoại đồng cảm cho bệnh nhân).

## Lộ trình nghiên cứu

1. **Khảo sát**: mỗi hướng một tổng quan trong `topics/`, đọc bài ghi vào `papers/`.
2. **Thu hẹp**: chọn 1-2 đề tài chính từ các điểm giao, nêu rõ khoảng trống và ứng dụng.
3. **Thí nghiệm**: mã và kết quả trong `experiments/`, có baseline và số liệu tái lập được.
4. **Viết bài**: `writing/<tên-bài>/`, nhắm hội nghị/tạp chí phù hợp (chọn sau khi có kết quả).

## Cấu trúc thư mục

- `topics/<hướng>.md` — tổng quan, câu hỏi nghiên cứu, khoảng trống, dataset, ứng dụng.
- `papers/` — mỗi bài một tệp: vấn đề, phương pháp, kết quả, hạn chế, dùng được gì.
- `experiments/` — thí nghiệm, mã, cấu hình (dữ liệu lớn/bệnh nhân không đưa vào git).
- `writing/` — bản thảo, mỗi bài một thư mục.

## Quy tắc

- Dữ liệu y tế/bệnh nhân: ẩn danh, có chấp thuận đạo đức; không đưa vào repo, chat hay commit.
- Chỉ trích dẫn bài đã kiểm chứng tồn tại (DOI/link); không bịa tài liệu tham khảo.
- GitHub: org `anhdev99-research-lab`. Mỗi bài báo hoặc đề tài là một repo **private** riêng (nhánh `develop` và `main`); thư mục này giữ ghi chú chung và khảo sát. Chưa có OpenProject/Slack.
- Không đưa nội dung nơi này sang các `units/` khác.

## Chưa biết, không bắt buộc ngay

GPU và dữ liệu răng hàm mặt có sẵn, số giờ mỗi tuần dành cho nghiên cứu.
