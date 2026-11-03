# Đặc tả <UCxx>: <tên use case>

> Trạng thái: <Giả định / Đã xác nhận> · Giai đoạn: <GĐ1a/GĐ1b/GĐ2/GĐ3> · Độ phức tạp: <Thấp/Trung bình/Cao>

| Phiên bản | Ngày | Người sửa | Nội dung thay đổi |
|---|---|---|---|
| 0.1 | <dd/mm/yyyy> | <...> | Tạo mới |

## 1. Mục tiêu và giá trị
<1–3 câu: ai dùng, để quyết định/làm việc gì>

## 2. Tác nhân và phân quyền

| Tác nhân | Vai trò | Phạm vi địa bàn | Được xem | Bị che |
|---|---|---|---|---|
| Cán bộ xã | <...> | Xã được giao | <...> | <số định danh: hiện 4 số cuối> |

## 3. Điều kiện
- Tiền điều kiện: <...>
- Hậu điều kiện (thành công): <...>
- Phụ thuộc: <T06, T07, ...>

## 4. Luồng chính
1. <Tác nhân> <hành động>.
2. Hệ thống <xử lý>, áp dụng BR-xx.
3. ...

## 5. Luồng thay thế
- 2a. <điều kiện>: <xử lý>.

## 6. Luồng ngoại lệ
- 3e. <lỗi/thiếu dữ liệu>: <thông báo, ghi log, xử lý>.

## 7. Quy tắc nghiệp vụ áp dụng

| Mã BR | Tóm tắt | Căn cứ |
|---|---|---|
| BR-xx | <...> | <Điều.. khoản.. văn bản> |

## 8. Dữ liệu

| Thực thể | Thuộc tính dùng | Nguồn (trong 7 nguồn) | Đọc/Ghi | Ghi chú chất lượng |
|---|---|---|---|---|
| NGƯỜI | số định danh, trạng thái sống/mất | <...> | Đọc | <tỷ lệ có CCCD từ UC01> |

## 9. Màn hình / đầu ra
- Bộ lọc: <...>
- Chỉ tiêu và cách tính: <...>
- Trình bày: <bảng/biểu đồ/drill-down/xuất Excel>

## 10. Yêu cầu phi chức năng
- Hiệu năng: <...> · Nhật ký: <...> · Lưu trữ: <...>

## 11. Tiêu chí nghiệm thu

| Mã | Cho (dữ liệu giả) | Khi | Thì | BR/luồng kiểm |
|---|---|---|---|---|
| TC-UCxx-01 | <...> | <...> | <...> | BR-xx |

## 12. Giả định và câu hỏi mở

| # | Nội dung | Loại (giả định/câu hỏi) | Hỏi ai | Đề xuất mã Q mới |
|---|---|---|---|---|
| 1 | <...> | <...> | <...> | <...> |
