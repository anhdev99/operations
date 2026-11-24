# Phản biện brief RES-14 — Trạng thái không hoàn thành

**Người phản biện:** Critic · **Ngày:** 2026-11-25 · **Trạng thái:** ⏸️ chờ RES-15

---

## Tóm tắt

- **RES-15** (`brief-university-docs-chatbot.md`): **bị stranded** — chưa tìm thấy tệp, không thể phản biện. Board cần retry/reassign RES-15.
- **RES-16** (cây thuốc nam): 3 đề tài có phát triển được; kiểm chứng được 17 trích dẫn từ 32.
- **RES-17** (răng 2D→3D): 3 đề tài có pháp lý; "99%" là sai khái niệm, nên đo theo mm.

---

## RES-15 Brief Chatbot Trường (chưa kiểm chứng)

| Item | Trạng thái | Ghi chú |
|---|---|---|
| Tệp `topics/brief-university-docs-chatbot.md` | ✗ Không tìm thấy | Dự kiến chứa hướng: chatbot hỏi đáp quy chế trường tiếng Việt |

**Blockers:**
- RES-15 đang gán cho agent nhưng bị stranded (stranded_assigned_issue).
- Không có brief để phản biện.

**Board cần:** Retry RES-15 hoặc reassign để hoàn thành brief; RES-18 chờ kết quả.

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
| RES-15 | **CHỜ BOARD** | Stranded, cần retry/reassign trước khi RES-18 tiếp tục |
| RES-16 | **GIỮ** | 3 đề tài hợp lệ; không lỗi nặng |
| RES-17 | **SỬA + GIỮ** | Làm rõ khái niệm đo lường (mm từng vùng, bất định); lưu ý khoảng cách sim↔thật |

**RES-18:** Chuyển sang `blocked` chờ RES-15.

---

Phản biện ngừng tại đây.
