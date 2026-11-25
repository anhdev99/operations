# Prototype P1: Benchmark ảo giác mức răng cho báo cáo X-quang panoramic tiếng Việt

Ngày: 2026-11-25. Trạng thái: **bản nháp để chủ nhóm đọc và xác minh, chưa phải kế hoạch đã chốt.**
Căn cứ: `verify-t1-panoramic.md` (kiểm độc lập), `recheck-top5.md`. Mọi con số/bài bên dưới có link; phần nào là **thiết kế của tôi (chưa ai kiểm)** được ghi rõ.

## 0. Vì sao chọn P1 làm prototype, và vì sao có thể bạn không chọn

- Chọn vì: bắt đầu được ngay không cần nha sĩ (dữ liệu tải tự do, đo tự động), demo rõ, nối được với các hướng ontology/chatbot sau này.
- **Nhưng** điểm sau kiểm chỉ 18-19/25 và tính mới giảm mạnh (Mới 2). Nếu bạn ưu tiên đề tài dựa trên tài sản đang có (văn bản trường, ảnh cây thuốc nam), hãy xem T1/T2 trong `focus.md` / `res14-de-xuat-huong-ncs.md`. Prototype này **không** thay quyết định đó.
- Định vị lại: **không** còn là "pipeline mới" (đã có), mà là **benchmark + chỉ số đo ảo giác mức răng + phân tích tiếng Việt**.

## 1. Vấn đề và định vị

Bài gần nhất (đã đọc abstract qua Crossref, chưa đọc toàn văn): Boulesnane et al., *Electronics* 2026, https://doi.org/10.3390/electronics15204729. Họ dùng YOLO (đánh số FDI + bệnh lý) → dữ kiện có cấu trúc → Qwen2.5-VL-3B không fine-tune, ảo giác giảm 53,7% → 14,0–16,8%, 100 ảnh ngoài có nha sĩ đánh giá.
Bài khác cần đối chiếu: OPGAgent (bộ ba Location-Field-Value) arXiv 2603.00462; AgenTeeth arXiv 2609.17800; PanDent arXiv 2607.27378; MMOral arXiv 2509.09254; DentFound https://doi.org/10.1038/s41551-026-01713-8.

Khoảng trống còn lại theo kiểm độc lập (chưa chắc, cần đọc toàn văn Electronics để xác nhận):
1. Báo cáo **tiếng Việt** (arXiv `dental AND Vietnamese` = 0 kết quả; OpenAlex và Google Scholar chưa tra).
2. Chỉ số ảo giác **mức răng chặt** (so sánh từng bộ ba vị trí-trường-giá trị với nhãn vàng), thay vì LLM-judge.
3. Phân tích: bao nhiêu bằng chứng từ detector là đủ; so với VLM fine-tune.
4. Ảnh Việt Nam (MMOral dùng bộ 3.924 ảnh Hanoi Medical University, CC BY 4.0, theo HTML bài MMOral; bộ gốc **chưa mở kiểm**).

## 2. Giả thuyết đóng góp (để so với bài đọc hằng ngày)

- C1: Một chỉ số ảo giác mức răng, tái lập được, tính tự động từ nhãn FDI của DENTEX, kèm mã nguồn.
- C2: Kết quả trên báo cáo tiếng Việt: VLM nhỏ đóng băng + bằng chứng detector so với VLM không bằng chứng, theo từng mức bằng chứng (0, vị trí, vị trí+chẩn đoán, + độ tin cậy).
- C3: Phân tích lỗi: lỗi nào còn lại (răng lân cận, FDI sai quadrant, bỏ sót), lệch giữa tiếng Anh và tiếng Việt.
- Rủi ro bị coi là trùng: C2 trùng Boulesnane nếu bài đó đã có tiếng Việt hoặc ablation bằng chứng. **Việc đầu tiên: đọc toàn văn.**

## 3. Thiết kế hệ thống (thiết kế của tôi, chưa kiểm chạy)

```
ảnh panoramic ──► detector (YOLO/RT-DETR, FDI + 4 chẩn đoán trên DENTEX)
                      │  JSON: [{fdi, label, bbox, conf}]
                      ▼
          bộ trình bày bằng chứng (4 mức A0..A3)
                      ▼
  VLM nhỏ đóng băng (≤4B, 4-bit) ── prompt mẫu báo cáo tiếng Việt
                      ▼
         báo cáo văn bản ──► bộ trích bộ ba (rule + LLM) ──► so với nhãn vàng ──► chỉ số
```

Mức bằng chứng: A0 chỉ ảnh; A1 + danh sách răng có mặt; A2 + chẩn đoán từng răng; A3 + độ tin cậy/cờ "không chắc".
VLM ứng viên: Qwen2.5-VL-3B (bài Electronics dùng), thêm 1-2 mô hình ≤4B khác (**chọn sau khi đọc license và kiểm chạy được trên GPU của bạn**).

## 4. Chỉ số ảo giác mức răng (đề xuất)

Với mỗi báo cáo, trích bộ ba (răng FDI, trường: vị trí/chẩn đoán/mức độ, giá trị). Xếp loại:
- **Đúng**: khớp nhãn vàng.
- **Ảo giác**: khẳng định không có trong nhãn vàng (răng không có bệnh hoặc răng không tồn tại).
- **Bỏ sót**: nhãn vàng có mà báo cáo không nhắc.
Báo cáo: tỉ lệ ảo giác = ảo giác / tổng khẳng định; precision/recall mức răng; 95% CI bằng bootstrap; 3 seed (nếu có lấy mẫu).
Hạn chế cần nêu: DENTEX chỉ có 4 chẩn đoán nên "ảo giác" chỉ đo trong phạm vi đó; bộ trích bộ ba có lỗi riêng, cần đo bằng 100 báo cáo gán tay.

