# BioCLIP: A Vision Foundation Model for the Tree of Life

- **Tác giả / năm / nơi:** Samuel Stevens, Jiaman Wu, Matthew J Thompson, Elizabeth G Campolongo, Chan Hee Song, David Edward Carlyn, Li Dong, Wasila M Dahdul, Charles Stewart, Tanya Berger-Wolf, Wei-Lun Chao, Yu Su (2023; CVPR 2024, oral camera-ready).
- **Trích dẫn:** arXiv:2311.18803 (v3 14/05/2024). DOI https://doi.org/10.48550/arXiv.2311.18803 · link đã mở: https://arxiv.org/abs/2311.18803 (abstract + metadata; PDF/HTML full-text sẵn). Code/dữ liệu: https://imageomics.github.io/bioclip, mô hình trên HuggingFace `imageomics/bioclip` (MIT).

## Bài toán
Nhận dạng sinh vật (cây, động vật, nấm) từ ảnh tự chụp (điện thoại, drone) ở quy mô lớn; mô hình phải tổng quát hoá được nhiều câu hỏi sinh học, không bespoke theo từng task.

## Phương pháp
Mô hình nền CLIP-họ (contrastive vision-language) được huấn luyện trên **TreeOfLife-10M**, bộ ảnh sinh vật ML-ready lớn nhất và đa dạng nhất lúc đó (cây + động vật + nấm). Đặc trưng "hierarchy-aware": tận dụng cấu trúc sinh học (cây phân loại) trong dữ liệu. So với CLIP thường (huấn trên web) có lợi thế ở miền sinh vật vì dữ liệu huấn luyện là ảnh thực vật/động vật/nấm thật, không phải web-generic.

## Dữ liệu & số liệu chính (theo abstract)
- Bộ TreeOfLife-10M: ~10M cặp ảnh-định danh sinh vật (đã mở metadata; quy mô exact không ghi ở abstract, chưa kiểm chứng lại trong PDF).
- Benchmark fine-grained biology classification: BioCLIP "xoutperforms baselines 16–17% absolute" (abstract). Chưa có số per-task trong abstract; muốn con số cụ thể phải đọc bảng PDF.
- Intrinsic evaluation: embedding học được **cấu trúc phân cấp theo tree of life** (giải thích độ tổng quát hoá).

## Hạn chế
- Ảnh chụp từ iNaturalist/nguồn research-grade; chưa đánh giá trực tiếp trên **ảnh lá cây thuốc Việt Nam** (ViMeLeaf).
- Abstract không nêu số liệu long-tail hay confounding species; đó là đóng góp của bản tiếp theo (BioCLIP 2 / BioTrove, xem tệp riêng).

## Dùng được gì cho Bài 2
- **Baseline chính khuyến nghị:** BioCLIP (frozen) + linear probe / k-prototype (1/5/10-shot) trên split chống rò rỉ của ViMeLeaf. Chiêm lợi: đặc trưng sinh học → tốt cho cặp loài trông giống (Dây giác/Sục sạc).
- So sánh đối chứng: DINOv2 frozen + linear probe (xem tệp dinov2), CLIP zero-shot (xem tệp clip-zero-shot-species).
- Nếu cần chạy nhanh trên GPU 8–12GB: dùng BioCLIP ViT-B/S đóng băng, chỉ train head (linear probe / LoRA nhẹ).
