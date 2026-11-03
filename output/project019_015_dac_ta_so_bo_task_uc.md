# Đặc tả sơ bộ Task và UC

> Bản nháp dựa trên giả định, chưa được bên giao việc xác nhận. Ngày lập: 27/10/2026. Mọi dữ liệu ví dụ trong tài liệu là dữ liệu giả.

| Phiên bản | Ngày | Người sửa | Nội dung thay đổi |
|---|---|---|---|
| 0.1 | 27/10/2026 | BA | Tạo mới |
| 0.2 | 28/10/2026 | BA | Đồng bộ: dẫn chiếu thêm BR-50 đến BR-53; UC01 mục 12 ghi Q59 (đã có trong checklist) |

Việc cần làm, mức sẵn sàng và kế hoạch: `output/project019_014_viec_can_lam_va_ke_hoach_so_bo.md`. Thực thể và sơ đồ UML của từng task, UC: sheet "UC – Thực thể – UML" và tài liệu 007 mục 4.4. Quy tắc BR-01 đến BR-42 và BR-50 đến BR-53: tài liệu 011.

## 0. Cách đọc

Tài liệu có ba mức chi tiết:

- **Phần A, đặc tả đầy đủ theo mẫu** cho 5 UC đi trước: UC01 và UC02 (demo 15/11), UC04, UC06, UC07 (GĐ1b). Mỗi UC có luồng, quy tắc, dữ liệu, tiêu chí nghiệm thu và câu hỏi mở.
- **Phần B, thẻ đặc tả** cho 14 UC còn lại và UC20 đề xuất. Mỗi thẻ có mục tiêu, tác nhân, luồng chính rút gọn và quy tắc. Thẻ cũng ghi tiêu chí chính và điều kiện để đặc tả tiếp.
- **Phần C, đặc tả task nền tảng** T01 đến T11: phạm vi, đầu ra, tiêu chí hoàn thành.

Vai trò người dùng VT01 đến VT07 lấy từ sheet "Nguồn thực thể" và đều là giả định (chờ Q56).

| Mã | Vai trò |
|---|---|
| VT01 | Quản trị hệ thống |
| VT02 | Quản trị dữ liệu |
| VT03 | Chuyên viên chính sách |
| VT04 | Người duyệt |
| VT05 | Cán bộ xã và tỉnh |
| VT06 | Thanh tra và tài chính |
| VT07 | Lãnh đạo và hoạch định |

### 0.1. Quy tắc mới đề xuất

Các UC dưới đây cần bốn quy tắc ngoài 30 BR ban đầu. Ngày 27/10/2026 đã thêm vào danh mục 011 (mục 3.4, trạng thái "Dự thảo"), kèm kịch bản TC-BR50-01 đến TC-BR53-01 và dòng truy vết ở mục 6.

| Mã BR | Tên | Logic | Căn cứ | UC dùng |
|---|---|---|---|---|
| BR-50 | Đếm người duy nhất | Số người = số E01 khác nhau sau ghép định danh. Bản ghi nguồn chưa ghép được (E17 trạng thái "không ghép được" hoặc "ghép mờ chờ duyệt") đếm riêng thành "hồ sơ chưa xác định người", không cộng vào số người | Báo cáo 003 mục 2, nguyên tắc chung | UC01, UC02, UC04 |
| BR-51 | Xét theo ngày chốt | Tuổi, thành viên hộ, diện, địa bàn cư trú xét tại ngày chốt người dùng chọn: bản ghi có hiệu lực khi `hieu_luc_tu ≤ ngày chốt` và (`hieu_luc_den` rỗng hoặc `≥ ngày chốt`) | Báo cáo 003 mục 2 | UC02, UC13, UC14 |
| BR-52 | Trạng thái sống chưa xác định | NGƯỜI có trạng thái sống "chưa xác định" không được coi là "còn sống" khi kiểm tra chi sai; kết quả kiểm tra là "chưa đủ dữ liệu", không phải "đúng" | Tài liệu 007 mục 4.1 | UC04, UC07 |
| BR-53 | Thiếu dữ liệu khác số 0 | Ô chỉ tiêu không tính được do thiếu dữ liệu hiển thị "chưa có dữ liệu", không hiển thị 0; nhóm "chưa rõ" luôn hiển thị | Báo cáo 003 mục 6 | UC01, UC02, UC03 |


## Phần A. Đặc tả đầy đủ

## UC01: Đánh giá chất lượng dữ liệu

> Trạng thái: Giả định · Giai đoạn: GĐ1a (15/11) · Độ phức tạp: Trung bình · Mã 003: PT09, DB05, một phần TH04

### 1. Mục tiêu và giá trị

Cho bên giao việc và đơn vị quản lý nguồn biết dữ liệu của từng nguồn dùng được đến đâu, trước khi dùng số liệu cho quản lý. Kết quả UC01 cũng quyết định UC nào ở GĐ2 cam kết được, nhất là các UC dùng quan hệ người với người (UC08, UC10, UC11).

### 2. Tác nhân và phân quyền

| Tác nhân | Vai trò | Phạm vi địa bàn | Được xem | Bị che |
|---|---|---|---|---|
| VT01, VT02 | Vận hành, quản trị dữ liệu | Toàn quốc | Mọi phép đo; mẫu bản ghi lỗi | Số định danh hiện 4 số cuối, họ tên hiện chữ cái đầu |
| VT07 | Lãnh đạo | Theo phân công | Phép đo tổng hợp | Không xem mẫu bản ghi |
| Chủ nguồn | Đơn vị quản lý nguồn | Nguồn của mình | Phép đo nguồn của mình | Như VT02 |

### 3. Điều kiện

- Tiền điều kiện: ít nhất một lần đồng bộ của nguồn đã hoàn tất (E17, lần đồng bộ ở trạng thái "hoàn tất").
- Hậu điều kiện: mỗi nguồn có bảng phép đo theo lần đồng bộ, lưu được để so giữa các lần.
- Phụ thuộc: T02, T03, T06 (phép đo tỷ lệ ghép được).

### 4. Luồng chính

1. Hệ thống chạy bộ phép đo sau mỗi lần đồng bộ, hoặc VT02 chọn nguồn và lần đồng bộ để chạy lại.
2. Hệ thống đo nhóm "đủ": tỷ lệ bản ghi có giá trị ở từng trường bắt buộc; mẫu số là số bản ghi của nguồn trong lần đồng bộ.
3. Hệ thống đo nhóm "đúng": tỷ lệ số định danh đúng độ dài và định dạng, ngày hợp lệ, mã danh mục có trong T04, mã địa bàn ánh xạ được qua T05.
4. Hệ thống đo nhóm "sạch": số bản ghi trùng khóa nguồn, số người được ghép từ nhiều bản ghi mâu thuẫn (ví dụ khác ngày sinh), tỷ lệ ghép được vào E01 theo BR-50.
5. Hệ thống đo nhóm "sống": độ trễ từ lần cập nhật cuối của nguồn đến ngày đo; tỷ lệ người đã mất theo nguồn dân cư mà nguồn nghiệp vụ vẫn ghi đang hưởng.
6. Hệ thống đo độ đầy đủ quan hệ: tỷ lệ E05 có người nhận tiền; tỷ lệ đối tượng NKT đặc biệt nặng có E06 loại chăm sóc; tỷ lệ người có E03 (thuộc hộ).
7. Hệ thống ghi kết quả theo nguồn × lần đồng bộ × phép đo và hiển thị trên DB05: biểu đồ nhiệt nguồn × phép đo, thanh độ trễ, bảng lỗi.
8. VT02 chọn một ô để xem mẫu bản ghi lỗi (đã che) và chuyển sang xử lý (TH04).

### 5. Luồng thay thế

- 1a. Nguồn chưa có lần đồng bộ nào: DB05 hiển thị nguồn với trạng thái "chưa có dữ liệu" theo BR-53.
- 4a. T06 chưa chạy: phép đo tỷ lệ ghép được hiển thị "chưa đánh giá", các phép đo khác vẫn chạy.

