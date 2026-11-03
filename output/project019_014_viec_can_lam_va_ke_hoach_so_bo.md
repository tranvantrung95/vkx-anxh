# Việc cần làm theo từng Task và UC, kế hoạch và danh sách task sơ bộ

> Bản nháp dựa trên giả định, chưa được bên giao việc xác nhận. Ngày lập: 27/10/2026. Toàn bộ 36 task và UC trong sheet "Task & Usecase" đang ở trạng thái "Giả định"; 59 câu hỏi trong sheet "Checklist họp" đều "Chưa hỏi", 40 câu trong đó ưu tiên Cao.

| Phiên bản | Ngày | Người sửa | Nội dung thay đổi |
|---|---|---|---|
| 0.1 | 27/10/2026 | BA | Tạo mới |
| 0.2 | 27/10/2026 | BA | Thêm đầu mục việc cho T12 đến T16 và UC20 ở mục 3; cập nhật số câu hỏi, số task và UC, số BR; ghi mức chi tiết theo chỉ đạo của bên giao việc |
| 0.3 | 28/10/2026 | BA | Đồng bộ: BA-01 tính tới Q59 |

Mức chi tiết của giai đoạn này (anh Hoàng Nam Dương, trao đổi 27/10/2026 lúc 11:57 đến 12:01): từ các phân tích rời rạc đã có, xác định mỗi task và UC cần làm những gì, lên kế hoạch và danh sách task sơ bộ, **gen ra các đầu mục trước**. Đặc tả ngắn gọn thì làm được; đặc tả chi tiết để khi có thông tin cụ thể mới làm cho đỡ mất công. Tài liệu này là phần đầu mục đó.

Đặc tả sơ bộ của từng task và UC nằm ở tài liệu đi kèm `output/project019_015_dac_ta_so_bo_task_uc.md`. Phần A của 015 (5 UC viết đầy đủ) là bản thử, không mở rộng thêm cho tới khi có biên bản khảo sát.

## 1. Nguồn đã gộp

Các phân tích trước được làm rời theo từng câu hỏi. Tài liệu này gộp lại theo đơn vị task và UC.

| Tài liệu | Nội dung lấy sang |
|---|---|
| `work/project019_005_checklist_hop_dang_cap_nhat.xlsx` | Sheet Task & Usecase (36 dòng từ bản 0.2, giai đoạn, phụ thuộc), Lộ trình, Checklist họp (Q1 đến Q59), Mô hình dữ liệu (22 thực thể), Nguồn thực thể (vai trò VT01 đến VT07), UC – Thực thể – UML |
| `output/project019_003_*` | Mã TH01 đến TH04, PT01 đến PT10, DB01 đến DB05, KT01 đến KT04; demo 15/11; công sức BA 9 đến 15 ngày công |
| `output/project019_007_*` | Thực thể E01 đến E32, ma trận thực thể × UC (mục 4.2, 4.4), sơ đồ UML 6.1 đến 6.8 |
| `output/project019_009_*` | Nhãn căn cứ của từng task và UC, 9 mục thiếu T-THIẾU-01 đến 09 |
| `output/project019_010_*`, `011_*` | 34 quy tắc: 30 BR từ BR-01 đến BR-42 và 4 BR dự thảo BR-50 đến BR-53; tham số theo kỳ, kịch bản kiểm thử mức quy tắc |

## 2. Hai hệ mã cần thống nhất

Sheet Excel dùng mã T và UC. Báo cáo 003 gửi VNPT-IT dùng mã TH, PT, DB, KT. Hai hệ mã mô tả cùng một phạm vi nhưng cắt khác nhau. Đề xuất giữ mã T và UC làm mã gốc cho đặc tả, ghi mã 003 làm mã tham chiếu.

