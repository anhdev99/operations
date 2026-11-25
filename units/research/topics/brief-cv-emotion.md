# Brief: Computer vision + nhận diện cảm xúc (RES-6)

Người soạn: Scholar · Ngày: 2026-11-24 · Dùng cho: RES-1 (chọn top 5 đề tài)

## Cách kiểm chứng

- Bài báo: tra qua OpenAlex API (metadata + abstract) trong lượt này; arXiv trả 429 nên không dùng được. Chỉ đọc **abstract**, chưa đọc toàn văn; số liệu trích đúng như abstract.
- Dataset: đã mở trang chính thức (BioVid, DAiSEE, RAF-DB, README EngageNet, README MER2024, trang tài nguyên Jeffrey Cohn cho UNBC/CK+). Trang AffectNet (mohammadmahoor.com) trả 404, nên điều kiện AffectNet **chưa kiểm chứng**.
- Nơi công bố: đã xác minh tồn tại qua OpenAlex (tên, ISSN-L, NXB, trang chủ). **Trạng thái Scopus chưa kiểm chứng trực tiếp**, chủ nhóm cần tra Scopus/SJR trước khi nộp.

## Bức tranh nhanh (mức bão hoà)

- **FER ảnh tĩnh 7 cảm xúc trên RAF-DB/AffectNet/FER2013: bão hoà.** Rất nhiều bài 2025-2026 chỉ so sánh ResNet/ViT/EfficientNet trên RAF-DB (tra OpenAlex thấy hàng loạt bài "comparative study" ở hội nghị nhỏ). Mạng nhẹ cũng đã nhiều (PAtt-Lite, LITE-FER, RS-Xception...). Tăng 0,5% accuracy không còn là đóng góp.
- **Đa phương thức (video + âm thanh + văn bản):** sân chơi chính là chuỗi challenge MER (2023, 2024, 2025) dữ liệu tiếng Trung, cần nhiều bộ trích đặc trưng và GPU; hướng mới là open-vocabulary và MLLM (EmoLLM/EmoBench 287k mẫu). Một người, GPU hạn chế khó cạnh tranh.
- **Ứng dụng y tế (đánh giá đau):** chưa bão hoà. Nhánh khuôn mặt còn yếu: baseline AI4Pain 2024 chỉ 40,1% (3 lớp) với video mặt; BioVid đa mức chỉ ~40%. Từ 2025 challenge AI4Pain chuyển sang tín hiệu sinh lý, nên nhánh **video mặt nhẹ, chạy thiết bị, kiểm chứng chéo dataset** ít người làm.
- **Giáo dục (mức tập trung/engagement):** nhiều bài ứng dụng, nhưng benchmark có vấn đề nhãn (DAiSEE κ ~0,05-0,09 giữa clip kề nhau, theo bài audit 2026). Khoảng trống nằm ở **đánh giá đúng cách**, không ở kiến trúc mới.

---

## Đề tài 1: Đánh giá đau từ video khuôn mặt bằng mô hình nhẹ, kiểm chứng chéo dataset, có độ bất định

**Câu hỏi nghiên cứu.** Mô hình video khuôn mặt ≤5M tham số chạy trên CPU/điện thoại có giữ được độ chính xác phát hiện đau (đau/không đau, 3 mức) khi chuyển từ BioVid sang dataset khác (UNBC-McMaster, AI4Pain 2024) không? Thêm ước lượng độ bất định (để "không chắc thì hỏi lại bệnh nhân") giảm bao nhiêu cảnh báo sai?

