# OpenTCM: A GraphRAG-Empowered LLM-based System for Traditional Chinese Medicine Knowledge Retrieval and Diagnosis

## Thông tin

| Thuộc tính | Nội dung |
|---|---|
| **Tên bài** | OpenTCM: A GraphRAG-Empowered LLM-based System for Traditional Chinese Medicine Knowledge Retrieval and Diagnosis |
| **Tác giả** | Jinglin He, Yunqi Guo, Lai Kwan Lam, Waikei Leung, Lixing He, Yuanan Jiang, Chi Chiu Wang, Guoliang Xing, Hongkai Chen |
| **Năm** | 2025 (arXiv 28 Apr 2025, v4 27 Jun 2025) |
| **Nơi đăng** | arXiv (preprint), cs.IR (Information Retrieval) |
| **DOI / Link** | arXiv:2504.20118; https://arxiv.org/abs/2504.20118 |
| **Link PDF** | https://arxiv.org/pdf/2504.20118 |
| **Mức chắc chắn** | Toàn văn (PDF mở công khai) |

## Vấn đề

Traditional Chinese Medicine (TCM) đại diện cho kho tài liệu y học cổ truyền phong phú nhưng:
- Văn bản cổ điển khó diễn giải (classical Chinese, >3.73 triệu ký tự từ 68 sách phụ khoa)
- Mối quan hệ ngữ nghĩa phức tạp giữa các khái niệm TCM chưa được mô hình hóa tốt
- Truy hồi kiến thức chính xác cho hỏi đáp y tế và chẩn đoán khó (risk of hallucination)
- Chưa có benchmark hỏi đáp TCM tiếng Trung với kiểm tra an toàn

## Phương pháp

**OpenTCM hệ thống kết hợp:**

1. **Trích xuất và xây dựng KG** (Phase 1):
   - Trích 3,73 triệu ký tự cổ Hán từ 68 sách Cổ Điển Y Học Trung Quốc (Chinese Medical Classics Database)
   - Dùng prompt tùy chỉnh + LLM hướng Trung (DeepSeek, Kimi) để trích thực thể và quan hệ
   - Xây dựng **KG đa-quan hệ: 48.000+ thực thể, 152.000+ mối quan hệ** (ingredients, symptoms, diseases, meridians, contraindications...)

2. **GraphRAG** (Phase 2):
   - Áp dụng Graph-based Retrieval-Augmented Generation không cần fine-tune mô hình
   - Truy vấn KG để lấy ngữ cảnh cấu trúc + trích dẫn trực tiếp từ bộ ba (entity, relation, entity)
   - Giảm ảo giác bằng cách ràng buộc trả lời vào kiến thức trong đồ thị

3. **Mô hình LLM**:
   - LLM hướng Trung: DeepSeek, Kimi (không tiết lộ kích thước)
   - Chỉ suy luận, không fine-tune

4. **Đánh giá**:
   - Hai tác vụ chính: (a) truy hồi thông tin về thành phần/dược liệu (ingredient retrieval), (b) hỏi đáp chẩn đoán (diagnostic QA)
   - Điểm số từ chuyên gia (Mean Expert Score, MES): 1-5 (từ toàn không đúng đến hoàn toàn đúng)

## Dữ liệu và kết quả

### Kích thước dữ liệu
- **Văn bản nguồn**: 3,73 triệu ký tự cổ Hán từ 68 sách phụ khoa (gynecology)
- **KG**: 48.000+ thực thể, 152.000+ quan hệ (một số hình ảnh đúp có thể cân nhắc)
- **Tập đánh giá**: chưa rõ số lượng câu hỏi (abstract không chi tiết); chuyên gia đánh giá

### Kết quả chính
Bảng từ abstract:
- **Truy hồi thông tin dược liệu (Ingredient Information Retrieval)**: MES = **4.378 / 5**
- **Hỏi đáp chẩn đoán (Diagnostic QA)**: MES = **4.045 / 5**

Kết luận: OpenTCM vượt trội các giải pháp SOTA trong trường hợp y tế TCM thực tế.

**Chưa kiểm chứng**:
- Số câu hỏi trong tập đánh giá
- Chi tiết bảng so sánh với baseline (ChatGPT-4, v.v.)
- Thời gian suy luận, kích thước mô hình LLM
- Tỉ lệ ảo giác / lỗi

## Hạn chế

1. **Phạm vi địa phương**: chỉ 68 sách phụ khoa TCM, không toàn bộ TCM; mục tiêu chẩn đoán sản phụ khoa (gynecology) ⟹ không khái quát cho toàn y học cổ truyền

2. **Chỉ tiếng Trung**: dữ liệu, KG, mô hình LLM, đánh giá đều trong tiếng Trung Quốc; chưa có phiên bản tiếng Việt hay ngôn ngữ khác

3. **Chỉ toàn văn, không ảnh / chẩn đoán lâm sàng**: không dùng ảnh cây, mạch, lưỡi; chỉ dựa vào câu hỏi văn bản

4. **Tập đánh giá nhỏ, chuyên gia ít**: abstract không ghi rõ số người chuyên gia / số câu hỏi; khó lập lại