### 6. Luồng ngoại lệ

- 2e. Nguồn đổi cấu trúc (thiếu trường bắt buộc so với mapping): dừng phép đo của nguồn đó, ghi lỗi vào lần đồng bộ (E17), báo VT01.
- 8e. Người dùng không có quyền xem mẫu: ẩn nút xem mẫu, chỉ hiện số đếm.

### 7. Quy tắc nghiệp vụ áp dụng

| Mã BR | Tóm tắt | Căn cứ |
|---|---|---|
| BR-50 | Đếm người duy nhất, tách hồ sơ chưa xác định người | Đề xuất (mục 0.1) |
| BR-53 | Thiếu dữ liệu khác số 0 | Đề xuất (mục 0.1) |

Ngưỡng "đạt" của từng phép đo chưa có căn cứ. Đề xuất chỉ hiển thị giá trị, chưa tô màu đạt hay không đạt cho đến khi bên giao việc chốt ngưỡng.

### 8. Dữ liệu

| Thực thể | Thuộc tính dùng | Nguồn | Đọc/Ghi | Ghi chú chất lượng |
|---|---|---|---|---|
| E17 NGUỒN, LẦN ĐỒNG BỘ, BẢN GHI NGUỒN | Khóa nguồn, trạng thái ghép, thời điểm, số bản ghi, lỗi | 7 nguồn (Q28) | Đọc, ghi kết quả đo | Chưa biết số nguồn thực tế |
| E01 NGƯỜI | Số định danh, ngày sinh, trạng thái sống | Nguồn dân cư, nguồn nghiệp vụ | Đọc | Tỷ lệ có số định danh chưa biết (Q34) |
| E05, E06, E03 | Người nhận, loại quan hệ, thành viên hộ | Nguồn NCC, TGXH, hộ nghèo | Đọc | Chưa biết nguồn nào có quan hệ (Q45, Q46) |
| E13 ĐỊA BÀN | Mã, ánh xạ | Danh mục địa bàn, T05 | Đọc | |

### 9. Màn hình và đầu ra

- Bộ lọc: nguồn, lần đồng bộ, nhóm phép đo, địa bàn.
- Chỉ tiêu: mỗi phép đo ghi tên, công thức, tử số, mẫu số, đơn vị phần trăm.
- Trình bày: DB05 theo báo cáo 003 mục 6; xuất Excel bảng phép đo.

### 10. Yêu cầu phi chức năng

- Hiệu năng: chạy xong trong cửa sổ đồng bộ (chờ Q13, Q54).
- Nhật ký: ghi người xem mẫu bản ghi lỗi (T10).
- Lưu trữ: giữ kết quả đo của mọi lần đồng bộ để so sánh.

### 11. Tiêu chí nghiệm thu

| Mã | Cho (dữ liệu giả) | Khi | Thì | BR/luồng kiểm |
|---|---|---|---|---|
| TC-UC01-01 | Nguồn X có 1.000 bản ghi, 50 bản ghi thiếu ngày sinh | Chạy phép đo | Phép đo "đủ ngày sinh" = 95,0%, mẫu số 1.000 | Bước 2 |
| TC-UC01-02 | 1.000 bản ghi, 900 ghép được vào 870 người, 100 không ghép được | Chạy phép đo | Số người 870; 100 hồ sơ chưa xác định người; không hiển thị 970 | BR-50 |
| TC-UC01-03 | Nguồn Y chưa đồng bộ lần nào | Mở DB05 | Nguồn Y hiển thị "chưa có dữ liệu", không hiển thị 0% | BR-53, 1a |
| TC-UC01-04 | Nguồn X thiếu trường bắt buộc so với mapping | Chạy phép đo | Dừng đo nguồn X, có lỗi trong nhật ký lần đồng bộ | 2e |
| TC-UC01-05 | Người dùng VT07 | Chọn ô lỗi | Không thấy nút xem mẫu | 8e |
| TC-UC01-06 | T06 chưa chạy | Chạy phép đo | Tỷ lệ ghép được hiển thị "chưa đánh giá", phép đo khác có giá trị | 4a |

### 12. Giả định và câu hỏi mở

| # | Nội dung | Loại | Hỏi ai | Mã Q |
|---|---|---|---|---|
| 1 | Ngưỡng đạt của từng phép đo | Câu hỏi | Bên giao việc | Q59 |
| 2 | Kết quả UC01 có trả về chủ nguồn qua API không | Câu hỏi | Bên giao việc | Q35 |
| 3 | Phép đo chạy trên toàn bộ hay trên mẫu | Giả định: toàn bộ | Kỹ thuật | Q13 |


## UC02: Dashboard thống kê tổng hợp (phần DB01)

> Trạng thái: Giả định · Giai đoạn: DB01 ở GĐ1a (15/11, theo 003), DB02 và DB03 ở GĐ1b · Độ phức tạp: Trung bình · Mã 003: PT01 đến PT05, DB01 đến DB03

Phần này đặc tả đầy đủ DB01. DB02 và DB03 ghi khung ở mục 9 và làm tiếp trong BA-15.

### 1. Mục tiêu và giá trị

Lãnh đạo và cán bộ tỉnh xem số người và số hộ thuộc từng nhóm chính sách tại một ngày chốt. Số liệu phân theo địa bàn và xem sâu được đến xã. Đây là luồng demo 15/11.

### 2. Tác nhân và phân quyền

| Tác nhân | Vai trò | Phạm vi địa bàn | Được xem | Bị che |
|---|---|---|---|---|
| VT07 | Lãnh đạo | Theo phân công (trung ương hoặc tỉnh) | Số tổng hợp mọi cấp trong phạm vi | DB01 không có dữ liệu cá nhân |
| VT05 | Cán bộ tỉnh, xã | Tỉnh hoặc xã được giao | Số tổng hợp trong địa bàn | Như trên |

DB01 chỉ hiển thị số tổng hợp. Muốn xem danh sách cá nhân phải chuyển sang UC04 và chịu quyền của UC04.

### 3. Điều kiện

- Tiền điều kiện: dữ liệu đã ghép định danh (T06), có diện (E04) và cư trú (E12) có hiệu lực, danh mục địa bàn đã ánh xạ (T05).
- Hậu điều kiện: không ghi dữ liệu nghiệp vụ; chỉ ghi nhật ký xuất file.
- Phụ thuộc: T05, T06, T07, UC01 (độ tin cậy hiển thị kèm).

### 4. Luồng chính

1. Người dùng mở DB01. Hệ thống đặt mặc định ngày chốt là ngày đồng bộ gần nhất, địa bàn là phạm vi được giao, mọi nhóm.
2. Người dùng chọn ngày chốt, địa bàn, nhóm, nguồn.
3. Hệ thống lấy tập người có diện hiệu lực tại ngày chốt và cư trú trong địa bàn, theo BR-51.
4. Hệ thống tính thẻ tổng: số người duy nhất (BR-50), số hộ, số hồ sơ chưa xác định người, thời điểm cập nhật, độ phủ nguồn lấy từ UC01.
5. Hệ thống tính thanh theo nhóm: số người thuộc từng nhóm. Một người thuộc nhiều nhóm được đếm ở mỗi nhóm; hệ thống ghi chú "tổng các nhóm lớn hơn số người duy nhất".
6. Hệ thống tính thanh theo địa bàn cấp dưới và bảng số liệu nhóm × địa bàn.
7. Người dùng chọn một thanh nhóm. Hệ thống lọc thanh địa bàn và bảng theo nhóm đó.
8. Người dùng chọn một địa bàn. Hệ thống xuống cấp dưới (tỉnh sang xã) với cùng bộ lọc.
9. Người dùng xuất Excel. Tệp có đúng số đang hiển thị, kèm ngày chốt, bộ lọc, nguồn và thời điểm xuất.

### 5. Luồng thay thế

