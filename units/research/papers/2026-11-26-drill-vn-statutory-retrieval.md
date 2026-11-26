# Structure and Lineage Evidence for Vietnamese Statutory Article Retrieval on DRiLL

Đề tài so sánh: **T1 EduReg-Time** (hỏi đáp quy chế đào tạo tiếng Việt biết hiệu lực văn bản). Ngày đọc: 2026-11-26.

## Thông tin
- Tên: *Structure and Lineage Evidence for Vietnamese Statutory Article Retrieval on DRiLL*
- Tác giả: Duc-Vu Nguyen, Ngan Luu-Thuy Nguyen (University of Information Technology, VNU-HCM)
- Năm: 2026 (nộp arXiv 06/11/2026, v1)
- Nơi đăng: arXiv preprint, cs.IR; **accepted at SOICT 2026** (theo arXiv comment)
- arXiv: 2611.09200 — DOI arXiv: 10.48550/arXiv.2611.09200 (DOI theo quy ước arXiv, chưa mở trang DOI)
- Link: https://arxiv.org/abs/2611.09200 , toàn văn HTML: https://arxiv.org/html/2611.09200v1

## Vấn đề
Truy xuất **Điều luật** (Article) tiếng Việt phù hợp cho câu hỏi pháp lý trên dataset **DRiLL** (VLSP 2025). Câu hỏi: có tồn tại bằng chứng **cấu trúc** (phân cấp Điều–Khoản–Điểm, số hiệu văn bản) và **hệ phả** (amendment, guidance, introduction) giúp truy xuất vượt ra ngoài độ tương đồng từ vựng/nội dung hay không? DRiLL có 59.636 Điều, 2.190 train / 312 dev / 627 test; 24,4% câu hỏi cần nhiều Điều (multi-Article).

## Phương pháp
- **Pipeline** (theo EDM [12]): Top-500 BM25 + BGE-M3 + HyDE + citation expansion → LambdaMART ranker (22 đặc trưng EDM) → Top-100 → LLM-assisted reranking (Qwen2.5-72B-Instruct, 100 pair scores + 1 collective judgment) → Top-10 → LightGBM pointwise selector (threshold τ₀=0.29, τ₁=0.30) → tập Điều cuối (Top-5 qua ngưỡng).
- **Đặc trưng pháp lý thêm** (27, mục 4.3, Bảng 2): ba nhóm:
  1. **Identity / local form** (1–10): khớp số Điều/alias, cue Khoản/Điểm tương thích, số hiệu văn bản, coreference Điều/Khoản/Điểm, log đếm Khoản/Điểm, khớp action sửa đổi.
  2. **Same-law support** (11–13): tỉ lệ, max, mean điểm của các ứng viên cùng văn bản luật trong pool.
  3. **Citation / lineage** (14–27): incoming/outgoing max/sum/mean từ điểm citation; introduced-ID (suffix chữ cái); typed outgoing/incoming (amendment, guidance); amendment-action match.
- **LLM evidence** (mục 4.5): prompt tiếng Việt, Qwen2.5-72B-Instruct, listwise 10 ứng viên, ngân sách 3.000 chữ/Điều, rubric 0–1, trả JSON scores + selected set.
- **Học**: LightGBM `rank_xendcg`, 5 seed, threshold tinh chỉnh trên dev.

## Dữ liệu và kết quả (ghi rõ nguồn trong bài)
- **DRiLL** (ref [17], VLSP 2025): 59.636 Điều; test 627 câu (474 single-Article, 121 two-Article, 32 ≥3).
- **F₂ chính thức** (mục 6.2, Bảng 6, 5-seed mean ± SD):
  - Control (22 đặc trưng EDM): P=57,13 %, R=76,68 %, **F₂=71,77 ± 0,47**
  - Proposed (22 + 27 đặc trưng pháp lý): P=59,11 ± 0,35, R=77,43 ± 1,03, **F₂=72,91 ± 0,68** (ΔF₂=+1,14 pp, p_BH=0,00078)
  - So với EDM (ref [12]): F₂=72,61 → proposed +0,30 pp (so sánh mô tả, khác cấu hình).
