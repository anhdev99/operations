# TCMaster: KG đông y đa nguồn có độ tin cậy theo cạnh, truy vấn đường đi có ngưỡng, KG-RAG

Đề tài so sánh: **T3** (KG cây thuốc nam + GraphRAG tiếng Việt có cảnh báo an toàn). Ngày đọc: 2026-11-25.

## Thông tin
- Tên: *TCMaster: Confidence-Aware Querying and Workload-Guided Physical Design for Multi-Source Traditional Chinese Medicine Knowledge Graphs*
- Tác giả: Zheng Chen, Yuzhu Li, Haoxuan Li, Zhongde Zhang, Lianshun Jin, Peiwu Qin (Tsinghua; Beijing University of Chinese Medicine; Guangdong Provincial Laboratory of TCM)
- Năm: 2026 (nộp arXiv 22/09/2026, v1)
- Nơi đăng: arXiv preprint, cs.AI (chưa thấy ghi hội nghị/tạp chí; chưa qua bình duyệt — chưa kiểm chứng)
- arXiv: 2609.25712 — DOI arXiv: 10.48550/arXiv.2609.25712 (DOI theo quy ước arXiv, chưa mở trang DOI)
- Link: https://arxiv.org/abs/2609.25712 , toàn văn HTML: https://arxiv.org/html/2609.25712v1

## Vấn đề
Các CSDL đông y sẵn có (TCMSP, TCMID, SymMap, HERB 2.0, ETCM) chỉ là kho tra cứu: không ghi độ tin cậy/nguồn gốc cho từng quan hệ, không hỗ trợ truy vấn đa bước có lọc theo độ tin cậy (Bảng I). Trong khi KG-RAG lâm sàng, **kiểm tra an toàn đơn thuốc** và tìm đích thuốc cần truy xuất đa bước có bằng chứng kiểm được (mục I).

## Phương pháp
- KG Neo4j 5 tầng (Bảng II): phân tử (vị thuốc–hoạt chất–đích), thuộc tính đông y (tính, vị, quy kinh, **độc tính**), đơn thuốc, "vi ngữ nghĩa" do LLM trích (bào chế, thực vật học, công năng…), lâm sàng (công năng/chủ trị đơn thuốc).
- Nguồn: HERB 2.0, SymMap, 11.845 đơn thuốc cổ phương, quan hệ do DeepSeek-V3 trích 11 loại (mục III-A). 7 luật làm sạch trước khi nạp.
- Mỗi cạnh có điểm tin cậy theo **loại nguồn** (Bảng III): dược điển/CSDL thực nghiệm 0,95; thuộc tính dược điển 0,90; tuyển chọn tay 0,85; LLM trích 0,70; dự đoán KGE 0,30–0,60. Tác giả nói rõ đây là thứ tự tin cậy, **không phải xác suất đã hiệu chỉnh** (mục IV-A).
- Viết lại Cypher tự động thêm `r.conf_score >= θ`; gộp điểm đường đi bằng PRODUCT / MIN / trung bình có trọng số; khuyên dùng PRODUCT cho tình huống an toàn (mục IV-C, IV-D).
- Chuyên gia sửa điểm cạnh (USER_VERIFIED) cập nhật cục bộ, không tính lại toàn đồ thị (mục IV-E).
- Tối ưu vật lý dựa trên độ lệch bản thể (đảo chiều duyệt, bitmap 28 bit thuộc tính, cạnh tắt Đơn→Đích) — phần hệ CSDL, ít liên quan T3.
- Ứng dụng KG-RAG: truy xuất KG (top-3, θ=0) + DeepSeek-V3 trả lời (mục VII-H, IX).