- 2a. Người dùng chọn ngày chốt trước lần đồng bộ đầu tiên: hệ thống báo không có dữ liệu cho ngày này, giữ bộ lọc cũ.
- 8a. Địa bàn đã là cấp xã: không xuống tiếp; nút xem danh sách chuyển sang UC04 nếu người dùng có quyền.

### 6. Luồng ngoại lệ

- 3e. Người có diện nhưng thiếu cư trú, hoặc mã địa bàn không ánh xạ được: đếm vào dòng "chưa rõ địa bàn", hiển thị trên bảng theo BR-53.
- 9e. Kết quả vượt giới hạn dòng xuất (chờ Q17): báo người dùng thu hẹp bộ lọc.

### 7. Quy tắc nghiệp vụ áp dụng

| Mã BR | Tóm tắt | Căn cứ |
|---|---|---|
| BR-50 | Đếm người duy nhất | Đề xuất |
| BR-51 | Xét theo ngày chốt | Đề xuất |
| BR-53 | Thiếu dữ liệu khác số 0; giữ nhóm chưa rõ | Đề xuất |

### 8. Dữ liệu

| Thực thể | Thuộc tính dùng | Nguồn | Đọc/Ghi | Ghi chú chất lượng |
|---|---|---|---|---|
| E01 NGƯỜI | Khóa nội bộ, ngày sinh, giới tính | Sau T06 | Đọc | Tỷ lệ ghép lấy từ UC01 |
| E04 DIỆN ĐỐI TƯỢNG | Diện, hiệu lực từ, đến | Nguồn nghiệp vụ | Đọc | Bộ mã diện theo T04 |
| E12 CƯ TRÚ, E13 ĐỊA BÀN | Địa bàn, hiệu lực; ánh xạ mã | Nguồn dân cư, T05 | Đọc | Mã cũ trước 01/07/2025 |
| E02, E03 HỘ, THÀNH VIÊN HỘ | Mã hộ, hiệu lực | Nguồn hộ nghèo, dân cư | Đọc | Số hộ chỉ hiển thị khi T08 xong; trước đó hiện "chưa có dữ liệu" |
| E17 | Nguồn, thời điểm đồng bộ | T02 | Đọc | |

### 9. Màn hình và đầu ra

- DB01: thẻ tổng phía trên; thanh theo nhóm và theo địa bàn ở giữa; bảng số liệu phía dưới (báo cáo 003 mục 6).
- Bộ lọc: ngày chốt, địa bàn, nhóm, nguồn. Bộ lọc tác động mọi khối.
- Xuất: Excel theo mẫu PT10 cố định.
- DB02 (khung, GĐ1b): phân bố tuổi, thuộc tính, biểu đồ nhiệt giao thoa nhóm × nhóm, bảng chéo. Không dùng biểu đồ tròn cho các nhóm chồng lấn.
- DB03 (khung, GĐ1b): giá trị hai kỳ, chênh lệch, đường theo thời gian. Cần T03 giữ lịch sử; thiếu lịch sử thì đánh dấu "chưa đáp ứng".

### 10. Yêu cầu phi chức năng

- Hiệu năng: thời gian mở DB01 cấp tỉnh chờ Q17.
- Nhật ký: ghi người xuất file, bộ lọc, thời điểm.

### 11. Tiêu chí nghiệm thu

| Mã | Cho (dữ liệu giả) | Khi | Thì | BR/luồng kiểm |
|---|---|---|---|---|
| TC-UC02-01 | Bà A thuộc hai diện NCT và NKT tại xã X | Mở DB01 xã X | Thẻ số người tính bà A 1 lần; thanh NCT và thanh NKT mỗi thanh tính bà A 1 lần; có ghi chú tổng nhóm lớn hơn số người | BR-50, bước 5 |
| TC-UC02-02 | Diện NKT của ông C hết hiệu lực 30/09/2026 | Chọn ngày chốt 15/10/2026 | Ông C không có trong thanh NKT | BR-51 |
| TC-UC02-03 | Ông D có diện, không có cư trú | Mở DB01 | Ông D ở dòng "chưa rõ địa bàn" | BR-53, 3e |
| TC-UC02-04 | T08 chưa xong | Mở DB01 | Thẻ số hộ hiện "chưa có dữ liệu" | BR-53 |
| TC-UC02-05 | Đang lọc nhóm NKT, tỉnh T | Xuất Excel | Số trong tệp bằng số trên màn hình; tệp ghi ngày chốt và bộ lọc | Bước 9 |
| TC-UC02-06 | Ngày chốt trước lần đồng bộ đầu | Chọn ngày | Thông báo không có dữ liệu, giữ bộ lọc cũ | 2a |
| TC-UC02-07 | Bộ lọc cho kết quả vượt giới hạn xuất | Xuất Excel | Báo thu hẹp bộ lọc, không xuất tệp bị cắt | 9e |

### 12. Giả định và câu hỏi mở

| # | Nội dung | Loại | Hỏi ai | Mã Q |
|---|---|---|---|---|
| 1 | Nhóm đối tượng và nguồn dùng cho demo | Câu hỏi | Bên giao việc | Q22, Q27 |
| 2 | Vẽ bằng Angular hay BI tool | Câu hỏi | Kỹ thuật | Q16 |
| 3 | Mẫu PT10 có theo biểu mẫu bắt buộc không | Câu hỏi | Bên giao việc | Q19 |


## UC04: Hồ sơ 360° theo số định danh

> Trạng thái: Giả định · Giai đoạn: GĐ1b · Độ phức tạp: Trung bình · Mã 003: KT01

### 1. Mục tiêu và giá trị

Cán bộ có thẩm quyền xem mọi vai trò của một người trên một màn hình. Màn hình cho biết người đó thuộc diện nào và hưởng chế độ gì. Màn hình cũng cho biết người đó chăm sóc ai, là thân nhân hay người nhận tiền của ai, thuộc hộ nào và đang có cảnh báo gì.

### 2. Tác nhân và phân quyền

| Tác nhân | Vai trò | Phạm vi địa bàn | Được xem | Bị che |
|---|---|---|---|---|
| VT05 | Cán bộ xã, tỉnh | Người cư trú hoặc có hồ sơ hưởng tại địa bàn được giao | Toàn bộ khối | Số tài khoản (E10) hiện 4 số cuối |
| VT06 | Thanh tra, tài chính | Theo phân công | Toàn bộ khối | Không che tài khoản khi đang xử lý cảnh báo được giao |
| VT02 | Quản trị dữ liệu | Toàn quốc | Khối nguồn và ghép định danh | Số định danh hiện 4 số cuối |

Mọi lần mở hồ sơ ghi nhật ký tra cứu: người tra, thời điểm, số định danh tra, lý do (Luật 91/2025, T10).

### 3. Điều kiện

- Tiền điều kiện: người dùng đăng nhập, có vai trò được phép tra cứu.
- Hậu điều kiện: có bản ghi nhật ký tra cứu.
- Phụ thuộc: T06, T07, T10; UC07 và UC11 cho khối cảnh báo.

### 4. Luồng chính

1. Người dùng nhập số định danh và chọn lý do tra cứu.
2. Hệ thống kiểm tra quyền theo vai trò và địa bàn; ghi nhật ký tra cứu.
3. Hệ thống tìm E01 theo số định danh và hiển thị khối thông tin chung: họ tên, ngày sinh, trạng thái sống, nơi cư trú hiện tại.
4. Hệ thống hiển thị khối "Là đối tượng": các diện E04 có hiệu lực, kết quả giám định E11.
5. Hệ thống hiển thị khối "Hưởng chế độ": các E05 mà người này là đối tượng, người được hưởng hoặc người nhận tiền, ghi rõ vai trò ở từng dòng; kỳ chi gần nhất từ E07.
6. Hệ thống hiển thị khối "Quan hệ": các E06 theo hai chiều (người này chăm sóc ai, ai chăm sóc người này, là thân nhân của ai), loại thân nhân theo BR-23.
7. Hệ thống hiển thị khối "Hộ": hộ và vai trò trong hộ (E03), phân loại hộ kỳ gần nhất (E14).
8. Hệ thống hiển thị khối "Cảnh báo": các E16 đang mở liên quan người này, nếu người dùng có quyền.
9. Hệ thống hiển thị khối "Nguồn": bản ghi nguồn đã ghép (E17) và độ tin cậy ghép.
10. Người dùng chọn một người liên quan ở khối 5 hoặc 6 để mở hồ sơ người đó (lặp lại từ bước 2).

