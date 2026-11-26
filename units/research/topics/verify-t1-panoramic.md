# Phản biện độc lập đề tài #1 (panoramic tiếng Việt, detector + VLM nhỏ đóng băng)

Ngày kiểm: 2026-11-25. Người kiểm: Critic (độc lập, tự mở nguồn gốc). Đối tượng: mục 1 của `top5-de-tai.md`.
Ký hiệu: ✓ khớp, ⚠ lệch hoặc chưa đủ chứng cứ, ✗ không tìm thấy. Chỉ ghi điều đã mở và đọc.

## 1. Bài và dataset được trích

| Bài / dataset | Link | Kết quả | Trích đoạn gốc (ngắn) và ghi chú |
|---|---|---|---|
| MMOral / OralGPT, Hao J. et al., 2025 | https://arxiv.org/abs/2509.09254 | ✓ tồn tại; ⚠ một số liệu lệch giữa các bản | arXiv API: tác giả đầu Jing Hao, ngày 2025-09-11. "MMOral consists of 20,563 annotated images paired with 1.3 million instruction-following instances" ✓. arXiv v1: "GPT-4o, only achieves 41.45% accuracy" ✓. **Nhưng** bản NeurIPS 2025 (Datasets and Benchmarks Track) ghi "GPT-4o, only achieves 43.31% accuracy" → nên trích 43,31% (bản đã công bố) hoặc nêu rõ bản arXiv v1. OralGPT = SFT trên Qwen2.5-VL-7B ✓ ("cần VLM 7B fine-tune" đúng). NeurIPS: https://proceedings.neurips.cc/paper_files/paper/2025/hash/3797b3a3c939156757857cf1b9afde3c-Abstract-Datasets_and_Benchmarks_Track.html |
| OPGAgent, Yu Z. et al., 2026 | https://arxiv.org/abs/2603.00462 | ✓ | Tác giả đầu Zhaolin Yu, 2026-02-28. "(Location, Field, Value) triples ... review of findings and hallucinations" ✓. "Code will be released upon acceptance" ✓ (theo v1). Ý "không tiếng Việt": abstract không nói ngôn ngữ, chưa xác nhận (suy đoán hợp lý). Có tầng tooth-level, dùng detector. |
| AgenTeeth, Rafid A. et al., 2026 | https://arxiv.org/abs/2609.17800 | ✓ | Ahmed Rafid đầu, 2026-09-15. "improves four backbone VLMs by 12.9-23.0 percentage points" ✓ (trên MMOral-OPG-Bench). "frozen Qwen2.5-VL-7B-Instruct with AgenTeeth reaches 48.11%" . Trọng tâm "Suppressing Hallucination in Frozen VLMs" — **gần hơn mô tả**: bài là chống ảo giác cho VLM đóng băng, abstract chỉ nói VQA, không thấy sinh báo cáo. Chưa đọc toàn văn để xác nhận có thử mô hình ≤4B hay không. |
| PanDent, Li X. et al., 2026 | https://arxiv.org/abs/2607.27378 | ✓ | Xiaohan Li đầu, 2026-07-29. "Current models generate fluent reports but exhibit substantial errors in fine-grained localization and tooth-level diagnosis" ✓. "Full data will be released upon publication" ✓. Abstract ghi 9.554 ảnh (9.049 train công khai + 505 ca in-house); một kết quả tìm kiếm ghi 9.524, lệch, tin abstract. Có mẫu 100 ca: https://huggingface.co/datasets/Desperado1103/Pandent_Sample (gated manual, license: other). Ngôn ngữ: abstract không nói, "chỉ tiếng Anh" chưa xác nhận. |
| DENTEX | https://huggingface.co/datasets/ibrahimhamamci/DENTEX | ✓ | Không gated; license cc-by-nc-sa-4.0; dung lượng 11.844.669.860 byte (≈11,8 GB) ✓. README: "693 X-rays ... quadrant", "634 ... enumeration", "1005 ... fully labeled", "four ... caries, deep caries, periapical lesions, and impacted teeth", "additional 1571 unlabeled" ✓. Đánh giá chỉ trên tập (c) 1.005 ảnh. |
| MMOral-OPG-Bench | https://huggingface.co/datasets/OralGPT/MMOral-OPG-Bench | ✓ | license: mit; không gated. README: "100 images, ... 491 closed-ended and 578 open-ended questions" ✓. Tệp là TSV câu hỏi (ảnh nằm trong TSV, ~577 MB). Ngôn ngữ: en. |
| MMOral-OPG-Training | https://huggingface.co/datasets/OralGPT/MMOral-OPG-Training | ⚠ | Còn sống nhưng gated "manual" (cần đăng nhập và được duyệt); thẻ không khai license; điều kiện xin chưa đọc được (trang yêu cầu đăng nhập). ~18,7 GB. Có Report/VQA/Chat/Attribute. |

