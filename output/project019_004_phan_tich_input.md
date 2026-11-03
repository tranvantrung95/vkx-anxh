# Phân tích thư mục input (project019)

Ngày lập: 26/10/2026. Người lập: BA project019.

Phạm vi: toàn bộ file trong `input/` tại thời điểm 26/10/2026. Tài liệu chỉ đọc nguồn, không sửa file nào trong `input/`.

Trạng thái: mọi task, UC và BR nhắc tới trong tài liệu này vẫn ở trạng thái **Giả định** hoặc **Chờ đối chiếu**. Không dùng tài liệu này như phạm vi đã chốt.

## 1. Danh mục file

| File | Nội dung | Ghi chú |
|---|---|---|
| `Checklist_hop_ky_thuat_module_tich_hop_du_lieu.xlsx` | 7 sheet: Checklist họp, Lộ trình, Task & Usecase, Ứng dụng dữ liệu, UC tham khảo PL III, Mô hình dữ liệu, Căn cứ pháp lý | Nguồn sự thật, chỉ đọc |
| `VKX - VNPT IT - Migrate ASSH [26-10-2026 08_54].zip` | 7 ảnh JPG, tổng khoảng 4,9 MB | Bản nén của thư mục cùng tên |
| Thư mục `VKX - VNPT IT - Migrate ASSH [26-10-2026 08_54]/` | 7 ảnh chụp màn hình điện thoại lúc 9:56 và 9:57, tài liệu tên `2.3_Dự_thảo_Hợp_đồng_người...` | Trùng nội dung với file zip |
| `~$Checklist_hop_ky_thuat_module_tich_hop_du_lieu.xlsx` | File khóa tạm của Excel | Cho biết file Excel đang mở. Đóng file trước khi chạy script đọc hoặc ghi |
| `.DS_Store` | File hệ thống macOS | Bỏ qua |

## 2. Bảy ảnh: Phụ lục III dự thảo hợp đồng

### 2.1. Nhận diện

Tiêu đề trong ảnh: "Phụ lục III: Yêu cầu kỹ thuật của phần mềm", kèm theo hợp đồng năm 2026 giữa Cục Người có công (Bộ Nội vụ) và Liên danh VNPT-VKX. Số hợp đồng và ngày ký còn để trống. Đây là bản **dự thảo**.

Bảy ảnh chụp gối lên nhau, phủ liên tục các mục từ 1 đến 208:

| Ảnh (đuôi tên file) | Mục |
|---|---|
| `...xxloovvteergqanqk8co1` | 1 đến 29 |
| `...xxrcf02vlqmzunwqjjke2` | 23 đến 56 |
| `...xxvbxmhvlfiukqyjsxy03` | 56 đến 85 |
| `...ozlioyoajnrreaca6nym4` | 84 đến 116 |
| `...6jmecbyth9s2fqsqo8gw5` | 111 đến 149 |
| `...jornidefgsx9hpmtan9c6` | 148 đến 175 |
| `...zg94fc5ep2kw3pf39liw7` | 174 đến 208 |

### 2.2. Cấu trúc yêu cầu

| Mục lớn | Tên | Số thứ tự | Số mục |
|---|---|---|---|
| A | Quản trị hệ thống (nhật ký, cấu hình, chữ ký, menu, phân quyền, quy trình động, biểu mẫu động, danh mục) | 1 đến 35 | 35 |
| B | Tích hợp hệ thống | 36 đến 71 | 36 |
| C | Thông tin dữ liệu bị lỗi | 72 đến 74 | 3 |
| D | Tiếp nhận và giải quyết hồ sơ thủ tục hành chính | 75 đến 107 | 33 |
| E | Tra cứu, thống kê, dashboard (I Tra cứu, II Báo cáo thống kê, III Dashboard, V Tra cứu báo cáo động) | 108 đến 197 | 90 |
| G | Hỗ trợ ra quyết định | 198 đến 201 | 4 |
| H | Quản lý chi trả chế độ ưu đãi và quà tri ân | 202 đến 208 | 7 |

### 2.3. Đối chiếu với sheet "UC tham khảo PL III"

Sheet lấy 153 trên 208 mục. 55 mục bị loại có chủ đích vì chúng tạo ra dữ liệu chứ không phân tích dữ liệu:

1. Mục A: 1 đến 24, 31, 34 (26 mục).
2. Mục B: 36, 37 (2 mục).
3. Mục D: 78, 85 đến 101, 104, 107 (20 mục).
4. Mục H: 202 đến 208 (7 mục).