### 5. Luồng thay thế

- 3a. Không tìm thấy số định danh: hệ thống cho tìm theo họ tên, ngày sinh, địa bàn; kết quả là danh sách ứng viên, không tự gộp.
- 3b. Người này có bản ghi nguồn đang "ghép mờ chờ duyệt": hiển thị cảnh báo "hồ sơ có thể chưa đầy đủ" (BR-50).

### 6. Luồng ngoại lệ

- 2e. Người cần tra ngoài địa bàn được giao: từ chối, ghi nhật ký lần bị từ chối.
- 3e. Trạng thái sống "chưa xác định": hiển thị đúng nhãn, không hiển thị "còn sống" (BR-52).

### 7. Quy tắc nghiệp vụ áp dụng

| Mã BR | Tóm tắt | Căn cứ |
|---|---|---|
| BR-23 | Thân nhân NCC chỉ gồm các loại theo Pháp lệnh | PL 02/2020 Điều 3 khoản 3, sửa bởi PL 05/2026 |
| BR-50 | Đếm người duy nhất; bản ghi chưa ghép | Đề xuất |
| BR-52 | Trạng thái sống chưa xác định | Đề xuất |

### 8. Dữ liệu

| Thực thể | Thuộc tính dùng | Nguồn | Đọc/Ghi | Ghi chú chất lượng |
|---|---|---|---|---|
| E01, E12 | Định danh, trạng thái sống, cư trú | Dân cư | Đọc | |
| E04, E11 | Diện, giám định | NCC, TGXH | Đọc | Q33 |
| E05, E07, E10 | Hưởng chế độ, kỳ chi, tài khoản | NCC, TGXH, chi trả | Đọc | Q32 |
| E06 | Quan hệ hai chiều | NCC, TGXH, dân cư | Đọc | Q45, Q46 |
| E02, E03, E14 | Hộ, thành viên, phân loại | Hộ nghèo, dân cư | Đọc | Q51 |
| E16, E17 | Cảnh báo, bản ghi nguồn | Hệ thống | Đọc | |
| Nhật ký tra cứu (nhóm D) | Người tra, thời điểm, lý do | Hệ thống | Ghi | |

### 9. Màn hình và đầu ra

Một trang, các khối theo thứ tự bước 3 đến 9. Khối không có dữ liệu ghi "không có" hoặc "chưa có dữ liệu" (BR-53). GĐ1b không có xuất file.

### 10. Yêu cầu phi chức năng

- Nhật ký tra cứu giữ theo NĐ 356/2025; thời hạn lưu chờ Q17.

### 11. Tiêu chí nghiệm thu

| Mã | Cho (dữ liệu giả) | Khi | Thì | BR/luồng kiểm |
|---|---|---|---|---|
| TC-UC04-01 | Ông B nhận tiền chăm sóc cho bà A | Tra ông B | Khối 5 có dòng chế độ của bà A với vai trò "người nhận tiền" | Bước 5 |
| TC-UC04-02 | Ông B chăm sóc bà A | Tra bà A | Khối 6 có dòng "được ông B chăm sóc"; chọn ông B mở được hồ sơ ông B | Bước 6, 10 |
| TC-UC04-03 | Cán bộ xã X tra người cư trú xã Y | Tra | Bị từ chối, có bản ghi nhật ký | 2e |
| TC-UC04-04 | Bà E trạng thái sống "chưa xác định" | Tra | Hiển thị "chưa xác định" | BR-52, 3e |
| TC-UC04-05 | Bà F là "cháu" của liệt sĩ trong nguồn | Tra bà F từ 01/01/2027 | Không hiển thị bà F là thân nhân NCC | BR-23 |
| TC-UC04-06 | Số định danh không tìm thấy | Tra | Cho tìm theo họ tên, ngày sinh; trả danh sách ứng viên | 3a |
| TC-UC04-07 | Ông G có bản ghi ghép mờ chờ duyệt | Tra | Có cảnh báo hồ sơ có thể chưa đầy đủ | BR-50, 3b |

### 12. Giả định và câu hỏi mở

| # | Nội dung | Loại | Hỏi ai | Mã Q |
|---|---|---|---|---|
| 1 | Có bắt buộc nhập lý do tra cứu không | Câu hỏi | Bên giao việc | Q8 |
| 2 | Cán bộ xã có xem hồ sơ người đã chuyển khỏi xã không | Câu hỏi | Bên giao việc | Q56 |


## UC06: Nhiều diện và quy tắc mức cao nhất

> Trạng thái: Giả định · Giai đoạn: GĐ1b · Độ phức tạp: Trung bình · Mã 003: một phần PT03

### 1. Mục tiêu và giá trị

Thanh tra, tài chính phát hiện người đang hưởng nhiều mức trái quy tắc. Trợ giúp xã hội chỉ cho hưởng một mức cao nhất, trừ ngoại lệ. Người có công được cộng dồn nhiều diện từ 01/01/2027. Vì hai quy tắc khác nhau, UC tách thành hai nhánh.

### 2. Tác nhân và phân quyền

| Tác nhân | Vai trò | Phạm vi địa bàn | Được xem | Bị che |
|---|---|---|---|---|
| Engine | Tính và sinh cảnh báo | Toàn quốc | | |
| VT06 | Thanh tra, tài chính | Theo phân công | Danh sách cảnh báo, chi tiết | Không che |
| VT05 | Cán bộ xã, tỉnh | Địa bàn được giao | Cảnh báo trong địa bàn | Số tài khoản 4 số cuối |

### 3. Điều kiện

- Tiền điều kiện: E04, E05 đã nạp cho kỳ cần kiểm; cấu hình E20 đến E23 có phiên bản đã duyệt cho kỳ đó.
- Hậu điều kiện: E31 cho mỗi người và kỳ; E16 cho mỗi sai lệch; E32 ghi lần tính.
- Phụ thuộc: T06, T09; E07 nếu có dữ liệu chi trả.

### 4. Luồng chính

1. VT01 kích hoạt, hoặc lịch chạy engine cho một kỳ hưởng; hệ thống tạo E32.
2. Engine lấy mọi người có từ 2 diện hiệu lực trong kỳ (E04).
3. Với chế độ trợ giúp xã hội: engine xác định các mức đủ điều kiện theo BR-01, BR-15, BR-16; áp BR-02 (một mức cao nhất), trừ trường hợp BR-03 (đơn thân nghèo nuôi con).
4. Với chế độ người có công từ kỳ 01/2027: engine áp BR-25 (hưởng nhiều diện, riêng trợ cấp người phục vụ và ưu đãi Điều 5 khoản 2 chỉ một mức) và BR-26 cho thân nhân. Kỳ trước 01/2027 dùng quy tắc cũ (chờ đối chiếu, mục 12).
5. Engine ghi E31: các chế độ và mức đáng hưởng của người trong kỳ.
6. Engine so E31 với E05 đang hưởng trong kỳ. Đang hưởng nhiều chế độ hơn số đáng hưởng, hoặc mức đang hưởng cao hơn mức đáng hưởng, thì tạo E16 loại "trùng chế độ" kèm quy tắc và số tiền ảnh hưởng.
7. Hệ thống hiển thị ma trận chồng lấn diện × diện (số người) và danh sách cảnh báo cho VT06.
8. VT06 mở cảnh báo, xem căn cứ, chuyển trạng thái theo sơ đồ 6.7 (xử lý ở UC20).