Bổ sung quan trọng đọc từ HTML của MMOral (https://arxiv.org/html/2509.09254v1): ảnh MMOral gồm TED3 (16.639 ảnh, Apache-2.0) và bộ của Hoang Viet Do (3.924 ảnh, **Hanoi Medical University**, CC BY 4.0). Tức là có nguồn ảnh panoramic Việt Nam công khai; báo cáo MMOral sinh bằng LLM (DeepSeek-R1-Distill-Llama-70B rồi GPT-4-turbo chỉnh), bài nhận rủi ro ảo giác nhưng "không báo cáo chỉ số ảo giác riêng" (theo bản đọc 100.000 ký tự đầu; 20.000 ký tự cuối chưa đọc).

Sai lệch ghi chú trong `top5-de-tai.md`: (1) GPT-4o 41,45% là bản arXiv v1, bản NeurIPS là 43,31%; (2) "Rafid A." thực ra Ahmed Rafid (họ ghi theo thứ tự tên đầu); (3) MMOral-OPG-Training "điều kiện chưa kiểm chứng" vẫn đúng, ta cũng chưa kiểm được.

## 2. Bài bị bỏ sót, làm giảm tính mới

Truy vấn đã chạy thành công: arXiv API (panoramic report generation; panoramic vision-language; dental hallucination; OralGPT; dental Vietnamese = 0 kết quả) và 5 truy vấn WebSearch (Vietnamese dental panoramic report; tooth-level hallucination; structured report FDI YOLO small model; Việt nha khoa X-quang; multilingual/low-resource dental report; dental VLM benchmark hallucination). OpenAlex bị hết hạn mức ngày (HTTP 429, "daily_budget"), arXiv bị 429 ở 3 truy vấn cuối, nên **OpenAlex chưa tra được lần nào**.

| Bài | Link | Mức trùng | Nội dung đã đọc |
|---|---|---|---|
| **A Dual-Stage Vision–Language Framework for Dental Report Generation**, Boulesnane et al., Electronics 2026, 14-10-2026 | https://doi.org/10.3390/electronics15204729 (Crossref xác nhận; trang MDPI trả 403 nên chỉ đọc abstract qua Crossref) | **Rất cao, trùng gần như nguyên thiết kế** | "two YOLO-based models perform tooth localization and pathology detection" + U-Net; FDI numbering; "Five open-weight VLMs ... best-performing model, Qwen2.5-VL-3B"; "without ... VLM fine-tuning"; "reduced the hallucination rate from 53.7% to 14.0–16.8%"; dentist đánh giá 100 ảnh ngoài. Khác đề tài: không thấy tiếng Việt, không thấy chỉ số ảo giác mức răng dạng bộ ba, không thấy so với VLM fine-tune. Chưa đọc toàn văn (chưa biết dataset, ngôn ngữ báo cáo). |
| DentFound / "Towards clinical-level interpretation of dental panoramic radiography using an instance-guided vision-language model", Zhu et al., Nature Biomedical Engineering, 25-06-2026 | https://doi.org/10.1038/s41551-026-01713-8 | Cao (báo cáo panoramic, instance-guided) | Chỉ Crossref xác nhận tiêu đề/ngày; Crossref không có abstract, Nature yêu cầu đăng nhập. Chi tiết (kích cỡ mô hình, 12 chuyên gia) lấy từ snippet tìm kiếm, **chưa tự đọc**. |
| OralGPT-Plus, Fan Y. et al., CVPR 2026 | https://arxiv.org/abs/2603.06366 | Trung bình-cao | 2026-03-06; agent dùng công cụ, huấn luyện RL, DentalProbe ~5.000 ảnh, MMOral-X 300 câu. Là VLM fine-tune, không phải detector + VLM đóng băng. |
| Generating Findings for Jaw Cysts ... SLSO, Hosokawa et al., Diagnostics 2026, 16, 1096 | https://arxiv.org/abs/2510.02001 | Trung bình | Vòng tự sửa + trích số răng + kiểm tính nhất quán, "suppressed hallucinations"; chỉ cho nang xương hàm, GPT lớn; ngôn ngữ báo cáo không nêu. |
| DentiAsk, Jha D. et al., 2026 | https://arxiv.org/abs/2607.08790 | Thấp-trung bình | VQA 1.000 ảnh/10.000 QA, 10 VLM; không sinh báo cáo, không ảo giác. |
| ViX-Ray (LREC 2026) và ViMed-PET (NeurIPS 2025) | https://arxiv.org/abs/2603.15513 ; https://arxiv.org/abs/2509.24739 | Chỉ trùng về ngôn ngữ Việt | X-quang ngực 5.400 ảnh và PET/CT 2.757 ca; **không phải nha khoa**; hữu ích làm tiền lệ "VLM tiếng Anh kém trên báo cáo Việt, hay ảo giác" (ViX-Ray: "frequent hallucination"). |
| Dịch vụ OPG tiếng Sinhala (Dasanayaka et al.) | MDPI (403, chưa mở) | Trung bình về ý tưởng (panoramic + ngôn ngữ ít tài nguyên) | Chỉ có snippet tìm kiếm ("7.5 out of 10"); **chưa mở, DOI chưa xác nhận**; không dùng làm trích dẫn. |
| Scoping review báo cáo nha khoa AI, Yon, Ng, Bornstein, Frontiers Oral Health 2026 | https://doi.org/10.3389/froh.2026.1817718 | Bối cảnh | Crossref abstract: 7 nghiên cứu, 6 về báo cáo panoramic; "Standardised evaluation frameworks, larger multilingual datasets ... are needed". Hỗ trợ lập luận khoảng trống đa ngôn ngữ và chuẩn đánh giá. |
| OralGPT-Omni (arXiv 2511.22055), Dental-TriageBench (2604.13060), survey 2606.02914 | arXiv | Thấp | Chỉ thấy tiêu đề trong kết quả tìm kiếm, **chưa đọc**. |

Nhận xét "chưa thấy bài nha khoa tiếng Việt": trong các truy vấn trên không tìm thấy bài panoramic tiếng Việt nào (arXiv "dental AND Vietnamese" = 0). Chưa đủ để khẳng định vì OpenAlex/Google Scholar chưa tra.

## 3. Dataset

- DENTEX: sống, không gated, CC BY-NC-SA 4.0 (không thương mại, chia sẻ giống nhau; ràng buộc sản phẩm demo), 11,8 GB. Chỉ 4 chẩn đoán, 1.005 ảnh gán nhãn đủ.
- MMOral-OPG-Bench: sống, MIT, tải tự do, chỉ 100 ảnh, tiếng Anh; ảnh có nguồn Hanoi Medical University nhưng test chỉ là tập con đã chọn.
- MMOral-OPG-Training: gated thủ công, license không khai trên thẻ, điều kiện chưa kiểm được.
- Bộ ảnh Việt Nam của Hoang Viet Do (3.924 ảnh, CC BY 4.0 theo bài MMOral) là nguồn ảnh tiếng-Việt-hoá tiềm năng nhưng **chưa mở trực tiếp bộ gốc** và chưa biết có nhãn FDI hay không.
- GitHub OralGPT chuyển sang https://github.com/isjinghao/OralGPT (301). README ghi ngày 2026-08-29 phát hành OralDetect (detector nha khoa mở, có training set và benchmark), là baseline detector sẵn có và cũng là đối thủ tiềm tàng; chưa mở kiểm.

## 4. Kết luận

**Sửa điểm, không loại.** Lý do: các bài trích đều có thật và số liệu cốt lõi đúng, nhưng bài Electronics 2026 (Boulesnane et al.) đã làm "YOLO (FDI + bệnh lý) -> findings có cấu trúc -> VLM 3B không fine-tune -> đo tỉ lệ ảo giác", gần như đúng khung phương pháp của đề tài. Khoảng trống còn lại hẹp hơn: (a) tiếng Việt, (b) chỉ số ảo giác mức răng chặt (bộ ba vị trí-trường-giá trị, kiểu OPGAgent) thay vì LLM-judge, (c) ablation lượng bằng chứng cần thiết, (d) so với VLM fine-tune, (e) dùng ảnh Việt Nam.

| Tiêu chí | Cũ | Mới | Lý do |
|---|---|---|---|
| Mới | 4 | **2** (3 nếu toàn văn Electronics xác nhận không có tiếng Việt/chỉ số mức răng) | pipeline đã công bố; còn lại là ngôn ngữ + đo lường |
| ƯD | 5 | 5 | không đổi |
| KT | 4 | 4 | không đổi; thêm ưu điểm có OralDetect/ảnh Hà Nội (chưa kiểm) |
| CB | 4 | **3** | tạp chí mới có bài gần giống; cần định vị là bài đo lường/tiếng Việt |
| NCS | 5 | **4** | cần nha sĩ Việt thẩm định và dữ liệu Việt, chưa có |
| Tổng | 22 | **18-19** | rớt từ hạng 1 xuống dưới #2-#4 (21-22) |

Khuyến nghị: nếu giữ, định vị lại thành "benchmark ảo giác mức răng tiếng Việt cho báo cáo panoramic" thay vì "pipeline mới"; đọc toàn văn Electronics trước khi viết bất cứ thứ gì.

## 5. Chưa kiểm được

- OpenAlex: không truy vấn được (hết hạn mức ngày). Google Scholar, Scopus, Vietnamese venues: chưa tra.
- Toàn văn Electronics 2026, DentFound (Nature BME), bài Sinhala, OralGPT-Omni, Dental-TriageBench: chưa đọc (chỉ abstract Crossref hoặc snippet).
- Phần cuối ~20.000 ký tự của HTML MMOral chưa đọc.
- Điều kiện xin MMOral-OPG-Training; license từng ảnh của DENTEX; bộ ảnh Hà Nội gốc.
- AgenTeeth và PanDent: toàn văn chưa đọc (ngôn ngữ báo cáo, mô hình ≤4B, mức trùng thực tế).
- Công thức tách "ngôn ngữ/ảo giác tiếng Việt" chưa có bài nào khẳng định không tồn tại; chỉ là không tìm thấy trong các truy vấn nêu trên.
