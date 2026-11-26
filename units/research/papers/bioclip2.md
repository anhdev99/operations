# BioCLIP 2: Emergent Properties from Scaling Hierarchical Contrastive Learning

- **Tác giả / năm / nơi:** Jianyang Gu, Samuel Stevens, Elizabeth G Campolongo, Matthew J Thompson, Net Zhang, Jiaman Wu, Andrei Kopanev, Zheda Mai, Alexander E. White, James Balhoff, Wasila M Dahdul, Daniel Rubenstein, Hilmar Lapp, Tanya Berger-Wolf, Wei-Lun Chao, Yu Su (2025; NeurIPS 2025 Spotlight).
- **Trích dẫn:** arXiv:2505.23883 (v2 23/10/2025). DOI https://doi.org/10.48550/arXiv.2505.23883 · link đã mở: https://arxiv.org/abs/2505.23883 (abstract + metadata; HTML full-text sẵn). Project: https://imageomics.github.io/bioclip-2/.

## Bài toán
Kế tiếp BioCLIP: mở rộng dữ liệu + mục tiêu "phân biệt loài" (species-level) ở quy mô, xem mô hình có xuất hiện tính chất "emergent" (khả năng mới vượt mục tiêu huấn luyện) hay không.

## Phương pháp
- Curation **TreeOfLife-200M**: ~214 triệu ảnh sinh vật, bộ lớn nhất và đa dạng nhất đến thời điểm đó.
- Huấn luyện BioCLIP 2 (contrastive vision-language theo cây phân loại, hierarchical) để phân biệt loài.
- Phân tích không gian embedding: mức **giữa loài** (inter-species) → các đặc trưng chức năng/sinh thái (ví dụ kích thước mỏ, habitat) được tách đúng; mức **trong loài** (intra-species, ví dụ giai đoạn phát triển, giới tính) được **bảo toàn và tách trong siêu phẳng trực giao** với trục phân biệt loài. Có chứng minh + phân tích tại sao giám sát phân cấp + contrastive khuyến khích điều này.

## Dữ liệu & số liệu chính (theo abstract)
- 214M ảnh (TreeOfLife-200M).
- Mục tiêu hẹp (phân biệt loài) nhưng "extraordinary accuracy" cho các task sinh học khác (phân loại habitat, dự đoán trait) — emergent.
- Abstract chưa nêu số chính xác per-benchmark; cần đọc bảng PDF để lấy con số so với BioCLIP gốc và Pl@ntCLEF/BioTrove (chưa kiểm chứng trong lượt này).

## Hạn chế
- Dữ liệu TreeOfLife-200M chủ yếu iNaturalist (English common names, phân bố khu vực); chưa đánh giá trực tiếp trên cây thuốc Việt Nam.
- Quy mô lớn (200M) → huấn luyện lại không khả thi cho một người; **dùng làm backbone frozen** thì mới hợp.

## Dùng được gì cho Bài 2
- Là "bản mới nhất của BioCLIP" (mục tiêu task: "BioCLIP (và bản mới nếu có)"). Nếu muốn so 2 backbone: **BioCLIP (10M) vs BioCLIP 2 (200M)** — cùng cách linear probe/few-shot trên ViMeLeaf, đo xem scaling có cải thiện trên cặp loài dễ nhầm không.
- Tính "intra-species variation preserved" rất khớp với Bài 2: cùng một loài có nhiều kiểu lá (mặt trên/dưới, non/trưởng thành) không bị coi là loài khác → hữu ích khi gộp nhiều khung hình video.
- Ghi chú: nếu BioCLIP 2 chưa có checkpoint sẵn dễ dùng, ưu tiên BioCLIP gốc (MIT) làm baseline khả thi; BioCLIP 2 để so khi có resource.