### 5. Luồng thay thế

- 6a. Có E07 thực chi: so thêm số thực chi với số phải chi trong E31.
- 6b. Không có E07: chỉ so E05 với E31, ghi rõ "chưa đối chiếu thực chi" trên cảnh báo.

### 6. Luồng ngoại lệ

- 3e. Kỳ cần kiểm chưa có phiên bản cấu hình đã duyệt: dừng, ghi lỗi vào E32, không sinh cảnh báo.
- 6e. Cảnh báo cùng quy tắc, người, kỳ đã tồn tại và đang xử lý: không tạo mới, không ghi đè phần xử lý (tài liệu 007 mục 3.5).

### 7. Quy tắc nghiệp vụ áp dụng

| Mã BR | Tóm tắt | Căn cứ |
|---|---|---|
| BR-01 | Mức trợ cấp xã hội hằng tháng | NĐ 335/2026 Điều 6 khoản 1 |
| BR-02 | Nhiều hệ số, nhiều văn bản: một mức cao nhất | NĐ 335/2026 Điều 6 khoản 2 |
| BR-03 | Ngoại lệ đơn thân nghèo nuôi con | NĐ 335/2026 Điều 6 khoản 2 |
| BR-15 | Người cao tuổi hưởng TGXH | NĐ 335/2026 Điều 5 khoản 5 |
| BR-16 | Hưu trí xã hội và TGXH: mức cao hơn | NĐ 335/2026 Điều 31 |
| BR-25 | NCC nhiều diện | PL 02/2020 Điều 6 khoản 3, sửa bởi PL 05/2026 |
| BR-26 | Trợ cấp tuất của thân nhân | PL 02/2020 Điều 6 khoản 5, 6 |

### 8. Dữ liệu

| Thực thể | Thuộc tính dùng | Nguồn | Đọc/Ghi | Ghi chú chất lượng |
|---|---|---|---|---|
| E04 | Diện, hiệu lực, cách sinh | NCC, TGXH | Đọc | |
| E05 | Chế độ, mức, hiệu lực | NCC, TGXH | Đọc | Q52 |
| E07 | Thực chi theo kỳ | Chi trả | Đọc | Q32 |
| E20 đến E23 | Chế độ, tham số, quy tắc | Cấu hình T09 | Đọc | |
| E31, E32, E16 | Đáng hưởng, lần tính, cảnh báo | Engine | Ghi | |

### 9. Màn hình và đầu ra

- Ma trận chồng lấn diện × diện; mỗi ô là số người duy nhất, chọn ô để xem danh sách (khi có quyền).
- Danh sách cảnh báo: người, kỳ, chế độ đang hưởng, chế độ đáng hưởng, quy tắc, số tiền ảnh hưởng, trạng thái.

### 10. Yêu cầu phi chức năng

- Chạy lại được: kết quả E31 được thay bằng lần tính sau, phần xử lý của E16 giữ nguyên.

### 11. Tiêu chí nghiệm thu

| Mã | Cho (dữ liệu giả) | Khi | Thì | BR/luồng kiểm |
|---|---|---|---|---|
| TC-UC06-01 | Bà A đủ hai hệ số TGXH 1,5 và 2,0, đang hưởng cả hai | Chạy kỳ 10/2026 | E31 chỉ giữ hệ số 2,0; tạo 1 cảnh báo trùng chế độ | BR-01, BR-02 |
| TC-UC06-02 | Bà H đơn thân nghèo nuôi con, đồng thời NKT nặng, hưởng cả hai | Chạy | Không tạo cảnh báo | BR-03 |
| TC-UC06-03 | Ông K là NCT đủ điều kiện hưu trí xã hội và TGXH, đang hưởng mức thấp hơn | Chạy | E31 ghi mức cao hơn; cảnh báo loại "sai mức" | BR-16 |
| TC-UC06-04 | Ông L vừa là thương binh vừa là bệnh binh, hưởng cả hai trợ cấp | Chạy kỳ 01/2027 | Không tạo cảnh báo | BR-25 |
| TC-UC06-05 | Ông L hưởng hai suất trợ cấp người phục vụ | Chạy kỳ 01/2027 | Tạo cảnh báo; E31 giữ một suất cao nhất | BR-25 |
| TC-UC06-06 | Bà M là thân nhân của 3 NCC, hưởng 3 suất tuất | Chạy | Cảnh báo vượt số suất tối đa | BR-26 |
| TC-UC06-07 | Bà N là NCT hộ nghèo, không có người phụng dưỡng | Chạy | E31 có chế độ Điều 5 khoản 5 điểm a | BR-15 |
| TC-UC06-08 | Kỳ 11/2026 chưa có cấu hình đã duyệt | Chạy | Dừng, E32 trạng thái lỗi, không có cảnh báo mới | 3e |
| TC-UC06-09 | Cảnh báo của bà A kỳ 10/2026 đang xác minh | Chạy lại kỳ 10/2026 | Không tạo cảnh báo thứ hai; trạng thái và kết quả xử lý giữ nguyên | 6e |

### 12. Giả định và câu hỏi mở

| # | Nội dung | Loại | Hỏi ai | Mã Q |
|---|---|---|---|---|
| 1 | Quy tắc NCC nhiều diện trước 01/01/2027 (chưa đọc bản gốc PL 02/2020 trước khi sửa) | Việc BA tự tra | BA | Không |
| 2 | "Đang hưởng" lấy từ nguồn hay do hệ thống tính | Câu hỏi | Bên giao việc | Q52 |


## UC07: Chi sai theo trạng thái đối tượng

> Trạng thái: Giả định · Giai đoạn: GĐ1b · Độ phức tạp: Cao · Mã 003: một phần PT06, PT07

### 1. Mục tiêu và giá trị

Phát hiện khoản vẫn chi khi đối tượng đã mất, đã chuyển đi, bị tạm đình chỉ hoặc chấm dứt, hoặc chi sai mức do qua mốc tuổi. Kiểm cả khoản chi cho người liên quan (kinh phí chăm sóc, thân nhân) khi trạng thái đối tượng thay đổi.

### 2. Tác nhân và phân quyền

Như UC06. VT06 xem số tài khoản đầy đủ khi xử lý cảnh báo được giao.

### 3. Điều kiện

- Tiền điều kiện: E01 có trạng thái sống và ngày mất; E05, E07 cho kỳ cần kiểm; cấu hình kỳ đã duyệt.
- Hậu điều kiện: E31, E16, E32 như UC06.
- Phụ thuộc: T06, T07, T09; T13 (truy lĩnh) nếu Q39 xác nhận đã chi truy lĩnh.

### 4. Luồng chính

1. Engine chạy cho kỳ T, tạo E32.
2. Với mỗi E05 đang hưởng trong kỳ T, engine lấy trạng thái của người là đối tượng tại kỳ T.
3. Đối tượng đã mất trước kỳ T: mức đáng hưởng từ tháng sau tháng mất bằng 0 (BR-05, BR-08 cho TGXH; BR-28 cho NCC). Engine lan kết quả sang E05 của người liên quan qua E06 (kinh phí chăm sóc theo BR-09).
4. Đối tượng NCC bị tạm đình chỉ hoặc chấm dứt: áp BR-28, lan sang thân nhân nếu có.
5. Đối tượng không nhận chế độ liên tục từ số tháng tham số trở lên: áp BR-07 (tạm dừng).
6. Đối tượng qua mốc tuổi làm đổi hệ số: tính lại mức (BR-01 cho TGXH; BR-22 cho con liệt sĩ đủ 18 tuổi).
7. Engine tính mức đáng hưởng kỳ T theo tham số áp dụng cho kỳ T, không theo ngày chi (BR-40, BR-20, BR-21; BR-13 cho kỳ từ 07/2026).
8. Engine gộp số đã chi của kỳ T, gồm khoản thường kỳ và khoản truy lĩnh cho kỳ T (BR-41), rồi so với mức đáng hưởng.
9. Chênh lệch khác 0 thì tạo E16 loại "chi sai", kèm quy tắc, sự kiện, số tiền ảnh hưởng.
10. VT06 xem danh sách và xử lý ở UC20.