**Khoảng trống (bài đã đọc abstract):**
1. Gkikas S., Tachos N.S., Andreadis S.T., Pezoulas V.C. et al., 2024, *Multimodal automatic assessment of acute pain through facial videos and heart rate signals utilizing transformer-based architectures*, Frontiers in Pain Research. https://doi.org/10.3389/fpain.2024.1372814. BioVid, video + nhịp tim, 82,74% (nhị phân) và 39,77% (đa mức), 9,62M tham số. **Chưa làm:** chỉ một dataset (BioVid), không kiểm chứng chéo, không đo độ bất định.
2. Fernandez Rojas R., Joseph C., Hirachan N., Seymour B. et al., 2024, *The AI4Pain Grand Challenge 2024: Advancing Pain Assessment with Multimodal fNIRS and Facial Video Analysis*, ACIIW 2024. https://doi.org/10.1109/aciiw63320.2024.00012. Baseline video mặt chỉ 40,1% test (3 lớp), thấp hơn fNIRS. **Chưa làm:** nhánh video mặt yếu; các năm 2025, 2026 bỏ video (DOI 10.1145/3747327.3764791, 10.1109/aciiw71585.2026.11712097), nên benchmark video mặt bị bỏ ngỏ.
3. Alabdouli A., Rabie T.F., Baziyad M.S., Bonny T., 2026, *AlamViT: A Lightweight Spatiotemporal Facial Expression Model for Automated Pain Recognition*, Mathematics (MDPI). https://doi.org/10.3390/math14183376. 3,11M tham số, ~2,2 GFLOPs/khung; BioVid 54,07% ± 4,62 (3 seed), AI4PAIN 3 lớp 51,33%. **Chưa làm (tác giả tự ghi):** chưa đo triển khai trên phần cứng biên/lâm sàng; hai dataset đánh giá riêng, không train-một-test-kia.
4. Pittara M. et al., 2025, *Machine learning methods on BioVid heat pain database for pain intensity estimation*, Scientific Reports. https://doi.org/10.1038/s41598-025-21987-3. CNN 0,71, MobileViT 0,60 (đau/không đau, khung đỉnh). **Chưa làm:** chỉ ảnh khung đỉnh, không video, không chéo dataset.
- Tổng quan hỗ trợ: Huo J. et al., 2024, JMIR, https://doi.org/10.2196/51250 (45 báo cáo, accuracy dao động 0,27-0,99, cho thấy giao thức đánh giá không đồng nhất).

Chỗ trống cụ thể: **mô hình nhẹ + đánh giá chéo dataset theo người (subject-independent) + độ bất định + đo thật trên CPU/điện thoại.**

**Dataset công khai (không phải dữ liệu bệnh nhân; đau gây ra thực nghiệm trên tình nguyện viên):**
| Tên | Link | Giấy phép / truy cập | Kích thước |
|---|---|---|---|
| BioVid Heat Pain (Part A) | https://www.nit.ovgu.de/BioVid.html | Chỉ nghiên cứu phi thương mại; người ký phải có **vị trí cơ hữu ở viện/trường** (sinh viên nhờ GV ký), gửi form cho nhóm Ulm | Part A: 8.700 mẫu, 87 người, 5 lớp, cửa sổ 5,5 s; có giao thức leave-one-subject-out khuyến nghị |
| UNBC-McMaster Shoulder Pain | https://www.jeffcohn.net/Resources/ | Yêu cầu từ giảng viên/nhà nghiên cứu; cấm thương mại | Kích thước chưa kiểm chứng trong lượt này |
| AI4Pain 2024 (video mặt + fNIRS) | DOI bài ở trên; trang ai4pain.github.io trả 404 | **Chưa kiểm chứng** cách tải | Chưa kiểm chứng |

**Baseline 1-2 tháng (GPU hạn chế):**
- Tuần 1-2: cắt mặt + chuẩn hoá (MediaPipe/OpenFace), trích đặc trưng từ backbone nhẹ đã train FER (MobileNet/MobileViT) đóng băng; temporal head nhỏ (1D-conv/GRU). BioVid Part A, giao thức 5 lớp và nhị phân, LOSO hoặc split của Gkikas (theo trang BioVid).
- Tuần 3-5: train BioVid, test UNBC (và ngược lại) để đo suy giảm chéo dataset; thêm MC-dropout hoặc temperature scaling, báo ECE và tỉ lệ cảnh báo sai ở ngưỡng từ chối.
- Tuần 6-8: xuất ONNX/TFLite int8, đo FPS và độ trễ trên laptop CPU + 1 điện thoại Android; 3 seed cho mọi số liệu.

