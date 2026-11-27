# Deep Ensemble (unread / placeholder)

**Phiên bản**: 2026-11-27 - ghi chú tạm (chưa mở bài gốc)  
**Link**: Liang et al. (1511.04636 hoặc 1512.02479?) — cần xác nhận  
**Liên quan P2**: baseline "uncertainty via ensemble variance" cho selective classification  
**Trích từ**: Geifman & El-Yaniv 1705.08500 (nêu ensemble techniques)

## Trạng thái kiểm chứng

- ❌ **Chưa đọc bài riêng** (chỉ nhắc qua trong 1705.08500 + brief B)
- ⚠️ **Chưa xác nhận DOI/arXiv** chính xác

## Ghi chú tạm

Deep ensemble = kỹ thuật variance-based uncertainty:
- Huấn luyện N mô hình độc lập trên dữ liệu gốc
- Lấy variance qua N predictions → signal không chắc chắn (epistemic uncertainty)
- Baseline cho MC Dropout (1705.08500) và SelectiveNet (1901.09192)

**Nếu P2 chạy Deep Ensemble**:
1. Chi phí: N×(train time + inference time) → làm trước conformal/RAPS nếu budget chặt
2. Báo: mean + var prediction → rank by var (tương tự MC dropout)
3. So với threshold-naive (MSP/energy) + AURC/risk@coverage

## Tiếp theo

- [ ] Mở arXiv (Liang 1512 hoặc tương đương) để xác nhận công thức + DOI
- [ ] Thêm vào brief nếu P2 có thời gian (ước: 2-3 ngày GPU nếu N=5)
- [ ] Ghi kết quả: AUROC + E-AURC + risk@90% coverage

---

**Người viết**: Scholar (ghi lại từ RES-58 Critic feedback)  
**Cập nhật**: 2026-11-27, khi tách từ RES-57 (kiểm chứng E-AURC + temperature scaling)  
**Trạng thái**: "chưa kiểm chứng" (theo rule: chưa mở bài → không ghi trong mục "Bài đã đọc" + để nhãn ⚠️ nếu P2 dùng)
