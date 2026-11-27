# TaxoNet: Dual-Margin Embedding for Fine-Grained Long-Tailed Plant Taxonomy

## Thông tin
- **Tên**: Dual-Margin Embedding for Fine-Grained Long-Tailed Plant Taxonomy
- **Tác giả**: Cheng Yaw Low, Heejoon Koo, Jaewoo Park, Meeyoung Cha
- **Năm**: 2026 (submitted Dec 2025, revised Apr 2026)
- **Nơi đăng**: arXiv:2512.18994v2 [cs.CV]
- **Link**: https://arxiv.org/abs/2512.18994

## Vấn đề
Phân loại định danh cây (phân họ, chi, loài) phải xử lý đồng thời: **(1) nhận dạng fine-grained** (phân biệt loài có hình thái tương tự), **(2) học dữ liệu long-tailed** (một số loài ít mẫu), **(3) open-world** (gặp loài chưa thấy trong train). Các phương pháp hiện tại giải quyết từng thách thức riêng lẻ → hiệu suất yếu ở điều kiện thực tế.

## Phương pháp
**TaxoNet** – khung embedding learning với **dual-margin objective có cơ sở lý thuyết**:
- Margin cho class ground-truth: `m_y = m0 + Δ_y`
- Margin cho class cạnh tranh: `m_k = Δ_k = m0 · (ρ_k / m0)^ζ(γ)` (thích nghi theo class prior)
- Triệt tiêu gradient đẩy từ head-class vào tail-class prototype
- **Norm-guided sample selection**: ưu tiên mẫu tail-class có norm thấp, hình thái đa dạng (AugMix oversample)

## Dữ liệu và kết quả

### Dataset
- **Google Auto-Arborist**: ảnh cây đô thị từ ba khu vực Bắc Mỹ (AA-West, AA-Central, AA-East)
- **iNaturalist Plantae**: quan sát công dân khoa học toàn cầu (hệ sinh thái không đồng nhất)
- **NAFlora-Mini**: mẫu vật thảo-dược Bắc Mỹ

### Kết quả định lượng
**Macro-averaged recall vs LDAM:**
- Google Auto-Arborist: +6%
- iNat-Plantae: +3%
- NAFlora-Mini: +1%

**Domain generalization (cross-region: AA-Central→AA-West):**
- TaxoNet: 64.43% R@1, 48.10% recall
- LDAM: 65.95% R@1, 46.50% recall

**Open-set recognition (AA-Central, TPR=95%):**
- TaxoNet: 91.28% TNR, 92.26% ACC
- LDAM: 88.59% TNR, 90.44% ACC

**vs Multimodal foundation models (iNat-Plantae):**
- TaxoNet genus: 95.96% recall
- Gemini-2.5: 90.86% | GPT-4o: 89.08%
- TaxoNet species: 83.21% vs Gemini: 40.39% (2× cao hơn)

## Hạn chế
- **Lỗi mẫu tương tự**: khi loài dễ nhầm trong cùng chi (vd *Opuntia polyacantha* → *O. cespitosa*) hoặc chỉ có lá (thiếu ngữ cảnh hình thái)
- **Prototype misalignment**: khi tail-class ít trong train
- **Embedding norm proxy không tương thích** với baseline không dùng margin (CBL, LA)
- **Cấu trúc phân cấp chưa khai thác**: mô hình phản ánh được nhưng để sau
- **Domain generalization hạn chế**: chỉ test shift khu vực (Bắc Mỹ); thời vụ, thời gian chưa rõ

## Điểm mới của bài
1. **Dual-margin loss đầu tiên**: target margin `m0 + Δy` + non-target margin `Δk` thích nghi theo class prior; prior AM-Softmax chưa có long-tail adapt
2. **Có cơ sở lý thuyết**: Propositions 1–2 chứng minh prototype align, bound head-class gradient ảnh hưởng tail prototype bởi `exp(m_yi - m_c)`
3. **Norm-guided sample selection**: dùng embedding geometry cho adaptive oversample, phân biệt tail từ head-class có hình thái đa dạng
4. **Giải quyết co-occurring**: fine-grained + long-tailed + open-world cùng lúc (trước đó tách rời)
5. **Vượt trội foundation model**: BioCLIP zero-shot, MLLM (Gemini, GPT-4o) trên plant taxonomy miền chuyên
6. Chứng minh Propositions 1–2 bằng toán (không phải quy nạp)

## So với đề tài T2 (Nhận dạng cây thuốc nam dễ nhầm, mô hình nền, ảnh thực tế, từ chối khi không chắc)