- **R@k** (mục 6.1, Bảng 4): R@10 87,33→88,27 (+0,95), R@100 96,75→97,52 (+0,77, có ý nghĩa thống kê sau BH).
- **Theo kích thước gold set** (mục 7.2, Bảng 8): two-Article F₂,q 61,34→65,79 (+4,45 pp, 61 thắng/42 hoà/18 thua); single-Article +0,42 pp; ≥3 +2,89 pp.
- **Độ quan trọng đặc trưng** (mục 7.1, Bảng 7, split-gain % selector): same-law 8,04 ± 0,57; citation/lineage 7,28 ± 0,32 (local references 4,83 + intro/amendment/guidance 1,32); identity/form 2,87 ± 0,16. Tổng đặc trưng pháp lý thêm: **18,20%** split-gain selector.
- **Case** (mục 7.2, Bảng 9–10):
  - Câu hỏi hồ sơ (Q8360): base Circular 26/2014/TT-BCT Điều 12 + amendment Circular 14/2018/TT-BCT Điều 1(6). Proposed lấy đủ cả hai gold trong 4/5 seed (control chỉ lấy base).
  - Câu hỏi thừa kế (Q411): proposed loại được Điều cùng luật gây nhiễu trong 5/5 seed, nhưng vẫn thiếu Điều 650.

## Hạn chế (tự ghi trong bài, mục 8)
- Chỉ đánh giá trên **DRiLL**, chưa cross-dataset validation.
- **Chưa có ablation** từng nhóm/từng đặc trưng pháp lý riêng lẻ; split-gain không bằng chứng nhân quả.
- First-ranker control/proposed **không capacity-matched**; selector dùng threshold dev khác nhau.
- Đặc trưng lineage (action tags, amendment cues) **không kiểm chứng lịch sử pháp lý hay ngày hiệu lực** — chỉ là tín hiệu liên quan.
- Không đo latency/chi phí API.
- Prompt LLM tiếng Việt, nhưng không so với LLM khác; chỉ Qwen2.5-72B.

## Điểm mới của bài
- Lần đầu (theo bài) dùng **đặc trưng cấu trúc pháp lý + hệ phả (amendment/guidance/introduction)** làm tín hiệu truy xuất Điều luật tiếng Việt trên DRiLL, tách incoming/outgoing citation, đồng luật, và action sửa đổi thành 27 đặc trưng rời.
- **So sánh chặt chẽ**: cùng Top-100, cùng LLM listwise, cùng learner, chỉ khác đặc trưng → F₂ +1,14 pp có ý nghĩa thống kê.
- **Case study** minh hoạ companion recovery (base + amendment) và distractor removal, cho thấy tín hiệu lineage hoạt động thực tế (mục 7.2).
- Phân tích theo kích thước gold set: lợi ích lớn nhất ở **two-Article** (câu cần cả Điều gốc + Điều sửa đổi).

## So với đề tài của mình (T1 EduReg-Time)
- **(a) Trùng với giả thuyết đóng góp**: Bài này **không** làm đồ thị phiên bản hay truy hồi theo mốc thời gian. Nó thêm đặc trưng tĩnh (citation, amendment tag) vào ranker; không mô hình hoá quan hệ "sửa đổi → thay thế → bãi bỏ" theo thời gian, không trả lời câu hỏi "theo quy chế hiện hành" hay "khoá K2019 áp dụng quy chế nào". **T1 vẫn giữ khoảng trống thời gian.**
- **(b) Khoảng trống còn lại**: (1) **trục thời gian** — T1 cần date hiệu lực + mốc áp dụng (khoá, năm học), bài này không có; (2) **đồ thị phiên bản** (node = điều/khoản, cạnh = sửa đổi/thay thế/căn cứ, thuộc tính = ngày hiệu lực) — bài chỉ dùng tag amendment tĩnh, không xây graph động; (3) **căn cứ chéo** (quy chế trường dẫn thông tư Bộ, rồi quyết định sửa đổi của trường) — chưa có trong DRiLL; (4) **so sánh API vs LLM cục bộ** trên kho 30k tệp — bài dùng Qwen2.5-72B API.
- **(c) Rủi ro bị coi là trùng**: **thấp đến vừa**. Bài là retrieval Điều luật (article-level), không phải QA theo hiệu lực; T1 đóng góp chính là **mô hình hoá quan hệ sửa đổi/thay thế theo thời gian + bộ câu hỏi có mốc thời gian**. Nếu T1 chỉ thêm tag amendment vào RAG thì trùng; nhưng T1 có đồ thị phiên bản + câu hỏi "theo quy chế hiện hành" nên khác biệt rõ. Cần dẫn bài này trong related work và so sánh trực tiếp (baseline retrieval + đặc trưng pháp lý không thời gian vs. đồ thị phiên bản + lọc theo mốc áp dụng).
- **(d) Đổi hướng / thêm baseline**: **Không đổi hướng.** Nên: (1) lấy **EDM + 27 đặc trưng pháp lý** làm baseline retrieval cho T1 (mục 6.2); (2) đọc thêm **DRiLL dataset paper** (ref [17], VLSP 2025) để hiểu cấu trúc corpus; (3) so T1 với bài này ở chỉ số F₂ + R@k trên DRiLL nếu có thể (DRiLL công khai); (4) thêm case "companion recovery" kiểu Bảng 9 của bài này vào bộ câu hỏi T1 (hỏi về Điều gốc + Điều sửa đổi cùng lúc).

