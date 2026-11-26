# Tổng hợp: mô hình nền & MLLM cho nhận dạng loài cây (Bài 2 ViMeLeaf)

Issue: RES-49 (con của RES-38, chuỗi Bài 2). Người viết: Scholar. Ngày: 2026-11-26.
Đọc 7 bài (đã mở được DOI/link, xem `units/research/papers/*.md`): BioCLIP (2311.18803), BioCLIP 2 (2505.23883), DINOv2 (2304.07193) + SimDINOv2-Plantae (2604.27538), CLIP zero-shot species (2310.09929), BioTrove (2406.17720), MLLM medicinal-plant benchmark (Jiang, DOI 10.3389/fpls.2026.1765281), Conformal long-tail (2507.06867) + TaxoNet (2512.18994) + Digital Taxonomist (2106.03774).
Mọi số liệu trích từ abstract/full-text đã mở; chưa chạy lại trên ViMeLeaf → ghi "chưa kiểm chứng".

## Câu hỏi (1): mô hình nào làm baseline, cấu hình gì

**Khuyến nghị: BioCLIP (frozen) + linear probe / k-shot prototype làm baseline chính.**

| Backbone | Vì sao chọn/bỏ | Cấu hình đề xuất |
|---|---|---|
| **BioCLIP (10M, MIT)** | Đặc trưng sinh học (cây+động+vật+nấm) → hợp cây; checkpoint sẵn, nhẹ, chạy được GPU 8–12GB. Trùng với "foundation model cho cây" (B8) nhưng có ngôn ngữ + hierarchical | frozen, linear probe (không train backbone); k-shot {1,5,10} bằng prototype; macro-F1 (không top-1, do 72 loài đuôi); so split ngẫu nhiên vs chống rò rỉ |
| **BioCLIP 2 (200M)** | Bản mới, "emergent" (giữ intra-species variation trong subspace trực giao) → hợp gộp nhiều khung hình video + cùng loài nhiều kiểu lá | chỉ so khi có resource; nếu chưa checkpoint dễ dùng thì bỏ, giữ BioCLIP gốc |
| **DINOv2 (không ngôn ngữ)** | Đối chứng: đặc trưng tổng quát, không sinh vật → đo "lợi thế sinh học" của BioCLIP | frozen, linear probe, cùng cách; **khử trùng gần trùng bằng cosine DINOv2** (kỹ thuật Bài 1 dùng) |
| **SimDINOv2-Plantae (2604.27538)** | SSL cây, affine/posterization (không blur/grayscale); iNaturalist-Plantae mạnh hơn ImageNet | fine-tune head nhẹ trên ViMeLeaf để đo "domain-specific SSL data có transfer sang cây thuốc Việt không" (câu hỏi mới) |
| **CLIP zero-shot (2310.09929)** | Mốc rẻ, chạy local, không train; prompt bằng common name (tên thường) thay tên Latin (2–5× accuracy) | đóng băng OpenCLIP; prompt bằng **tên Việt + khoa học**; đo top-1/macro-F1 zero-shot để so với có-train |

Kết luận: baseline = **BioCLIP frozen + linear probe 5-shot** làm mốc; đối chứng = DINOv2 frozen, SimDINOv2-Plantae fine-tune, CLIP zero-shot. Nếu muốn so scaling, thêm BioCLIP 2.

## Câu hỏi (2): MLLM có "tự tin sai" không, có bài đo calibration/từ chối không

**Có bằng chứng MLLM sai 100% trên cặp loài dễ nhầm (cùng họ/chi), nhưng không có bài đo calibration/từ chối của MLLM cho cây thuốc → khoảng trống Bài 2 lấp.**