**Ứng dụng/demo:** ứng dụng theo dõi đau cho điều dưỡng/nha sĩ: camera máy tính bảng đặt cạnh ghế nha/giường hậu phẫu, chạy cục bộ (không gửi video lên mạng), hiển thị chỉ số đau + mức không chắc chắn; nhắc hỏi bệnh nhân khi vượt ngưỡng. Demo chỉ chạy trên người tình nguyện/chính tác giả, **không quay bệnh nhân thật** khi chưa có phê duyệt đạo đức.

**Nơi công bố (OpenAlex; Scopus cần tra lại):**
- Frontiers in Pain Research (Frontiers, ISSN-L 2673-561X) — https://www.frontiersin.org/journals/pain-research
- IEEE Access (IEEE, ISSN-L 2169-3536) — http://ieeexplore.ieee.org/servlet/opac?punumber=6287639
- IEEE Transactions on Affective Computing (IEEE, ISSN-L 1949-3045, mục tiêu cao) — http://ieeexplore.ieee.org/servlet/opac?punumber=5165369

**Điểm:**
| Tiêu chí | Điểm | Lý do |
|---|---|---|
| Tính mới | 4 | Chéo dataset + độ bất định + đo thật trên thiết bị cho đau từ mặt còn trống; AlamViT tự nhận chưa đo trên biên. |
| Ứng dụng | 5 | Bệnh nhân không nói được (hậu phẫu, trẻ em, người già) là nhu cầu lâm sàng rõ; nối với nha khoa. |
| Khả thi một người | 3 | Mô hình nhỏ, GPU vừa đủ; nhưng **truy cập dữ liệu cần người có vị trí cơ hữu ký** và chờ duyệt. |
| Công bố | 4 | Tạp chí y sinh/affective nhận bài đánh giá có kiểm soát; số liệu tuyệt đối thấp nhưng câu chuyện "trung thực" bán được. |
| Hồ sơ NCS | 4 | Chuỗi: đau từ mặt nhẹ → chéo dataset/bất định → đa phương thức (mặt + giọng) → thử nghiệm phòng khám nha có phê duyệt; nối hướng chatbot đồng cảm. |
| **Tổng** | **20/25** | |

**Rủi ro:** không được cấp BioVid/UNBC (điều kiện ký); đau thực nghiệm (nhiệt ở tay) khác đau nha khoa thật; độ chính xác đa mức thấp (~40-55%) khiến demo kém thuyết phục; triển khai lâm sàng sau này cần phê duyệt đạo đức.

---

## Đề tài 2: Đo mức tập trung của người học trực tuyến bằng mô hình nhẹ, đánh giá theo từng người

**Câu hỏi nghiên cứu.** Khi đánh giá đúng cách (tách người, đo phân biệt trong-cùng-một-người, kiểm tra nhất quán nhãn), mô hình nhẹ dựa trên đặc trưng mặt/ánh nhìn/tư thế còn giữ được lợi thế so với baseline đơn giản không? Mô hình chạy trên trình duyệt có đủ để giáo viên dùng trong lớp trực tuyến?

