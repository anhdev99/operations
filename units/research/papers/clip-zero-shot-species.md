# Prompting Scientific Names for Zero-Shot Species Recognition (CLIP zero-shot)

- **Tác giả / năm / nơi:** Shubham Parashar, Zhiqiu Lin, Yanan Li, Shu Kong (2023).
- **Trích dẫn:** arXiv:2310.09929 (v1 15/10/2023). DOI https://doi.org/10.48550/arXiv.2310.09929 · link đã mở: https://arxiv.org/abs/2310.09929 (abstract).

## Bài toán
Dùng VLM kiểu CLIP (huấn trên web-scale image-text) để nhận dạng **loài** (birds/plants/animals) zero-shot. Vấn đề: prompt dùng **tên khoa học** (Latin/Greek, ví dụ "a photo of Lepus Timidus") thì CLIP yếu, vì tên đó hầu như không có trong training set của CLIP.

## Phương pháp
- So 2 chiến lược prompt: (a) dùng LLM sinh **mô tả** (màu, hình dạng) rồi nhét vào prompt → chỉ tăng nhẹ (marginal). (b) **dịch tên khoa học sang tên thường** (common name, ví dụ Lepus Timidus → "mountain hare") rồi prompt → common name dễ có trong training set của CLIP hơn.

## Số liệu chính (theo abstract)
- Prompt bằng common name đạt **2–5 lần accuracy** so với prompt bằng tên khoa học, trên benchmark fine-grained species recognition (nhiều dataset; con số exact per-dataset không ở abstract, chưa kiểm chứng).

## Hạn chế
- Kết luận "common name thắng" phụ thuộc **ngôn ngữ** (English common names trong training set CLIP). Với cây thuốc Việt Nam, common name tiếng Việt + tên khoa học cùng lúc → cần thử cả prompt tiếng Việt và tiếng Anh.
- Zero-shot, không fine-tune → không tận dụng được 62k ảnh ViMeLeaf; chỉ là baseline tham chiếu, không phải model cuối.

## Dùng được gì cho Bài 2
- Là baseline **CLIP zero-shot** để trả lời câu hỏi (1) "mô hình nào làm baseline". Cách đặt: đóng băng CLIP (hoặc OpenCLIP), prompt bằng cả tên khoa học + tên Việt (ví dụ "lá Dây giác" / "Dây giác leaf"), đo top-1/macro-F1 trên tập test ViMeLeaf mà **không train**.
- So với linear probe của BioCLIP/DINOv2 (frozen, có train head) để thấy: zero-shot có đủ mạnh không, hay cần ít nhất 1-5 shot.
- Khi đánh giá MLLM (GPT-4o/Gemini/Qwen-VL) zero-shot (xem tệp mllm-medicinal-plant-benchmark): CLIP zero-shot là mốc "rẻ, chạy local" để so chi phí/độ tin cậy.