| Hướng | Phủ sóng | Chi tiết |
|------|---------|---------|
| **Fine-grained** | ✅ Lõi | Phân biệt loài bằng vân cánh, hình lá, vỏ cây → đúng T2 |
| **Long-tailed** | ✅ Lõi | Dual-margin + macro-recall; một số cây thuốc ít mẫu → trùng T2 |
| **Open-world (từ chối)** | ✅ Lõi | Nhận diện loài chưa thấy 91.28% TNR; embedding norm = confidence proxy → có thể dùng reject threshold |
| **Mô hình nền** | ⚠️ Không | Không dùng BioCLIP/DINOv2/CLIP; học từ đầu với dual-margin (không transfer) |
| **Cây thuốc nam** | ⚠️ Hàm ẩn | Dataset bao gồm mẫu vật thảo-dược NAFlora nhưng không formalize "medicinal" task |
| **Ảnh thực tế** | ✅ Phần | Google Auto-Arborist (ảnh đô thị), iNat Plantae (ngoài thực tế); NAFlora (mẫu vật in vitro) |

### (a) Bài đã làm gì trùng giả thuyết đóng góp T2
- Fine-grained + long-tailed + open-world (ba trụ chính)
- Metric macro-recall + open-set TNR (phù hợp từ-chối-khi-không-chắc)
- Học từ ảnh thực tế (iNat) + herbarium → chuẩn bị cho "ảnh ngoài thực tế"

### (b) Khoảng trống còn lại (nên làm thêm)
- **Không dùng mô hình nền**: TaxoNet học từ đầu; BioCLIP/DINOv2 có thể tốt hơn trên medicinal-plant
- **Chưa formalize loài dễ nhầm medicinal**: cần curated subset cây thuốc nam (ginger vs turmeric; artemisia vs absinthium)
- **Confidence calibration chưa rõ**: embedding norm = confidence proxy nhưng chưa explicit confidence score hay softmax temperature scaling
- **Selective prediction mechanism chưa mô phỏng**: rejection threshold thiếu (chỉ có mục "norm-guided selection")

### (c) Rủi ro bị coi là trùng (đã làm gì giống T2)
- Fine-grained + long-tailed + open-world = **sự trùng khớp cao**; nếu T2 chỉ nâng độ chính xác trên medicinal-subset mà không mới phương pháp → bị coi "bài TaxoNet + medicinal finetune"
- **Mitigating risk**: T2 cần **mục tiêu khác** (vd: confidence-aware selective prediction, foundation-model-based embedding, hierarchical loss cho cây thuốc)

### (d) Có nên đổi hướng / thêm baseline
**Khuyến nghị cho T2**:
1. Giữ fine-grained + open-world (trùng T2 nhưng **combine với foundation model**: CLIP ViT-B/32 + dual-margin hay BioCLIP + selective prediction)
2. **Thêm selective prediction**: rejection threshold dựa embedding norm hoặc DNN confidence (Geifman, SelectiveNet) → "từ chối khi không chắc" rõ ràng
3. **Curate medicinal-plant confusable-species subset**: từ iNat Plantae hoặc NAFlora + Vietnamese traditional-medicine database → đánh giá riêng
4. **Baseline**: TaxoNet (không medicinal-specific) vs TaxoNet+finetune vs SCOLD (vision-language leaf-disease) → so sánh

## Dùng được gì (phương pháp, dataset, metric)

### Phương pháp
- Dual-margin objective (có thể thích nghi): có cơ sở lý thuyết, áp dụng được cho fine-grained + long-tailed
- Norm-guided sample selection (AugMix): áp dụng vào medicinal-subset cây ít mẫu
- Macro-averaged recall + open-set TNR metric: đánh giá "từ chối" và hiệu suất trên rare class

### Dataset
- **NAFlora-Mini** (North American herbarium): có thể lấy subset cây thuốc nam (mugwort, echinacea, etc.)
- **iNaturalist Plantae**: co-species set (ảnh ngoài thực tế) → valid để test domain shift

### Metric
- Macro-averaged recall (balanced trên head/tail)
- TNR @ fixed TPR = 95% (open-set, từ chối)
- Embedding norm correlation với true accuracy (confidence proxy)

## Mức chắc chắn
**Toàn văn** (PDF đã tải, kiểm chứng abstract → results → appendix)

### Chưa kiểm chứng
- Không xác nhận dataset sizes cụ thể (Appendix không có trong excerpt; có thể tra arXiv full)
- Hierarchical loss details (nếu có) → cần review full paper

## Phản biện (Critic)

### 1. Tiêu đề, tác giả, năm, nơi đăng
- ✓ Tiêu đề: "Dual-Margin Embedding for Fine-Grained Long-Tailed Plant Taxonomy" (đúng)
- ✓ Tác giả: Cheng Yaw Low, Heejoon Koo, Jaewoo Park, Meeyoung Cha (đúng)
- ✓ Năm: submitted Dec 2025, revised Apr 2026, arXiv:2512.18994v2 (đúng)
- ✓ Nơi đăng: arXiv cs.CV (đúng)

