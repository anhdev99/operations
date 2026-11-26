# Phản biện độc lập: đề tài 5 (đau từ video mặt, mô hình nhẹ, chuyển chéo BioVid ↔ UNBC, ECE)

Ngày kiểm: 2026-11-25. Chỉ ghi điều đã mở và đọc trong phiên này. Ký hiệu: ✓ đúng, ⚠ đúng một phần/cần sửa, ✗ sai, ? chưa kiểm được.

## 1. Kiểm từng bài / dataset

| Mục | DOI/link | Kết quả | Bằng chứng (trích từ Crossref/OpenAlex/trang gốc) |
|---|---|---|---|
| Gkikas 2024 | 10.3389/fpain.2024.1372814 | ✓ tồn tại, ✓ số liệu | Crossref: "Multimodal automatic assessment of acute pain through facial videos and heart rate signals utilizing transformer-based architectures", Front. Pain Res., 27/03/2024. Tóm tắt: "82.74% and 39.77% accuracy were achieved for the binary and multi-level pain classification task, respectively, utilizing 9.62 million parameters for the entire framework." Chỉ dùng BioVid (đúng ý "một dataset"). Câu "không đo bất định": tóm tắt không nhắc; ? chưa đọc toàn văn. |
| AI4Pain 2024 | 10.1109/aciiw63320.2024.00012 | ✓ tồn tại, ✓ số liệu | OpenAlex/Crossref: "The AI4Pain Grand Challenge 2024..." (Fernandez-Rojas, Joseph, Hirachan, Seymour, Goecke), ACIIW 15/09/2024. Tóm tắt: video mặt "40.0% for the validation set and 40.1% for the test set" (3 lớp); fNIRS 43.3% test; kết hợp 41.7% test. |
| AlamViT 2026 | 10.3390/math14183376 | ✓ tồn tại, ✓ 3,11M | Crossref: AlAbdouli, Rabie, Baziyad, Bonny, Mathematics, 17/09/2026. "The baseline contains 3.11 M parameters and requires approximately 2.2 GFLOPs per frame"; "deployment performance on clinical or edge hardware was not evaluated"; đánh giá "independently on the BioVid ... and AI4PAIN" (không train-một-test-kia). **Bổ sung mô tả còn thiếu:** BioVid ba seed chỉ 54,07%±4,62% (lần đầu 60,13%); AI4Pain nhị phân 90,97% là trên tập validation, không phải test; 3 lớp 51,33% test. Tức là nhóm này TẢI ĐƯỢC AI4Pain dù trang cũ 404. |
| Pittara 2025 | 10.1038/s41598-025-21987-3 | ✓ tồn tại | OpenAlex: "Machine learning methods on BioVid heat pain database for pain intensity estimation", Sci. Rep., 31/10/2025 (Pittara, Anastasiou, Andreou, Matsangidou, Panayides, Petkov, Pattichis). Tóm tắt: ảnh "captured during peak pain and no-pain moments", CNN 0.71, CvT 0.69, MobileViT50 0.60, VGG16 0.56; chỉ BioVid. Khớp "chỉ khung đỉnh, không video, không chéo dataset". |
| BioVid | https://www.nit.ovgu.de/BioVid.html | ✓ tồn tại; ⚠ cách ghi điều kiện | WebFetch (bản tóm lược của công cụ, không phải trích nguyên văn): "available for non-commercial research only"; Medical Psychology group, Ulm University cấp quyền; cố vấn ký phải có vị trí học thuật cố định ("permanent academic post"), sinh viên cần giáo sư ký. Part A: 87 người, 8.700 mẫu ✓. Lưu ý: bên cấp quyền là **Ulm**, không phải Magdeburg; "vị trí cơ hữu" ≈ permanent post, giảng viên đại học có biên chế/hợp đồng dài hạn có thể đạt, ? chưa rõ họ có chấp nhận cơ sở ngoài châu Âu/hợp đồng không biên chế. |
| UNBC-McMaster | https://www.jeffcohn.net/Resources/ | ✓ tồn tại; ✓ điều kiện | WebFetch: "Commercial use is not permitted"; "Requests must come from a university faculty member or research scientist", qua link PainArchive. Trang không nêu số video/người/khung; kích thước ? chưa kiểm (kiến thức chung: 200 video/25 người, nhưng KHÔNG xác minh trong phiên này, đừng trích). |
| AI4Pain | https://sites.google.com/view/ai4pain | ⚠ | Trang cũ ai4pain.github.io 404 (chưa tự mở lại). Site mới trên Google Sites còn sống; trang "Data and Protocol" chỉ nói đăng ký đội, **không có link tải hay quy trình xin dữ liệu**. WebSearch: 65 người (41 train/12 val/12 test), video Logitech 30 FPS; một bài arXiv 2025 nói dữ liệu sinh lý chưa công khai; kỳ 2025 chuyển sang tín hiệu sinh lý, có kỳ 2026. AlamViT và Prajod 2024 (arXiv 2406.11808, BioVid→AI4Pain) đã dùng được video AI4Pain, nên có đường tải (qua ban tổ chức), cách cụ thể ? chưa rõ. |

