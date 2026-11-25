# ShenNongDiet: KG dược thiện + truy xuất lai đồ thị–vector + sinh có ràng buộc bằng chứng, có quan hệ chống chỉ định theo nhóm người

Đề tài so sánh: **T3** (KG cây thuốc nam + GraphRAG tiếng Việt có cảnh báo an toàn). Ngày đọc: 2026-11-25.

## Thông tin
- Tên: *ShenNongDiet: a medicine diet recommendation system based on graph-semantic hybrid retrieval and evidence constraint generation*
- Tác giả: Xiangying Yan, Zhuang Guo, Na Lin, Yanqiong Zhang (Institute of Chinese Materia Medica, China Academy of Chinese Medical Sciences)
- Năm: 2026 (nhận 08/06/2026, chấp nhận 09/08/2026, đăng 26/08/2026)
- Nơi đăng: *Chinese Medicine* (BMC), tập 21, bài 214; có bình duyệt; open access CC BY 4.0
- DOI: 10.1186/s13020-026-01505-x — PMID 42649519 — PMCID PMC13508355
- Link: https://doi.org/10.1186/s13020-026-01505-x ; toàn văn đã đọc qua Europe PMC: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13508355/fullTextXML

## Vấn đề
Người dùng tự tra cứu dược thiện (món ăn–thuốc đông y) mà không có kiểm tra chống chỉ định như đơn thuốc được dược sĩ duyệt. Có khoảng cách ngôn ngữ đời thường – thuật ngữ đông y, thông tin công khai thiếu nhãn đối tượng phù hợp/chống chỉ định; nhóm nguy cơ cao (thai kỳ, trẻ em, cơ địa dị ứng) không có công cụ cảnh báo tương tự cảnh báo tương tác thuốc (mục Introduction). Các hệ trước (TCM-DS, Yaoshi-RAG, TCM-KLLaMA) chưa mô hình hoá chống chỉ định theo nhóm người và truy vết bằng chứng một cách hệ thống (theo nhận định của tác giả).

## Phương pháp
- **Dữ liệu**: OCR bộ sách *Guoyi Jinghua Yao Shan* → 3.376 bản ghi dược thiện sau khử trùng (mục Data source). 7 trường: tên, công thức (liều), cách làm, công năng, cách dùng, ghi chú (tính vị quy kinh, chống chỉ định, đối tượng phù hợp), nguồn.
- **KG Neo4j** (Bảng 1, 2): 6 loại thực thể (Dược thiện, Bệnh, Nguyên liệu, Triệu chứng, Công năng, Nhóm người); 6 quan hệ: COMPOSED_OF, HAS_EFFECT, MODULATES, ALLEVIATES, SUITABLE_FOR, **CONTRAINDICATED_FOR** (Dược thiện → Nhóm người). Trích thực thể bằng DeepSeek-V4-Pro theo prompt cố định; chuẩn hoá tên theo Dược điển TQ, Bảng thành phần thực phẩm TQ, Trung dược học…; 8 nghiên cứu viên kiểm đồng nghĩa/biến thể/mơ hồ, 3 chuyên gia phân xử. Giữ ánh xạ tên gốc → tên chuẩn; thiếu bằng chứng thì không tạo quan hệ.
- **Truy xuất lai**: GPT-5.4 (temperature 0,1) phân tích ý định → entity → đếm số cạnh khớp trong KG làm điểm g(m); song song FAISS (Qwen3-Embedding-8B, 4096 chiều, top-50), điểm s = 1/(1+d). Chuẩn hoá max rồi trộn S = w_g·g + w_s·s, chọn (0,2; 0,8) qua quét 9 cặp (Bảng 5). Lấy top-15 làm ngữ cảnh.
- **Sinh có ràng buộc bằng chứng**: Qwen3-8B LoRA (r=128, α=256, 3 epoch; Bảng 3) trên 8.509 mẫu train / 868 val, do DeepSeek-V4-Pro sinh + người kiểm. Quy tắc: thông tin không có trong bằng chứng ghi "not recorded in the provided materials"; cấm sinh công năng/chống chỉ định không có bằng chứng. Hệ thống trả lời "chưa đủ bằng chứng trong CSDL" khi thiếu, và hiện đường đi KG "Dược thiện–CONTRAINDICATED_FOR–Nhóm người" khi cảnh báo (mục Results, Fig. 4).
- Chạy trên Dify 1.13.0.