## Dùng được gì
- **DRiLL dataset** (công khai, VLSP 2025): 59.636 Điều, 2.829 câu hỏi, gold multi-Article — dùng làm testbed mở cho T1 (bộ câu hỏi có mốc thời gian sinh từ DRiLL + văn bản Bộ GD&ĐT).
- **27 đặc trưng pháp lý** (Bảng 2): danh sách cụ thể, tái lập được; dùng làm baseline retrieval không thời gian.
- **Pipeline EDM + LightGBM + Qwen2.5-72B**: tham khảo kiến trúc retrieval; so với đồ thị phiên bản của T1.
- **Chỉ số**: F₂ chính thức DRiLL, R@10/100, per-query F₂ theo gold-size; cách so sánh control/proposed cùng input (5-seed, BH correction).
- **Case study design**: companion recovery + distractor removal (mục 7.2) — mẫu cho bộ câu hỏi T1.

## Mức chắc chắn
Đọc **toàn văn** bản HTML arXiv v1 (mục 1–8, Bảng 1–10, Fig 1–5). Bài đã **accepted at SOICT 2026** (theo arXiv comment, chưa kiểm chứng trang proceedings). DRiLL dataset: công khai, link ref [17] chưa mở (chưa kiểm chứng điều khoản tái sử dụng). Qwen2.5-72B: API, không rõ chi phí/latency (bài không đo). Số liệu F₂, R@k: khớp đúng giữa abstract và bảng kết quả. Đặc trưng 1–4, 20 có zero gain trong mọi model (mục 7.1) — chưa rõ lý do.

## Ghi chú thêm
- Tác giả: **UIT HCM** (cùng cộng đồng P2 ViHERMES, P5 ViLegalExpert, P6 VLegal-Bench trong brief). Cần theo dõi xem họ có mở rộng DRiLL sang giáo dục không (rủi ro nêu trong brief).
- Bài này **không** dùng GraphRAG; đồ thị citation/amendment là nguồn đặc trưng, không phải truy vấn graph. T1 dùng GraphRAG đồ thị phiên bản — khác biệt rõ.
- SOICT 2026: không thấy ghi Scopus trong bài; **chưa kiểm chứng** trạng thái Scopus.

## Phản biện (Critic)

Ngày: 2026-11-26. Đã mở lại toàn văn HTML arXiv v1 (mục 1–8, Bảng 1–11) + arXiv API metadata để đối chiếu từng mục bài đọc.

### 1. Thông tin bài (mở lại arXiv 2611.09200)
✓ Khớp: tiêu đề; tác giả Duc-Vu Nguyen, Ngan Luu-Thuy Nguyen (affiliation trong paper: UIT + VNU-HCM, khớp); publish 06/11/2026 v1 (arXiv API: `published 2026-11-06T09:21:59Z`); cs.IR (primary category); arXiv comment "Accepted at SOICT 2026" khớp ghi chú. DOI `10.48550/arXiv.2611.09200` là quy ước arXiv (chưa mở trang DOI) — bài đọc ghi đúng như vậy, không thổi phồng.

