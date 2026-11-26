# Brief: Computer vision + răng hàm mặt (RES-2)

Người soạn: Scholar · Ngày: 2026-11-24 · Dùng cho: RES-1 (chọn top 5 đề tài)

## Cách kiểm chứng

- Mọi bài dưới đây đã mở trang abstract trên arXiv (hoặc tra DOI qua Crossref) trong lượt này. Chỉ đọc **abstract + trang dataset/README**, chưa đọc toàn văn; số liệu trích lại đúng như abstract.
- Dataset: đã mở trang Hugging Face / GitHub / Figshare, ghi giấy phép và dung lượng như trang hiển thị.
- Nơi công bố: đã xác minh tồn tại qua OpenAlex (tên, ISSN-L, nhà xuất bản, trang chủ). **Trạng thái Scopus chưa kiểm chứng trực tiếp** (SCImago trả 403 khi truy cập tự động); chủ nhóm cần tra lại trên Scopus/SJR trước khi nộp.

## Bức tranh nhanh (mức bão hoà)

- **Phân đoạn răng (panoramic, CBCT): bão hoà.** Đã có 2 challenge MICCAI (STS 2023, STS 2024) với >90.000 ảnh/lát, top đội dùng SAM + bán giám sát (arXiv:2511.22911). Làm thêm một mạng phân đoạn khó có điểm mới.
- **Phát hiện răng bất thường + đánh số FDI: gần bão hoà.** DENTEX (MICCAI 2023) đã có benchmark, baseline khuếch tán HierarchicalDet, nhiều đội top.
- **Vision-language / sinh báo cáo: đang nóng, chạy rất nhanh.** Từ 9/2025 đến 11/2026 có ít nhất MMOral/OralGPT (NeurIPS'25), OPGAgent, DentiAsk, PanDent, AgenTeeth, Pocket-Dentist, PeriaTrace, DentAgent. Hướng mở chỉ còn ở ngách: ngôn ngữ khác tiếng Anh/Trung, mô hình nhỏ chạy cục bộ, kiểm soát ảo giác ở mức răng.
- **Landmark cephalometric:** có dataset mới đa thiết bị (Aariz, Scientific Data 2025) nên bài toán **tổng quát hoá giữa máy chụp** còn đất.

---

## Đề tài 1: Sinh báo cáo panoramic tiếng Việt có căn cứ ở mức răng, chạy trên GPU nhỏ

**Câu hỏi nghiên cứu.** Pipeline "detector chuyên biệt + VLM nhỏ (≤4B) đóng băng" có sinh được báo cáo panoramic **tiếng Việt** có cấu trúc (vị trí FDI, phát hiện, mức độ) với tỉ lệ ảo giác ở mức răng thấp hơn VLM fine-tune trực tiếp không? Bằng chứng từ công cụ cần bao nhiêu để đủ?

**Khoảng trống (bài đã mở):**
1. Hao J. et al., 2025, *Towards Better Dental AI: A Multimodal Benchmark and Instruction Dataset for Panoramic X-ray Analysis* (MMOral/OralGPT), NeurIPS 2025 (theo README repo). https://arxiv.org/abs/2509.09254 · DOI 10.48550/arXiv.2509.09254. 20.563 ảnh, 1,3 triệu instruction, GPT-4o chỉ 41,45% trên MMOral-Bench. **Chưa làm:** chỉ tiếng Anh; dùng Qwen2.5-VL-7B SFT, cần GPU lớn.
2. Yu Z. et al., 2026, *OPGAgent: An Agent for Auditable Dental Panoramic X-ray Interpretation*, arXiv. https://arxiv.org/abs/2603.00462. Đề xuất OPG-Bench dạng bộ ba (Location, Field, Value) để đo ảo giác. **Chưa làm:** code "sẽ phát hành khi được nhận"; benchmark dựng từ báo cáo lâm sàng riêng; không tiếng Việt.
3. Rafid A. et al., 2026, *AgenTeeth: ... Suppressing Hallucination in Frozen Vision-Language Models on Dental X-Rays via Tool Evidence Injection*, arXiv. https://arxiv.org/abs/2609.17800. 7 mô hình chuyên gia, VLM đóng băng, +12,9 đến 23,0 điểm trên MMOral-OPG-Bench; có phát hành mã và mô hình. **Chưa làm:** chỉ VQA, không sinh báo cáo đầy đủ; không xét mô hình nhỏ chạy cục bộ; không đa ngôn ngữ.
4. Li X. et al., 2026, *PanDent: Toward Comprehensive Tooth-Level Structure-Language Consistency in Dental Radiology*, arXiv. https://arxiv.org/abs/2607.27378. 9.554 ảnh, đo cả văn bản lẫn nhất quán mức răng; mô hình "viết trôi chảy nhưng sai vị trí". **Chưa làm:** dữ liệu đầy đủ chưa phát hành; chỉ tiếng Anh.

Chỗ trống cụ thể: **báo cáo tiếng Việt + VLM nhỏ + đo ảo giác mức răng**. Chưa thấy bài nào về nha khoa tiếng Việt (tìm arXiv bị giới hạn tần suất, **chưa kiểm chứng đầy đủ** — cần tra thêm Google Scholar trước khi chốt).

**Dataset công khai:**
| Tên | Link | Giấy phép / truy cập | Kích thước |
|---|---|---|---|
| DENTEX | https://huggingface.co/datasets/ibrahimhamamci/DENTEX | CC BY-NC-SA 4.0, tải tự do | 11,8 GB; 693 + 634 + 1.005 ảnh có nhãn phân cấp, 1.571 ảnh không nhãn; 4 chẩn đoán (sâu răng, sâu sâu, tổn thương quanh chóp, răng ngầm) |
| MMOral-OPG-Bench | https://huggingface.co/datasets/OralGPT/MMOral-OPG-Bench | MIT, không gated | 100 ảnh, 491 câu đóng + 578 câu mở (~364 MB TSV) |
| MMOral-OPG-Training | https://huggingface.co/datasets/OralGPT/MMOral-OPG-Training | gated "manual" (phải xin), giấy phép chưa kiểm chứng | chưa kiểm chứng |

**Baseline 1-2 tháng (GPU hạn chế):**
- Tuần 1-3: YOLOv8/v11 hoặc RT-DETR trên DENTEX (đánh số FDI + 4 chẩn đoán); đã có mô hình cộng đồng trên HF để đối chiếu.
- Tuần 4-6: chuyển đầu ra detector thành JSON (FDI, phát hiện, độ tin cậy) và đưa vào VLM nhỏ đóng băng (Qwen2.5-VL-3B hoặc tương đương, 4-bit) để viết báo cáo tiếng Việt theo mẫu; so với VLM không có bằng chứng.
- Tuần 7-8: đo trên tập test DENTEX quy về bộ ba (răng, phát hiện, giá trị): precision/recall mức răng, tỉ lệ ảo giác; bản dịch tiếng Việt MMOral-OPG-Bench (100 ảnh) cho VQA. Cần 1 nha sĩ duyệt mẫu nhỏ báo cáo.

**Ứng dụng/demo:** web app (Gradio) cho phòng khám nha nhỏ: nha sĩ tải ảnh panoramic, nhận bản nháp báo cáo tiếng Việt có khung đánh dấu từng răng, sửa rồi in cho bệnh nhân. Chạy trên 1 GPU 8-12 GB hoặc CPU chậm.

**Nơi công bố (đã kiểm chứng tồn tại qua OpenAlex; Scopus cần tra lại):**
- Dentomaxillofacial Radiology (Oxford University Press, ISSN-L 0250-832X) — https://www.birpublications.org/toc/dmfr/current
- Journal of Imaging Informatics in Medicine (Springer, ISSN-L 0897-1889) — https://link.springer.com/journal/10278
- IEEE Access (IEEE, ISSN-L 2169-3536) — http://ieeexplore.ieee.org/servlet/opac?punumber=6287639

**Điểm:**
| Tiêu chí | Điểm | Lý do |
|---|---|---|
| Tính mới | 4 | Tiếng Việt + VLM nhỏ + đo ảo giác mức răng chưa thấy ai làm; nhưng mảng chung rất đông. |
| Ứng dụng | 5 | Bản nháp báo cáo tiếng Việt dùng ngay được ở phòng khám, demo trực quan. |
| Khả thi một người | 4 | Toàn bộ là ghép mô hình sẵn + detector nhỏ; khó nhất là có nha sĩ duyệt. |
| Công bố | 4 | Có câu chuyện rõ (ngôn ngữ ít tài nguyên, ảo giác); tạp chí ứng dụng nhận tốt. |
| Hồ sơ NCS | 5 | Chuỗi tự nhiên: detector → báo cáo VI → hỏi đáp/chatbot RAG → đánh giá lâm sàng; nối với hướng chatbot + ontology. |
| **Tổng** | **22/25** | |

**Rủi ro:** mảng chạy nhanh, có thể bị bài khác (kể cả tiếng Việt) đi trước trong 6 tháng; DENTEX là NC-SA nên demo chỉ phi thương mại; thiếu nha sĩ thẩm định thì bài yếu; DENTEX chỉ 4 chẩn đoán nên báo cáo hẹp.

---

## Đề tài 2: Phát hiện răng bất thường ít nhãn trên DENTEX bằng nhãn giả từ mô hình nền

**Câu hỏi nghiên cứu.** Tận dụng nhãn từng phần (chỉ góc phần tư, chỉ đánh số) và 1.571 ảnh không nhãn của DENTEX, kết hợp nhãn giả từ mô hình nền (SAM/open-vocabulary detector), có đạt độ chính xác chẩn đoán gần mức có đủ nhãn với ít hơn 25% ảnh có chẩn đoán không?

**Khoảng trống (bài đã mở):**
1. Hamamci I.E. et al., 2023/2025, *DENTEX: Dental Enumeration and Tooth Pathosis Detection Benchmark for Panoramic X-ray*, arXiv. https://arxiv.org/abs/2305.19112 · DOI 10.48550/arXiv.2305.19112. Tổng kết challenge: thắng nhờ pipeline dẫn bởi phân đoạn, Transformer, khuếch tán. **Chưa làm:** benchmark đánh giá trên tập đủ nhãn; không có giao thức chuẩn cho "bao nhiêu nhãn là đủ".
2. Hamamci I.E. et al., 2023, *Diffusion-Based Hierarchical Multi-label Object Detection to Analyze Panoramic Dental X-Rays*, MICCAI 2023, LNCS. DOI 10.1007/978-3-031-43987-2_38 (đã tra Crossref). Baseline chính thức của DENTEX dùng nhãn phân cấp. **Chưa làm:** chưa dùng ảnh không nhãn; mô hình khuếch tán nặng.
3. Wang Y. et al., 2025, *MICCAI STS 2024 Challenge: Semi-Supervised Instance-Level Tooth Segmentation in Panoramic X-ray and CBCT Images*, arXiv. https://arxiv.org/abs/2511.22911. Bán giám sát + SAM tăng IA >44 điểm so với nnU-Net chỉ dùng nhãn. **Chưa làm:** chỉ phân đoạn răng, **không chẩn đoán bệnh lý**.
4. Silva B. et al., 2024, *Semi-supervised classification of dental conditions in panoramic radiographs using large language model and instance segmentation*, arXiv. https://arxiv.org/abs/2406.17915. LLM gán nhãn từ báo cáo, MAE pre-train, 13 tình trạng. **Chưa làm:** dữ liệu 8.795 ảnh là dữ liệu thực tế riêng (không thấy link công khai trong abstract — chưa kiểm chứng); phân loại mức ảnh/răng, không phát hiện kèm vị trí trên benchmark công khai.

**Dataset công khai:**
| Tên | Link | Giấy phép / truy cập | Kích thước |
|---|---|---|---|
| DENTEX | (như trên) | CC BY-NC-SA 4.0 | 11,8 GB, như trên |
| STS 2024 (2D OPG + 3D CBCT) | https://github.com/ricoleehduu/STS-Challenge-2024 (Google Drive / Baidu / Zenodo 10.5281/zenodo.17712688) | README ghi "công khai cho mục đích nghiên cứu"; giấy phép cụ thể chưa kiểm chứng (Zenodo chặn truy cập tự động) | 2.380 ảnh OPG + 330 CBCT (theo abstract) |

**Baseline 1-2 tháng:** YOLO/RT-DETR có giám sát với 10/25/50/100% ảnh đủ nhãn (đường cong nhãn); thêm Mean-Teacher/nhãn giả trên ảnh không nhãn; thêm bước tinh chỉnh khung bằng SAM. Chạy được trên GPU 12-16 GB với ảnh resize 1024. Báo cáo mAP theo giao thức DENTEX, 3 seed.

**Ứng dụng/demo:** công cụ sàng lọc nhanh cho nha sĩ và **cho chính việc gán nhãn**: phòng khám Việt Nam có ảnh mới thì chỉ cần gán ít nhãn để tinh chỉnh mô hình. Cũng là "công cụ" cho Đề tài 1.

**Nơi công bố (OpenAlex; Scopus cần tra lại):**
- Computerized Medical Imaging and Graphics (Elsevier, ISSN-L 0730-4862) — https://www.journals.elsevier.com/computerized-medical-imaging-and-graphics
- Diagnostics (MDPI, ISSN-L 2075-4418) — http://www.mdpi.com/journal/diagnostics
- BMC Oral Health (BioMed Central, ISSN-L 1472-6831) — https://bmcoralhealth.biomedcentral.com/

**Điểm:**
| Tiêu chí | Điểm | Lý do |
|---|---|---|
| Tính mới | 3 | Bán giám sát cho chẩn đoán ít hơn phân đoạn, nhưng ý tưởng kỹ thuật đã quen. |
| Ứng dụng | 3 | Có ích (giảm công gán nhãn) nhưng demo ít ấn tượng nếu đứng riêng. |
| Khả thi một người | 5 | Dataset sẵn, tải tự do, baseline chuẩn, chạy GPU vừa. |
| Công bố | 4 | Kết quả định lượng rõ trên benchmark công khai, dễ ra tạp chí Q2-Q3. |
| Hồ sơ NCS | 4 | Tốt làm bài 1 (nền kỹ thuật) cho chuỗi dẫn sang Đề tài 1. |
| **Tổng** | **19/25** | |

**Rủi ro:** cải thiện nhỏ so với baseline mạnh thì khó bán; mảng phát hiện DENTEX đã đông, cần so sánh đủ với các đội top challenge; giấy phép NC-SA.

---

## Đề tài 3: Landmark cephalometric bền vững giữa các máy chụp + tự động tính chỉ số chỉnh nha

**Câu hỏi nghiên cứu.** Mô hình phát hiện 29 landmark huấn luyện trên một số máy chụp giảm sai số bao nhiêu khi gặp máy mới, và các kỹ thuật thích nghi miền không cần nhãn (augmentation theo thiết bị, test-time adaptation) bù được bao nhiêu? Sai số landmark ảnh hưởng thế nào tới các góc chỉnh nha (SNA, SNB, ANB)?

**Khoảng trống (bài đã mở):**
1. Khalid M.A. et al., 2023/2025, *'Aariz: A Benchmark Dataset for Automatic Cephalometric Landmark Detection and CVM Stage Classification*, arXiv https://arxiv.org/abs/2302.07797; bản tạp chí *Scientific Data* 2025, DOI 10.1038/s41597-025-05542-3 (Crossref). 1.000 ảnh từ 7 thiết bị, 29 landmark, nhãn CVM. **Chưa làm (theo abstract/README):** chia train/val/test phân tầng theo thiết bị, tức là **chưa đánh giá kiểu để-một-máy-ra-ngoài** (leave-one-device-out).
2. Wang C.-W. et al., 2016, *A benchmark for comparison of dental radiography analysis algorithms*, Medical Image Analysis, DOI 10.1016/j.media.2016.02.004 (chỉ tra Crossref, **chưa đọc abstract** — không dùng để chấm). Benchmark ISBI kinh điển; dùng làm tập ngoài để kiểm tra chéo dataset nếu tải được (link tải chưa kiểm chứng).

**Dataset công khai:**
| Tên | Link | Giấy phép / truy cập | Kích thước |
|---|---|---|---|
| Aariz | https://doi.org/10.6084/m9.figshare.27986417.v1 · code https://github.com/manwaarkhd/aariz | CC BY 4.0 (Figshare), tải tự do | Aariz.zip ~2,0 GB; 1.000 ảnh, 29 landmark, CVM |

**Baseline 1-2 tháng:** heatmap regression (HRNet-W32 hoặc U-Net) với dataloader có sẵn trong repo Aariz; giao thức leave-one-device-out; đo MRE, SDR@2/2,5/3/4 mm; sau đó thêm augmentation mô phỏng thiết bị và TTA đơn giản. GPU 8-12 GB đủ.

**Ứng dụng/demo:** bác sĩ chỉnh nha tải phim sọ nghiêng, nhận landmark + bảng chỉ số Steiner/Downs tự động, kéo chỉnh điểm sai, xuất PDF tiếng Việt. Trực tiếp giảm thời gian đo tay.

**Nơi công bố (OpenAlex; Scopus cần tra lại):**
- Journal of Dentistry (Elsevier, ISSN-L 0300-5712) — https://www.journals.elsevier.com/journal-of-dentistry
- Dentomaxillofacial Radiology (như trên)
- IEEE Access (như trên)

**Điểm:**
| Tiêu chí | Điểm | Lý do |
|---|---|---|
| Tính mới | 3 | Tổng quát hoá giữa máy chụp trên Aariz còn ít bài (chưa rà đủ — tra arXiv bị giới hạn); bài toán landmark đã lâu đời. |
| Ứng dụng | 4 | Đo cephalometric là việc lặp lại hằng ngày của chỉnh nha, demo dễ dùng. |
| Khả thi một người | 5 | Dataset nhỏ, CC BY 4.0, có code đọc dữ liệu, GPU nhỏ đủ. |
| Công bố | 3 | Dễ ra tạp chí ứng dụng; khó lên venue mạnh nếu chỉ cải thiện nhỏ. |
| Hồ sơ NCS | 3 | Tách khỏi mạch VLM/báo cáo, khó nối thành chuỗi 3-4 bài với hướng chatbot. |
| **Tổng** | **18/25** | |

**Rủi ro:** có thể đã có bài làm leave-one-device-out trên Aariz (chưa rà hết); MRE tính theo mm cần độ phân giải pixel từng máy — phải kiểm tra file metadata; khác biệt dân số (Pakistan) so với người Việt.

---

## Tổng hợp

| # | Đề tài | Mới | Ứng dụng | Khả thi | Công bố | NCS | Tổng |
|---|---|---|---|---|---|---|---|
| 1 | Báo cáo panoramic tiếng Việt, căn cứ mức răng, VLM nhỏ | 4 | 5 | 4 | 4 | 5 | **22** |
| 2 | Phát hiện răng bất thường ít nhãn trên DENTEX | 3 | 3 | 5 | 4 | 4 | **19** |
| 3 | Landmark cephalometric bền vững giữa máy chụp | 3 | 4 | 5 | 3 | 3 | **18** |

Khuyến nghị: gộp 2 → 1 thành một chuỗi (bài 1: detector ít nhãn; bài 2: báo cáo tiếng Việt có căn cứ; bài 3: hỏi đáp/RAG cho bệnh nhân). Đề tài 3 là phương án dự phòng an toàn, nhanh ra bài.

## Đã cân nhắc nhưng loại

- **Phân đoạn răng CBCT/panoramic thuần tuý:** bão hoà sau 2 challenge STS (arXiv:2511.22911), CBCT 3D lại tốn GPU, khó có điểm mới cho một người.
- **Ảnh chụp trong miệng bằng điện thoại (OMNI-Dent, arXiv:2602.07041; dataset đa phương thức arXiv:2511.04948):** hấp dẫn cho sàng lọc cộng đồng nhưng dữ liệu công khai còn ít/gated và chưa kiểm chứng điều kiện tải; để sau.
- **Ảnh cận chóp (PRAD-10K, arXiv:2504.07760; PeriaTrace, arXiv:2611.23012):** PRAD ghi "sẽ công khai", chưa thấy link tải; PeriaTrace dùng dữ liệu nội bộ — không đáp ứng ưu tiên dữ liệu công khai ở thời điểm này.

## Việc cần chủ nhóm làm trước khi chốt

1. Tra Scopus/SJR cho các tạp chí trên (tự động bị chặn).
2. Tra Google Scholar "nha khoa" + "tiếng Việt" + "AI" để xác nhận khoảng trống Đề tài 1.
3. Tìm 1 nha sĩ/bác sĩ chẩn đoán hình ảnh cộng tác thẩm định (cần cho Đề tài 1, nên có cho 2-3).