| Mã 003 | Tên trong 003 | T, UC tương ứng | Ghi chú |
|---|---|---|---|
| TH01 | Tiếp nhận dữ liệu nguồn | T02 | |
| TH02 | Chuẩn hóa và ánh xạ | T04, T05, T06 | |
| TH03 | Nạp và cập nhật dữ liệu | T02, T03 | |
| TH04 | Đối soát và xử lý lỗi | T02, UC01 | Phần xử lý lỗi chưa có UC riêng |
| PT01, DB01 | Tổng hợp hiện trạng | UC02 | Luồng demo 15/11 |
| PT02 đến PT04, DB02 | Cơ cấu, giao thoa, so sánh địa bàn | UC02, UC06 (giao thoa diện), UC14 | |
| PT05, DB03 | Biến động | UC02 (chiều thời gian), UC17 | Cần T03 giữ lịch sử |
| PT06, DB04 | Thực hiện hỗ trợ | UC12 (phần thực chi) | Cần dữ liệu chi trả E07 |
| PT07, DB04 | Độ bao phủ | UC09, UC10 | |
| PT08, DB04 | Nguồn lực theo kịch bản | UC12 | |
| PT09, DB05 | Chất lượng, độ phủ | UC01 | |
| PT10 | Phân tích tùy chọn, báo cáo | UC03 | |
| KT01 | Tra cứu hồ sơ người, hộ | UC04, UC05 | |
| KT02 | Lập danh sách tác nghiệp | UC13, danh sách từ UC09, UC10 | |
| KT03 | Theo dõi xác minh | Không có | Đề xuất UC20 (mục 4) |
| KT04 | Cung cấp tập dữ liệu | UC19 | |

Chỗ lệch giữa hai tài liệu: báo cáo 003 đặt DB01 vào demo 15/11, sheet Task & Usecase xếp UC02 vào GĐ1b (30/11). Kế hoạch ở mục 5 tách UC02 thành hai phần: phần DB01 trên dữ liệu mẫu vào GĐ1a, phần DB02 và DB03 ở GĐ1b. Cần bên giao việc chốt (Q22).

## 3. Mỗi task và UC cần làm gì

Cột "Mức" cho biết BA viết đặc tả đến đâu được với thông tin hiện có:

- **M1**: logic đã có căn cứ văn bản (BR đã đối chiếu), đặc tả đủ chi tiết được ngay, chỉ chờ xác nhận nguồn dữ liệu.
- **M2**: viết được luồng, màn hình và chỉ tiêu; chỗ phụ thuộc dữ liệu ghi thành giả định.
- **M3**: chưa viết sâu được, vì còn chờ quyết định phạm vi, hạ tầng hoặc biểu mẫu.

### 3.1. Task nền tảng