Phép tính 208 trừ 55 bằng 153. Kết quả khớp tổng cột "Số UC tham khảo" ở sheet "Ứng dụng dữ liệu": N0 8, N1 32, N2 17, N3 7, N4 41, N5 8, N6 7, N7 8, N8 5, N9 20. Mô tả các mục kiểm tra ngẫu nhiên (29, 52, 109, 132, 147, 201) khớp với ảnh.

## 3. Excel: tình trạng từng sheet

| Sheet | Tình trạng |
|---|---|
| Checklist họp | 26 câu hỏi trong 6 nhóm. Cả 26 câu ở trạng thái "Chưa hỏi". Cột trả lời và người phụ trách trống |
| Lộ trình | 4 giai đoạn: GĐ1a (15/11/2026, 8 task/UC), GĐ1b (30/11/2026, 9), GĐ2 (9), GĐ3 (4). Tổng 30. Cột "Tổng ngày công" bằng 0 ở mọi dòng |
| Task & Usecase | 11 task nền tảng (T01 đến T11) và 19 UC (UC01 đến UC19). Cả 30 dòng ở trạng thái "Giả định". Cột ước lượng ngày công trống |
| Ứng dụng dữ liệu | 10 nhóm N0 đến N9 kèm trình tự phân tích 5 bước. Cột "Đã đánh giá phù hợp" và "Không đủ dữ liệu" bằng 0 |
| UC tham khảo PL III | 153 mục, cả 153 ở trạng thái "Chưa đánh giá" |
| Mô hình dữ liệu | 8 thực thể khái niệm: NGƯỜI, HỘ, THÀNH VIÊN HỘ, DIỆN ĐỐI TƯỢNG, HỒ SƠ HƯỞNG, QUAN HỆ NGƯỜI-NGƯỜI, CHI TRẢ, QUY TẮC CHÍNH SÁCH. Ví dụ "Bà A", "ông B" là dữ liệu giả |
| Căn cứ pháp lý | 21 văn bản trong 5 nhóm. Tra cứu ngày 22/10/2026 |

## 4. Vấn đề cần làm rõ với bên giao việc

### 4.1. Phạm vi nghiệp vụ lệch giữa Phụ lục III và Excel

Phụ lục III chỉ nói về **người có công** do Cục Người có công quản lý. Excel mở rộng sang trợ giúp xã hội theo NĐ 335/2026/NĐ-CP, hộ nghèo (T08, UC05, UC15), người khuyết tật và trẻ em (UC10, UC13). Các nguồn thuộc Bộ Y tế và Bộ NN&MT trong T04 không xuất hiện trong Phụ lục III.

Tên thư mục ảnh là "Migrate ASSH". Tên này gợi ý việc thật có thể là chuyển đổi hệ thống an sinh xã hội hiện có, không chỉ xây module phân tích.

Câu hỏi đề xuất:

1. Phạm vi giao là người có công hay toàn bộ an sinh xã hội?
2. Việc giao là xây mới module phân tích hay chuyển đổi hệ thống hiện có? Nếu chuyển đổi thì hệ thống nguồn là gì?

### 4.2. "7 nguồn API" đang gộp nguồn và đích

Sheet "UC tham khảo PL III" gán nhãn "Nguồn 1" đến "Nguồn 7" (giả định). Đối chiếu với nội dung các mục trong ảnh:

| Hệ thống | Mục PL III | Chiều dữ liệu theo câu chữ PL III |
|---|---|---|
| HT giải quyết TTHC Bộ Nội vụ | 38, 40 (vào); 42, 44 (ra) | Hai chiều |
| CSDL quốc gia về dân cư | 46, 47 | Vào (xác thực) |
| Trung tâm dữ liệu quốc gia | 48, 49 | Ra (đồng bộ lên) |
| CSDL quốc gia về ASXH | 50, 51 (ra); 52 đến 55 (vào: kết quả đối soát, cảnh báo) | Hai chiều |
| Trung tâm điều hành thông minh IOC | 56, 57 | Ra |
| CSDL Liệt sĩ, mộ liệt sĩ và nghĩa trang liệt sĩ | 58 đến 61 | Chưa rõ ("đồng bộ với") |
| Cơ quan quản lý NCC thuộc BQP/BCA | 75 đến 77 | Nhập liệu thủ công, không phải API |

Hệ quả: số connector chiều vào ít hơn 7, và có thêm các connector chiều ra mà T02 chưa tính. Ước lượng T02 cần xem lại sau khi chốt danh sách.

