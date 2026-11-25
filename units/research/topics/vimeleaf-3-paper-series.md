# ViMeLeaf: đề xuất chuỗi 3 bài báo liên tục

Issue: RES-27. Người đề xuất: Dean. Ngày: 2026-11-26. Trạng thái: **bản nháp**, chờ Scholar kiểm tính mới và Critic phản biện.
Thay cho tên tạm "VNMedPlant-Clean" ở RES-14/RES-26: dataset thật của chủ nhóm tên **ViMeLeaf**.

## Dữ kiện đo trực tiếp trên `E:\ViMeLeaf_Dataset` (chỉ đọc, không chép ảnh)

Lệnh tái lập: đọc `manifest.csv`, `deleted_near_dups_log.csv`, `deleted_junk_log.csv`, `metadata/*.xlsx` bằng Python (csv + openpyxl).

| Mục | Số liệu |
|---|---|
| Ảnh / video còn lại | 62.102 ảnh, 268 video (mp4/MOV) |
| Nguồn | An Giang 27.186, Tây Ninh 22.174, Đồng Tháp 6.721, bổ sung v1 1.633, bổ sung v2 2.485, nhóm xung đột nhãn 2.171 (đếm theo manifest, gồm cả video) |
| Thư mục lớp | 195; sau chuẩn hoá tên (bỏ số thứ tự, dấu, ngoặc) còn **~165 tên loài** |
| Phân bố | ít nhất 20, trung vị 247, nhiều nhất 2.610 ảnh/tên; **72 tên < 100 ảnh** (đuôi dài) |
| Trùng lặp đã xoá | **37.980 ảnh gần trùng** (có cột `kept_path` chỉ ảnh được giữ) + 4.188 tệp rác, đều có log |
| Trùng giữa nguồn | 30 tên loài có ở cả An Giang và bổ sung v1; loài gần như không trùng giữa 3 tỉnh (1 loài) |
| Xung đột nhãn | `_review/conflict_day_giac_vs_suc_sac`: Dây giác và Sục sạc (lá 3 chét, dễ nhầm) |
| Metadata | `ViMeLeaf Dataset 80 Special.xlsx`: 80 loài; 66 loài có đủ tên khoa học, họ, mô tả, bộ phận dùng, tính vị, công dụng, liều dùng, ghi chú; 19 loài thuộc danh mục 70 cây của Bộ Y tế; khớp tên với 61 lớp ảnh |

Hệ quả cho thiết kế:
- Log gần trùng cho sẵn **nhóm trùng** (ảnh xoá ↔ ảnh giữ): dựng lại được bộ "trước khử trùng" để đo accuracy bị thổi phồng bao nhiêu, không cần đoán.
- Loài không trùng giữa tỉnh nên **không đo được tổng quát hoá chéo vùng theo loài**; chỉ đo được chéo đợt chụp (An Giang gốc ↔ bổ sung v1, 30 loài).
- Bảng metadata là hạt giống cho đồ thị tri thức (bài 3); nguồn là website tham khảo nên cần chuyên gia dược duyệt trước khi dùng cho cảnh báo an toàn.

## Chuỗi 3 bài

Một sợi chỉ: **nhận dạng cây thuốc nam đáng tin cậy, từ dữ liệu sạch đến trợ lý hỏi đáp an toàn.** Mỗi bài dùng kết quả của bài trước.

| # | Bài | Câu hỏi nghiên cứu | Đóng góp dự kiến | Nơi nộp ứng viên (Scopus chưa tra) | Thời gian |
|---|---|---|---|---|---|
| 1 | **ViMeLeaf: bộ ảnh lá cây thuốc nam Việt Nam, khử trùng và split chống rò rỉ** (data paper) | Ảnh trùng làm accuracy bị thổi phồng bao nhiêu trên ảnh cây thuốc tự thu? | Công bố ~62k ảnh + video, ~165 loài, 3 tỉnh; log khử trùng; split theo nhóm trùng/đợt chụp; đo chênh lệch accuracy split ngẫu nhiên (trước khử trùng) và split sạch; baseline 3 seed | Data in Brief; Scientific Data | ~6 tuần |
| 2 | **Nhận dạng loài dễ nhầm, đuôi dài, biết từ chối** | Mô hình nền (DINOv2/CLIP-họ) + dự đoán có chọn lọc giảm nhầm loài nguy hiểm bao nhiêu ở cùng độ phủ? | Benchmark cặp dễ nhầm (bắt đầu từ Dây giác/Sục sạc), đuôi dài 72 loài < 100 ảnh, chéo đợt chụp; đường risk–coverage; gộp nhiều khung hình video lúc suy luận | Ecological Informatics; Frontiers in Plant Science; Computers and Electronics in Agriculture | 2-3 tháng |
| 3 | **Ảnh → đồ thị tri thức → GraphRAG tiếng Việt có cảnh báo an toàn** | Lọc an toàn cứng theo KG có giảm câu trả lời nguy hiểm so với RAG thường và trộn mềm không? | KG ~66-80 loài từ metadata (đã chuyên gia duyệt); hệ thống chụp lá → nhận dạng (bài 2, từ chối khi không chắc) → hỏi đáp có trích căn cứ; benchmark an toàn tiếng Việt; thí nghiệm E1, E2 ở `experiments/backlog.md` | KSE; ACIIDS; JMIR Formative Research | 2-3 tháng |

Quan hệ với đề tài cũ: bài 1 = #5 VNMedPlant-Clean (RES-26), bài 2 = T2, bài 3 = T3. T1 EduReg-Time vẫn là bài lõi của mạch văn bản trường; hai mạch chạy song song.

## Rủi ro và việc cần làm trước

- **Trùng với bài FAIR 2025 và luận văn ThS** của chủ nhóm: bài 1 phải trích và nêu rõ phần mới. Cần tên/link bài FAIR 2025.
- **Tính mới chưa kiểm**: cần Scholar tra các bộ ảnh cây thuốc Việt Nam đã công bố (VNPlant-200 và các bộ khác) và các bài selective prediction cho cây; chưa được nói "chưa ai làm".
- **Nhãn**: 195 thư mục → ~165 tên là ước lượng bằng chuẩn hoá chuỗi; cần ánh xạ thủ công sang tên khoa học (dùng bảng metadata) trước khi công bố.
- **Bản quyền/quyền công bố**: chủ nhóm xác nhận ảnh được công bố (RES-14). Cần chọn giấy phép (ví dụ CC BY 4.0) và nơi lưu (Zenodo).
- **Chi phí APC**: Data in Brief, Scientific Data có thu phí; cần board duyệt hoặc chọn nơi không phí.
- **An toàn y tế**: bài 3 không đưa ra liều dùng nếu chưa có chuyên gia dược duyệt KG.

## Việc tiếp theo (đã tạo issue con của RES-27)

1. Builder: chạy pipeline RES-26 trên ViMeLeaf ở chế độ chỉ đọc, đo độ thổi phồng accuracy từ log trùng, dựng split.
2. Scholar: kiểm tính mới cho 3 bài (bộ dữ liệu, phương pháp, hệ thống tương tự), kèm DOI/arXiv đã mở.
3. Critic: phản biện đề xuất này sau khi Scholar xong.