**Khoảng trống (bài đã đọc abstract):**
1. Le Truong Giang, Xu X., Mai X.-D., 2026, *Auditing Label Consistency and Person-Level Variance in Video-Based Engagement Recognition Benchmarks: Evidence From DAiSEE and EngageNet*, IEEE Access. https://doi.org/10.1109/access.2026.3755835. DAiSEE: κ giữa clip kề nhau 0,085 (val) và 0,053 (test); EngageNet κ 0,45-0,53 nhưng ~một nửa phương sai nhãn nằm giữa các người. Khuyến nghị báo cáo nhất quán nhãn, phân biệt trong-người. **Chưa làm:** chỉ audit, không đề xuất mô hình nhẹ/triển khai theo các thước đo mới.
2. Singh M., Hoque X., Zeng D., Wang Y., 2026, *EngageNet++: Affective Integration and Interpretable Multimodal Engagement Prediction*, IEEE TAFFC. https://doi.org/10.1109/taffc.2026.3739572. TCN + Transformer song song, thêm đặc trưng cảm xúc, có giải thích. **Chưa làm:** không nhắm thiết bị nhẹ; abstract không báo thước đo trong-người.
3. Zhao Z., Li Y., Yang J., Ma Y., 2024, *A lightweight facial expression recognition model for automated engagement detection*, Signal, Image and Video Processing. https://doi.org/10.1007/s11760-024-03020-8 (chỉ có metadata, **không có abstract** trên OpenAlex, không dùng để chấm).
4. Karimah S.N., Hasegawa S., 2022, *Automatic engagement estimation in smart education/learning settings: a systematic review...*, Smart Learning Environments. https://doi.org/10.1186/s40561-022-00212-y. 47 bài; engagement cảm xúc đo qua tín hiệu affect chiếm đa số. Booth B.M., Bosch N., D'Mello S.K., 2023, Proceedings of the IEEE, https://doi.org/10.1109/jproc.2023.3309560: nhấn mạnh engagement là khái niệm đa thành phần, gắn bối cảnh.

Chỗ trống cụ thể: **mô hình nhẹ chạy trình duyệt + báo cáo theo bộ thước đo của bài audit (1) + giải thích được cho giáo viên.** Chưa thấy dataset engagement người Việt công khai (chỉ tra OpenAlex, **chưa kiểm chứng đầy đủ**).

**Dataset công khai:**
| Tên | Link | Giấy phép / truy cập | Kích thước |
|---|---|---|---|
| DAiSEE | https://people.iith.ac.in/vineethnb/resources/daisee/index.html | Điền form; chỉ nghiên cứu; không chia sẻ cho bên thứ hai; chỉ in ảnh của một số người được phép | 9.068 clip, 112 người, 4 trạng thái × 4 mức; ~15 GB |
| EngageNet | https://github.com/engagenet/engagenet_baselines | Gửi email xin (abhinav@iitrpr.ac.in); giấy phép cụ thể **chưa kiểm chứng** | ~31 giờ, 127 người, 11,3K clip 10 s, 4 mức; split theo người 90/11/26 |

**Baseline 1-2 tháng:** trích đặc trưng mỗi khung bằng MediaPipe Face Mesh (ánh nhìn, tư thế đầu, blendshape) + FER nhẹ đóng băng; TCN/GRU nhỏ. Báo cáo accuracy, macro-F1 **và** thước đo trong-người/nhất quán nhãn theo bài audit. So với baseline chỉ dùng tư thế đầu. Chạy trên GPU 8 GB hoặc CPU. 3 seed.

**Ứng dụng/demo:** extension/web app cho giáo viên dạy trực tuyến: chạy hoàn toàn trên máy học viên (không gửi video), chỉ gửi chỉ số tổng hợp ẩn danh của cả lớp theo thời gian ("phút 12-15 nhiều học viên mất tập trung"). Học viên phải đồng ý bật.

**Nơi công bố (OpenAlex; Scopus cần tra lại):**
- Smart Learning Environments (Springer Nature, ISSN-L 2196-7091) — https://slejournal.springeropen.com
- Education and Information Technologies (Springer, ISSN-L 1360-2357) — https://www.springer.com/journal/10639
- IEEE Access (như trên)

**Điểm:**
| Tiêu chí | Điểm | Lý do |
|---|---|---|
| Tính mới | 3 | Đánh giá theo người + mô hình nhẹ là góc mới, nhưng mảng engagement đông bài. |
| Ứng dụng | 4 | Giáo viên dùng ngay được; nhưng giám sát học viên nhạy cảm về quyền riêng tư. |
| Khả thi một người | 4 | DAiSEE tải qua form, GPU nhỏ đủ; EngageNet phải xin email. |
| Công bố | 4 | Tạp chí giáo dục-công nghệ nhận tốt nghiên cứu ứng dụng có đánh giá cẩn thận. |
| Hồ sơ NCS | 3 | Chuỗi có thể (nhẹ → đa phương thức → triển khai lớp học VN) nhưng xa hướng y tế/răng hàm mặt. |
| **Tổng** | **18/25** | |