### 5. Luồng thay thế

- 2a. Đối tượng chuyển nơi cư trú: không coi là chi trùng nếu nơi cũ thôi chi đúng tháng (BR-06); phần đầy đủ chờ T15.
- 8a. Không có E07: so E05 với E31, ghi "chưa đối chiếu thực chi".

### 6. Luồng ngoại lệ

- 2e. Trạng thái sống "chưa xác định": không kết luận chi sai; tạo E16 loại "thiếu dữ liệu xác minh" (BR-52).
- 8e. Nguồn chi trả không phân biệt khoản truy lĩnh: chỉ so khoản thường kỳ; cảnh báo kỳ 07 đến 09/2026 gắn nhãn "có thể do truy lĩnh" (chờ Q39).

### 7. Quy tắc nghiệp vụ áp dụng

| Mã BR | Tóm tắt | Căn cứ |
|---|---|---|
| BR-05 | Thôi hưởng và điều chỉnh mức | NĐ 335/2026 Điều 8 khoản 4 |
| BR-06 | Chuyển nơi cư trú | NĐ 335/2026 Điều 8 khoản 3 |
| BR-07 | Tạm dừng do không nhận | NĐ 335/2026 Điều 9 khoản 1 |
| BR-08 | Trường hợp thôi hưởng TGXH | NĐ 335/2026 Điều 9 khoản 2 |
| BR-09 | Thôi hỗ trợ nhận chăm sóc | NĐ 335/2026 Điều 9 khoản 3 |
| BR-13 | Chuyển mức từ 01/07/2026 | NĐ 335/2026 Điều 32 |
| BR-20, BR-21 | Mức NCC theo bảng phụ lục; hai mốc áp dụng NĐ 321/2026 | NĐ 321/2026 (chờ đối chiếu) |
| BR-22 | Con liệt sĩ đủ 18 tuổi | NĐ 321/2026 Phụ lục I (chờ đối chiếu) |
| BR-28 | Tạm đình chỉ, chấm dứt, lan sang thân nhân | PL 02/2020 Điều 54 |
| BR-40 | Tính mức đúng theo kỳ hưởng | Suy từ NĐ 335 Điều 32, NĐ 321 Điều 3 |
| BR-41 | Gộp truy lĩnh khi đối chiếu | Suy luận BA, chờ Q32 |
| BR-52 | Trạng thái sống chưa xác định | Đề xuất |

### 8. Dữ liệu

| Thực thể | Thuộc tính dùng | Nguồn | Đọc/Ghi | Ghi chú chất lượng |
|---|---|---|---|---|
| E01 | Trạng thái sống, ngày mất, nguồn xác nhận | Dân cư, liên thông khai tử | Đọc | |
| E05, E09 | Hưởng chế độ, quyết định | NCC, TGXH | Đọc | Q31, Q50 |
| E06 | Quan hệ chăm sóc, thân nhân | NCC, TGXH | Đọc | Q45, Q46 |
| E07, E10 | Kỳ chi, loại khoản, số thực chi, tài khoản | Chi trả | Đọc | Q32 |
| E15 | Sự kiện mất, chuyển cư trú | UC11 | Đọc | |
| E22, E23 | Tham số, quy tắc theo kỳ | T09 | Đọc | |
| E31, E32, E16 | Đáng hưởng, lần tính, cảnh báo | Engine | Ghi | |

### 9. Màn hình và đầu ra

Danh sách cảnh báo chi sai: người, kỳ, khoản, số đã chi, số đáng chi, chênh lệch, quy tắc, sự kiện căn cứ, trạng thái. Lọc theo loại sự kiện, địa bàn, kỳ.

### 10. Yêu cầu phi chức năng

Như UC06.

### 11. Tiêu chí nghiệm thu

| Mã | Cho (dữ liệu giả) | Khi | Thì | BR/luồng kiểm |
|---|---|---|---|---|
| TC-UC07-01 | Bà A mất 15/09/2026, kỳ 10/2026 vẫn chi trợ cấp | Chạy kỳ 10/2026 | Cảnh báo chi sai, mức đáng hưởng 0 | BR-05, BR-08 |
| TC-UC07-02 | Bà A đã mất; ông B vẫn nhận kinh phí chăm sóc bà A kỳ 10/2026 | Chạy | Thêm cảnh báo cho khoản của ông B | BR-09 |
| TC-UC07-03 | Ông P không nhận chế độ đủ số tháng tham số | Chạy | Cảnh báo tạm dừng | BR-07 |
| TC-UC07-04 | Kỳ 07/2026 chi theo mức cũ, kỳ 10/2026 truy lĩnh phần chênh cho kỳ 07 | Chạy kỳ 07/2026 | Không cảnh báo, vì số đã chi gồm truy lĩnh bằng mức đáng hưởng | BR-13, BR-40, BR-41 |
| TC-UC07-05 | Thương binh bị tạm đình chỉ do chấp hành án tội cố ý; thân nhân vẫn hưởng | Chạy | Cảnh báo cho cả thương binh và thân nhân | BR-28 |
| TC-UC07-06 | Con liệt sĩ đủ 18 tuổi tháng 08/2026, kỳ 10/2026 vẫn hưởng mục 3.1 | Chạy | Cảnh báo sai mức | BR-22 |
| TC-UC07-07 | Bà E trạng thái sống chưa xác định | Chạy | Cảnh báo loại "thiếu dữ liệu xác minh", không phải "chi sai" | BR-52, 2e |
| TC-UC07-08 | Mức NCC kỳ 08/2026 thuộc Điều 6 NĐ 321 | Chạy | Dùng bảng của văn bản cũ (mốc 01/2027) | BR-20, BR-21 |
| TC-UC07-09 | Nguồn chi trả không có loại khoản | Chạy kỳ 08/2026 | Cảnh báo gắn nhãn "có thể do truy lĩnh" | 8e |
| TC-UC07-10 | Không có E07 | Chạy | Cảnh báo ghi "chưa đối chiếu thực chi" | 8a |
| TC-UC07-11 | Ông Q chuyển tỉnh tháng 09/2026, nơi cũ thôi chi từ 10/2026 | Chạy kỳ 10/2026 | Không cảnh báo chi trùng | BR-06, 2a |

### 12. Giả định và câu hỏi mở

| # | Nội dung | Loại | Hỏi ai | Mã Q |
|---|---|---|---|---|
| 1 | Khoản chênh 07 đến 09/2026 đã chi truy lĩnh chưa, ghi thế nào | Câu hỏi | Bên giao việc | Q39 |
| 2 | Nguồn có ghi sự kiện án phạt tù, xuất cảnh trái phép không | Câu hỏi | Bên giao việc | Q47 |
| 3 | Kỳ đã chốt có tính lại không | Câu hỏi | Bên giao việc | Q54 |


## Phần B. Thẻ đặc tả các UC còn lại

Mỗi thẻ đủ để ước lượng sơ bộ và xếp lịch, chưa đủ để phát triển. Dòng "Điều kiện" là việc phải có trước khi viết đặc tả đầy đủ theo mẫu.

### UC03: Báo cáo định kỳ theo biểu mẫu (GĐ2, PT10)

- Mục tiêu: xuất báo cáo tháng, quý, năm theo biểu mẫu nghiệp vụ bắt buộc.
- Tác nhân: VT05, VT07.
- Luồng chính:
  1. Chọn biểu mẫu và kỳ.
  2. Hệ thống tính từng ô theo chỉ tiêu đã định nghĩa ở UC02.
  3. Kiểm tổng dòng, tổng cột.
  4. Xuất file theo mẫu.