## Dữ liệu và kết quả (ghi rõ nguồn trong bài)
- KG (mục "Basic data of the KG"): 9.321 thực thể; 38.669 quan hệ, trong đó COMPOSED_OF 19.868, HAS_EFFECT 11.508, MODULATES 2.740, ALLEVIATES 2.356, SUITABLE_FOR 2.099, **CONTRAINDICATED_FOR chỉ 98**.
- Chọn mô hình nền (Bảng 4, 2.000 câu trắc nghiệm tự xây): Qwen3-8B TUI 66,75% (Acc công năng 93,27%, Acc công thức 27,96%); DeepSeek-R1-8B 60,50%; glm-4v-9b 56,75%; Hunyuan-7B 52,30%; Baichuan2-7B 2,05%.
- LoRA vs gốc (cùng bằng chứng): Hit@1 69,9% → 74,8%; Hit@3 80,4% → 82,5%; recall đáp án 44,44% → 56,89%; tỉ lệ truy vết bằng chứng 58,67% → 84,67% (mục "Comparison results before and after model fine-tuning").
- Kết quả chính (Bảng 6, 150 câu ShenNongDiet-Test, bootstrap 95% CI): Hit@1 84,00% [77,33; 88,67], Hit@3 90,00%, Hit@5 92,67%, MRR 0,8778.
- RAGAs 0.4.3: faithfulness 0,831; context recall 0,526; **context precision 0,064** (mục RAGAs).
- Chuyên gia (Bảng 7, 2 chuyên gia, 150 bộ): accuracy 0,807 / 0,920; faithfulness 0,651 / 0,648; lặp lại top-5 0,215 / 0,218.
- Ablation (Bảng 8): Hybrid Hit@1 84,0% | Dense-only 61,3% | BM25 48,0% | Graph-only 29,3% (P<0,001, McNemar). Hit@5 hybrid vs dense: 92,0 vs 89,3, không khác biệt có ý nghĩa (P=0,2188).
- Tập test: câu hỏi chống chỉ định chỉ **2,7%** (≈4/150 câu), nhóm người đặc biệt 16,0% (mục Dataset construction (4)). **Không có số liệu riêng** cho độ chính xác/recall cảnh báo chống chỉ định.

## Hạn chế
- Chống chỉ định chỉ 98 cạnh, lấy từ ghi chú sách; tác giả tự nói **chưa chứng minh được năng lực nhận diện rủi ro toàn diện hay an toàn đã kiểm chứng lâm sàng**; dự kiến xây tập test an toàn riêng đo recall chống chỉ định, tỉ lệ khuyến nghị không phù hợp, độ chính xác từ chối (mục Discussion).
- Trọng số KG chỉ 0,2: xếp hạng chủ yếu dựa vector; Graph-only rất kém (29,3%) — KG đóng vai trò "neo bằng chứng" hơn là bộ lọc an toàn cứng. Bài không mô tả rõ có loại bỏ cứng ứng viên vi phạm CONTRAINDICATED_FOR trước khi xếp hạng hay không (chưa kiểm chứng).
- Context precision 0,064: ngữ cảnh top-15 nhiều nhiễu.
- Độ lặp lại top-5 thấp (~0,22).
- Một nguồn sách duy nhất; chỉ tiếng Trung; tập test 150 câu bán tự động; quan hệ không có điểm tin cậy/nguồn gốc theo cạnh.
- Không mô hình hoá tương tác thuốc tây–thảo dược, độc tính vị thuốc, nhầm loài.
- Cách công bố dữ liệu/mã nguồn: phần "Availability of data" không đọc được (bản tải bị cắt) — chưa kiểm chứng.

## Điểm mới của bài
- Đưa **chống chỉ định theo nhóm người/thể trạng** thành quan hệ tường minh trong KG (CONTRAINDICATED_FOR, SUITABLE_FOR) và hiện đường đi KG làm bằng chứng cảnh báo trong câu trả lời.
- **Sinh có ràng buộc bằng chứng** qua SFT: quy ước "không có trong tài liệu" + từ chối khi thiếu bằng chứng; đo bằng tỉ lệ truy vết bằng chứng (58,67% → 84,67%).
- Ablation rõ ràng hybrid vs graph-only vs dense-only vs BM25, có kiểm định McNemar và bootstrap CI.