**Rủi ro:** nhãn DAiSEE nhiễu nặng (κ thấp) nên kết quả trần thấp; bài audit 2026 có thể đã có phần tiếp theo; vấn đề đạo đức/riêng tư khi demo ở lớp học thật cần sự đồng ý.

---

## Đề tài 3: FER nén cho thiết bị biên: độ chính xác, công bằng và độ bền với khuôn mặt châu Á

**Câu hỏi nghiên cứu.** Lượng tử hoá int8 + chưng cất + cắt tỉa ảnh hưởng thế nào tới khoảng cách hiệu năng giữa các nhóm (giới, tuổi, chủng tộc) của FER trên RAF-DB, và có giữ được khi chuyển sang khuôn mặt người Việt không?

**Khoảng trống (bài đã đọc abstract):**
1. Stoychev S., Güneş H., 2023, *The Effect of Model Compression on Fairness in Facial Expression Recognition*, LNCS (Springer). https://doi.org/10.1007/978-3-031-37745-7_9. Trên RAF-DB, nén không làm tăng chênh lệch giới/chủng tộc/tuổi; trên CK+ làm tăng thiên lệch giới. **Chưa làm:** dùng một mạng phân loại cơ bản, chưa thử mạng nhẹ hiện đại, chưa đo trên thiết bị thật, chưa có dữ liệu châu Á riêng.
2. Biçer E., Köse H., 2024, *LITE-FER: A Lightweight Facial Expression Recognition Framework for Children in Resource-Limited Devices*, FG 2024. https://doi.org/10.1109/fg59268.2024.10581970. KD + cắt tỉa, 113,98K tham số, 30 FPS CPU. **Chưa làm:** không đo công bằng.
3. Lian T., Çeliktutan O., 2026, *Towards Pareto Efficiency in Fair Facial Expression and Action Unit Recognition*, FG 2026. https://doi.org/10.1109/fg67764.2026.11557017. Tối ưu đa mục tiêu utility-fairness, có code (github.com/Supltz/UFTO, README chưa mở được). **Chưa làm:** không xét mô hình nén/biên.
4. Chau M.T., Dam A.D., 2024, *Enhancing Emotion Recognition with Stacked Machine Learning Models: Insights from a Novel Vietnamese Facial Expression Dataset*, ICIIT 2024. https://doi.org/10.1145/3654522.3654523. 3.087 ảnh, 441 người Việt, 7 cảm xúc, 84,25%. **Tính công khai của dataset chưa kiểm chứng** (abstract không có link).

**Dataset công khai:**
| Tên | Link | Giấy phép / truy cập | Kích thước |
|---|---|---|---|
| RAF-DB | http://www.whdeng.cn/RAF/model1.html | Phi thương mại; email từ tài khoản trường đại học để lấy mật khẩu; không phân phối lại | 29.672 ảnh; 7 cảm xúc cơ bản + 12 phức hợp; có nhãn chủng tộc, tuổi, giới |
| AffectNet / AffectNet+ | bài TAFFC 2025: https://doi.org/10.1109/taffc.2025.3634523 | **Chưa kiểm chứng** (trang chủ 404) | chưa kiểm chứng |
| Bộ người Việt (Chau & Dam) | không có link | **Chưa kiểm chứng** công khai | 3.087 ảnh (theo abstract) |

**Baseline 1-2 tháng:** MobileNetV3/EfficientNet-Lite trên RAF-DB; ma trận thí nghiệm FP32 / int8 PTQ / QAT / KD; báo accuracy tổng + chênh lệch nhóm (equal opportunity, worst-group accuracy) theo nhãn chủng tộc/tuổi/giới của RAF-DB; đo độ trễ ONNX/TFLite trên CPU và điện thoại. 3 seed. Rất nhẹ GPU.