- Quy tắc: BR-50, BR-51, BR-53; quy tắc riêng của từng biểu mẫu.
- Tiêu chí chính: số ở mỗi ô bằng kết quả truy vấn đối chiếu trên cùng tập dữ liệu và kỳ.
- Điều kiện: có biểu mẫu (Q16, Q19, TT 18/2025/TT-BNV).

### UC05: Hồ sơ 360° theo hộ (GĐ2, KT01)

- Mục tiêu: xem một hộ gồm thành viên, diện của từng người, chính sách theo hộ, tổng trợ cấp hộ nhận.
- Tác nhân: VT05 cấp xã.
- Luồng chính:
  1. Nhập mã hộ hoặc số định danh một thành viên.
  2. Hiển thị chủ hộ, thành viên có hiệu lực, phân loại hộ theo kỳ rà soát.
  3. Tổng các E05 mà người hoặc hộ được hưởng.
  4. Mở hồ sơ từng người (UC04).
- Quy tắc: BR-42 (phân loại theo kỳ), BR-50.
- Tiêu chí chính: hộ cư trú và hộ rà soát nghèo không trùng nhau thì hiển thị cả hai, ghi rõ loại hộ.
- Điều kiện: T08 xong; Q51.

### UC08: Chi sai theo vai trò liên quan (GĐ2)

- Mục tiêu: phát hiện chi sai cho người chăm sóc, người nhận, NKT mang thai hoặc nuôi con nhỏ.
- Tác nhân: Engine, VT06.
- Luồng chính:
  1. Với mỗi E05 có người hưởng khác đối tượng.
  2. Kiểm người chăm sóc còn đủ điều kiện (BR-09).
  3. Kiểm con đã quá số tháng tham số mà vẫn hưởng hệ số BR-11.
  4. Kiểm vợ và chồng cùng là NKT nhận hai suất (BR-11).
  5. Đếm số đối tượng một người nhận chăm sóc, vượt ngưỡng thì cảnh báo bất thường.
- Quy tắc: BR-09, BR-11; ngưỡng bất thường chưa có căn cứ.
- Tiêu chí chính: con của NKT đã quá 36 tháng (dữ liệu giả) mà vẫn hưởng hệ số 1,5 thì có cảnh báo.
- Điều kiện: Q27 (phạm vi có TGXH), Q46; UC01 đo được độ đầy đủ quan hệ chăm sóc.

### UC09: Đối tượng đủ điều kiện chưa hưởng (GĐ2, PT07)

- Mục tiêu: lập danh sách người đáp ứng tiêu chí nhưng chưa có hồ sơ hưởng.
- Tác nhân: Engine, VT05.
- Luồng chính:
  1. Engine tính E31 cho mọi người có dữ liệu tiêu chí.
  2. Lấy người có E31 nhưng không có E05 tương ứng.
  3. Phân ba trạng thái không chồng lấn (đã có ghi nhận, chưa tìm thấy, chưa đủ dữ liệu đối chiếu).
  4. Tạo danh sách KT02 cho cán bộ xã xác minh.
- Quy tắc: BR-01, BR-04, BR-14, BR-15, BR-16.
- Tiêu chí chính: người thiếu dữ liệu giám định không bị xếp vào "chưa tìm thấy".
- Điều kiện: biết nguồn nào cho danh sách người đủ tiêu chí (tuổi, khuyết tật, hộ nghèo) độc lập với nguồn hồ sơ hưởng; Q31, Q33.

### UC10: Người liên quan chưa hưởng (GĐ2, PT07)

- Mục tiêu: phát hiện hộ chăm sóc NKT đặc biệt nặng, NKT mang thai, đơn thân nghèo, thân nhân NCC đã mất chưa hưởng chế độ.
- Tác nhân: Engine, VT05.
- Luồng chính:
  1. Duyệt E06 và E03 quanh mỗi đối tượng.
  2. Áp BR-03, BR-11, BR-12, BR-23, BR-24, BR-26 để tính E31 cho người liên quan.
  3. So với E05.
  4. Tạo cảnh báo loại "bỏ sót".
- Tiêu chí chính: hộ chăm sóc NKT đặc biệt nặng không có E05 hỗ trợ chăm sóc (dữ liệu giả) thì có cảnh báo.
- Điều kiện: Q45, Q46; kết quả UC01.

### UC11: Chuyển đổi chế độ theo sự kiện vòng đời (GĐ2)

- Mục tiêu: tự phát hiện sự kiện và các chế độ phải thay đổi theo sự kiện đó.
- Tác nhân: Engine, VT05 xác nhận sự kiện.
- Luồng chính:
  1. So hai snapshot liên tiếp (T03) hoặc nhận sự kiện từ nguồn.
  2. Ghi E15 (mất, chuyển cư trú, qua mốc tuổi, sinh con, đổi giám định, đổi phân loại hộ).
  3. VT05 xác nhận hoặc bác.
  4. Engine tính lại E31 cho người và người liên quan.
  5. Tạo cảnh báo chuyển đổi chế độ (dừng chế độ cũ, phát sinh mai táng theo BR-10 hoặc BR-27, tuất theo BR-26).
- Quy tắc: BR-05, BR-06, BR-08, BR-10, BR-11, BR-22, BR-23, BR-26, BR-27, BR-28.
- Tiêu chí chính: NCC mất (dữ liệu giả) sinh hai cảnh báo: dừng trợ cấp, phát sinh mai táng cho người tổ chức; thân nhân đủ điều kiện có cảnh báo hưởng tuất.
- Điều kiện: T03 giữ lịch sử; Q47; nguồn trả về người đi khai tử.

### UC12: Dự toán ngân sách và mô phỏng (GĐ2, PT06, PT08, DB04)

- Mục tiêu: tổng chi theo xã, tỉnh, tách khoản; mô phỏng khi mức chuẩn hoặc hệ số thay đổi.
- Tác nhân: VT06, VT07.
- Luồng chính:
  1. Chọn kỳ và địa bàn.
  2. Tổng E31 chính thức, tách năm khoản (trợ cấp trực tiếp, kinh phí chăm sóc, mai táng, tuất, chính sách theo hộ).
  3. VT07 sao cấu hình thành bản nháp, đổi tham số.
  4. Engine chạy E32 với kịch bản "mô phỏng".
  5. So các phương án.
- Quy tắc: BR-01, BR-10, BR-12, BR-13, BR-20, BR-21, BR-27, BR-40.
- Tiêu chí chính: kết quả mô phỏng không ghi vào kết quả chính thức.
- Điều kiện: Q44 (bên mình có xây chức năng chi trả không), Q58.

### UC13: Danh sách dễ tổn thương khi khẩn cấp (GĐ1b, KT02)

- Mục tiêu: lập nhanh danh sách người cần ưu tiên khi thiên tai tại một địa bàn, kèm người chăm sóc.
- Tác nhân: VT05.
- Luồng chính:
  1. Chọn địa bàn và ngày chốt.
  2. Lọc NKT nặng, NCT neo đơn, trẻ nhỏ hộ nghèo (BR-15, BR-51).
  3. Gắn người chăm sóc và liên hệ (E06).
  4. Xếp người không có người chăm sóc lên đầu.
  5. Lưu danh sách kèm tiêu chí, ngày chốt, người lập.
  6. Xuất file.
- Tiêu chí chính: người không có E06 chăm sóc nằm đầu danh sách.
- Điều kiện: khách xác nhận nhu cầu (UC này không có trong PL III); quyền xuất danh sách cá nhân (T10).

### UC14: Bản đồ mật độ đối tượng (GĐ2, PT04)

- Mục tiêu: mật độ theo xã, tỉnh, theo diện; chỉ số người cần chăm sóc chưa có người chăm sóc.
- Luồng chính:
  1. Tính số người theo địa bàn (BR-50, BR-51).
  2. Chia cho diện tích hoặc dân số nếu có mẫu số.
  3. Vẽ bản đồ.
- Tiêu chí chính: mẫu số hiển thị hoặc xem được; xã chưa rõ ranh giới ghi riêng.
- Điều kiện: ranh giới hành chính sau sắp xếp 2025; nguồn dân số làm mẫu số.