## So với đề tài của mình (T3)
- **(a) Trùng với giả thuyết đóng góp**: đã có KG thảo dược/dược thiện + RAG lai đồ thị–vector + **cảnh báo chống chỉ định theo đối tượng (thai kỳ, trẻ em, thể trạng)** + từ chối khi thiếu bằng chứng. Cộng với TCMaster (độc tính + độ tin cậy theo cạnh), khối "KG + GraphRAG + cảnh báo an toàn" ở TCM giờ đã có 2 bài 2026 phủ hai mặt khác nhau. Điểm (b)(2) "chống chỉ định theo đối tượng" nêu trong ghi chú TCMaster **không còn là khoảng trống hoàn toàn**.
- **(b) Khoảng trống còn lại**:
  1. Tiếng Việt, cây thuốc nam, nguồn VN (Dược điển VN, Đỗ Tất Lợi) — bài không đụng.
  2. **Đánh giá an toàn định lượng**: bài chỉ có ~4 câu chống chỉ định, không đo recall cảnh báo/tỉ lệ khuyến nghị nguy hiểm/độ chính xác từ chối — chính tác giả nêu là việc tương lai. Đây là khoảng trống rõ nhất cho T3: một **tập test an toàn tiếng Việt** + chỉ số bỏ sót cảnh báo.
  3. An toàn ở mức **cứng**: lọc/chặn bằng quan hệ KG trước khi sinh (bài trộn mềm với trọng số KG 0,2).
  4. Tương tác thuốc tây–thảo dược, độc tính, **nhầm loài/tên địa phương** — cả ShenNongDiet và TCMaster đều không mô hình hoá.
  5. Kết hợp độ tin cậy/nguồn gốc theo cạnh (TCMaster) với quan hệ chống chỉ định theo đối tượng (ShenNongDiet) — chưa bài nào làm cả hai.
- **(c) Rủi ro bị coi là trùng**: **vừa** (tăng nhẹ so với sau TCMaster). Nếu T3 trình bày đóng góp là "KG + RAG lai + quan hệ chống chỉ định theo đối tượng + từ chối khi thiếu bằng chứng" thì gần như là ShenNongDiet bằng tiếng Việt. Vẫn không cao vì phần đánh giá an toàn định lượng, lọc cứng, nhầm loài và tài nguyên tiếng Việt còn trống.
- **(d) Đổi hướng / baseline**: không cần đổi hướng; nên **dịch trọng tâm đóng góp sang đánh giá an toàn** (benchmark cảnh báo tiếng Việt, đo bỏ sót/khuyến nghị nguy hiểm/từ chối đúng) và lọc cứng có truy vết. Thêm ShenNongDiet làm baseline kiến trúc: hybrid (0,2/0,8) + graph-only + dense-only + BM25, so với cấu hình lọc cứng của mình trên cùng tập an toàn.

## Dùng được gì
- Lược đồ quan hệ SUITABLE_FOR / CONTRAINDICATED_FOR (Vị thuốc/Bài thuốc → Nhóm người) — áp thẳng cho cây thuốc nam (thai kỳ, trẻ em, bệnh nền).
- Quy trình chuẩn hoá thực thể: từ điển chuẩn + người kiểm + chuyên gia phân xử; giữ ánh xạ tên gốc → tên chuẩn (hữu ích cho tên địa phương cây thuốc nam).
- Công thức trộn điểm max-normalize + quét trọng số với bootstrap CI.
- Quy ước SFT "not recorded in the provided materials" + chỉ số **tỉ lệ truy vết bằng chứng**.
- Bộ chỉ số: Hit@K, MRR, RAGAs (faithfulness, context recall, context precision), chấm chuyên gia mù + Bland-Altman, McNemar cho ablation.
- Danh sách chỉ số an toàn tác giả đề xuất mà chưa làm (recall chống chỉ định, tỉ lệ khuyến nghị không phù hợp, độ chính xác từ chối) — dùng làm thiết kế đánh giá cho T3.

## Mức chắc chắn
Đọc **toàn văn** (JATS XML Europe PMC): Abstract, Introduction, Methods, Results, Discussion, Conclusions, Bảng 1–8. Không xem được hình (Fig. 1–7) và Supplementary Table S1; phần Availability of data/code không đọc được (bản tải bị cắt) — chưa kiểm chứng có công bố mã/dữ liệu. Bài đã bình duyệt; số liệu chưa tái lập.

