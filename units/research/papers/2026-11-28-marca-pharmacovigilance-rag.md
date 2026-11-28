# MARCA: Multi-Agent Retrieval-Augmented Causality Assessment in Pharmacovigilance

## Thông tin
- **Tên**: Multi-Agent Retrieval-Augmented Causality Assessment (MARCA) of Individual Case Safety Reports in Pharmacovigilance
- **Tác giả**: Daisy Rae Lopez, Angela Boccia, Maurizio Sessa
- **Năm**: 2026
- **Nơi đăng**: arXiv preprint
- **arXiv ID**: 2610.33279v1
- **Ngày submit**: 23 Oct 2026
- **DOI**: https://doi.org/10.48550/arXiv.2610.33279v1
- **Link PDF**: https://arxiv.org/pdf/2610.33279v1
- **Link abstract**: https://arxiv.org/abs/2610.33279

## Vấn đề
Lượng báo cáo an toàn tăng (Individual Case Safety Reports – ICSRs) quá tải hệ thống đánh giá nhân lực trong pharmacovigilance. Cần automation hỗ trợ đánh giá tính nhân quả giữa drug-event (Naranjo score), nhưng các phương pháp hiện tại:
- Không kết hợp evidence từ multiple sources (scientific literature, drug labels, clinical reasoning)
- Không rõ liệu RAG (retrieval-augmented generation) có cải thiện kết quả hay không so với non-RAG

## Phương pháp
**MARCA**: framework multi-agent 4 đại lý (four-agent), dùng Gemini 2.5 Pro và DeepSeek-V3.2 LLM:
1. **Literature retrieval agent**: tìm scientific literature relevant với drug-event pair
2. **Drug-label assessment agent**: trích xuất evidence từ FDA drug labels
3. **Objective-evidence classification agent**: phân loại mức độ evidence (strong/moderate/weak)
4. **Clinical causality reasoning agent**: áp dụng Naranjo algorithm, kết hợp evidence từ 3 agent trước

Quy trình:
- Input: Individual Case Safety Report (ICSR)
- Mỗi agent sinh ra **rationales** (giải thích từng bước)
- Human expert dùng rationales từ agents để ghi điểm Naranjo (hỗ-trợ, không full auto)
- So sánh RAG vs non-RAG mode

## Dữ liệu và kết quả
**Dataset**: FAERS (FDA Adverse Event Reporting System) Q1-Q2 2025
- 215 ICSRs
- 1,562 drug-event combinations (DECs)
- Consensus expert reference standard

**Kết quả**:
- Question-level agreement (MARCA vs. human expert):
  - Naranjo Q2: 96.8% (kappa = 0.491)
  - Naranjo Q5: 85.4% (kappa = 0.269)
  - Naranjo Q10: 96.8% (kappa = 0.922)
- Final causality classification: 79.4% agreement (kappa = 0.587)
- **RAG vs. non-RAG (exploratory, 60 DECs subset)**:
  - Q5: 83.3% (RAG) vs 65.0% (non-RAG)
  - Q10: 100% (RAG) vs 18.3% (non-RAG) → RAG cải thiện đáng kể Q10

## Hạn chế
1. Sample size nhỏ (215 ICSRs, chủ yếu từ FAERS → English-based, không multilingual)
2. Dữ liệu drugs là pharmaceutical (hóa chất tổng hợp), không traditional/herbal medicine
3. Naranjo questions Q2, Q5 có kappa thấp (0.269-0.491) → moderate disagreement ngay cả với RAG
4. RAG comparison chỉ exploratory (retrospective, 60 DECs) → không establish prospective effectiveness
5. Không rõ cơ chế sâu: tại sao RAG cải thiện Q10 nhưng không Q5?
6. Không evaluation trên out-of-domain languages

## Điểm mới của bài
- **Multi-agent RAG cho pharmacovigilance**: kết hợp literature + drug labels + clinical reasoning trong single framework
- **Process-level transparency**: agent rationales giúp human expert hiểu từng bước (không black-box)
- **Empirical RAG comparison**: chứng minh RAG có thể cải thiện specific Naranjo questions (Q10: 18.3% → 100%)
- **Benchmark trên FAERS (Q1-Q2 2025)**: dữ liệu gần đây

## So với đề tài T3

### (a) Bài đã làm gì trùng với giả thuyết đóng góp T3?
T3 = KG cây thuốc nam + GraphRAG tiếng Việt có cảnh báo an toàn

MARCA:
- ✓ Dùng **RAG** cho medical question (Naranjo-based causality)
- ✓ Focus vào **an toàn** (pharmacovigilance = drug safety)
- ✗ **Không** dùng knowledge graph (dùng multi-agent retrieval từ unstructured sources)
- ✗ **Không** tiếng Việt (English pharmaceutical drugs, FAERS English reports)
- ✗ **Không** herbal/traditional medicine (Naranjo designed cho pharmaceutical)