Kết luận mục 1: không bịa trích dẫn; 4 DOI đều thật, các số 82,74%, 9,62M, 40,1%, 3,11M đúng. Hai điểm cần sửa trong mô tả: (a) AlamViT độ chính xác thực tế thấp (54%) và đã dùng AI4Pain; (b) bên cấp BioVid là Ulm.

## 2. Bài bỏ sót

Công cụ: Crossref (nhiều truy vấn), OpenAlex (4 lần đầu ok, rồi hết hạn mức ngày "daily_budget", không dùng được nữa; không đăng ký khoá bằng email người dùng), arXiv API (HTTP 429 suốt phiên, không dùng được), WebSearch (5 truy vấn). Nên số truy vấn arXiv/OpenAlex đạt yêu cầu ≥6 là **chưa đủ**; phần bù bằng Crossref + WebSearch.

Đã mở và đọc (tóm tắt/trang gốc):
- **Morsali & Ghaffari, ErAS-Net, Sci. Rep. 2025, DOI 10.1038/s41598-025-04552-w** (Europe PMC abstract): huấn luyện UNBC (LOSO nhị phân 89,83%), rồi "cross-dataset experiment ... using the BioVid Heat Pain Database ... 78.14% accuracy for binary pain detection on unseen data without fine-tuning". Tức **đã có chuyển chéo giữa UNBC và BioVid**, hướng nhiều khả năng UNBC→BioVid (tóm tắt không ghi rõ hướng; một kết quả WebSearch nói "trained only on UNBC and tested on BioVid", chưa tự xác minh toàn văn). Không thấy đề cập số tham số hay hiệu chỉnh.
- **Othman, Werner, Saxen, Al-Hamadi, Walter, "Cross-Database Evaluation of Pain Recognition from Facial Video", ISPA 2019, DOI 10.1109/ispa.2019.8868562** (Crossref, không có abstract): có thật; theo WebSearch dùng BioVid và X-ITE (không UNBC). Nội dung ? chưa đọc.
- **Prajod, Schiller, Withanage Don, André, arXiv 2406.11808 (17/06/2024)**: CNN huấn luyện trên BioVid làm bộ trích đặc trưng, chuyển sang AI4Pain (đau điện), 3 lớp, vượt baseline. Chuyển chéo BioVid→AI4Pain đã có; không thấy UNBC trên trang.
- **Wang, Liu, Gunes, GraphAU-Pain, arXiv 2505.19802**: chỉ UNBC, không chéo dataset, không bất định.
- **Lee et al., arXiv 2006.12246 (2020)**: ước lượng đau từ video điện thoại bằng keypoint 2D/3D trên bệnh nhân sau mổ; chưa rõ kích thước mô hình/tốc độ.
- **Pain-Adapter, DOI 10.1145/3809986.3810091 (2026-03)** và **SecFePAS, DOI 10.1109/sec62691.2024.00046 (IEEE/ACM SEC 2024, "at the Edge")**: chỉ thấy tiêu đề trên Crossref, không có abstract; ? nội dung, nhưng gợi ý đã có hướng "tham số-hiệu quả" và "edge" cho đánh giá đau.
- Dai, Broekens, Truong 2019 (TU Delft, WebSearch tóm tắt): nói gần như mọi bài chỉ train/test trong UNBC, hỏi về tổng quát hoá. Không mở được PDF (ECONNREFUSED) nên ? kết quả.
- Xu & de Sa 2021 (NSF PAR 10300302): bất định cho cá nhân hoá đau trên UNBC (theo WebSearch, chưa mở). Neo & Chen arXiv 2312.11542: ECE cho FER nói chung, không riêng đau.