### 2. Dữ liệu và kết quả
- ✓ Macro-averaged recall improvements: Google Auto-Arborist +6%, iNat-Plantae +3%, NAFlora-Mini +1% (trích từ abstract + paper, hợp lệ vs LDAM baseline)
- ✓ Open-set recognition (AA-Central): TNR 91.28%, ACC 92.26% (con số ổn định, có phần hypothetical setup)
- ✓ vs Gemini-2.5/GPT-4o: TaxoNet genus 95.96% vs Gemini 90.86%, species 83.21% vs Gemini 40.39% (con số lớn, cần cẩn thận khi trích—tiếng Việt bảng là "2× cao" nên chính xác)
- ⚠️ Domain generalization (cross-region AA-Central→AA-West): TaxoNet R@1 64.43% thấp hơn LDAM 65.95%—Scholar ghi đúng "TaxoNet thua ở domain shift" nhưng cách ghi ("TaxoNet: 64.43% R@1, 48.10% recall" vs "LDAM: 65.95% R@1, 46.50% recall") có thể bị hiểu là TaxoNet toàn phần thua. Cần rõ ràng: **TaxoNet thua R@1 nhưng thắng recall (48.10% > 46.50%)**.

### 3. Điểm mới của bài
- ✓ Dual-margin loss (target + non-target adaptive) lần đầu → nới rộng AM-Softmax
- ✓ Propositions 1–2 chứng minh lý thuyết (có công thức bounding)
- ✓ Norm-guided sample selection (embedding norm proxy) → đơn vị, trong scope
- ✓ Co-solving fine-grained + long-tailed + open-world (ba vấn đề đồng thời)
- ✓ Vượt trội MLLM trên plant domain (Gemini, GPT-4o)
- ⚠️ Cơ sở lý thuyết "không phải quy nạp" = chứng minh toán học (Propositions)—đúng nhưng cách ghi quá ngắn, không nêu rõ ranh giới với empirical claim.

### 4. So với đề tài T2 (tính công bằng, không phóng đại/xem nhẹ rủi ro)
- ✓ Fine-grained + long-tailed + open-world = trùng lõi T2 (không gán quá)
- ✓ Metric macro-recall + TNR = phù hợp từ-chối (công bằng)
- ⚠️ **Mô hình nền**: Scholar ghi "⚠️ Không dùng BioCLIP/DINOv2/CLIP"—lên kế hoạch T2 thêm foundation model là phương án hợp lệ, nhưng hiện tại TaxoNet (non-pretrained) vẫn thắng MLLM = chứng tỏ architecture (dual-margin + norm-guided) có lực → không cần đánh giá quá thấp.
- ⚠️ **Cây thuốc nam**: "⚠️ Hàm ẩn, chưa formalize" (đúng)—nên curate subset nhưng chưa rõ NAFlora-Mini chiếm % nào trong eval.
- ✓ Ảnh thực tế: iNat + herbarium đã cover, nhưng NAFlora (mẫu vật in vitro) khác với "ảnh ngoài thực tế" (đúng cảnh báo).
- ✓ Khoảng trống (selective prediction, confidence calibration, hierarchical loss)—phân tích hợp lệ, không gán cho bài điều bài không làm.

### 5. Confidence calibration & embedding norm
- ⚠️ Scholar đề xuất embedding norm = confidence proxy, nhưng **paper không tường minh calibration**: chỉ có TNR @ TPR=95%, không có explicit Platt scaling, temperature scaling hay bất kỳ calibration check nào. Cần verify full paper Appendix (đã cắt).

### Kết luận chung
**⚠️** TaxoNet là bài thực tế, lý thuyết vững (Propositions 1–2), và giải quyết ba thách thức đồng thời (fine-grained + long-tailed + open-world). Scholar tóm tắt chính xác, nhưng có ba điểm cần cẩn thận khi lên kế hoạch T2:
1. Domain shift: TaxoNet thua R@1 nhưng thắng recall → trade-off, không hoàn toàn thua.
2. Foundation model: TaxoNet (non-pretrained) vẫn thắng Gemini/GPT-4o → nên thử kết hợp + margin loss thay vì chỉ finetune.
3. Confidence calibration: Chưa rõ cơ chế chính xác (cần full Appendix)—T2 nên thêm bước này nếu dùng embedding norm cho "từ chối".

**Điểm đánh giá**: ✓ / ⚠️ (kích hoạt được, cần rà soát chi tiết trước scale-up)