**Ứng dụng/demo:** module FER chạy cục bộ trong app (ví dụ tablet ở phòng chờ nha khoa để đo phản ứng khi xem video thư giãn, hoặc robot/kiosk giáo dục), kèm "thẻ công bằng" cho từng bản nén để chọn bản phù hợp.

**Nơi công bố (OpenAlex; Scopus cần tra lại):**
- Signal, Image and Video Processing (Springer, ISSN-L 1863-1703) — https://www.springer.com/journal/11760
- Multimedia Tools and Applications (Springer, ISSN-L 1380-7501) — https://www.springer.com/journal/11042
- IEEE Access (như trên)

**Điểm:**
| Tiêu chí | Điểm | Lý do |
|---|---|---|
| Tính mới | 2 | Bài 2023 đã làm câu hỏi gốc; phần thêm (mạng nhẹ hiện đại, thiết bị thật) là mở rộng nhỏ. |
| Ứng dụng | 3 | Module dùng lại được, nhưng tự nó không giải bài toán người dùng cụ thể. |
| Khả thi một người | 4 | Dataset nhỏ, chạy rẻ; RAF-DB cần email trường đại học. |
| Công bố | 3 | Dễ ra tạp chí ứng dụng; khó lên venue mạnh vì FER đã bão hoà. |
| Hồ sơ NCS | 3 | Làm bài "nền" cho Đề tài 1/2 được, đứng riêng thì mạch yếu. |
| **Tổng** | **15/25** | |

**Rủi ro:** dễ bị phản biện "FER bão hoà, chỉ là thí nghiệm"; nhãn chủng tộc RAF-DB thô (không tách Đông Nam Á); không có dataset người Việt công khai đã kiểm chứng.

---

## Tổng hợp

| # | Đề tài | Mới | Ứng dụng | Khả thi | Công bố | NCS | Tổng |
|---|---|---|---|---|---|---|---|
| 1 | Đánh giá đau từ video mặt, mô hình nhẹ, chéo dataset + bất định | 4 | 5 | 3 | 4 | 4 | **20** |
| 2 | Engagement người học, mô hình nhẹ, đánh giá theo người | 3 | 4 | 4 | 4 | 3 | **18** |
| 3 | FER nén cho biên: công bằng + khuôn mặt châu Á | 2 | 3 | 4 | 3 | 3 | **15** |

Khuyến nghị: Đề tài 1 hợp nhất với điểm giao y tế/răng hàm mặt và chatbot đồng cảm (bộ phát hiện đau/lo âu cấp tín hiệu cho chatbot). Bước đầu tiên cần làm ngay: nhờ người có vị trí cơ hữu ký form BioVid/UNBC, vì chờ duyệt là rủi ro lớn nhất. Đề tài 3 chỉ nên làm như chương phụ của Đề tài 1.

## Đã cân nhắc nhưng loại

- **Nhận diện cảm xúc đa phương thức kiểu MER (video + âm thanh + văn bản):** dữ liệu tiếng Trung, phải ký EULA, pipeline nặng nhiều bộ trích đặc trưng, track open-vocabulary cần API OpenAI trả phí (README MER2024); không hợp một người, GPU hạn chế.
- **MLLM hiểu cảm xúc (EmoLLM/EmoBench, https://doi.org/10.48550/arxiv.2406.16442):** cần fine-tune mô hình đa phương thức lớn trên 287k mẫu, tốn GPU; cạnh tranh với nhóm lớn.
- **Đo lo âu nha khoa từ video bệnh nhân thật:** không có dataset công khai (tìm OpenAlex "facial expression dental" không ra kết quả), phải quay bệnh nhân, vướng quy tắc dữ liệu y tế; để sau khi có phê duyệt đạo đức.

## Việc cần chủ nhóm làm trước khi chốt

1. Tra Scopus/SJR cho các tạp chí trên.
2. Xác định người ký form BioVid (vị trí cơ hữu) và gửi yêu cầu UNBC-McMaster; hỏi cách tải AI4Pain 2024.
3. Liên hệ tác giả Chau & Dam (ICIIT 2024) xem bộ ảnh người Việt có chia sẻ cho nghiên cứu không.
