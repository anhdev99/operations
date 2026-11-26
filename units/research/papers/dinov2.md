# DINOv2 (và SimDINOv2 trên dữ liệu cây)

## 1) DINOv2: Learning Robust Visual Features without Supervision
- **Tác giả / năm / nơi:** Maxime Oquab, Timothée Darcet, Théo Moutakanni, Huy Vo, Marc Szafraniec, et al. (25 tác giả, Meta AI, 2023).
- **Trích dẫn:** arXiv:2304.07193 (v2 02/02/2024). DOI https://doi.org/10.48550/arXiv.2304.07193 · link đã mở: https://arxiv.org/abs/2304.07193 (abstract + metadata; HTML full-text sẵn).

### Bài toán
Đặc trưng ảnh "all-purpose" không cần giám sát, dùng lại được nhiều task/distribution mà không fine-tune.

### Phương pháp
Self-supervised (SSL), ViT-1B huấn luyện trên dataset tự curate + đa nguồn; distill thành các model nhỏ hơn (S/B/L/giant). Trùng ảnh gần bằng cosine đặc trưng DINOv2 (kỹ thuật dùng trong pipeline khử trùng của Bài 1).

### Số liệu chính (theo abstract)
- DINOv2 (các size) "surpass OpenCLIP on most benchmarks at image and pixel level" (abstract). Chưa có số per-benchmark ở abstract.

### Hạn chế
- Huấn luyện trên dữ liệu tự giám sát tổng quát (không phải sinh vật) → đặc trưng chưa tối ưu cho fine-grained plant species; cần kiểm chứng trên cây.

## 2) SimDINOv2 trên dữ liệu cây (dùng làm "linear probe trên dữ liệu thực vật")
- **Tác giả / năm:** Ilyass Moummad, Kawtar Zaher, Hervé Goëau, Jean-Christophe Lombardo, Pierre Bonnet, Alexis Joly (2026).
- **Trích dẫn:** arXiv:2604.27538 (v2 29/06/2026), "Self-Supervised Learning of Plant Image Representations". DOI https://doi.org/10.48550/arXiv.2604.27538 · link đã mở: https://arxiv.org/abs/2604.27538 (abstract).

### Phát hiện chính (theo abstract)
- Tăng cường thông dụng trong SSL (Gaussian blur, grayscale, solarization) **có hại** cho ảnh cây vì xoá mất tín hiệu fine-grained. Đổi sang affine + posterization thì hợp hơn cho cây.
- Huấn SimDINOv2 trên **iNaturalist 2021 Plantae** (không phải ImageNet-1K) → đặc trưng mạnh hơn rõ, nhất quán trên ViT-Base và ViT-Large.
- Trong **few-shot**, mô hình của họ "competitive / sometimes outperform" các baseline giám sát mạnh **Pl@ntCLEF** và **BioCLIP** (tên được nêu trong abstract; số chưa ghi, chưa kiểm chứng).

### Dùng được gì cho Bài 2
- **So backbone cho Bài 2:** (a) BioCLIP (cây sinh vật + ngôn ngữ), (b) DINOv2 (không sinh vật, không ngôn ngữ), (c) SimDINOv2-Plantae (SSL cây, affine/posterization).
- Cấu hình đề xuất: **frozen + linear probe**, k-shot (1/5/10) bằng prototype, đo trên split chống rò rỉ + cặp dễ nhầm + 72 loài đuôi (<100 ảnh). Macro-F1 thay top-1 do mất cân bằng.
- Nếu có đủ GPU: fine-tune SimDINOv2-Plantae head nhẹ trên ViMeLeaf để đo hiệu ứng "domain-specific SSL data" (iNaturalist Plantae) có transfer được sang cây thuốc Việt không — câu hỏi mới, chưa ai đo trên ViMeLeaf.