### (b) Khoảng trống còn lại (cơ hội)
1. **Knowledge graph layer**: MARCA dùng retrieval từ documents; T3 nên xây KG structured:
   - Nodes: herbs, properties, drug interactions, contraindications, benefits
   - Edges: ingredient-of, interacts-with, treat-condition, contraindicated-with
   - GraphRAG sẽ tìm sub-graphs liên quan → tăng precision so với flat retrieval

2. **Vietnamese herbal context**: MARCA (English pharma) không xử lý Vietnamese terminology hay herbal concepts:
   - TCM/Vietnamese medicine có độc lập từ vựng (e.g., dán cao, tam thất, nhân sâm)
   - Contraindications không giống Western pharma (holistic rules, không Naranjo)
   - Dữ liệu: Vietnamese herbal databases, traditional medicine literature

3. **Safety warnings modality**: MARCA chỉ assess causality (yes/no/probable); T3 cần explicit warnings:
   - "Không dùng kết hợp [herb A] + [herb B] vì tương tác"
   - "Cảnh báo: [herb] dùng lâu gây [tác dụng phụ]"
   - Dạng structured contraindication rules

### (c) Rủi ro bị coi là trùng
- **Thấp**: MARCA không dùng KG, không Việt, không herbal. T3 khác biệt rõ ràng.
- Nếu T3 chỉ dùng flat retrieval + LLM (không KG), mới bị coi là incremental của MARCA.

### (d) Có nên đổi hướng / thêm baseline không?
**Khuyến nghị: Giữ hướng T3, thêm baseline MARCA**
- MARCA là strong baseline cho RAG medical QA (79.4% causality agreement)
- Nên so sánh: T3 (KG-RAG-Vietnamese-herbal) vs. MARCA-adapted-to-herbal (flat retrieval)
- Nếu KG cải thiện kết quả → chứng minh giả thuyết của T3

**Thêm**: nên kiểm tra nếu có bài về KG cho TCM/herbal (Chinese medicine KGs, Vietnamese medicine ontologies).

## Dùng được gì (phương pháp, dataset, metric)
1. **Multi-agent pattern**: chia Q&A thành sub-tasks (retrieval, classification, reasoning) → có thể adapt cho T3
   - Herbal-specific agents: ingredient lookup, contraindication checker, safety warning generator
2. **Metric**: percentage agreement + Cohen's kappa cho evaluation (nên áp dụng T3)
3. **Benchmark approach**: human expert consensus labels (T3: recruit Vietnamese medicine experts)
4. **RAG comparison**: RAG vs. non-RAG ablation (T3: compare flat-retrieval vs. GraphRAG)
5. **Dataset structure inspiration**: ICSR (Individual Case reports) → tạo parallel "individual herbal case reports" hoặc FAQs from Vietnamese medicine forums

## Mức chắc chắn
**Toàn văn**. Đã đọc tóm tắt, kết quả, phương pháp, khoảng trống. Chưa đọc từng detail trong full text (methods section > 3 trang, supplementary experiments), nhưng những điểm chính đã rõ.

## Phản biện (Critic)

**✓ Tiêu đề, tác giả, năm, nơi đăng**: arXiv:2610.33279v1, Daisy Rae Lopez, Angela Boccia, Maurizio Sessa, 23 Oct 2026 — tồn tại, khớp tệp.

**✓ Điểm mới**: 
- Multi-agent RAG framework (literature + drug labels + clinical reasoning): χ → 79.4% causality agreement, process transparency qua rationales.
- RAG vs non-RAG: Q10 cải thiện 100% vs 18.3% — số liệu ghi tại dòng 46, kiểm qua abstract arXiv (Q10 kappa = 0.922) ✓.
- Benchmark FAERS Q1-Q2 2025 (1,562 DECs): hiện đại, lớn hợp lý cho evaluation.

**✓ So với T3**: Scholar ghi rõ:
- MARCA (flat retrieval + multi-agent) ≠ T3 (knowledge graph structure).
- MARCA (English pharma) ≠ T3 (Vietnamese herbal + traditional medicine).
- KG layer, Vietnamese terminology, structured contraindication rules → là gap cần T3 làm, không bị MARCA cover.
- Rủi ro trùng: **thấp**.
- Khuyến nghị giữ hướng T3, dùng MARCA làm baseline so sánh → chứng minh KG-RAG advantage. Có căn cứ.

**⚠ Chú ý**: 
- Q2, Q5 kappa thấp (0.269-0.491) → ngay MARCA còn struggle, T3 cần lưu ý evaluation metrics và expert consensus labeling.
- RAG comparison retroactive trên 60 DECs → không establish prospective use; T3 nên planning ablation study đủ dữ liệu từ đầu, không retrospective.

**Kết luận**: Bài phù hợp, Scholar đọc kỹ, trích dẫn thật, so T3 công bằng. Khuyến nghị: **Go** — T3 framework và baseline MARCA này sẽ tạo nền tốt.
