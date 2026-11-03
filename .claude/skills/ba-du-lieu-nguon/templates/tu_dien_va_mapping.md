# Từ điển dữ liệu và mapping: <tên nguồn>

## 1. Thông tin nguồn

| Mục | Giá trị |
|---|---|
| Cơ quan chủ quản | <Bộ ...> |
| Phương thức | <API REST / DB link / file> · xác thực: <...> · giới hạn gọi: <...> |
| Đồng bộ | <full / incremental theo trường ...> · tần suất: <...> |
| Đơn vị dữ liệu | <cá nhân / hộ / hồ sơ hưởng> |
| Có dữ liệu chi trả | <có / không / chưa rõ> |
| Có quan hệ người–người | <thân nhân / người chăm sóc / người nhận / không / chưa rõ> |
| Mã địa bàn | <trước / sau sắp xếp 2025 / chưa rõ> |

## 2. Từ điển trường

| Trường nguồn | Kiểu | Mô tả | Bắt buộc | Tỷ lệ trống | Mẫu định dạng (đã che) | Danh mục |
|---|---|---|---|---|---|---|
| <ten_truong> | <chuỗi/số/ngày> | <...> | <C/K> | <x%> | <9999…> | <mã danh mục nếu có> |

## 3. Mapping sang mô hình lõi

| Trường nguồn | Thực thể | Thuộc tính | Phép biến đổi | Ghi chú |
|---|---|---|---|---|
| <so_dinh_danh> | NGƯỜI | Số định danh | chuẩn hóa 12 số | khóa ghép T06 |
| <...> | — | không dùng | — | <lý do> |

## 4. Chuyển mã danh mục (T04)

| Danh mục | Mã nguồn | Ý nghĩa nguồn | Mã dùng chung | Ghi chú |
|---|---|---|---|---|
| Mức độ khuyết tật | <...> | <...> | <DB_NANG/NANG/NHE> | |

## 5. Chất lượng "đúng–đủ–sạch–sống"

| Tiêu chí | Chỉ số | Kết quả | Ngưỡng chấp nhận | Đạt |
|---|---|---|---|---|
| Đúng | Tỷ lệ CCCD hợp lệ | <x%> | <chưa chốt> | <...> |
| Đủ | Tỷ lệ trống trường bắt buộc | <...> | | |
| Sạch | Số dòng trùng khóa | <...> | | |
| Sống | Ngày cập nhật gần nhất | <...> | | |
| Quan hệ | Tỷ lệ hồ sơ có người nhận/người chăm sóc/hộ | <...> | | |

## 6. Khả dụng theo UC

| UC | Trường cần | Tình trạng | Ảnh hưởng |
|---|---|---|---|
| UC07 | trạng thái sống/mất, kỳ chi | <Đủ / Thiếu ... / Không có> | <...> |

## 7. Câu hỏi mở cho đơn vị quản lý nguồn
- <...>