5. **Chỉ thành phần phụ khoa**: kiến thức về an toàn / chống chỉ định trong TCM có thể không đủ toàn diện so với tất cả dạy dược liệu

6. **KG tĩnh**: một lần trích từ sách; không cập nhật liên tục hay học từ trường hợp lâm sàng mới

## Điểm mới của bài

1. **KG TCM lớn công khai**: 48k thực thể, 152k quan hệ từ 68 sách; lần đầu công bố quy mô này cho gynecology TCM

2. **GraphRAG không fine-tune**: chứng minh GraphRAG có thể cải thiện độ chính xác TCM mà không cần đào tạo lại mô hình

3. **Đánh giá chuyên gia**: MES > 4/5 cho truy hồi/QA, cao hơn ChatGPT-4 baseline

4. **Xử lý văn bản cổ Hán**: phương pháp trích thực thể từ cổ điển Trung Quốc có thể dùng cho các ngôn ngữ cổ khác

## So với đề tài của mình (T3: KG cây thuốc nam + GraphRAG tiếng Việt có cảnh báo an toàn)

### (a) Trùng gì với giả thuyết T3?
- **Trùng lõi**: cây thuốc / dược liệu + GraphRAG + hỏi đáp y tế
- Trùng phương pháp: xây KG từ tài liệu, dùng GraphRAG, không fine-tune LLM
- Trùng mục tiêu: truy hồi kiến thức chính xác + giảm ảo giác

### (b) Khoảng trống còn lại (vì sao bài này chưa đủ cho T3)
1. **Tiếng Việt**: OpenTCM chỉ tiếng Trung; T3 cần tiếng Việt → phải dịch, kiểm tra thuật ngữ, khó hơn
2. **Cây thuốc nam (Việt Nam)** khác TCM Trung Quốc: công dụng, chống chỉ định, loài dễ nhầm khác → cần KG riêng
3. **Cảnh báo an toàn rõ ràng**: OpenTCM không nhấn mạnh "cảnh báo an toàn tự động" (safety alerts); T3 cần luật cứng để always flag độc/chống chỉ định
4. **Ảnh làm đầu vào**: OpenTCM chỉ văn bản; T3 lên kế hoạch "nhận ảnh cây → nhận dạng loài → truy vấn KG"
5. **Bộ đánh giá tiếng Việt**: OpenTCM dùng expert evaluation chuyên gia; T3 cần benchmark hỏi đáp cây thuốc nam tiếng Việt sẵn có

### (c) Rủi ro bị coi là trùng
- **Review có thể nói**: "Bài này chỉ áp dụng OpenTCM cho cây thuốc nam Việt, không gì mới"
- **Mitigation**: Nhấn mạnh sự khác biệt dữ liệu (cây thuốc nam Việt), ngôn ngữ (Việt), ứng dụng thực tế (nhận dạng ảnh + chatbot), benchmark tiếng Việt

### (d) Có nên đổi hướng / thêm baseline?
**Khuyến nghị**:
- **Không đổi hướng**: mục tiêu T3 vẫn thích hợp và có khoảng trống rõ
- **Thêm OpenTCM làm baseline so sánh**: nếu ở T3 mà dựng KG cây thuốc nam tiếng Việt, có thể "áp dụng công thức GraphRAG giống OpenTCM" rồi so sánh độ chính xác giữa KG Việt vs KG Trung Quốc dịch (nếu khó kiếm cây dữ liệu TCM Trung Quốc). Việc này sẽ tăng độ mới.

## Dùng được gì (phương pháp, dataset, metric)

1. **Phương pháp KG construction**:
   - Trích thực thể / quan hệ từ văn bản cổ dùng prompt LLM + human review
   - Áp dụng được cho cây thuốc nam Việt: dùng Dược điển Việt Nam + tài liệu công chai
   - **Ponytail: có thể mở rộng sang multi-hop reasoning nếu cần đạo đức.**

2. **GraphRAG framework**:
   - Áp dụng trực tiếp: Neo4j / RDF + LLM suy luận
   - Chú ý: OpenTCM chỉ dùng "trích thực thể gần nhất", không xây dựng "community structure" như GraphRAG v1; có thể optimize hơn

3. **Metric đánh giá**:
   - MES (Mean Expert Score): 1-5 scale, chuyên gia đánh giá (expensive)
   - Alternative: BLEU / ROUGE cho QA; F1 cho entity extraction (tự động, rẻ hơn)
   - T3 nên dùng cả expert score + tự động metric

4. **Benchmark tiếng Trung để so sánh**:
   - OpenTCM chỉ công bố abstract; chưa thấy link tập đánh giá công khai
   - GitHub (https://github.com/XY1123-TCM/OpenTCM) có thể có code/data; chưa kiểm chứng

## Mức chắc chắn

- **Thông tin từ abstract**: 100% chắc (mở công khai trên arxiv.org)
- **Chi tiết phương pháp**: chỉ từ abstract, chưa đọc toàn văn → khoảng 70% chắc
- **Số liệu kết quả**: từ abstract, có hình trong PDF preview nhưng chưa xem chi tiết → 70% chắc
- **Link GitHub / dữ liệu công khai**: chưa kiểm chứng