## 5. Dữ liệu (đã kiểm ở verify-t1)

| Dữ liệu | Link | Giấy phép / truy cập | Dùng cho |
|---|---|---|---|
| DENTEX | https://huggingface.co/datasets/ibrahimhamamci/DENTEX | CC BY-NC-SA 4.0, không gated, 11,8 GB; 1.005 ảnh nhãn đủ; 4 chẩn đoán | huấn luyện detector, nhãn vàng |
| MMOral-OPG-Bench | https://huggingface.co/datasets/OralGPT/MMOral-OPG-Bench | MIT, 100 ảnh, tiếng Anh | so sánh, VQA phụ |
| MMOral-OPG-Training | https://huggingface.co/datasets/OralGPT/MMOral-OPG-Training | gated thủ công, điều kiện xin chưa đọc được | tuỳ chọn |
| Ảnh Hanoi Medical University (qua MMOral) | xem HTML https://arxiv.org/html/2509.09254v1 | CC BY 4.0 theo bài; **bộ gốc chưa mở** | mở rộng ảnh Việt Nam, cần xác nhận có nhãn FDI không |

Ràng buộc: DENTEX cấm thương mại → demo chỉ phi thương mại. Không dùng ảnh bệnh nhân thật của phòng khám nào khi chưa có chấp thuận đạo đức.

## 6. Kế hoạch thực nghiệm (bạn chạy; 8 tuần, GPU 8-12 GB, **ước lượng của tôi**)

| Tuần | Việc | Đầu ra | Cần ai |
|---|---|---|---|
| 0 | Đọc toàn văn Electronics 2026, OPGAgent, AgenTeeth; tra Google Scholar "nha khoa" + "tiếng Việt" | Quyết định go/no-go dựa trên khoảng trống | Chủ nhóm |
| 1-2 | Tải DENTEX; baseline detector (FDI + 4 chẩn đoán) | mAP, bảng lỗi | Chủ nhóm |
| 3 | Xuất JSON bằng chứng; viết bộ trích bộ ba và chỉ số | mã chỉ số + kiểm tay 100 báo cáo | — |
| 4-5 | Chạy A0..A3 × 2-3 VLM, báo cáo tiếng Việt và tiếng Anh | bảng ảo giác theo mức bằng chứng | — |
| 6 | So với VLM fine-tune nhỏ (LoRA) nếu còn GPU | 1 bảng so sánh | — |
| 7 | Phân tích lỗi, bootstrap CI | hình + bảng | — |
| 8 | Viết khung bài, 1 nha sĩ duyệt 30-50 báo cáo (nếu tìm được) | bản thảo v0 | nha sĩ (chưa có) |

Dừng sớm nếu: tuần 0 phát hiện Electronics đã có tiếng Việt + chỉ số mức răng; hoặc detector mAP quá thấp để làm bằng chứng.

## 7. Nơi công bố (tồn tại; **Scopus chưa tra**)

Dentomaxillofacial Radiology; Journal of Imaging Informatics in Medicine; IEEE Access (theo `top5-de-tai.md`); cân nhắc hội nghị về VLM y tế nếu định vị là benchmark. Chủ nhóm tra Scopus/SJR trước khi chọn.

## 8. Danh sách tự xác minh (làm theo thứ tự)

1. Mở https://doi.org/10.3390/electronics15204729 và đọc toàn văn: dataset, ngôn ngữ báo cáo, có chỉ số mức răng không, có ablation bằng chứng không. (Kiểm độc lập chỉ thấy abstract qua Crossref; MDPI trả 403.)
2. Mở arXiv 2603.00462, 2609.17800, 2607.27378, 2509.09254: xác nhận đúng như bảng ở `verify-t1-panoramic.md` mục 1.
3. GPT-4o: bản arXiv v1 ghi 41,45%, bản NeurIPS ghi 43,31% (https://proceedings.neurips.cc/paper_files/paper/2025/hash/3797b3a3c939156757857cf1b9afde3c-Abstract-Datasets_and_Benchmarks_Track.html). Trích bản NeurIPS.
4. Google Scholar: "dental" "Vietnamese" "panoramic" "report generation"; Scholar "Hanoi Medical University panoramic dataset". (OpenAlex/Scholar chưa tra được trong lần kiểm.)
5. Kiểm https://github.com/isjinghao/OralGPT (OralDetect, phát hành 2026-08-29 theo README): có thể là detector baseline sẵn và cũng là đối thủ.
6. Xác nhận MMOral-OPG-Training: đăng nhập HF xem điều kiện xin.
7. Tra Scopus/SJR các tạp chí ở mục 7.

## 9. Điều tôi chưa biết

- GPU thực tế của bạn, số giờ/tuần, có tìm được nha sĩ không.
- Mức trùng thật với Electronics 2026, DentFound, AgenTeeth (chưa đọc toàn văn).
- Bộ trích bộ ba tự động chính xác đến đâu; cách chọn VLM cụ thể.
- Số truy vấn OpenAlex/Scholar chưa đủ nên "chưa có bài tiếng Việt" vẫn là giả định.