## Dữ liệu và kết quả (ghi rõ nguồn trong bài)
- Quy mô: 221.225 thực thể, 722.671 cạnh gốc, 27 loại thực thể, 23 loại quan hệ (mục II-A); 15.092 nút vị thuốc (mục V-A).
- Chất lượng (mục VII-F): độ chính xác cặp vị thuốc–hoạt chất 93,7%; quan hệ LLM trích 95,5% (sau làm sạch, trước là 91,2%); tỉ lệ ảo giác 8,3% → 4,5%; recall thành phần đơn thuốc 76,0% (F1 72,4%).
- QA (Bảng VIII, TCMbench v3, 2.000 câu, **bộ tự xây từ artifact của chính tác giả**):
  - Tổng: Baseline 52,5% | Vector-RAG 52,5% | KG-RAG 72,5% (+20,0 điểm %); khoảng Wilson KG-RAG 70,5–74,4%.
  - **Safety Audit**: 40,2% | 44,1% | 72,2%.
  - Clinical Prescription: 17,9% | 14,1% | 45,3% (Vector-RAG kém baseline).
  - Prescription Logic: 99,7% | 99,4% | 100%.
- Lọc theo ngưỡng (Bảng IX): truy vấn Q7 "an toàn" (Đơn–Vị thuốc–An toàn) không bị lọc ở mọi θ 0,10–0,45; Q3 (đường hỗn hợp có cạnh dự đoán) lọc 39,3% ở θ=0,18, 69,5% ở θ=0,30.
- Ví dụ Ma hoàng thang (mục VII-J): trả về cảnh báo độc tính Ma hoàng (0,85, CURATED), độ tin cậy đường đi 0,72, 6,7 ms.
- Độ trễ truy vấn 5,2–12,0 ms (Bảng V).

## Hạn chế
- Điểm tin cậy cố định theo loại nguồn, không học, không hiệu chỉnh (mục IX).
- Thí nghiệm KG-RAG dùng θ=0: **không chứng minh** lọc độ tin cậy giúp QA (tác giả tự nói, mục VII-H).
- TCMbench v3 là bộ tự xây, chỉ tiếng Trung/đông y; Safety Audit 72,2% — tác giả ghi "không đủ cho dùng lâm sàng tự động" (mục VII-K).
- Một LLM (DeepSeek-V3), một ví dụ case study, một phần cứng.
- Không thấy mô hình hoá rõ **tương tác thuốc–thảo dược**, **chống chỉ định theo đối tượng** (thai kỳ, bệnh nền) hay **nhầm loài/đồng danh**: "an toàn" chủ yếu là nút Toxicity/Warning gắn với vị thuốc (mục V-A, VII-J). Danh sách loại quan hệ đầy đủ không đọc được trong bản HTML (chưa kiểm chứng có/không).
- Chưa có link artifact công khai lúc đọc (mục Artifact: "sau khi công bố sẽ lên GitHub").

## Điểm mới của bài
- Đưa **độ tin cậy + nguồn gốc theo từng cạnh** thành tín hiệu thực thi truy vấn trên KG đông y (lọc ngưỡng, xếp hạng đường đi), tách cạnh LLM trích (0,70) khỏi cạnh dược điển.
- Có chiều đánh giá "Safety Audit" riêng trong QA, cho thấy KG-RAG vượt Vector-RAG rõ nhất ở câu an toàn (+28,1 điểm % so với Vector-RAG, tính từ Bảng VIII).