### UC15: Mô phỏng chuẩn nghèo 2027 theo hộ (GĐ3)

- Mục tiêu: chạy chuẩn NĐ 351/2025 trên dữ liệu hộ, ra hộ rơi vào hoặc thoát nghèo và số thành viên bị ảnh hưởng.
- Quy tắc: BR-42.
- Điều kiện: Q27 (ngoài phạm vi nếu chỉ làm NCC); có dữ liệu thu nhập và chiều thiếu hụt (E14).

### UC16: Phân tích liên ngành (GĐ3)

- Mục tiêu: trẻ hộ nghèo không đi học, đối tượng chưa có thẻ BHYT.
- Điều kiện: có nguồn giáo dục, y tế ngoài 7 nguồn. Chưa có BR.

### UC17: Đánh giá hiệu quả chính sách (GĐ3, PT05)

- Mục tiêu: theo dõi hộ, người qua nhiều kỳ: thoát nghèo bền vững, tái nghèo.
- Quy tắc: BR-40, BR-42.
- Điều kiện: T03 giữ lịch sử ít nhất hai kỳ rà soát; Q51.

### UC18: Dự báo và quy hoạch nguồn lực (GĐ3)

- Mục tiêu: nhu cầu cơ sở bảo trợ xã hội, cán bộ.
- Điều kiện: nhóm C (E24, E25) theo Q27; lịch sử nhiều kỳ. Chưa có BR.

### UC19: API cung cấp dữ liệu (GĐ2, KT04)

- Mục tiêu: hệ thống chi trả, dịch vụ công tra cứu hoặc xác thực diện, vai trò, quan hệ.
- Tác nhân: hệ thống ngoài được cấp quyền.
- Luồng chính:
  1. Hệ thống ngoài gửi yêu cầu kèm mục đích.
  2. Kiểm quyền và phạm vi trường (T10).
  3. Trả kết quả từ E01, E04, E05, E06.
  4. Ghi nhật ký cung cấp.
- Tiêu chí chính: trường ngoài phạm vi được duyệt không xuất hiện trong kết quả.
- Điều kiện: danh mục bên nhận và trường được cung cấp (Q35, Q44).

### UC20 (đề xuất): Xử lý cảnh báo và theo dõi xác minh (GĐ2, KT03)

- Mục tiêu: cán bộ xác minh và ghi kết quả cho các cảnh báo do UC06 đến UC11 sinh ra.
- Tác nhân: VT05, VT06; người quản lý theo dõi.
- Luồng chính:
  1. Nhận cảnh báo theo địa bàn.
  2. Phân công.
  3. Ghi kết quả và bằng chứng.
  4. Chuyển trạng thái theo sơ đồ 6.7 (mới, đang xác minh, xác nhận đúng, cảnh báo sai, đã xử lý).
  5. Báo cáo tiến độ.
- Tiêu chí chính: chạy lại engine không ghi đè kết quả xử lý (tài liệu 007 mục 3.5).
- Điều kiện: Q35 (lưu ở module mình hay trả về nguồn), Q43 (quy trình thực tế).


## Phần C. Đặc tả task nền tảng

Task nền tảng không có tác nhân nghiệp vụ, nên dùng khung rút gọn: phạm vi, đầu ra, tiêu chí hoàn thành.

| Mã | Phạm vi | Đầu ra | Tiêu chí hoàn thành |
|---|---|---|---|
| T01 Khảo sát và BA | Toàn module; 40 câu ưu tiên Cao; bản đồ nguồn; chốt phạm vi demo | Biên bản, checklist cập nhật, backlog phân kỳ | Có biên bản xác nhận phạm vi; Q27, Q28, Q30 có câu trả lời |
| T02 Tích hợp 7 nguồn | Đợt 1: một luồng đại diện. Các luồng khác: danh mục giao tiếp | Đặc tả TH01, TH03; mapping nguồn và đích | Đối soát số bản ghi nhận, hợp lệ, lỗi khớp; chạy lại cùng đợt không sinh trùng; kiểm đủ thêm, sửa, hủy (báo cáo 003 mục 3) |
| T03 Staging và lịch sử | Snapshot theo lần đồng bộ, mã bản chụp | Quy định lưu lịch sử | So được hai snapshot liên tiếp của một người; E32 tham chiếu được mã bản chụp |
| T04 Danh mục dùng chung | Diện, mức độ khuyết tật, loại quan hệ (các loại thân nhân theo BR-23), chế độ E20, vai trò | Từ điển danh mục, bảng chuyển mã từng nguồn | Mọi mã ở nguồn đại diện chuyển được, hoặc nằm trong danh sách "không chuyển được" |
| T05 Ánh xạ địa giới | Mã tỉnh, xã trước và sau QĐ 19/2025 | Bảng ánh xạ E13 có ngày áp dụng | Mã cũ tra ra mã mới đúng theo ngày; mã không ánh xạ được được đếm ở UC01 |
| T06 Ghép định danh | Khóa số định danh; ghép mờ khi thiếu; VT02 duyệt gộp, tách | Đặc tả quy tắc ghép, ngưỡng tin cậy | Trên mẫu có báo cáo tỷ lệ ghép và số ghép mờ chờ duyệt; không tự gộp bản ghi ghép mờ |
| T07 Mô hình hồ sơ và quan hệ | E01 đến E32, 3 vai trò của HƯỞNG CHẾ ĐỘ, quan hệ người với người | Mô hình đã duyệt, sơ đồ UML cập nhật | Bên giao việc duyệt; Q31 đến Q37, Q50 đến Q52 đã trả lời hoặc ghi giả định có người chịu trách nhiệm |
| T08 Ghép hộ | Hộ cư trú, hộ rà soát nghèo, chủ hộ, thành viên theo hiệu lực | Đặc tả ghép hộ | Một người thuộc hộ cư trú và hộ rà soát khác nhau được giữ cả hai liên kết |
| T09 Bộ quy tắc chính sách | 30 BR, tham số theo kỳ, 4 BR đề xuất; soạn và duyệt phiên bản (VT03, VT04) | Danh mục BR đã duyệt, bảng tham số | Mọi TC-BR ở tài liệu 011 mục 5 có kết quả kỳ vọng; đổi mức chuẩn không phải sửa mã |
| T10 Phân quyền, che, nhật ký | Vai trò × địa bàn; trường che; nhật ký tra cứu | Ma trận phân quyền | Mỗi UC có dòng quyền trong ma trận; mọi lần tra cứu cá nhân có nhật ký |
| T11 Kiểm thử, UAT | Bộ dữ liệu giả, kết quả kỳ vọng, kịch bản UAT | Test case từ TC-UCxx, TC-BRxx | Mọi TC trong đặc tả có ca kiểm thử; UAT có biên bản |


## Tự rà

| Mục kiểm | Kết quả |
|---|---|
| UC ở trạng thái "Giả định" có cờ ở đầu | Có: cờ chung ở đầu tài liệu và dòng trạng thái của từng UC |
| Mọi BR có mã | Có; BR-50 đến BR-53 đã vào danh mục 011 mục 3.4, trạng thái Dự thảo |
| Mỗi BR mà UC phần A dùng có ít nhất 1 TC | Có (xem cột "BR/luồng kiểm" ở mục 11 của từng UC) |
| Mỗi luồng ngoại lệ ở phần A có 1 TC | Có |
| Thực thể đều có trong mô hình | Có; riêng nhật ký tra cứu thuộc nhóm D, chưa có sơ đồ lớp |
| Ô mẫu `<...>` còn sót | Không |

## Việc tiếp theo

1. Đã làm 27/10/2026: BR-50 đến BR-53 vào tài liệu 011; Q59 vào Checklist họp.
2. Sau buổi khảo sát: viết đặc tả đầy đủ T02 (một luồng), T06, rồi hoàn thiện UC01, UC02 theo câu trả lời.