- Bằng chứng (Jiang 2026, full text): MLLM 4-lựa chọn đạt 85–90,5% tổng thể nhưng **sai 100% trên *Anoectochilus roxburghii*, *Salvia przewalskii*, *Berberis* spp.** (cùng họ/chi, khác nhẹ gân lá), 80% trên 7 loài khác. 36 loài dễ phân biệt đạt 100%. → **hiện tượng "confidently wrong" trên confusable pairs đúng như task hỏi.**
- **Khoảng trống:** Jiang **không đo** calibration (ECE/temperature), **không có cơ chế từ chối**, không so baseline CV, format 4-lựa chọn đơn giản hơn open-set. → Bài 2: đặt **selective prediction / từ chối** làm trục chính, vì MLLM raw không biết "đang ở cặp nguy hiểm".
- Bài đo calibration/từ chối **có guarantee** để so: **Conformal long-tail (2507.06867)** — prevalence-adjusted softmax + interpolation, chạy Pl@ntNet-300K (1081 lớp) & iNat-2018 (8142 lớp). Dùng làm khung "từ chối có guarantee" so với MLLM raw.
- Bài open-set cây thuốc gần nhất: **Sinha 2025 (2502.17289)** — phân cấp phylum→species, unknown species accuracy phylum 83,36% → family 43,32% (tụt mạnh xuống mức loài) → bằng chứng "loài lạ vẫn yếu" (trùng với brief-novelty B6).
- Cẩn thận (brief-novelty B9): **từ chối không tự động an toàn** (automation bias: người dùng bỏ sót cảnh báo khi AI từ chối). Bài 2 phải đo **tỉ lệ nhầm nguy hiểm ở mức coverage 90%** + hiệu ứng người dùng, không chỉ AURC.

## Câu hỏi (3): kỹ thuật đuôi dài nào phổ biến

Ba hướng chính (từ các bài đọc + task liệt kê):
1. **Logit adjustment / prevalence-adjusted** — hiệu chỉnh logit theo tỉ lệ lớp; biến thể hiện đại: **prevalence-adjusted softmax** (2507.06867, tối ưu macro-coverage).
2. **Balanced / dual-margin** — **dual-margin objective** (TaxoNet, 2512.18994) thay đổi decision boundary theo tần suất lớp trong không gian embedding; cùng họ với logit adjustment nhưng ở embedding.
3. **Re-sampling** — over-sample hiếm / under-sample phổ biến (kỹ thuật kinh điển; không có trong 7 bài trên, ghi "chưa kiểm chứng trong phạm vi này").

Áp cho ViMeLeaf (72 loài < 100 ảnh / 165): **logit adjustment + prevalence-adjusted softmax + từ chối conformal** là bộ hợp lý nhất; dual-margin nếu muốn fine-tune. Re-sampling dùng phụ, không làm chính (dễ overfit do ảnh hiếm quá ít).

## Khoảng trống mà Bài 2 lấp (tóm)

- Không bài nào **mô hình nền + từ chối có guarantee + gắn an toàn khi nhầm** cho cây thuốc Việt/ĐNA:
  - MLLM (Jiang): không từ chối, không calibration, dataset riêng không công khai, tên tiếng Trung.
  - Foundation model plant (BioCLIP/BioCLIP2/SimDINOv2/PlantCLEF): chưa đánh giá **cặp dễ nhầm + an toàn + OOD điện thoại** trên cây thuốc Việt.
  - Conformal long-tail (2507.06867): có guarantee nhưng **không gắn độc tính / cặp nguy hiểm**, dataset tổng quát (Pl@ntNet/iNat).
- Điểm mới của Bài 2: **benchmark cặp dễ nhầm có nhãn an toàn (Dây giác/Sục sạc) + đường risk-coverage conformal + OOD điện thoại + tỉ lệ nhầm nguy hiểm ở coverage cố định**; so MLLM raw (Jiang) với foundation model + từ chối.

## Việc tiếp theo (giao RES-38, không tự chạy)

- [ ] Chạy baseline BioCLIP/DINOv2 frozen + linear probe 5-shot trên split chống rò rỉ ViMeLeaf, macro-F1 + AURC (Critic/Builder).
- [ ] Chạy MLLM (GPT-4o/Gemini/Qwen) trên 10–20 cặp ViMeLeaf dễ nhầm, ghi error-rate + đo "confidently wrong".
- [ ] Áp prevalence-adjusted softmax / conformal làm lớp từ chối; so threshold-naive; đo AURC + tỉ lệ nhầm nguy hiểm @ coverage 90%.
- [ ] Cần **chuyên gia dược** đánh dấu cặp nào nhầm = nguy hiểm (độc/không dùng) để đo được "an toàn khi nhầm"; nếu chưa, thu hẹp claim thành "risk-coverage trên cặp đã chọn".
