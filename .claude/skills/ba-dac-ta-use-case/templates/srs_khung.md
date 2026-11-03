# Đặc tả yêu cầu phần mềm (SRS): <phạm vi>

Dùng khung này khi bên giao việc chưa đưa mẫu bắt buộc (Q19). Có mẫu bắt buộc thì ánh xạ các mục dưới đây vào mẫu đó.

1. Giới thiệu: mục đích, phạm vi (giai đoạn, danh sách T/UC), thuật ngữ, tài liệu tham chiếu (TKCS/TKKT, căn cứ pháp lý).
2. Tổng quan: bối cảnh 7 nguồn, tác nhân, ràng buộc (Angular 19, Spring Boot, Oracle, pattern source có sẵn), giả định và phụ thuộc.
3. Mô hình dữ liệu lõi: thực thể, quan hệ, nguyên lý "đáng hưởng" so với "đang hưởng".
4. Yêu cầu chức năng: mỗi UC một mục con, nhúng hoặc dẫn tới đặc tả UC đầy đủ.
5. Danh mục quy tắc nghiệp vụ: bảng BR-xx kèm căn cứ và hiệu lực.
6. Yêu cầu tích hợp: theo từng nguồn (giao thức, xác thực, lịch đồng bộ, full/incremental, xử lý lỗi).
7. Yêu cầu phi chức năng: hiệu năng, bảo mật và dữ liệu cá nhân (Luật 91/2025, NĐ 356/2025), nhật ký, lưu trữ, khả dụng.
8. Tiêu chí nghiệm thu: tổng hợp TC theo UC, đơn vị nghiệm thu (Q18).
9. Ma trận truy vết: YC ↔ UC ↔ BR ↔ TC.
10. Phụ lục: câu hỏi mở, lịch sử thay đổi, CR đã duyệt.
