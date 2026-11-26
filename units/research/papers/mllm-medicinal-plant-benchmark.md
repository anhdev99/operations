# Benchmarking multimodal LLMs for medicinal plant identification (Jiang 2026)

- **Tác giả / năm / nơi:** Yue Jiang, Zhenzhong Dai, Wen Jin, Weinan Lin, Yijun Xu, Jiangda Wang, Zhaoxi Fang (Shaoxing University + Univ. of South Africa), 2026. Frontiers in Plant Science, vol. 17 (Data Report).
- **Trích dẫn:** DOI https://doi.org/10.3389/fpls.2026.1765281 · link đã mở: https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2026.1765281/full (full text, lượt này).

## Bài toán
Đánh giá hệ thống 5 MLLM chính (GPT-4o, Llama4Scout, Gemma3-27B, Qwen3-VL-235B, DeepSeek-VL2) trong nhận dạng ảnh cây thuốc, format **trắc nghiệm 4 lựa chọn**.

## Phương pháp
- Dữ liệu: **880 ảnh cây thuốc riêng** (copyright CNBLOG), chọn **200 ảnh / 68 loài** làm test (sampling tầng, khử trùng + near-duplicate thủ công; nhãn có chuyên gia kiểm tra).
- Mỗi ảnh: 1 loài đúng + **3 distractor là loài cây thuốc thật** (không phải bịa). Tên chỉ dùng **common name tiếng Trung**, không Latin/English.
- Chạy qua **API công khai, default params** (temperature/top-p/max-tokens/seed cố định), cùng prompt template; model chỉ trả nhãn A/B/C/D, không sinh lý do.
- Phân tích theo 7 bộ phận (lá/hoa/rễ/cành/quả...) + top-10 loài hay sai nhất.

## Số liệu chính (đọc trực tiếp full text)
| Model | Accuracy |
|---|---|
| Qwen3-VL-235B | **90,50%** |
| GPT-4o | 85,00% |
| Gemma3-27B | 65,50% |
| Llama4Scout | 58,50% |
| DeepSeek-VL2 | 58,00% |

- **Hoa (flower)**: Qwen3-VL-235B đạt 100% (đặc trưng hoa dễ phân biệt). **Rễ/sỏi (root/rhizome)**: accuracy thấp nhất chung (loài giống nhau cao về hình thái).
- **Top-3 loài sai 100%: *Anoectochilus roxburghii*, *Salvia przewalskii*, *Berberis* spp.** — cùng họ/cùng chi, chỉ khác nhẹ hình dạng lá + gân → đúng hiện tượng "cặp dễ nhầm". 7 loài tiếp theo (Lemna minor, Sophora tonkinensis, Dictamnus dasycarpus, Dipsacus asperoides, Anisomeles indica, Rhodomyrtus tomentosa, Sauropus spatulifolius) **sai 80%**. 36 loài (ví dụ *Artemisia annua*) đạt 100% mọi model.

## Hạn chế (tự nêu trong Discussion)
- Format 4-lựa chọn **nhanh đơn giản hơn open-set thật**; **không có** kiểm định thống kê, confidence interval, **không so với baseline CV truyền thống** (ResNet/EfficientNet/ViT/Swin fine-tune).
- Dữ liệu riêng (không công khai), tên chỉ common name tiếng Trung → khó so với cây thuốc Việt Nam (tên Việt + khoa học).
- Không đo **calibration / từ chối (abstain)** — chỉ đúng/sai theo chọn lựa.

## Dùng được gì cho Bài 2 (gắn trực tiếp)
- **Trả lời câu hỏi (2) "MLLM có xu hướng tự tin sai không?":** Có bằng chứng. MLLM đạt 85–90,5% tổng thể (4-lựa chọn) nhưng **sai 100% trên các loài cùng họ/cùng chi khó phân biệt** — tức đúng "confidently wrong trên cặp dễ nhầm". Đây là nền để Bài 2 đặt **từ chối/calibration** làm trục chính: MLLM raw không biết "mình đang ở cặp nguy hiểm" → phải có cơ chế selective/abstain.
- **Đối chứng MLLM cho Bài 2:** dùng lại setup này (hoặc tự chạy GPT-4o/Gemini/Qwen trên 10–20 cặp ViMeLeaf dễ nhầm) làm baseline "MLLM zero-shot", so với BioCLIP/DINOv2 linear probe + từ chối.
- **Cảnh báo (B9 trong brief-novelty):** từ chối không tự động an toàn (automation bias). MLLM sai 100% trên cặp giống nhau → khi nó từ chối, người dùng có bỏ sót cảnh báo độc không? Bài 2 phải đo hiệu ứng này, không chỉ AURC.
