# Kế hoạch thực nghiệm (chủ nhóm tự chạy)

Dean thêm đề xuất từ các bài đã đọc: mục tiêu, dữ liệu, baseline, metric, cần GPU không.

## E1 (T3) Lọc độ tin cậy cạnh KG có giảm câu trả lời nguy hiểm không

- Nguồn: RES-20, bài TCMaster (arXiv 2609.25712, `papers/2026-11-25-tcmaster-confidence-kg.md`). Bài gán điểm tin cậy theo loại nguồn cho từng cạnh nhưng chạy KG-RAG với θ=0 (mục VII-H), nên chưa ai chứng minh lọc θ>0 có ích. Đây là chỗ T3 có thể đóng góp.
- Mục tiêu: trên KG cây thuốc nam, so câu trả lời an toàn khi lọc cạnh theo ngưỡng θ ∈ {0; 0,3; 0,5; 0,7; 0,85} và khi gộp đường đi bằng PRODUCT/MIN.
- Dữ liệu: KG thử 10-20 loài cây thuốc nam có nguồn công khai (Dược điển VN, sách tra cứu đã xuất bản); mỗi cạnh ghi nguồn và điểm tin cậy theo bảng kiểu Bảng III của TCMaster. Bộ câu hỏi tiếng Việt khoảng 100-200 câu, có nhóm câu an toàn (chống chỉ định thai kỳ/bệnh nền, tương tác thuốc tây, nhầm loài/tên địa phương), đáp án do người có chuyên môn dược duyệt.
- Baseline: (1) LLM không truy xuất; (2) Vector-RAG trên văn bản nguồn; (3) KG-RAG θ=0 (tương đương thiết lập TCMaster); (4) KG-RAG θ>0.
- Metric: accuracy theo nhóm câu (chung / an toàn); **tỉ lệ bỏ sót cảnh báo** (recall của cảnh báo bắt buộc), tỉ lệ cảnh báo sai; tỉ lệ cạnh bị lọc theo θ; trích dẫn có căn cứ (câu trả lời dẫn đúng cạnh/nguồn). Báo khoảng Wilson.
- GPU: không bắt buộc nếu dùng LLM qua API; nếu chạy LLM mở cục bộ (7-8B) cần GPU khoảng 16 GB. KG nhỏ chạy Neo4j trên CPU.
- Ghi chú: trước khi chạy, đọc thêm OpenTCM (ref [29] trong TCMaster) để tránh trùng.
