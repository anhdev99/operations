# BioTrove: A Large Curated Image Dataset Enabling AI for Biodiversity

- **Tác giả / năm / nơi:** Chih-Hsuan Yang, Benjamin Feuer, Zaki Jubery, Zi K. Deng, et al. (Google, 2024).
- **Trích dẫn:** arXiv:2406.17720 (v2 09/04/2025). DOI https://doi.org/10.48550/arXiv.2406.17720 · link đã mở: https://arxiv.org/abs/2406.17720 (abstract).

## Bài toán
Thiếu dataset ảnh sinh vật đủ lớn + đủ sạch + đủ metadata (tên khoa học, hệ phân loại, common name) cho AI bảo tồn/biodiversity. Cần benchmark đánh giá **zero-shot** theo nhiều chiều: life stage, **loài hiếm (rare)**, **loài gây nhầm (confounding species)**, nhiều mức phân loại học.

## Phương pháp
- Curation **BioTrove**: **161,9 triệu ảnh** từ iNaturalist, chỉ giữ ảnh research-grade, ~**366,6K loài** (3 giới: Animalia, Fungi, Plantae). Mỗi ảnh có tên khoa học + hierarchy + common name.
- Rút **BioTrove-Train**: tập con ~**40M cặp ảnh-caption** (focus 7 nhóm ít được đại diện: Aves, Arachnida, Insecta, Plantae, Fungi, Mollusca, Reptilia) để train suite **CLIP model**.
- Đưa benchmark zero-shot: accuracy theo life stages, rare species, **confounding species**, nhiều taxonomic levels.

## Số liệu chính (theo abstract)
- 161,9M ảnh, 366,6K loài; BioTrove-Train 40M captioned; 7 nhóm target.
- Số accuracy per-benchmark không nằm ở abstract; cần đọc bảng PDF (chưa kiểm chứng).

## Hạn chế
- Dữ liệu iNaturalist (ảnh cộng đồng, phân bố theo độ phổ biến) → long-tail mạnh (loài hiếm ít ảnh) — đúng bản chất, nhưng không thay được ảnh tự chụp ViMeLeaf (ảnh lá cây thuốc Việt, không phải ảnh toàn cây iNaturalist).
- Sinh vật nói chung; cây thuốc Việt Nam không phải focus → cần dùng làm **so sánh backbone**, không làm data chính.

## Dùng được gì cho Bài 2
- **Nguồn so sánh long-tail + confounding**: benchmark "confounding species" và "rare species" của BioTrove đúng hai trục Bài 2 (cặp dễ nhầm + 102 loài đuôi, RES-42). Có thể chạy lại benchmark confounding trên backbone BioTrove-CLIP như đối chứng cho "loài nào hay gây nhầm".
- **CLIP-họ làm baseline**: suite CLIP của BioTrove là một lựa chọn backbone (nhỏ hơn, focus sinh vật) để so với BioCLIP.
- Nếu muốn pretrain/loại dữ liệu phụ cho cây: BioTrove Plantae subset là nguồn ảnh cây công khai lớn; dùng kiểm tra chéo (không thay ảnh ViMeLeaf).
