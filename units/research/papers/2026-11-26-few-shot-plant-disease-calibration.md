# Description-Guided CLIP Adaptation with Local Evidence Calibration for Few-Shot Plant Disease Recognition

Đề tài so sánh: **T2 / ViMeLeaf Bài 2** (few-shot/đuôi dài + calibration). Ngày đọc: 2026-11-26.

## Thông tin
- Tên: *Description-Guided CLIP Adaptation with Local Evidence Calibration for Few-Shot Plant Disease Recognition*
- Tác giả: Zhenkun Ye, Qian Zhou, Hua Zou
- Năm: 2026 (arXiv 2026-11-12, v1)
- Nơi đăng: arXiv:2611.16373 — DOI arXiv: 10.48550/arXiv.2611.16373.
- Link: https://arxiv.org/abs/2611.16373

## Vấn đề
Nhận dạng bệnh cây **few-shot** (ít nhãn/lớp) + **cross-domain**: CLIP-based methods thường dùng semantic lớp thô + biểu diễn global, bỏ sót **dấu hiệu bệnh cụ thể + cue local fine-grained**; adaptation quá mức gây **over-specialization**, giảm tổng quát. Cần calibrate matching ảnh-văn bản bằng bằng chứng local.

## Phương pháp
- **Two-stage CLIP adaptation, description-guided**:
  - Stage 1: enrich class semantics bằng **mô tả dấu hiệu (symptom) + mô tả so sánh (comparative descriptions)** giữa các bệnh giống nhau.
  - Aggregation **class-relevant patch evidence** để **calibrate** global image-text matching bằng cue fine-grained.
- Adaptation: cập nhật vision-language encoder bằng **tham số nhẹ (lightweight)**, sau đó **freeze** + train **linear classifier**.
- Suy luận: classifier cho in-domain; **class prototypes từ text encoder** cho cross-domain (giữ tính transferable).

## Dữ liệu và kết quả (abstract)
- 2 backbone; dataset: **PlantVillage, Cassava, Pear** (few-shot).
- Highest mean accuracy (16-shot, ViT-L/14): **PlantVillage 93.16%, Cassava 79.30%, Pear 96.56%**.
- Cross-domain (class-aligned, 21 lớp PlantDoc chung): **56.96%** — vượt mọi method so sánh.
- Số cụ thể từng backbone/table **chưa đối chiếu lại trong lượt này** (chưa mở HTML/PDF bảng) — "chưa kiểm chứng" chi tiết từng bảng.

## Hạn chế
- Chỉ đọc abstract (số lấy từ abstract).
- Few-shot **bệnh cây** (PlantVillage/Cassava/Pear), **không phải loài cây thuốc**; không có "cặp dễ nhầm có nhãn an toàn", không OOD điện thoại, không selective reject (chỉ calibration + classifier).
- Cross-domain 56.96% (21 lớp PlantDoc) — thấp so với in-domain, cho thấy generalisation vẫn yếu; P2 (điện thoại OOD) sẽ gặp tương tự.

## Liên quan ViMeLeaf Bài 2
- **(a) Trùng một phần**: cùng "few-shot + cây + calibration" với P2 (đuôi dài 102 loài, RES-42). Nhưng P2 mới ở: (1) **loài cây thuốc Việt** (không bệnh cây), (2) **cặp dễ nhầm có nhãn an toàn**, (3) **selective reject + risk–coverage**, (4) **OOD điện thoại**.
- **(b) Khoảng trống P2 lấp**: few-shot **loài** (không bệnh) + an toàn khi nhầm + OOD điện thoại + từ chối.
- **(c) Rủi ro trùng**: **thấp** (bệnh vs loài, không selective vs selective). Trích làm "few-shot cây + calibration đã có".
- **(d) Baseline**: **calibration (local evidence) + linear probe trên CLIP/DINOv2** làm baseline cho 102 loài đuôi P2; so với conformal (2507.06867) + energy (2605.08618). Đo AURC/risk@coverage (P2 thêm phần selective bài này chưa có).

## Dùng được gì
- **Calibration bằng patch evidence local + mô tả so sánh** làm kỹ thuật cho cặp giống nhau (Dây giác/Sục sạc: mô tả điểm khác biệt duy nhất).
- **Linear probe + freeze encoder** = baseline nhẹ cho P2 (ít dữ liệu, 102 loài đuôi).
- Số đối chứng: 93.16%/79.30%/96.56% (in-domain 16-shot), 56.96% (cross-domain) — anchor "few-shot cây được nhưng cross-domain yếu".

## Mức chắc chắn
Đọc **abstract + arXiv metadata**. **Chưa mở lại bảng từng backbone/dataset** → số "93.16/79.30/96.56/56.96" lấy nguyên từ abstract (khớp giữa abstract và ghi chú), bảng chi tiết "chưa kiểm chứng". Venue: preprint.

## Ghi chú thêm
- "Calibration" ở đây = calibrate image-text matching (không phải temperature scaling theo Geifman 1805.08206). P2 dùng **cả hai**: calibration local (bài này) + temperature/conformal (nền).