| Mã | Việc BA | Việc phát triển, kiểm thử | Bị chặn bởi | Đầu ra bàn giao | Mức |
|---|---|---|---|---|---|
| T01 | Chạy buổi khảo sát theo các câu ưu tiên Cao; lập bản đồ nguồn, danh mục giao tiếp nguồn và đích; phân 7 nguồn theo cá nhân hay hộ, có quan hệ người với người, có chi trả không; biên bản chốt phạm vi | Không | Q12, Q20, Q21, Q27, Q28, Q30 | Biên bản họp, bản đồ nguồn, backlog phân kỳ | M2 |
| T02 | Đặc tả hành vi tích hợp cho một luồng đại diện: lịch, kiểu nạp, nhận biết thay đổi, xử lý lỗi, chạy lại không sinh trùng; tiêu chí đối soát số bản ghi | Viết connector, lịch đồng bộ, retry, log; kiểm thử thêm, sửa, hủy, chạy lại | Q12, Q13, Q14, Q28, Q37 | Đặc tả luồng TH01, TH03; mapping nguồn và đích | M3 |
| T03 | Chốt mức lịch sử cần giữ (snapshot mỗi lần đồng bộ hay chỉ phần thay đổi), thời gian lưu | Bảng staging, snapshot, mã bản chụp cho E32 | Q13, Q17, Q54 | Quy định lưu lịch sử | M3 |
| T04 | Lập danh mục dùng chung (diện, mức độ khuyết tật, loại quan hệ, chế độ E20) và bảng chuyển mã theo từng nguồn | Bảng danh mục, chức năng quản lý danh mục | Q15, Q45 | Từ điển danh mục, bảng chuyển mã | M3 |
| T05 | Lập quy tắc ánh xạ địa bàn cũ sang mới theo QĐ 19/2025, xử lý mã không ánh xạ được | Bảng E13 ánh xạ, hàm tra mã theo ngày | Danh mục địa bàn của nguồn | Bảng ánh xạ, kịch bản kiểm thử | M2 |
| T06 | Quy tắc ghép định danh: khóa chính, ghép mờ, ngưỡng tin cậy, luồng duyệt gộp và tách (VT02); xử lý người không có số định danh | Thuật toán ghép, màn hình duyệt ghép mờ | Q34, Q55 | Đặc tả ghép định danh, kết quả thử trên mẫu | M2 |
| T07 | Chốt mô hình lõi E01 đến E32 với bên giao việc; lấy câu trả lời Q31 đến Q37, Q50 đến Q52; cập nhật sơ đồ UML | Thiết kế CSDL vật lý từ mô hình khái niệm | Q31 đến Q37, Q50 đến Q52 | Mô hình dữ liệu đã duyệt (khóa trước khi viết UC) | M2 |
| T08 | Quy tắc ghép hộ cư trú với hộ rà soát nghèo; xác định chủ hộ, hiệu lực thành viên | Bảng E02, E03, E14; hàm đối chiếu hộ | Q51 | Đặc tả ghép hộ | M2 |
| T09 | Hoàn thiện 30 BR và tham số theo kỳ; xác nhận 6 BR "Chờ đối chiếu"; quy trình soạn, duyệt, phiên bản cấu hình (VT03, VT04) | Engine tính E31, E32; màn hình cấu hình E20 đến E23 | Q27, Q30, Q53 | Danh mục BR đã duyệt, bảng tham số | M1 |
| T10 | Ma trận quyền theo vai trò và địa bàn; danh sách trường che; quy định nhật ký tra cứu theo Luật 91/2025 | Dùng cơ chế phân quyền có sẵn; ghi nhật ký | Q8, Q10, Q56 | Ma trận phân quyền | M3 |
| T11 | Bộ dữ liệu giả và kết quả kỳ vọng cho UAT; kịch bản kiểm thử từ TC-UCxx, TC-BRxx | Kiểm thử tích hợp, hiệu năng; tài liệu HDSD | Q18, Q19 | Bộ test case, kịch bản UAT | M3 |
| T12 | Kiểm kê hệ thống hiện hữu (bảng, khối lượng, lịch sử); quy tắc chuyển sang E01, E05, E07, E09 và giữ dấu vết ở E17; tiêu chí đối soát trước và sau chuyển đổi | Script chuyển đổi, báo cáo đối soát | Q38; tài liệu hệ thống hiện hữu | Phương án chuyển đổi, bảng ánh xạ | M3 |
| T13 | Quy tắc ghi khoản truy lĩnh, truy thu gắn với kỳ hưởng gốc; kịch bản kỳ 07 đến 09/2026 | Trường loại khoản và kỳ truy lĩnh ở E07; gộp theo BR-41 khi đối chiếu | Q32, Q39 | Quy tắc truy lĩnh, kịch bản kiểm thử | M2 |
| T14 | Bảng chọn bộ quy tắc theo ngày tiếp nhận hồ sơ (NĐ 335 Điều 33; PL 05/2026 Điều 2) | Phiên bản E23 theo ngày tiếp nhận | Q40, Q42 | Quy tắc chuyển tiếp | M2 |
| T15 | Quy tắc nhận biết chuyển nơi cư trú để không tính là chi trùng; thôi chi nơi cũ, hưởng nơi mới (BR-06) | Sự kiện chuyển cư trú E15; nối hai hồ sơ | Q41 | Quy tắc chuyển vùng, kịch bản kiểm thử | M1 |
| T16 | Danh sách tỉnh có mức chuẩn TGXH riêng và kỳ áp dụng | Tham số E22 phạm vi tỉnh | Q48 | Bảng tham số theo tỉnh | M1 |

### 3.2. Use case

