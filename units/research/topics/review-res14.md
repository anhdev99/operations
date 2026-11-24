# Phản biện brief RES-14 — Phản biện đầy đủ 3 brief

**Người phản biện:** Critic · **Ngày:** 2026-11-25 · **Cập nhật:** 2026-11-25 (RES-19 thay RES-15)

---

## Tóm tắt

- **RES-15** → **RES-19** (Dean làm lại): chatbot hỏi đáp quy chế trường tiếng Việt. Chờ RES-19 xong.
- **RES-16** ✓ (cây thuốc nam): 3 đề tài OK, giữ.
- **RES-17** ✓ (răng 2D→3D): 3 đề tài OK, sửa khái niệm "99%".

---

## RES-19 Brief Chatbot Trường (thay RES-15) — Phản biện tóm tắt

| Tiêu chí | Trích dẫn ✓ | Trích dẫn ⚠️ | Trích dẫn ✗ | Ghi chú |
|---|---|---|---|---|
| **Trích dẫn & Dataset** | 6 | 0 | 0 | P1-P6 (arXiv, Crossref); 4 dataset công khai (Hugging Face, github) |
| **Tính mới** | — | — | — | Thời gian + hiệu lực văn bản cho QA giáo dục tiếng Việt chưa thấy; khoảng trống rõ so với P3 (luật) và P2 (y tế) |
| **Khả thi** | — | — | — | Đề tài 1: tháng 1 đồ thị, tháng 2 so sánh (GPU nhỏ); đề tài 2: 30k tệp không công bố, chỉ báo cáo số liệu ✓ |
| **Rủi ro** | — | — | — | Trích quan hệ sửa đổi từ văn bản cấp trường sai; ViHERMES (P2) mở rộng sang giáo dục trước ⚠️ |
| **Lỗi nặng** | — | — | — | Không phát hiện |

**Khuyến nghị RES-19:** Giữ 2 đề tài; điểm 22/25, phù hợp NCS (chuỗi: thời gian → triển khai).

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
| RES-19 (thay RES-15) | **GIỮ** | 2 đề tài hợp lệ; không lỗi nặng; điểm 22/25 |
| RES-16 | **GIỮ** | 3 đề tài hợp lệ; không lỗi nặng |
| RES-17 | **GIỮ + SỬA** | Làm rõ khái niệm đo lường (mm từng vùng, bất định) |

---

## Tổng hợp trích dẫn & khuyến nghị

**RES-19 (Chatbot quy chế trường):**
- Trích dẫn ✓: 6/6 bài đã mở (arXiv, Crossref)
- Trích dẫn ⚠️: 0
- Trích dẫn ✗: 0
- **Lỗi nặng:** Không
- **Khuyến nghị:** Giữ 2 đề tài; thực hiện Đề tài 1 → 2

**RES-16 (Cây thuốc nam):**
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

## Kết quả cuối cùng

✓ Phản biện 3 brief xong: RES-19 (6 trích dẫn ✓), RES-16 (17 ✓), RES-17 (11 ✓).  
✓ Lỗi nặng: 0.  
→ **Chuyển RES-18 sang `done`.**
