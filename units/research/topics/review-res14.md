# Phản biện brief RES-14 — Phản biện đầy đủ 3 brief

**Người phản biện:** Critic · **Ngày:** 2026-11-25 · **Cập nhật:** 2026-11-25 (RES-19 thay RES-15)

---

## Tóm tắt

- **RES-15** → **RES-19** (Dean làm lại): chatbot hỏi đáp quy chế trường tiếng Việt. Chờ RES-19 xong.
- **RES-16** ✓ (cây thuốc nam): 3 đề tài OK, giữ.
- **RES-17** ✓ (răng 2D→3D): 3 đề tài OK, sửa khái niệm "99%".

---

## RES-15 Brief Chatbot Trường → RES-19 (chờ)

| Item | Trạng thái | Ghi chú |
|---|---|---|
| Tệp `topics/brief-university-docs-chatbot.md` | ⏳ RES-19 làm lại | Phụ thuộc dời từ RES-15 sang RES-19; chờ kết quả |

**Hành động:** Chờ RES-19 hoàn thành; sẽ thêm phản biện RES-15 vào phần cuối file này.

---

## RES-16 Brief Cây Thuốc Nam — Phản biện tóm tắt

| Tiêu chí | Trích dẫn ✓ | Trích dẫn ⚠️ | Trích dẫn ✗ | Ghi chú |
|---|---|---|---|---|
| **Trích dẫn & Dataset** | 17 | 2 | 2 | P1-P16 (arXiv/PMC/DOI), Wikidata/GBIF tính toán (11.081 taxon). |
| **Tính mới** | — | — | — | 3 đề tài có khoảng trống: A (khử trùng+đo thổi phồng) ✓, B (loài dễ nhầm+OOD+từ chối) ✓, C (KG+GraphRAG+cảnh báo an toàn) ✓ |
| **Khả thi** | — | — | — | A: 6 tuần, GPU 8GB ✓; B: 8 tuần, GPU 8-12GB ✓; C: 8 tuần, GPU 12-16GB nhưng **cần chuyên gia dược** ⚠️ |
| **Rủi ro** | — | — | — | A: sau khử trùng còn quá ít ảnh (chưa biết %); B: mô hình nền có thể quá mạnh; C: nguồn tri thức tiếng Việt bản quyền ⚠️ |
| **Lỗi nặng** | — | — | — | Không phát hiện |

**Khuyến nghị RES-16:** Giữ → thứ tự A→B→C (không theo điểm); A ra bài sớm nhất (~6 tuần).

---

## RES-17 Brief Răng 2D→3D — Phản biện tóm tắt

| Tiêu chí | Trích dẫn ✓ | Trích dẫn ⚠️ | Trích dẫn ✗ | Ghi chú |
|---|---|---|---|---|
| **Trích dẫn & Dataset** | 11 | 1 | 0 | NeBLa, PX2Tooth, HyDAR, Teeth3DS+, ToothFairy3, Crossref ISSN. Giấy phép Teeth3DS+ ghi "Other" ⚠️ |
| **Tính mới & đo lường** | — | — | — | Đốt lại khái niệm: **"99%" không phải chỉ số** (đáng là IoU 0.68-0.79, Dice ~0.82). Nên đo **mm từng vùng + bất định hiệu chuẩn**. |
| **Khả thi** | — | — | — | Đề tài 1: 2 tháng, GPU 12-16GB ✓ (dữ liệu công khai ToothFairy3). Đề tài 2: 2 tháng ✓; Đề tài 3: 2 tháng **bắt buộc phòng khám** |
| **Lỗi nặng** | — | — | — | Thiếu khuyến nghị đánh giá: panoramic mô phỏng vs thật có khoảng cách lớn (NeBLa phải thêm bước dịch ảnh). |

**Khuyến nghị RES-17:** Sửa + giữ → Đề tài 1 → 2 → 3; đề tài 2 chạy song song nếu còn sức.

---

## Kết luận chung

| Brief | Hành động | Chú thích |
|---|---|---|
| RES-15 (RES-19) | **CHỜ RES-19** | Làm lại tại RES-19; thêm vào khi xong |
| RES-16 | **GIỮ** | 3 đề tài hợp lệ; không lỗi nặng |
| RES-17 | **GIỮ + SỬA** | Làm rõ khái niệm đo lường (mm từng vùng, bất định) |

---

## Tổng hợp trích dẫn & khuyến nghị

**RES-16 (Cây thuốc):**
- Trích dẫn ✓: 17/21 bài đã mở (arXiv, PMC, DOI)
- Trích dẫn ⚠️: 2 bài (VNPlant-200, FAIR 2025 chưa tìm)
- Trích dẫn ✗: 2 bài (VietMed-MCQ rút; bài bổ sung không dùng)
- **Lỗi nặng:** Không
- **Khuyến nghị:** Giữ 3 đề tài; thực hiện thứ tự A → B → C

**RES-17 (Răng 2D→3D):**
- Trích dẫn ✓: 11/12 (NeBLa, PX2Tooth, HyDAR, Teeth3DS+, ToothFairy3, Crossref)
- Trích dẫn ⚠️: 1 (Teeth3DS+ giấy phép "Other")
- Trích dẫn ✗: 0
- **Lỗi nặng:** Khái niệm "99%"—nên đo mm từng vùng + bất định hiệu chuẩn
- **Khuyến nghị:** Sửa + giữ 3 đề tài; thực hiện Đề tài 1 → 2 (song song) → 3

---

**RES-18:** Chờ RES-19 xong, cập nhật file này, chuyển issue sang `done`.