| Mã | Việc BA | Việc phát triển, kiểm thử | Bị chặn bởi | BR dùng | Mức |
|---|---|---|---|---|---|
| UC01 | Định nghĩa các phép đo chất lượng theo khung đúng, đủ, sạch, sống; mẫu số từng phép đo; độ đầy đủ quan hệ; bố cục DB05 | Job profiling, DB05 | Q6, Q7, Q12 | BR-50 (đề xuất) | M2 |
| UC02 | Định nghĩa chỉ tiêu PT01 đến PT05; bộ lọc, drill-down; đặc tả DB01 đầy đủ, DB02 và DB03 dạng khung | Truy vấn tổng hợp, DB01 đến DB03, xuất Excel | Q16, Q22 | BR-50, BR-51 (đề xuất) | M2 |
| UC03 | Thu thập biểu mẫu bắt buộc; ánh xạ từng ô biểu mẫu tới chỉ tiêu UC02 | Mẫu báo cáo | Q16, Q19; biểu mẫu TT 18/2025 | Theo biểu mẫu | M3 |
| UC04 | Đặc tả hồ sơ 360° một người: các khối vai trò, quan hệ, quyền lợi; quyền xem và che | Màn hình tra cứu KT01 | Q20, Q31, Q34, Q56 | BR-23, BR-50, BR-52 | M2 |
| UC05 | Như UC04, áp cho hộ | Màn hình hồ sơ hộ | Q51, T08 | BR-42 | M2 |
| UC06 | Ma trận chồng lấn diện; tách logic TGXH (một mức cao nhất) và NCC (cộng dồn từ 01/01/2027) | Quy tắc engine, danh sách cảnh báo | Q32, Q52 | BR-01 đến BR-03, BR-15, BR-16, BR-25, BR-26 | M1 |
| UC07 | Kịch bản chi sai theo trạng thái; xử lý truy lĩnh; trạng thái sống "chưa xác định" | Quy tắc engine, cảnh báo, màn hình xác minh | Q32, Q39, Q47 | BR-05, BR-07, BR-08, BR-13, BR-20 đến BR-22, BR-28, BR-40, BR-41, BR-52 | M1 |
| UC08 | Kịch bản chi sai theo người chăm sóc; ngưỡng bất thường (chờ khách) | Quy tắc engine | Q46, Q27 (phạm vi có TGXH) | BR-09, BR-11 | M1 |
| UC09 | Xác định tập "đủ điều kiện" lấy từ đâu; trạng thái không chồng lấn của PT07 | Quy tắc engine, danh sách KT02 | Q31, Q33, nguồn danh sách đủ điều kiện | BR-01, BR-04, BR-14 đến BR-16 | M3 |
| UC10 | Kịch bản bỏ sót người liên quan: hộ chăm sóc, NKT mang thai, thân nhân hưởng tuất | Quy tắc engine | Q45, Q46 | BR-03, BR-11, BR-12, BR-23, BR-24, BR-26 | M1 |
| UC11 | Danh mục sự kiện, cách phát hiện (nguồn đẩy hay so snapshot), chế độ phát sinh và chấm dứt | Bộ phát hiện sự kiện E15, cảnh báo | Q47, T03 | BR-05, BR-06, BR-08, BR-10, BR-11, BR-22, BR-23, BR-26 đến BR-28 | M1 |
| UC12 | Cách tách khoản chi; kịch bản mô phỏng tham số | Engine mô phỏng, DB04 | Q44, Q58 | BR-01, BR-10, BR-12, BR-13, BR-20, BR-21, BR-27, BR-40 | M3 |
| UC13 | Tiêu chí nhóm dễ tổn thương, thứ tự ưu tiên; mẫu danh sách | Màn hình lập danh sách KT02 | Khách xác nhận nhu cầu | BR-15 | M2 |
| UC14 | Chỉ tiêu mật độ; nguồn ranh giới hành chính | Bản đồ | Ranh giới địa bàn sau sắp xếp | BR-06 | M2 |
| UC15 | Kịch bản chuẩn nghèo NĐ 351/2025 | Engine mô phỏng hộ | Q27 (ngoài phạm vi NCC), Q51 | BR-42 | M3 |
| UC16 | Xác định nguồn giáo dục, y tế | Phân tích liên ngành | Có nguồn ngoài 7 nguồn không | Chưa có | M3 |
| UC17 | Chỉ tiêu thoát nghèo bền vững, tái nghèo | Phân tích nhiều kỳ | T03, Q51 | BR-40, BR-42 | M3 |
| UC18 | Chỉ tiêu nhu cầu cơ sở, cán bộ | Dự báo | Nhóm C (Q27) | Chưa có | M3 |
| UC19 | Danh mục trường cung cấp, bên nhận, quy trình duyệt KT04 | API | Q35, Q44, T10 | Theo UC nguồn | M2 |
| UC20 | Vòng đời cảnh báo (sơ đồ 6.7); phân công theo địa bàn; kết quả và bằng chứng xác minh (KT03) | Màn hình xử lý cảnh báo; chạy lại engine không ghi đè phần người dùng nhập (R5) | Q35, Q43 | Theo UC sinh cảnh báo (UC06 đến UC11) | M2 |