## So với đề tài của mình (T3)
- **(a) Trùng với giả thuyết đóng góp**: TCM đã có KG đa nguồn lớn + KG-RAG + nhánh câu hỏi an toàn (độc tính/cảnh báo) + truy vết nguồn gốc bằng chứng. Khẳng định "TCM đã có KG" được củng cố thêm; ý "GraphRAG có cảnh báo an toàn" ở mức khái niệm **không còn mới tuyệt đối**.
- **(b) Khoảng trống còn lại**: (1) cây thuốc nam Việt Nam, nguồn tiếng Việt (Dược điển VN, sách Đỗ Tất Lợi…), QA tiếng Việt — bài không đụng; (2) an toàn chi tiết: chống chỉ định theo đối tượng, tương tác thuốc tây–thảo dược, **nhầm loài/tên địa phương trùng nhau** — bài không mô hình hoá rõ; (3) chứng minh lọc độ tin cậy/nguồn gốc thực sự giảm câu trả lời nguy hiểm (bài để θ=0); (4) đo tỉ lệ bỏ sót cảnh báo, không chỉ accuracy.
- **(c) Rủi ro bị coi là trùng**: trung bình. Nếu T3 chỉ là "KG + GraphRAG + nút cảnh báo" thì phản biện sẽ nói đây là TCMaster/OpenTCM dịch sang tiếng Việt. Cần đặt đóng góp vào (b)(2)–(b)(4) và tài nguyên tiếng Việt.
- **(d) Đổi hướng / baseline**: không cần đổi hướng. Nên: (1) lấy TCMaster làm baseline thiết kế (điểm tin cậy theo nguồn + PRODUCT) và so 3 chế độ Baseline / Vector-RAG / KG-RAG như Bảng VIII; (2) thêm thí nghiệm θ>0 mà bài bỏ ngỏ; (3) đọc thêm OpenTCM (ref [29] trong bài, chưa mở) vì tác giả coi là gần nhất về ứng dụng.

## Dùng được gì
- Thiết kế bản thể 5 tầng; tách thuộc tính (tính/vị/quy kinh/độc tính) thành nút riêng.
- Bảng điểm tin cậy theo loại nguồn (Bảng III) + quy trình 2 lượt gán điểm (mục IV-A); nhãn USER_VERIFIED cho dược sĩ duyệt.
- Gộp đường đi PRODUCT cho truy vấn an toàn; mẫu Cypher viết lại ngưỡng.
- Quy trình kiểm LLM trích: luật làm sạch + mô hình audit (temperature 0,1, JSON) + đo ảo giác trước/sau.
- Chỉ số: accuracy theo chiều (kê đơn / logic / an toàn), khoảng Wilson, tỉ lệ lọc theo θ.
- Nguồn dữ liệu tham khảo: HERB 2.0, SymMap (chỉ cho phần dược lý chung; không thay được dữ liệu cây thuốc VN).

## Mức chắc chắn
Đọc **toàn văn** bản HTML arXiv v1 (mục I–IX, Bảng I–IX). Không xem được hình (Fig. 3–6) và danh sách đầy đủ 23 loại quan hệ. Bài là preprint, chưa bình duyệt; artifact chưa công khai nên số liệu chưa tái lập được.

## Phản biện (Critic)

### 1. Thông tin & DOI ✓
- arXiv ID: 2609.25712 chính xác
- Tiêu đề, tác giả (6 người, Tsinghua/Beijing TCM/Guangdong Lab), năm 2026 (nộp 22/09/2026) **khớp hoàn toàn**.
- DOI: 10.48550/arXiv.2609.25712 ✓

### 2. Dữ liệu & Số liệu ✓
- **221.225 entities, 722.671 base edges** (Table II): khớp Abstract "approximately 221K entities and 723K base edges"
- **5 lớp ontology** (Molecular, TCM Attributes, Prescription, Micro-semantics, Clinical): khớp
- **Confidence scores** (Table III): 0,95 (Authoritative) → 0,90 (Pharma) → 0,85 (Curated) → 0,70 (LLM) → 0,30–0,60 (Predicted): **khớp đúng**
- **QA Results** (Table VIII): Baseline 52.5%, Vector-RAG 52.5%, KG-RAG 72.5% (+20 pp); Safety Audit 72.2%: **khớp đúng**
- **Confidence filtering** (Table IX): Q3 (mixed path) = 39.3% lọc ở θ=0.18, 69.5% ở θ=0.30; Q7 (safety) = 0% ở mọi θ: **khớp đúng**

### 3. Điểm mới của bài ✓
- **Độ tin cậy + nguồn gốc theo từng cạnh** làm thành tín hiệu thực thi (lọc ngưỡng, xếp hạng đường đi): bài tự nêu rõ, **đúng và mới cho TCM**.
- **Safety Audit riêng trong QA** (72.2% vs 44.1% Vector-RAG, +28.1 pp): bài ghi (Table VIII, mục VII-H), **đúng**.

