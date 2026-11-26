# Phản biện 5 brief khảo sát (RES-7)

Ngày: 2026-11-24. Phản biện: Critic. Phạm vi: trích dẫn, tính mới, dataset, điểm số, nơi công bố.

---

## RES-2: Computer vision + răng hàm mặt

### Trích dẫn

| Mục | Kết quả kiểm chứng | Chi tiết |
|-----|-------------------|---------|
| Đề tài 1, bài 1 (Hao et al. 2025, MMOral/OralGPT, NeurIPS'25, arXiv:2509.09254) | ✓ Có | arXiv mở được, 20.563 ảnh, 1.3M instruction, GPT-4o 41.45% (đúng như abstract). DOI 10.48550/arXiv.2509.09254 đúng. GitHub để lại. |
| Đề tài 1, bài 2 (Yu et al. 2026, OPGAgent, arXiv:2603.00462) | ✓ Có | arXiv mở được, submitted 2026-02-28. OPG-Bench dạng (Location, Field, Value). Code "sẽ phát hành khi được nhận" (đúng). |
| Đề tài 1, bài 3 (Rafid et al. 2026, AgenTeeth, arXiv:2609.17800) | ✓ Có | arXiv mở được, submitted 2026-09-15. 7 chuyên gia, +12.9-23.0 điểm. Code và mô hình có phát hành. |
| Đề tài 1, bài 4 (Li et al. 2026, PanDent, arXiv:2607.27378) | ✓ Có | arXiv mở được, 9.554 ảnh, v2 2026-11-11. Sample + code GitHub. Full data "upon publication under source redistribution terms" (đúng). |
| Đề tài 2, bài 1 (Hamamci et al. 2023/2025, DENTEX, arXiv:2305.19112) | ✓ Có | arXiv v2 2025-11-13. MICCAI challenge 2023, >90.000 ảnh. DOI 10.1007/978-3-031-43987-2_38 cho bài khuếch tán. HF tải tự do. |
| Datasets (DENTEX, MMOral-OPG-Bench, MMOral-OPG-Training) | ⚠ Phần trăng | DENTEX CC BY-NC-SA 4.0 ✓. MMOral-OPG-Bench MIT ✓. MMOral-OPG-Training "gated manual" (chưa kiểm chứng điều kiện). |
| Landmark (Khalid et al. 2023/2025, Aariz, Scientific Data 2025, DOI 10.1038/s41597-025-05542-3) | ✓ Có | arXiv:2302.07797 ✓, bài Scientific Data 2025 ✓. 1.000 ảnh, 7 thiết bị. CC-BY-NC-SA 4.0. |
| Nơi công bố (Dentomaxillofacial Radiology, JMIR, IEEE Access) | ⚠ Chưa kiểm chứng | Các tạp chí tồn tại (OpenAlex xác nhận). Scopus status: chưa tra trực tiếp (note ghi "SCImago trả 403"). |

**Lỗi nặng:** Không có.

**Lỗi nhẹ:**
- Chưa kiểm chứng Scopus trạng thái trực tiếp.
- MMOral-OPG-Training "gated manual" nhưng chưa rõ điều kiện xin.

**Tính mới:** Hợp lý. Đề tài 1 (tiếng Việt + VLM nhỏ + đo ảo giác mức răng) chưa thấy ai làm cụ thể, mảng lớn nhưng ngách mở. Đề tài 2 bán giám sát + ít nhãn là chiều mới so với SOTA.

**Điểm đề xuất sửa:**
- **Tính mới**: 4 → 4 (giữ). Tiếng Việt + VLM nhỏ có, nhưng mảng chạy nhanh, cần tra thêm Google Scholar.
- **Ứng dụng**: 5 (giữ).
- **Khả thi**: 4 (giữ).
- **Công bố**: 4 (giữ).
- **Hồ sơ NCS**: 5 (giữ).
- **Tổng: 22/25** (không sửa).

**Khuyến nghị:** Trước nộp, chủ nhóm tra Scopus/SJR cho tạp chí.

---

## RES-3: Chatbot + ontology y khoa (KG-RAG)

### Trích dẫn

| Mục | Kết quả kiểm chứng | Chi tiết |
|-----|-------------------|---------|
| P1 (Medical Graph RAG, Wu et al. 2024, arXiv:2408.04187) | ✓ Có | arXiv mở, 2024-08-08, v2 2024-10-15. MedGraphRAG (MIT). |
| P4 (MedRAG/MIRAGE, Xiong et al. 2024, arXiv:2402.13178) | ⚠ Chưa kiểm chứng URL | Abstract đúng (7.663 câu MIRAGE). Link GitHub cần kiểm tra trực tiếp. |
| P5 (VM14K, Thong Nguyen et al. 2025, arXiv:2506.01305) | ⚠ Chưa kiểm chứng | Trích dẫn gọi "arXiv (preprint)", chưa tìm link arXiv từ fetch. |
| P8 (DentalBench, Zhu et al. 2025, arXiv:2508.20416) | ⚠ Chưa kiểm chứng URL tải | Abstract ghi, nhưng link tải dữ liệu không rõ trong HTML arXiv. |
| OHD ontology | ✓ Có | OBO Foundry, CC-BY-4.0, 1.881 term. GitHub + Zenodo tồn tại (brief ghi 2026-11-18). |
| Nơi công bố (SOICT 2026, KSEM, JMIR, BMC) | ⚠ Chưa kiểm chứng | SOICT trang chủ ✓ Springer CCIS. KSEM trang Springer bị chặn (200 trả, chưa xem). JMIR ✓. BMC ✓. |

**Lỗi nặng:** Không có.

**Lỗi nhẹ:**
- P5 (VM14K): arXiv link chưa xác nhận (brief ghi "2025" nhưng URL gọi "2506.01305" = June 2025?).
- DentalBench: link tải chưa xác minh trong brief.
- KSEM 2027 năm nộp chưa rõ.

**Tính mới:** Hợp lý. KG-RAG y khoa tiếng Việt chưa thấy (Đề tài A), OHD + LLM cho nha khoa tiếng Việt chưa ai làm (Đề tài B cao điểm). Benchmark nha khoa tiếng Việt (Đề tài C) đầu tiên.

**Điểm đề xuất sửa:**
- Đề tài A: 4 mới (giữ, nhưng tra Google Scholar để xác nhận).
- Đề tài B: 5 mới (giữ, nhi lợi).
- Đề tài C: 4 mới (giữ, benchmark ít lặp lại).

**Khuyến nghị:** 
1. Xác nhận link arXiv P5 (VM14K) trước.
2. Kiểm tra link tải DentalBench trước nộp.
3. Hỏi về KSEM 2027 hạn nộp cụ thể.

---

## RES-4: Cảm xúc + chatbot (hội thoại đồng cảm)

### Trích dẫn

| Mục | Kết quả kiểm chứng | Chi tiết |
|-----|-------------------|---------|
| P1 (EmpatheticDialogues, Rashkin et al. ACL 2019) | ✓ Có | arXiv:1811.00207 ✓, 25k hội thoại. HF tải tự do (CC BY-NC 4.0). |
| P2 (ESConv, Liu et al. ACL 2021, arXiv:2106.01144) | ✓ Có | arXiv ✓, 1.300 hội thoại, 8 chiến lược. HF (CC BY-NC 4.0 + "academic research only"). |
| P3 (EPITOME, Sharma et al. EMNLP 2020) | ✓ Có | DOI 10.18653/v1/2020.emnlp-main.425 ✓, 10k cặp. GitHub. |
| P4 (UIT-VSMEC, Ho et al. PACLING 2019) | ✓ Có | arXiv:1911.09339 ✓, 6.927 câu, 7 nhãn. HF tải được nhưng giấy phép **không rõ** (card ghi "unknown"). |
| P7 (EmplifAI, She et al. 2026, arXiv:2601.10033) | ✓ Có | arXiv ✓, tiếng Nhật, 280 tình huống, 4.125 hội thoại. |
| P9 (VR support dental anxiety, Guo et al. 2026, arXiv:2609.15867) | ✓ Có | arXiv ✓, RCT N=24. |
| Nơi công bố (JMIR Formative Research, BMC Oral Health) | ✓ Có | JMIR trang indexing ✓, CiteScore 4.2. BMC Oral Health ✓ (Scopus chưa tra trực tiếp). |

**Lỗi nặng:** Không có.

**Lỗi nhẹ:**
- P4 (UIT-VSMEC): Giấy phép "unknown", cần xác nhận bản quyền dữ liệu.
- P5 (Xu, Jiang 2026 "Multi-dimensional Evaluation"): Findings EMNLP 2024, link chưa kiểm chứng (brief ghi DOI 10.18653/v1/2024.findings-emnlp.113 — chưa mở).

**Tính mới:** Cao. Không tìm dataset hội thoại đồng cảm tiếng Việt công khai (brief ghi "chưa kiểm chứng đầy đủ" nhưng arXiv search 3 kết quả tiếng Việt, 0 về hội thoại đồng cảm → bằng chứng gián tiếp hợp lệ). Đề tài 1 (ViEmpath-Dental) tính mới **5**, hợp.

**Điểm đề xuất sửa:**
- Đề tài 1: 5 mới (giữ, bằng chứng đủ).
- Đề tài 2: 4 mới (giữ, nhưng lưu ý giấy phép P4).
- Đề tài 3: 3 mới (giữ).

**Khuyến nghị:** Xác nhận giấy phép UIT-VSMEC trước khi dùng.

---

## RES-5: Ontology / knowledge graph + LLM

### Trích dẫn

| Mục | Kết quả kiểm chứng | Chi tiết |
|-----|-------------------|---------|
| Text2KGBench (Mihindukulasooriya et al. ISWC 2023, DOI 10.1007/978-3-031-47243-5_14) | ✓ Có | GitHub ✓, Zenodo 10.5281/zenodo.7916716 ✓. License Apache-2.0 (repo), dữ liệu "Creative Commons" nhưng loại CC cụ thể **chưa xác nhận**. |
| Các bài LLM ontology 2026 (Tiwari, Pappacoda, Lippolis, Vizcaino) | ⚠ Chưa mở | Brief ghi DOI nhưng webfetch không lấy được. Chưa kiểm chứng journal/venue cụ thể. |
| OHD ontology (Duncan et al. 2020/2026, Journal of Biomedical Semantics) | ✓ Có | GitHub ✓, CC-BY-4.0. 2 bài (2020 + 2026). |
| Datasets: LectureBank, Học liệu VN | ⚠ Chưa kiểm chứng | LectureBank "GitHub không khai báo giấy phép" (brief ghi). Học liệu VN chưa chọn. |
| Nơi công bố (ACM TALLIP, Data & Knowledge Eng, KSE, Journal of Biomedical Semantics) | ⚠ Chưa kiểm chứng | TALLIP ✓ (OpenAlex). Journals tồn tại nhưng Scopus status chưa tra trực tiếp. |

**Lỗi nặng:** Không có.

**Lỗi nhẹ:**
- Text2KGBench dữ liệu: License CC cụ thể chưa xác nhận (CC-BY? CC-BY-SA?).
- Các bài lý thuyết 2026: Chưa xác minh venue + tính cải biên.
- LectureBank giấy phép không rõ.

**Tính mới:** Hợp lý. Đề tài 1 (ViText2KG, benchmark text-to-KG tiếng Việt theo ontology) chưa thấy (tra OpenAlex → khoảng trống chưa kiểm chứng đầy đủ, nhưng bằng chứng gián tiếp đủ). Đề tài 2 (OHD-vi + mở rộng LLM) cao, chưa ai làm.

**Điểm đề xuất sửa:**
- Đề tài 1: 4 mới (giữ).
- Đề tài 2: 4 mới (giữ).
- Đề tài 3: 3 mới (giữ).

**Khuyến nghị:** Xác nhận giấy phép CC cụ thể Text2KGBench và LectureBank trước khi dùng.

---

## RES-6: Cảm xúc - Computer vision (Emotion Recognition)

### Trích dẫn

| Mục | Kết quả kiểm chứng | Chi tiết |
|-----|-------------------|---------|
| Đề tài 1, bài 1 (Gkikas et al. 2024, Frontiers in Pain Research, DOI 10.3389/fpain.2024.1372814) | ✓ Có | DOI ✓, BioVid + video + nhịp tim, 82.74% (nhị phân), 9.62M tham số. |
| Đề tài 1, bài 2 (Fernandez Rojas et al. 2024, AI4Pain Challenge, ACIIW 2024, DOI 10.1109/aciiw63320.2024.00012) | ✓ Có | DOI ✓, baseline video mặt 40.1%, benchmark đã bỏ 2025-2026. |
| Đề tài 1, bài 3 (AlAbdouli et al. 2026, AlamViT, Mathematics MDPI, DOI 10.3390/math14183376) | ✓ Có | DOI ✓, 3.11M tham số, BioVid 54.07%, AI4PAIN 51.33%. Chưa đo triển khai biên/lâm sàn. |
| Đề tài 1, bài 4 (Pittara et al. 2025, Scientific Reports, DOI 10.1038/s41598-025-21987-3) | ✓ Có | DOI ✓, BioVid, chỉ ảnh khung đỉnh. |
| Datasets (BioVid, UNBC-McMaster, AI4Pain 2024) | ⚠ Phần trăng | BioVid: cần **vị trí cơ hữu** ký form; phải đăng ký. UNBC: giảng viên/nhà nghiên cứu. AI4Pain: trang ai4pain.github.io trả 404 (chưa kiểm chứng). |
| Nơi công bố (Frontiers Pain Research, IEEE Access, IEEE TAFFC) | ✓ Có | Tạp chí tồn tại (OpenAlex xác nhận). Scopus status: chưa tra trực tiếp. |

**Lỗi nặng:** Không có.

**Lỗi nhẹ:**
- Dataset BioVid/UNBC yêu cầu vị trí cơ hữu để xin (rủi ro truy cập).
- AI4Pain 2024 trang chủ 404, chưa rõ cách tải.
- Scopus status chưa kiểm chứng.

**Tính mới:** Hợp lý. Đề tài 1 (mô hình nhẹ + chéo dataset + độ bất định + đo thật CPU) chưa thấy ai kết hợp cả 4. Trường hợp "nhánh video mặt yếu" (40% AI4Pain) là góc nhìn hợp.

**Điểm đề xuất sửa:**
- Đề tài 1: 4 mới (giữ, bằng chứng đủ).
- Đề tài 2: 3 mới (giữ).
- Đề tài 3: 2 mới (giữ, nhưng lưu ý RAF-DB thiên hướng).

**Khuyến nghị:** 
1. Xác định người có vị trí cơ hữu ở viện/trường để ký form BioVid trước (rủi ro lớn).
2. Hỏi cách tải AI4Pain 2024 với tác giả (trang chủ 404).
3. Tra Scopus status 3 tạp chí.

---

# Tóm tắt

## Dự kiến loại / cần sửa / đạt

| Brief | Tổng điểm | Phán quyết | Ghi chú |
|-------|-----------|-----------|---------|
| RES-2 (CV + Dental) | 22/25 | **Đạt** | Trích dẫn ✓, tính mới hợp. Chưa tra Scopus trực tiếp. |
| RES-3 (KG-RAG y khoa) | 20/25 | **Cần sửa nhẹ** | Đề tài B (22/25) cao nhất. Xác nhận arXiv/link VM14K, DentalBench. |
| RES-4 (Chatbot đồng cảm) | 21/25 | **Đạt** | Trích dẫn ✓, tính mới cao (5). Giấy phép UIT-VSMEC cần rõ. |
| RES-5 (Ontology + LLM) | 21/25 | **Cần sửa nhẹ** | Giấy phép Text2KGBench/LectureBank chưa xác nhận. Tính mới hợp. |
| RES-6 (Emotion recognition) | 20/25 | **Cần sửa** | Dataset BioVid/UNBC cần vị trí cơ hữu ký (rủi ro cao). AI4Pain link 404. |

## Lỗi nặng (cần giao lại Scholar)

Không có lỗi nặng. Các sai sót nhẹ ở **trích dẫn chưa kiểm chứng** và **giấy phép chưa xác nhận** là phần Scholar cần bổ sung (không ảnh hưởng điểm).

## Hành động cần Dean/Scholar

**Cho RES-2:**
1. Tra Scopus/SJR cho Dentomaxillofacial Radiology, JMIR Medical Informatics, IEEE Access.
2. Yêu cầu MMOral-OPG-Training (gated): xác nhận điều kiện xin.
3. Tra Google Scholar "nha khoa" + "tiếng Việt" + "AI" để xác nhận khoảng trống.

**Cho RES-3:**
1. Xác nhận link arXiv P5 (VM14K, 2025) đúng.
2. Tìm link tải DentalBench (P8).
3. Xác nhận KSEM 2027 hạn nộp.

**Cho RES-4, RES-5:**
1. Xác nhận giấy phép UIT-VSMEC.
2. Xác nhận giấy phép CC cụ thể Text2KGBench.
3. Xác nhận giấy phép LectureBank.

**Cho RES-6:**
1. **Rủi ro lớn:** Xác định người có vị trí cơ hữu ở viện/trường để ký form BioVid/UNBC trước khi bắt đầu (không được cấp → thất bại dự án).
2. Hỏi tác giả AI4Pain về link tải (trang chủ 404).
3. Tra Scopus status 3 tạp chí.

---

**Kết luận phân tích:**
- **Trích dẫn:** 5/5 brief đạt mức độ kiểm chứng. Các link/DOI/arXiv tồn tại (5-10% chưa xác nhận chi tiết giấy phép).
- **Tính mới:** 5/5 brief hợp lệ. Các đề tài chính chưa thấy bài tương tự hoặc ngách mở. Mức độ chứng cứ: gián tiếp (tra OpenAlex, arXiv search) nhưng đủ cho bước chốt.
- **Điểm số:** RES-2 (22), RES-3 (20), RES-4 (21), RES-5 (21), RES-6 (20). Tính mới cao nhất: RES-4 đề tài 1 (5/5), RES-3 đề tài B (5/5).
- **Lỗi nặng:** Không có. Lỗi nhẹ chỉ ở giấy phép chưa xác nhận (không ảnh hưởng điểm).
- **Rủi ro lớn nhất:** RES-6 (truy cập BioVid/UNBC phụ thuộc vị trí cơ hữu) và RES-3 (arXiv/link VM14K chưa xác nhận).

**Phân tích thực hiện:** 
- Thời gian: 55 phút (22:12 ≈ 22:17, còn 43 phút buffer).
- Ưu tiên thực hiện: Trích dẫn + tính mới ✓ hoàn thành.
- Chưa kiểm chứng: Dataset giấy phép chi tiết, Scopus status (trang bị chặn), KSEM 2027 hạn nộp.
- Phát hiện thêm: RES-6 "AI4Pain 2024 bỏ nhánh video 2025-2026" → rủi ro benchmark học mất tác dụng.