Tổng 36 mục: M1 có 8 mục (T09, T15, T16, UC06, UC07, UC08, UC10, UC11), M2 có 15 mục, M3 có 13 mục. Bản 0.1 xếp mức cho 30 mục; 6 mục T12 đến T16, UC20 xếp mức ở bản 0.2.

Nhóm M1 là nhóm kiểm soát chi và bỏ sót, xếp ở GĐ1b và GĐ2. Nhóm của demo 15/11 (T02, T06, T07, UC01, UC02) chỉ ở M2 hoặc M3, vì phụ thuộc dữ liệu thực tế. Tuần này BA nên dồn sức vào câu hỏi dữ liệu, không dồn vào hoàn thiện quy tắc.

## 4. Việc chưa có trong danh sách task và UC

Lấy từ T-THIẾU-01 đến 09 (tài liệu 009) và KT03 (tài liệu 003). Mã T12 đến T16 và UC20 là đề xuất; ngày 27/10/2026 đã thêm vào sheet Task & Usecase (tô xanh lá, trạng thái Giả định). T12 chưa có giai đoạn nên chưa vào số đếm của sheet Lộ trình.

| Mã đề xuất | Nội dung | Lý do cần | Phụ thuộc |
|---|---|---|---|
| T12 | Chuyển đổi dữ liệu từ hệ thống hiện hữu | PL III mục 10, 11, 29, 108 ghi "Nâng cấp"; có thể là khối lượng lớn nhất | Q38 |
| T13 | Truy lĩnh, truy thu theo kỳ hưởng | Thiếu thì UC07 báo sai hàng loạt cho kỳ 07 đến 09/2026 (BR-13, BR-21, BR-41) | Q32, Q39 |
| T14 | Chuyển tiếp hồ sơ đang giải quyết | NĐ 335 Điều 33, PL 05/2026 Điều 2 (BR-14, BR-29) | Q40, Q42 |
| T15 | Chuyển nơi cư trú, di chuyển hồ sơ NCC giữa tỉnh | Bản ghi trùng giữa hai tỉnh bị UC07 hiểu nhầm thành chi trùng (BR-06) | Q41 |
| T16 | Mức chuẩn TGXH riêng theo tỉnh | NĐ 335 Điều 4 khoản 3; thiếu thì tính sai mức đúng | Q48 |
| UC20 | Xử lý cảnh báo và theo dõi xác minh (KT03) | Cảnh báo E16 có vòng đời (sơ đồ 6.7) và người xử lý VT05, VT06, nhưng chưa UC nào đặc tả màn hình và quy trình xử lý | Q35, Q43 |

Ba nhóm việc ngoài phân tích chưa đưa vào kế hoạch: thủ tục hành chính (PL III mục D), quy trình và biểu mẫu động, chi trả và quà tri ân (PL III mục H). Bên mình nhận phần nào chờ Q30 và Q44.

## 5. Kế hoạch sơ bộ

### 5.1. Các mốc

| Mốc | Ngày | Điều kiện đạt |
|---|---|---|
| M0 Khảo sát xong | 30/10/2026 | Biên bản chốt phạm vi; các câu ưu tiên Cao đã trả lời; chọn luồng đại diện và nhóm đối tượng cho demo |
| M1 Mô hình lõi đã duyệt | 04/11/2026 | T07 duyệt; Q31 đến Q37, Q50 đến Q52 có câu trả lời |
| M2 Đặc tả đợt 1 xong | 06/11/2026 | Đặc tả T02 (một luồng), T06, UC01, UC02 phần DB01 đủ để đội kỹ thuật ước lượng |
| M3 Demo | 15/11/2026 | Một luồng nguồn đã đối soát → chỉ tiêu PT01 → DB01 → xuất báo cáo; DB05 trên cùng luồng |
| M4 GĐ1b | 30/11/2026 (chờ xác nhận) | T08 đến T11; UC02 đầy đủ, UC04, UC06, UC07, UC13; UAT |
| M5 GĐ2, GĐ3 | Chưa có mốc | Xếp lại sau khi UC01 cho biết dữ liệu dùng được đến đâu |