**Trả lời câu hỏi:** Chuyển chéo BioVid→UNBC theo đúng hướng đề xuất: **không tìm thấy** trong các nguồn đã tra (không có nghĩa là không tồn tại; arXiv/OpenAlex không tra được đầy đủ). Nhưng UNBC↔BioVid (ErAS-Net) và BioVid→AI4Pain đã có người làm, nên "chưa ai chuyển chéo" không còn đúng ở dạng tổng quát. Không thấy bài nào kết hợp ECE/hiệu chỉnh với đau từ video mặt ở các nguồn đã tra.

## 3. Thực tế

- **Ít liên quan nha khoa trực tiếp**: đúng. BioVid là đau nhiệt ở cẳng tay trên tình nguyện viên; UNBC là đau vai tự nhiên khi vận động (bệnh nhân) nhưng nhãn PSPI do người chấm, mất cân bằng nặng (kiến thức chung, chưa xác minh trong phiên). Nhãn BioVid theo nhiệt độ kích thích, nhãn UNBC theo quan sát viên, nên chéo dataset còn lệch định nghĩa nhãn. Sau chuyển chéo, giá trị lâm sàng nha khoa vẫn cần dữ liệu mới.
- **Truy cập**: chủ nhóm là giảng viên nên phù hợp điều kiện của cả BioVid (cố vấn có vị trí cố định) lẫn UNBC (faculty/research scientist). Chưa nộp thì chưa chắc; thời gian duyệt ? không biết. Đây là điều kiện chặn: gửi form trước khi chốt.
- **Đủ sức làm NCS?** Là một chương nhỏ/1-2 bài, chưa đủ làm trục chính: tính mới đã bị thu hẹp (ErAS-Net, Prajod, Pain-Adapter, AlamViT), kết quả chéo dataset có thể thấp và khó đứng riêng. Mạnh ở chỗ: khoảng trống "độ bất định + nhẹ + chéo dataset đồng thời" vẫn trống theo các nguồn đã tra; bài benchmark/kiểm chứng tái lập có thể đăng IEEE Access hoặc hội nghị affective computing. Hợp làm đề tài phụ gắn với hướng cảm xúc, không nên là #1 cho hồ sơ NCS.

## 4. Kết luận

**Giữ ở top 5 có điều kiện nhưng hạ điểm.** Điểm cũ 4/5/3/4/4 = 20.

| Tiêu chí | Cũ | Đề xuất | Lý do |
|---|---|---|---|
| Mới | 4 | **3** | Đã có chuyển chéo UNBC→BioVid (ErAS-Net), BioVid→AI4Pain; AlamViT/Pain-Adapter/SecFePAS chiếm "nhẹ/edge". Còn trống: tổ hợp ≤5M + chéo hai hướng + ECE + đo CPU/điện thoại. |
| Ứng dụng | 5 | **4** | Đau nhiệt ≠ đau lâm sàng nha khoa; demo chỉ tình nguyện viên. |
| Khả thi | 3 | 3 | Đúng; phụ thuộc duyệt dữ liệu; AlamViT cho thấy độ chính xác thực ~54% 5 lớp. |
| Chuẩn bị | 4 | 4 | Giữ. |
| NCS | 4 | **3** | Chỉ đủ một chương, tính mới hẹp. |
| **Tổng** | 20 | **17** | |

Với 17 điểm, đề tài xuống dưới phương án thay (DENTEX 19 điểm theo file gốc, chưa kiểm trong phiên này). Khuyến nghị: nếu Dean vẫn giữ thì chỉ theo đuổi sau khi nhận được BioVid + UNBC; nếu không, chuyển sang DENTEX. Nếu giữ, định vị lại là "benchmark chéo hai hướng, đối chiếu ErAS-Net, thêm hiệu chỉnh" và nêu rõ ErAS-Net/Prajod trong khoảng trống.

## Chưa kiểm được
- arXiv API bị 429 và OpenAlex hết hạn mức: các truy vấn arXiv/OpenAlex không hoàn thành; tìm bài sót chưa đầy đủ, nhất là 2025-2026.
- Toàn văn: Gkikas (có đo bất định không), ErAS-Net (hướng chéo, tham số), Othman 2019, Dai 2019, Pain-Adapter, SecFePAS, Xu & de Sa.
- Câu chữ nguyên văn điều kiện BioVid/UNBC (WebFetch chỉ trả bản tóm lược); thời gian duyệt; kích thước UNBC; link tải AI4Pain; điểm DENTEX.