### 4. So với T3 (KG cây thuốc VN + GraphRAG + cảnh báo an toàn) ⚠
#### 4.1 Trùng lặp — rủi ro trung bình
- TCMaster **đã làm**: KG đa nguồn + KG-RAG + nhánh câu hỏi an toàn (Safety Audit là chiều riêng).
- Nếu T3 "chỉ là KG + GraphRAG + nút cảnh báo" → sẽ bị coi là TCMaster dịch tiếng Việt.
- **Nhận xét Scholar**: "Khẳng định TCM đã có KG được củng cố; ý GraphRAG có cảnh báo không còn mới tuyệt đối" — **hợp lý, không quá nặng**.

#### 4.2 Khoảng trống T3 còn lại (đã nêu đúng)
1. **Tiếng Việt + dữ liệu VN**: TCMaster không đụng; Dược điển VN, sách Đỗ Tất Lợi chưa có.
2. **An toàn chi tiết**: chống chỉ định theo đối tượng (thai kỳ, bệnh nền), tương tác thuốc tây–thảo dược, **nhầm loài/tên địa phương trùng nhau** — TCMaster không mô hình hoá.
3. **Chứng minh lọc**: bài để θ=0 trong KG-RAG (mục VII-H), **không chứng minh** θ>0 giúp QA (rủi ro đoán).
4. **Đo bỏ sót**: chỉ có accuracy, **không có tỉ lệ bỏ sót cảnh báo** (recall).

#### 4.3 Kết luận so sánh
- Scholar **không gán quá nặng** cho TCMaster: thừa nhận 4 lỗ hổng có thể; đồng ý dùng TCMaster làm baseline thiết kế.
- **Rủi ro trùng: trung bình**. Với tài nguyên tiếng Việt + mô hình hoá chi tiết + thí nghiệm θ>0, T3 sẽ riêng biệt.

### 5. Hạn chế bài & ảnh hưởng T3
- **Confidence cố định, không học**: mục IX, không hiệu chỉnh theo data — T3 cũng có nguy cơ này.
- **Thí nghiệm θ=0**: bài bỏ ngỏ lợi ích lọc độ tin cậy (mục VII-H) → **T3 phải chứng minh rõ θ>0 giảm câu trả lời nguy hiểm**.
- **TCMbench v3 do bài xây**: chỉ tiếng Trung/đông y, không có tiếng Việt → T3 cần QA tiếng Việt riêng.
- **Artifact chưa công khai lúc đọc** → số liệu chưa tái lập được (chưa kiểm chứng toàn bộ).

### 6. Tính công bằng & logic so sánh
- Scholar viết "không mô hình hoá rõ tương tác thuốc–thảo dược" về TCMaster: **kiểm trong V-A, VII-J—đúng**, bài chủ yếu là Toxicity node gắn vị thuốc.
- Scholar nói "chưa có link artifact công khai": **kiểm Abstract—đúng**, artifact chỉ ghi "sẽ lên GitHub sau công bố".
- Scholar đề xuất "so 3 chế độ Baseline / Vector-RAG / KG-RAG như Bảng VIII" cho T3: **hợp lý, có basis từ TCMaster**.

### Kết luận tổng
**✓ Thông tin & số liệu đúng. ⚠ So sánh hợp lý, rủi ro trùng được định tính (không gán quá nặng). ✓ Khuyến nghị baseline đáng tin.**

**Điểm yếu Scholar nên sửa**:
- Chưa ghi rõ "θ=0 trong QA có nghĩa là **không chứng minh** lọc giúp" — nên viết "bài bỏ ngỏ lợi ích θ>0 (rủi ro)".
- Danh sách 23 loại quan hệ không đọc được → ghi "chưa kiểm chứng đầy đủ danh sách RELATIONSHIP_TYPES".

**Phê chuẩn**: Bài TCMaster tồn tại thực, số liệu chính xác, khuyến nghị T3 rõ ràng. So sánh không phóng đại TCMaster nhưng cũng không phớt lờ rủi ro trùng. Sẵn sàng dùng làm baseline.