### 5.2. Phân việc theo giai đoạn

| Giai đoạn | Task, UC | Ghi chú |
|---|---|---|
| Tuần khảo sát 27 đến 30/10 | T01 | Đang chạy; chậm một ngày so với lịch 003 (26 đến 30/10) |
| GĐ1a đến 15/11 | T02 (một luồng), T03, T04, T05, T06, T07, UC01, UC02 phần DB01 | T02, T06, T07 có độ phức tạp Cao. UC02 phần DB01 kéo lên theo 003 |
| GĐ1b đến 30/11 | T08, T09, T10, T11, UC02 (DB02, DB03), UC04, UC06, UC07, UC13 | UC07 cần T13 truy lĩnh nếu Q39 xác nhận đã chi truy lĩnh |
| GĐ2 | UC03, UC05, UC08 đến UC12, UC14, UC19, UC20, T13 đến T16 | UC08, UC10, UC11 chỉ cam kết khi UC01 xác nhận nguồn có quan hệ chăm sóc, thân nhân |
| GĐ3 | UC15 đến UC18 | UC15 ngoài phạm vi nếu Q27 chốt chỉ người có công |
| Chưa xếp | T12, PL III mục D, H | Chờ Q30, Q38, Q44 |

### 5.3. Đường găng

T01 → T07 → (T06, T02) → UC01 → UC02 phần DB01 → demo 15/11.

T07 nằm giữa đường găng vì mọi UC đọc thực thể của nó. Nếu mô hình lõi chưa duyệt trước 04/11, các bước sau chỉ còn khoảng 9 ngày làm việc trước demo. Phương án dự phòng: demo DB01 trên một nhóm đối tượng và một nguồn, chỉ dùng E01, E04, E13, E17 (không cần E05 đến E07).

## 6. Danh sách task sơ bộ của BA

Ước lượng tính theo ngày công BA, là giả định trước khảo sát. Việc phát triển và kiểm thử ước lượng riêng sau mốc M2. BA1 là BA đầu mối nghiệp vụ, BA2 là BA dữ liệu (cơ cấu theo 003).