## Phản biện (Critic)

### 1. Thông tin & DOI ✓
- DOI: 10.1186/s13020-026-01505-x **khớp chuẩn BMC format**
- Tên: *ShenNongDiet: a medicine diet recommendation system...* **khớp Abstract**
- Tác giả: Xiangying Yan, Zhuang Guo, Na Lin, Yanqiong Zhang (Institute of Chinese Materia Medica, China Academy of Chinese Medical Sciences) **khớp**
- Năm: 2026 (nhận 08/06, chấp nhận 09/08, đăng 26/08) **khớp đúng**
- PMID 42649519, PMCID PMC13508355 **khớp**

### 2. Dữ liệu & Số liệu ✓
- **9.321 entities, 38.669 edges** (mục "Basic data of the KG"): khớp Abstract "9,321 entities and 38,669 relationships"
- **CONTRAINDICATED_FOR chỉ 98 cạnh** (Bảng 2): khớp, là 0,25% tổng cạnh (mục Results)
- **Qwen3-8B TUI 66,75%** (Bảng 4, 2.000 câu tự xây): khớp đúng
  - Accuracy công năng 93,27%, công thức 27,96% **khớp**
- **LoRA improvement** (mục "Comparison results"): 69,9% → 74,8% Hit@1; 80,4% → 82,5% Hit@3; truy vết bằng chứng 58,67% → 84,67% **khớp**
- **ShenNongDiet-Test (150 câu, Bảng 6)**: Hit@1 84,00% [77,33; 88,67], Hit@3 90,00%, Hit@5 92,67%, MRR 0,8778 **khớp đúng**
- **RAGAs 0.4.3**: faithfulness 0,831; context recall 0,526; context precision **0,064** **khớp đúng** (thấp)
- **Chuyên gia (Bảng 7)**: 2 chuyên gia, accuracy 0,807 / 0,920; faithfulness 0,651 / 0,648 **khớp**
- **Ablation (Bảng 8)**: Hybrid 84,0% | Dense 61,3% | BM25 48,0% | Graph-only 29,3%, McNemar P<0,001 **khớp**
- **Tập test chống chỉ định chỉ 2,7%** (≈4/150 câu): khớp mục "Dataset construction"

### 3. Điểm mới của bài ✓
- **CONTRAINDICATED_FOR + SUITABLE_FOR** làm quan hệ tường minh trong KG, hiện đường đi làm bằng chứng cảnh báo: bài tự nêu rõ (mục Results, Fig. 4), **đúng và mới cho medicine diet**.
- **SFT với ràng buộc bằng chứng** ("not recorded in the provided materials" + từ chối khi thiếu): bài ghi rõ quy ước + đo tỉ lệ truy vết (58,67% → 84,67%), **đúng**.
- **Ablation hybrid vs graph-only vs dense-only vs BM25** có McNemar & bootstrap CI: bài ghi rõ (Bảng 8), **đúng**.

### 4. So với T3 (KG cây thuốc VN + GraphRAG + cảnh báo an toàn) ⚠
#### 4.1 Trùng lặp — rủi ro vừa phải
- ShenNongDiet **đã làm**: KG dược thiện + hybrid retrieval (graph 0,2 / vector 0,8) + quan hệ CONTRAINDICATED_FOR + ràng buộc bằng chứng SFT.
- Nếu T3 "chỉ là KG + GraphRAG + nút chống chỉ định" → sẽ bị coi là ShenNongDiet dịch tiếng Việt + cây thuốc nam thay dược thiện.
- **Nhận xét Scholar**: "giờ đã có 2 bài 2026 phủ hai mặt khác nhau; điểm (b)(2) không còn là khoảng trống hoàn toàn" — **đánh giá chính xác, không quá nặng**.

#### 4.2 Khoảng trống T3 còn lại
1. **Tiếng Việt + dữ liệu VN**: ShenNongDiet chỉ tiếng Trung (Guoyi Jinghua Yao Shan); không có Dược điển VN, Đỗ Tất Lợi.
2. **Đánh giá an toàn định lượng**: ShenNongDiet chỉ có ~4 câu chống chỉ định (2,7%), **không có recall cảnh báo / tỉ lệ khuyến nghị nguy hiểm / độ chính xác từ chối** — tác giả tự nêu là việc tương lai (mục Discussion). **Đây là lỗ hổng lớn**.
3. **Lọc an toàn cứng**: ShenNongDiet trộn mềm (trọng số KG chỉ 0,2); không mô tả rõ có loại bỏ CONTRAINDICATED_FOR trước sinh hay không (chưa kiểm chứng).
4. **Context precision thấp** (0,064): top-15 nhiều nhiễu → cảnh báo có thể bị chôn trong câu trả lời.
5. **Tương tác thuốc tây–thảo dược, độc tính vị, nhầm loài**: cả ShenNongDiet và TCMaster đều không mô hình hoá.

