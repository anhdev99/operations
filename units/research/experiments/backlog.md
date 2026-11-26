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

## E2 (T3) Lọc an toàn cứng theo KG so với trộn mềm, trên benchmark an toàn tiếng Việt

- Nguồn: RES-23, bài ShenNongDiet (Chinese Medicine 21:214, 2026, DOI 10.1186/s13020-026-01505-x, `papers/2026-11-25-shennongdiet-kg-rag-contraindication.md`). Bài đã có quan hệ CONTRAINDICATED_FOR theo nhóm người và RAG lai (trọng số đồ thị 0,2 / vector 0,8), nhưng tập test chỉ có khoảng 2,7% câu chống chỉ định (khoảng 4/150), không đo recall cảnh báo; tác giả tự nêu đây là việc tương lai (mục Discussion). Bài không mô tả có lọc cứng trước khi sinh hay không (chưa kiểm chứng). Giả thuyết đóng góp của T3 nên dịch sang: **benchmark an toàn tiếng Việt + lọc cứng có truy vết**.
- Mục tiêu: so tỉ lệ bỏ sót cảnh báo giữa (i) trộn mềm kiểu ShenNongDiet và (ii) lọc cứng: loại/gắn cờ ứng viên vi phạm CONTRAINDICATED_FOR với nhóm người trong câu hỏi trước khi sinh, kèm đường đi KG làm bằng chứng.
- Dữ liệu: dùng chung KG thử và bộ câu hỏi của E1; tăng nhóm câu an toàn lên ít nhất 30-40% (thai kỳ, trẻ em, bệnh nền, tương tác thuốc tây, nhầm loài/tên địa phương), mỗi câu có danh sách cảnh báo bắt buộc do người có chuyên môn dược duyệt. Chỉ nguồn công khai, không dữ liệu bệnh nhân.
- Baseline: (1) Dense-only; (2) BM25; (3) Graph-only; (4) Hybrid trộn mềm w_g=0,2 (thiết lập ShenNongDiet); (5) Hybrid + lọc cứng (của mình); kết hợp lọc θ từ E1 nếu E1 có ích.
- Metric: Hit@1/Hit@3, MRR (so được với ShenNongDiet); **recall cảnh báo bắt buộc**, tỉ lệ khuyến nghị không phù hợp, độ chính xác từ chối (ba chỉ số tác giả đề xuất mà chưa làm); tỉ lệ truy vết bằng chứng; McNemar giữa (4) và (5), bootstrap 95% CI.
- GPU: không bắt buộc nếu dùng LLM qua API và embedding nhỏ; nếu chạy LLM mở 7-8B hoặc embedding lớn cục bộ cần GPU khoảng 16-24 GB. Không fine-tune ở bước này.
- Ghi chú: E1 và E2 chạy chung một KG và một bộ câu hỏi để tiết kiệm công gán nhãn.

## E3 (T1) Đồ thị phiên bản + lọc theo mốc áp dụng so với đặc trưng hệ phả tĩnh

- Nguồn: RES-33/RES-34, bài *Structure and Lineage Evidence for Vietnamese Statutory Article Retrieval on DRiLL* (arXiv 2611.09200, `papers/2026-11-26-drill-vn-statutory-retrieval.md`). Bài thêm 27 đặc trưng cấu trúc + hệ phả (citation/amendment/guidance) vào pipeline EDM, F2 71,77→72,91 trên DRiLL, lợi nhất ở câu cần Điều gốc + Điều sửa đổi (+4,45 pp, Bảng 8). Bài tự ghi các tín hiệu này "không kiểm chứng lịch sử pháp lý hay ngày hiệu lực" (mục 4.3), nên trục thời gian vẫn là khoảng trống của T1. Giả thuyết T1 không đổi, nhưng cần baseline mạnh này.
- Mục tiêu: chứng minh đồ thị phiên bản (cạnh sửa đổi/thay thế/bãi bỏ có ngày hiệu lực) + lọc theo mốc áp dụng (ngày hỏi, khoá học) trả lời đúng hơn so với đặc trưng hệ phả tĩnh, đặc biệt ở câu "theo quy chế hiện hành" và câu cần Điều gốc + Điều sửa đổi.
- Dữ liệu: (1) DRiLL (VLSP 2025, công khai; kiểm điều khoản dùng lại trước khi chạy) để tái lập baseline; (2) bộ câu hỏi có mốc thời gian dựng từ văn bản **công khai** của Bộ GD&ĐT (quy chế đào tạo và các văn bản sửa đổi), không dùng văn bản nội bộ trường; thêm nhóm câu "companion" (Điều gốc + Điều sửa đổi) theo kiểu Bảng 9 của bài.
- Baseline: (1) BM25; (2) BGE-M3 dense; (3) EDM 22 đặc trưng; (4) EDM + 27 đặc trưng pháp lý (thiết lập của bài); (5) GraphRAG không thuộc tính thời gian; (6) của mình: đồ thị phiên bản + lọc theo mốc áp dụng.
- Metric: F2 chính thức DRiLL và R@10/R@100 (so được với bài); trên bộ câu thời gian: độ chính xác điều khoản còn hiệu lực tại mốc hỏi, tỉ lệ trích dẫn điều khoản đã hết hiệu lực, F2 theo kích thước gold set (1 / 2 / ≥3 Điều); 5 seed, kiểm định có hiệu chỉnh BH như bài.
- GPU: tái lập đầy đủ bài cần LLM rerank cỡ 72B (Qwen2.5-72B), nên bỏ bước LLM hoặc dùng LLM nhỏ 7-8B (GPU khoảng 16-24 GB) và ghi rõ khác cấu hình; ranker LightGBM và BM25 chạy CPU; BGE-M3 embedding nên có GPU (khoảng 8-16 GB) nhưng chạy CPU được với 59.636 Điều.
- Ghi chú: đọc bài dataset DRiLL (ref [17]) trước khi chạy; tác giả cùng nhóm UIT, cần theo dõi nếu họ mở rộng sang văn bản giáo dục.