Câu hỏi đề xuất: "7 nguồn API" gồm những hệ thống nào, mỗi hệ thống theo chiều vào, chiều ra hay hai chiều?

### 4.3. Đánh số Phụ lục III bị hụt

Các mục lớn đi từ E sang G, không có F. Trong E có I, II, III, V, không có IV. Có hai cách hiểu: lỗi soạn thảo, hoặc một nhóm yêu cầu đã bị cắt khỏi bản dự thảo.

Câu hỏi đề xuất: phần F và mục E.IV có tồn tại trong bản đầy đủ không?

### 4.4. Khối lượng ngoài phân tích dữ liệu chưa được ước lượng

Nếu hợp đồng giao trọn Phụ lục III, các phần sau chưa có task tương ứng trong Excel:

1. Quy trình động và biểu mẫu động (14 đến 22).
2. Toàn bộ quy trình thủ tục hành chính (mục D, 33 mục).
3. Chi trả và quà tri ân (mục H, 7 mục).

Câu hỏi đề xuất: bên mình nhận phần phân tích dữ liệu hay trọn Phụ lục III?

## 5. Sai lệch nội bộ trong Excel

1. Sheet "Lộ trình", ghi chú rủi ro: "GĐ1a có 4 task độ phức tạp Cao (T02, T06, T07 + UC01 phụ thuộc)". UC01 đang ở mức Trung bình, nên con số đúng là 3, khớp cột "Độ phức tạp Cao" của chính sheet.
2. Cột "Tổng ngày công" bằng 0 vì cột ước lượng ở sheet Task & Usecase chưa điền. Chưa có cơ sở để báo giá hoặc kiểm tra tính khả thi của mốc.
3. Số task/UC theo giai đoạn (8, 9, 9, 4) và số task mức Cao (3, 2, 4, 4) đếm đúng theo sheet Task & Usecase.

## 6. Căn cứ pháp lý chưa xác minh

| # | Văn bản | Tình trạng |
|---|---|---|
| 3 | Luật BVDLCN 91/2025/QH15 | Cần đối chiếu toàn văn |
| 7 | NĐ về CSDL quốc gia về an sinh xã hội | Dự thảo. Khung tham chiếu cho T07, T08 |
| 13 | NĐ 56/2017/NĐ-CP hướng dẫn Luật Trẻ em | Cần xác nhận còn hiệu lực |
| 15 | NĐ 131/2021/NĐ-CP | Cần xác nhận còn hiệu lực hoặc đã sửa đổi |
| 19 | Quy trình rà soát hộ nghèo hằng năm | Chưa có số hiệu |
| 20 | Luật BHYT sửa đổi 2024 | Chưa có số hiệu |
| 21 | Vùng đặc biệt khó khăn, vùng DTTS sau sắp xếp | Chưa có số hiệu |

Nếu phạm vi chốt là người có công (mục 4.1), các văn bản trợ giúp xã hội và giảm nghèo (dòng 9 đến 13, 17 đến 19) chuyển sang tham khảo. Pháp lệnh 02/2020/UBTVQH14, NĐ 131/2021/NĐ-CP và NĐ 321/2026/NĐ-CP trở thành căn cứ chính.

## 7. Rủi ro tiến độ

Mốc GĐ1a là 15/11/2026, còn 20 ngày tính từ 26/10/2026. GĐ1a gồm T02, T06, T07 ở mức Cao. T07 (mô hình hồ sơ và quan hệ) là nền của mọi UC quan hệ và hộ. Nếu mục 4.1 đổi phạm vi sang người có công, T07 phải thiết kế lại theo quan hệ người có công với thân nhân thay vì người chăm sóc và hộ.

## 8. Việc cần làm

| Mã | Việc | Đầu vào | Trạng thái |
|---|---|---|---|
| VL-01 | Bổ sung 4 câu hỏi ở mục 4 vào checklist họp (bản `work/`) | Mục 4 | Chưa làm |
| VL-02 | Tách cột "UC tham khảo PL III" của T02 thành tích hợp chiều vào và chiều ra | Mục 4.2 | Chờ đối chiếu |
| VL-03 | Sửa ghi chú rủi ro GĐ1a từ "4 task" thành "3 task" trong bản làm việc | Mục 5 | Chưa làm |
| VL-04 | Xin bản đầy đủ Phụ lục III dạng file (không phải ảnh chụp) | Mục 4.3 | Chưa làm |
| VL-05 | Điền ước lượng ngày công sau khi chốt phạm vi | Mục 4.1, 4.4 | Chờ đối chiếu |