#### 4.3 Kết luận so sánh
- Scholar **đánh giá công bằng**: thừa nhận 2 bài (TCMaster + ShenNongDiet) phủ khác nhau; nên dịch trọng tâm T3 sang **đánh giá an toàn định lượng** (benchmark cảnh báo) + lọc cứng + nhầm loài.
- **Rủi ro trùng: vừa phải**. Nếu T3 tiêu đề/lời tự không phân biệt rõ, chỉ là "KG + RAG + chống chỉ định", sẽ bị phỏng ngờ. Nhưng với tập test an toàn tiếng Việt + chỉ số bỏ sót cảnh báo + lọc cứng, T3 sẽ riêng biệt.

### 5. Hạn chế bài & ảnh hưởng T3
- **CONTRAINDICATED_FOR chỉ 98 cạnh** từ ghi chú sách, không đầy đủ: tác giả tự thừa nhận "chưa chứng minh được năng lực nhận diện rủi ro toàn diện hay an toàn đã kiểm chứng lâm sàng" (mục Discussion).
- **Tập test an toàn chỉ 2,7%** (≈4 câu): quá nhỏ để rút kết luận; không có benchmark recall riêng → **T3 phải xây tập test an toàn riêng lớn hơn**.
- **Context precision 0,064**: top-15 nhiễu cao → T3 cần thí nghiệm lọc cứng để giảm nhiễu.
- **Graph-only rất kém** (29,3%): KG chủ yếu là "neo bằng chứng" chứ không phải "bộ lọc an toàn cứng" (trọng số 0,2). → T3 nên thử trọng số KG lớn hơn hoặc lọc cứng trước sinh.
- **Một nguồn sách duy nhất**; không có điểm tin cậy/nguồn gốc theo cạnh (không như TCMaster).
- **Chưa công bố mã/dữ liệu** (phần Availability bị cắt) → không tái lập được.

### 6. Tính công bằng & logic so sánh
- Scholar viết "CONTRAINDICATED_FOR chỉ 98": **kiểm Bảng 1, 2—đúng**, là 0,25% tổng cạnh.
- Scholar nói "2,7% chống chỉ định chỉ trong tập test": **kiểm mục Dataset—đúng**, nhóm người đặc biệt 16% (không phải chống chỉ định lặp lại).
- Scholar đề xuất "dịch trọng tâm sang đánh giá an toàn định lượng + lọc cứng + nhầm loài": **hợp lý, có basis từ hạn chế bài**.

### Kết luận tổng
**✓ Thông tin & số liệu đúng. ⚠ Rủi ko trùng vừa phải (ShenNongDiet + TCMaster phủ gần nhau, lỗ hổng an toàn định lượng là cơ hội T3). ✓ Khuyến nghị dịch trọng tâm đáng tin.**

**Điểm yếu Scholar nên sửa**:
- Dòng 36: "Graph-only rất kém (29,3%) — KG đóng vai trò neo bằng chứng hơn là bộ lọc an toàn cứng. **Bài không mô tả rõ có loại bỏ cứng ứng viên vi phạm CONTRAINDICATED_FOR trước khi xếp hạng hay không (chưa kiểm chứng).**" — nên sửa thành "bài không tường minh nêu có loại bỏ cứng + KG-RAG (mục Results) không ghi θ hay quy tắc lọc".

**Phê chuẩn**: Bài ShenNongDiet tồn tại thực, số liệu chính xác, hạn chế được xác định đúng (tập test nhỏ, graph-only yếu, không có benchmark an toàn định lượng). Khuyến nghị T3 rõ ràng. So sánh 2 bài (TCMaster + ShenNongDiet) không phóng đại trùng lặp nhưng cũng không che giấu rủi ro. Có thể tiếp tục T3 với trọng tâm dịch sang đánh giá an toàn.