### 2. Số liệu mục "Dữ liệu và kết quả"
- ✓ DRiLL (mục 3, Bảng 1): 59.636 Điều; 2.190 train / 312 dev / 627 test; test sau dedup: 474 single / 121 two / 32 ≥3; 24,4% multi-Article — khớp đúng.
- ✓ F₂ (mục 6.2, Bảng 6): Control P=57,13 ± 0,80, R=76,68 ± 0,51, F₂=71,77 ± 0,47; Proposed P=59,11 ± 0,35, R=77,43 ± 1,03, F₂=72,91 ± 0,68; ΔF₂=+1,14 pp, p_BH=0,00078 — khớp đúng. Ghi chú "± SD 5-seed" khớp mục 5.2.
- ✓ R@k (mục 6.1, Bảng 4): R@10 87,33→88,27 (+0,95), R@100 96,75→97,52 (+0,77); chỉ R@100 có ý nghĩa sau BH — bài đọc nói "có ý nghĩa thống kê sau BH" đúng (R@100). ⚠ Nhỏ: bài đọc nói "R@10 ... (+0,95)" không kèm đánh dấu không ý nghĩa — không sai, chỉ thiếu; paper nói ranker hyperparameters khác nhau nên không quy được cho đặc trưng riêng.
- ✓ Theo gold set (mục 7.2, Bảng 8): two-Article F₂,q 61,34→65,79 (+4,45, 61W/42T/18L); single +0,42 pp; ≥3 +2,89 pp — khớp đúng.
- ✓ Split-gain (mục 7.1, Bảng 7, selector): same-law 8,04 ± 0,57; citation/lineage 7,28 ± 0,32 (gồm local ref 4,83 + intro/amend/guidance 1,32); identity/form 2,87 ± 0,16; tổng 18,20% — khớp đúng.
- ✓ Case Q8360 (Bảng 9): gold {49460, 49474}; control chỉ {49460}; proposed đủ cả hai ở 4/5 seed (thiếu ở seed 3) — khớp "4/5".
- ✓ Case Q411 (Bảng 10): proposed loại Điều cùng-luật gây nhiễu (652) trong 5/5 seed nhưng vẫn thiếu Điều 650 — khớp.
- ⚠ Bài đọc không nhắc **Table 11 (Q7758, failure: proposed bỏ amendment ở 2/5 seed)** — paper đưa ra case failure để cân bằng; bỏ qua không sai nhưng thiếu một case quan trọng khi nhận định "case study minh hoạ ... hoạt động thực tế".
- ✓ "Đặc trưng 1–4, 20 zero gain mọi model" (mục 7.1) — khớp.

### 3. Phát biểu "Điểm mới"
✓ Không thổi phồng: "lần đầu (theo bài)" dùng đúng scope trong bài; so sánh control/proposed cùng Top-100, cùng LLM, cùng learner — khớp mục 4.1/6.2; F₂ +1,14 pp có ý nghĩa thống kê (BH) — khớp; case study hai hướng (companion recovery + distractor removal) — khớp Bảng 9–10; lợi ích lớn nhất ở two-Article — khớp Bảng 8 (Δ +4,45 pp).

### 4. Phần "So với đề tài T1 EduReg-Time"
✓ Công bằng: bài này đúng là retrieval Article tĩnh + tag amendment (mục 4.3: "Action tags label citing Articles, not verified edges", "These cues do not verify legislative histories or effective dates") — không mô hình hoá trục thời gian/hiệu lực, khớp nhận định (a). (b) 4 khoảng trống nêu đều có cơ sở trong paper (không có date hiệu lực, không có graph động, không so LLM khác). (c) Rủi ro "thấp đến vừa" hợp lý: khác mục tiêu (retrieval Điều vs QA theo hiệu lực + mốc thời gian). (d) Khuyến nghị baseline EDM+27 đặc trưng và so F₂/R@k trên DRiLL — hợp lý, DRiLL công khai (ref [17]).
⚠ Nhỏ: mục (b) điểm (4) "so sánh API vs LLM cục bộ trên kho 30k tệp — bài dùng Qwen2.5-72B API": paper không nói đây là "API" (chỉ nói "external LLM services", không đo latency/chi phí) — ghi chú của bài đọc đưa thêm suy luận, nên tách khỏi nội dung bài.

### Kết luận chung
✓ — Thông tin và số liệu khớp toàn văn; nhận định so với T1 công bằng. ⚠ hai điểm nhỏ (thiếu case failure Table 11; suy luận "API" về Qwen2.5) không làm sai kết luận chính.

*Command tái lập:* mở https://arxiv.org/html/2611.09200v1 (đã lưu snapshot `drill.html.txt`, 43.748 ký tự, ngày 2026-11-26) + `http://export.arxiv.org/api/query?id_list=2611.09200`.