| Mã | Việc | Thuộc | Người làm | Ngày công | Hạn | Phụ thuộc | Đầu ra |
|---|---|---|---|---|---|---|---|
| BA-01 | Họp khảo sát, hỏi 40 câu ưu tiên Cao trong Q1 đến Q59; ghi biên bản | T01 | BA1 | 1 | 28/10 | Lịch họp | Biên bản, checklist cập nhật |
| BA-02 | Kiểm kê 7 nguồn: trường, khóa, quan hệ, chi trả; chọn luồng đại diện | T01, T02 | BA2 | 1,5 | 29/10 | Quyền đọc (Q5, Q6) | Bản đồ nguồn |
| BA-03 | Chốt hai hệ mã (mục 2), phạm vi demo, xếp giai đoạn | T01 | BA1 | 0,5 | 30/10 | BA-01 | Biên bản phạm vi |
| BA-04 | Rà mô hình lõi với bên giao việc, chốt E05 và E31 (Q52), E09 và E14 (Q50, Q51); cập nhật sheet và UML | T07 | BA1, BA2 | 1,5 | 04/11 | BA-01 | Mô hình đã duyệt |
| BA-05 | Đặc tả luồng tích hợp đại diện và tiêu chí đối soát | T02, T03 | BA2 | 1,5 | 05/11 | BA-02 | Đặc tả TH01, TH03 |
| BA-06 | Đặc tả ghép định danh, thử trên mẫu | T06 | BA2 | 1 | 05/11 | BA-02, Q34 | Đặc tả T06, kết quả thử |
| BA-07 | Danh mục dùng chung, bảng chuyển mã, ánh xạ địa bàn | T04, T05 | BA2 | 1 | 06/11 | BA-02 | Từ điển danh mục |
| BA-08 | Đặc tả UC01 và DB05 | UC01 | BA2 | 1 | 06/11 | BA-05 | Đặc tả UC01 |
| BA-09 | Đặc tả UC02 phần DB01 và mẫu xuất PT10 | UC02 | BA1 | 1,5 | 06/11 | BA-04 | Đặc tả DB01, phác thảo màn hình |
| BA-10 | Bộ dữ liệu giả và kết quả kỳ vọng cho demo | T11 | BA2 | 1 | 10/11 | BA-08, BA-09 | Bộ mẫu kiểm thử |
| BA-11 | Hỗ trợ phát triển, nghiệm thu nội bộ bản demo | UC01, UC02 | BA1, BA2 | 1 | 15/11 | Bản dựng | Biên bản demo |
| BA-12 | Hoàn thiện 30 BR, xác nhận 6 BR "Chờ đối chiếu", thêm BR-50 đến BR-53 | T09 | BA1 | 1,5 | 18/11 | Q27, Q53 | Danh mục BR đã duyệt |
| BA-13 | Ma trận phân quyền, che dữ liệu, nhật ký | T10 | BA1 | 1 | 18/11 | Q56 | Ma trận quyền |
| BA-14 | Đặc tả ghép hộ | T08 | BA2 | 1 | 18/11 | Q51 | Đặc tả T08 |
| BA-15 | Đặc tả đầy đủ UC04, UC06, UC07, UC13; DB02, DB03 | UC02, UC04, UC06, UC07, UC13 | BA1, BA2 | 3 | 20/11 | BA-12, BA-13 | 4 đặc tả UC, khung DB02 và DB03 |
| BA-16 | Kịch bản UAT GĐ1b | T11 | BA2 | 1 | 25/11 | BA-15 | Kịch bản UAT |
| BA-17 | Xếp lại GĐ2, GĐ3 theo kết quả UC01; đặc tả khung UC20, T13 | Lộ trình | BA1 | 1 | 30/11 | BA-08 | Backlog GĐ2 |

Tổng BA: 21 ngày công đến 30/11, trong đó 12,5 ngày công đến demo 15/11 (BA-01 đến BA-11). Con số 12,5 vượt cận trên của kịch bản A (9 đến 12) và nằm trong khoảng 11 đến 15 của kịch bản B ở báo cáo 003. Hai BA làm song song thì mỗi người làm khoảng 6 đến 7 ngày. Khối lượng này vừa với lịch đặc tả từ 28/10 đến 06/11 và phần hỗ trợ đến 15/11.

## 7. Rủi ro chính

| Rủi ro | Ảnh hưởng | Cách giảm |
|---|---|---|
| Chưa có quyền đọc dữ liệu thật (Q5, Q6, Q7) | UC01, T06 chỉ dựa trên giả định; demo không có số liệu thật | Xin bản dump đã che (Q7); nếu không có, demo bằng dữ liệu giả và ghi rõ |
| Phạm vi chỉ người có công (Q27) | UC08, phần chăm sóc của UC10, UC13, UC15 mất căn cứ; BR-01 đến BR-16 không dùng | Hỏi Q27 đầu tiên trong buổi họp |
| Có hệ thống hiện hữu cần chuyển đổi (Q38) | Thêm T12, có thể vượt toàn bộ công sức đang ước | Hỏi Q38 cùng lúc với Q27 |
| Nguồn không có dữ liệu chi trả (Q32) | UC06 đến UC08 chỉ so được "đáng hưởng" với quyết định, không so được với thực chi | Hạ UC07 thành so với E05 nếu thiếu E07 |
| Mô hình lõi duyệt trễ | Đường găng demo vỡ | Phương án demo một nguồn, một nhóm (mục 5.3) |

## 8. Việc người dùng cần quyết

1. Dùng mã T và UC làm mã gốc, mã 003 làm tham chiếu (mục 2).
2. Kéo UC02 phần DB01 vào GĐ1a theo báo cáo 003.
3. Thêm T12 đến T16 và UC20 vào sheet Task & Usecase (đã làm 27/10/2026).
4. Nhận ước lượng BA 12,5 ngày công đến demo và 21 ngày công đến 30/11 làm số liệu sơ bộ.
