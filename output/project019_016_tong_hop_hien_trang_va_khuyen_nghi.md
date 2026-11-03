# Tổng hợp hiện trạng BA và khuyến nghị việc tiếp theo

Ngày lập: 27/10/2026. Người lập: BA project019. Tài liệu chỉ đọc nguồn, không sửa file nào khác trong dự án.

Cập nhật 28/10/2026: đồng bộ sau rà soát. File `project019_007_lich_su_thay_doi_chinh_sach_va_truong_du_lieu.md` đổi số thành **017**, mã VL-10 đến VL-13 của file đó đổi thành VL-18 đến VL-21. Mâu thuẫn 8, 9, 13, 14, 15, 16 ở mục 3.5 đã xử lý; ghi chú từng dòng. Bản sao lưu trước khi sửa: `tmp/sao_luu_dong_bo_20261028_134514_78792/`.

Ký hiệu nguồn dùng trong bảng:

- **XL-W** là `work/project019_005_checklist_hop_dang_cap_nhat.xlsx` (file làm việc, 12 sheet). Bản `output/project019_013_checklist_kem_so_do_uml.xlsx` (gọi là **XL-013**) có cùng 12 sheet, giá trị khớp 100% từng ô khi so ngày 27/10/2026, cộng thêm sheet "Sơ đồ UML".
- **XL-IN** là `input/Checklist_hop_ky_thuat_module_tich_hop_du_lieu.xlsx` (bản gốc, 7 sheet).
- **0xx** là `output/project019_0xx_*.md`.
- Số liệu trong tài liệu này đếm bằng script Python (openpyxl, regex) ngày 27/10/2026, không chép lại từ tài liệu cũ.

Nguồn đã đọc và nguồn chưa đọc trọn:

| Nguồn | Mức đọc |
|---|---|
| CLAUDE.md, README.md, `work/CHECKPOINT.md`, bộ nhớ vai trò BA | Đọc hết |
| 13 file .md trong `output/` | Đọc hết đề mục; đọc kỹ 011, 014, phần tóm tắt và việc cần làm của 002, 003, 004, 006, cả hai file 007, 009, 010, 012, 015; 008 chỉ đọc phần B |
| 2 file .docx (003, 012) | So chữ với bản .md: 003 lệch 1 từ (thẻ `br`), 012 khớp hết |
| XL-W, XL-013, XL-IN | Đọc mọi sheet; đếm theo cột trạng thái |
| `~/Workspace/NHAT_KY_VAP_NGA.md` | 12 mục PF gắn project019 (PF-098 đến PF-100, PF-102 đến PF-110) |
| 7 ảnh JPG Phụ lục III trong `input/` | **Chưa xem trực tiếp.** Dùng bản phân tích ở 004 mục 2 |
| Ảnh SVG, PNG sơ đồ UML | **Chưa xem lại hình.** Chỉ đếm file và ảnh nhúng |
| `tmp/` (bản sao lưu, bản render), `graphify-out/` | Không đọc nội dung; là bản trung gian |

## 1. Tóm tắt hiện trạng

1. Dự án đang ở **tuần khảo sát** (26 đến 30/10/2026, 003 mục 10), trước mốc M0 30/10 của 014 mục 5.1. Chưa có biên bản họp nào với khách hàng (009 mục 5).
2. Đã có bản dựng nghiệp vụ đầy đủ ở dạng giả định: 36 task và UC (XL-W, sheet Task & Usecase), 59 câu hỏi khảo sát (sheet Checklist họp), mô hình 22 thực thể (sheet Mô hình dữ liệu), 47 văn bản pháp lý (sheet Căn cứ pháp lý).
3. Bộ quy tắc chính sách là phần chắc nhất: 34 BR, trong đó 23 BR đã đối chiếu bản gốc Công báo hoặc VBHN (011 mục 3).
4. Đặc tả: 5 UC viết đầy đủ kèm 40 ca kiểm thử (015 phần A), 15 thẻ UC (015 phần B), khung 11 task (015 phần C); kế hoạch 17 việc BA, 21 ngày công đến 30/11 (014 mục 6).
5. **Chưa có mục nào được khách hàng xác nhận**: 59/59 câu hỏi "Chưa hỏi", 36/36 task và UC "Giả định", 0/36 dòng có ước lượng ngày công.
6. Hai câu hỏi lớn nhất chưa có lời đáp: phạm vi là người có công hay toàn bộ an sinh xã hội (Q27), và việc thật là xây module phân tích hay chuyển đổi hệ thống hiện có (Q38).

## 2. Kiểm kê sản phẩm BA

### 2.1. Tài liệu

| Tài liệu | Nội dung chính | Mức hoàn thiện | Nguồn |
|---|---|---|---|
| 002 Bài toán BA dữ liệu an sinh | Phát biểu bài toán, phạm vi BA, 10 PT, 5 DB, 4 KT, câu hỏi khảo sát ban đầu | Dự thảo 22/10, phần 11, 12 cập nhật sau phản hồi | 002 dòng 3, mục 11, 12 |
| 003 Báo cáo use case và nhân sự BA (.md, .docx) | Đề xuất cho ban giám đốc XVK: 10 PT trên 5 DB, KT01 đến KT04, demo DB01 ngày 15/11, công BA 9 đến 12 hoặc 11 đến 15 ngày công, 2 BA cộng 1 dự phòng | Đã gửi bản trình; QA render ở `tmp/project019_003_render_dashboard_scope_checked` (CHECKPOINT) | 003 mục 1, 8, 11 |
| 004 Phân tích input | Đối chiếu Phụ lục III với Excel; lệch phạm vi; "7 nguồn API" gộp nguồn và đích; PL III thiếu mục F, E.IV | Xong; VL-01, VL-03 đã áp; VL-02, VL-04, VL-05 còn mở | 004 mục 4, 8 |
| 006 Rà soát căn cứ pháp lý | 9 dòng cần sửa, 16 dòng thêm, hai mốc áp dụng trong một văn bản | Đã áp vào sheet (sheet có cột "Áp dụng từ" và 47 văn bản) | 006 mục 1, 5; XL-W sheet Căn cứ pháp lý |
| 017 Lịch sử thay đổi chính sách và trường dữ liệu (trước 28/10/2026 đánh số 007) | Mức chuẩn NCC, TGXH, hưu trí, lương cơ sở, chuẩn nghèo qua các kỳ; trường cần thiết kế cho T09 | Xong phần tra cứu (mức TV, BC); VL-19, VL-21 còn mở; VL-20 đã thành Q32, Q39 | 017 mục 1, 4 |
| 007 Rà soát mô hình dữ liệu | Thực thể nhóm A đến D, ba lớp dữ liệu, ai thêm hoặc sửa, ma trận thực thể × UC, 8 sơ đồ UML 6.1 đến 6.8 kèm sơ đồ 09 | Cập nhật tới 27/10; VL-10, VL-14 đến VL-17 chờ khách | 007 mục 1, 6, 7 |
| 008 System prompt agent BA | Prompt và cấu hình harness cho agent BA chạy tự động | Xong | 008 phần A, B |
| 009 Kết quả agent BA | Phân loại bản dựng (CÓ CĂN CỨ, GIẢ ĐỊNH, THIẾU), bản đồ phạm vi, 23 câu ưu tiên P1 đến P3, ba phương án đợt 1 | Bước 1 đến 4, 6, 7 xong; bước 5 bị chặn vì chưa có biên bản | 009 mục 1.7, 4, 5, 7 |
| 010 Căn cứ pháp lý và tham số theo kỳ | Đối chiếu bản gốc 8 văn bản; NĐ 335 chuyển tiếp ở Điều 33; NĐ 63/2024 đã sửa bởi NĐ 301/2026 | Xong; còn 11 nhóm con số "chưa xác minh" | 010 mục 2, 6 |
| 011 Đặc tả quy tắc và truy vết | Tham số P-, 34 BR, từ điển E21 đến E23, 27 kịch bản TC-BR, ma trận văn bản → BR → UC → TC | Bản đầu của danh mục BR; chưa chép sang `work/` theo quy ước skill | 011 mục 1, 3, 5, 6 |
| 012 Profile BA gửi VNPT-IT (.md, .docx) | Thư trả lời nháp, cơ cấu 2+1 BA, mẫu profile | Nháp; thiếu thông tin thật của BA, người nhận, người ký | 012 mục 6 |
| 014 Việc cần làm và kế hoạch sơ bộ | Đối chiếu mã 003 với T/UC, mức sẵn sàng M1 đến M3, mốc M0 đến M5, 17 việc BA-01 đến BA-17 | Bản 0.3, chờ người dùng quyết 4 điểm ở mục 8 | 014 mục 2, 3, 5, 6, 8 |
| 015 Đặc tả sơ bộ task và UC | Phần A: UC01, UC02 (DB01), UC04, UC06, UC07; phần B: 15 thẻ; phần C: T01 đến T11; BR-50 đến BR-53 | Bản 0.1; tự rà đạt; T12 đến T16 chưa có đặc tả | 015 mục 0, Tự rà |
| XL-W (file làm việc) | 12 sheet, xem 2.2 | Bản làm việc chính | `work/` |
| XL-013 | Bản xuất của XL-W kèm sheet "Sơ đồ UML" 9 ảnh | Đồng bộ với XL-W ngày 27/10 | `output/` |
| Bộ skill BA | 4 skill `ba-*`, mẫu biên bản, BR, ma trận truy vết, script cập nhật checklist | Đã kiểm 23/10 (CHECKPOINT) | `.claude/skills/ba-*` |

Số thứ tự 001 và 005 không có trong `output/`: 001 là bản sao lưu skill trong `work/`, 005 là file làm việc XL-W.

### 2.2. Các sheet Excel và số liệu đếm được

| Sheet (XL-W) | Đếm được | Trạng thái |
|---|---|---|
| Checklist họp | 59 câu (Q1 đến Q59), 12 nhóm; ưu tiên Cao 40, Trung bình 18, Thấp 1 | 59/59 "Chưa hỏi"; cột Trả lời và Người phụ trách trống 59/59 |
| Task & Usecase | 36 dòng: T01 đến T16 (16), UC01 đến UC20 (20). Giai đoạn: GĐ1a 8, GĐ1b 9, GĐ2 14, GĐ3 4, chưa xếp 1 (T12). Độ phức tạp: Cao 15, Trung bình 18, Thấp 3 | 36/36 "Giả định"; cột Ước lượng trống 36/36 |
| Lộ trình | 4 giai đoạn, công thức đếm tới dòng 51 | Tổng ngày công bằng 0 vì cột Ước lượng trống; T12 không vào số đếm |
| Ứng dụng dữ liệu | 10 nhóm N0 đến N9 | Cột "Đã đánh giá Phù hợp" bằng 0 |
| UC tham khảo PL III | 153 mục Phụ lục III gán vào N0 đến N9 | 153/153 "Chưa đánh giá" |
| Mô hình dữ liệu | 22 thực thể (E01 đến E07, E09 đến E17, E20 đến E23, E31, E32) | Giả định; cột Lớp dữ liệu và Ai thêm hoặc sửa chờ Q50 đến Q58 |
| UC – Thực thể – UML | 36 dòng, khớp 36 task và UC | Lấy từ ma trận 007 mục 4.2, 4.4 |
| Mô hình hóa thực thể | 1 ảnh UML cấu trúc 22 thực thể, bảng 22 dòng | Giả định |
| Căn cứ pháp lý | 47 văn bản (số # tới 49, đã xóa #24, #25). Phạm vi: Chung 20, Mở rộng TGXH và hộ nghèo 15, Lõi người có công 12 | Ghi chú kiểm tra từng dòng; nhiều dòng còn "chưa đọc toàn văn" |
| Tham số NCC | Mức chuẩn, mức hưởng theo kỳ | Mức tin cậy TV, chưa so bản ký số (010 mục 6) |
| Tham số TGXH | Mức chuẩn, hệ số theo kỳ | 18 chỗ ghi "chưa xác minh" trong sheet |
| Nguồn thực thể | Khối A (22 thực thể, 3 lớp), B (12 chuỗi ảnh hưởng), C (10 quy tắc chạy lại R1 đến R10), D (8 điều chỉnh D1 đến D8, đã áp), E (ai thêm hoặc sửa), F (10 tác nhân, 7 vai trò VT01 đến VT07) | Giả định, chờ Q50 đến Q58 |

### 2.3. Đặc tả, quy tắc, thực thể và sơ đồ

| Hạng mục | Số lượng | Nguồn |
|---|---|---|
| BR | 34: Đã đối chiếu 23 (BR-01 đến BR-16, BR-23 đến BR-29); Chờ đối chiếu 6 (BR-20, BR-21, BR-22, BR-30, BR-41, BR-42); BR-40 đối chiếu cho TGXH, chờ cho NCC; Dự thảo 4 (BR-50 đến BR-53) | 011 mục 3, dòng tổng hợp |
| Kịch bản mức quy tắc | 27 mã TC-BR | 011 mục 5 |
| Ca kiểm thử mức UC | 40 mã TC-UC: UC01 6, UC02 7, UC04 7, UC06 9, UC07 11 | 015 phần A |
| UC có đặc tả đầy đủ | 5 trên 20 | 015 phần A |
| UC có thẻ đặc tả | 15 (14 UC cộng UC20) | 015 phần B |
| Task có khung đặc tả | 11 (T01 đến T11); T12 đến T16 chưa có | 015 phần C |
| Mức sẵn sàng | M1 8, M2 15, M3 13 trên 36 dòng (014 bản 0.2; bản 0.1 chỉ xếp 30 dòng) | 014 mục 3 |
| Thực thể trong sheet | 22 (nhóm A sửa và nhóm B) | XL-W sheet Mô hình dữ liệu |
| Thực thể chỉ có trong 007 | 7 nhóm C (E24 đến E30, chờ Q27); 3 nhóm D chưa có mã | 007 mục 3.3, 3.4 |
| Mã thực thể bỏ trống | E08 (đã tách thành E20 đến E23), E18, E19 (để dành) | 007 mục 3.1, 3.2 |
| Sơ đồ UML | 9 sơ đồ dùng trong 007 (6.1 đến 6.8 và sơ đồ 09); 9 SVG ở `output/project019_007_uml/` và `baoyu/`; thêm 8 bản trùng ở `kieu_b/` và 6 mẫu ở `mau/`; 8 file Mermaid ở `work/project019_007_uml/` | 007 mục 6; liệt kê thư mục |
| Ảnh sơ đồ trong Excel | XL-013 sheet "Sơ đồ UML" 9 ảnh; sheet "Mô hình hóa thực thể" 1 ảnh (cả XL-W và XL-013) | Đếm ảnh nhúng bằng openpyxl |
| Việc BA đã lên kế hoạch | 17 việc, 21 ngày công đến 30/11, 12,5 ngày công đến demo | 014 mục 6 |

### 2.4. Phân loại: đã chốt, giả định, câu hỏi mở

| Loại | Nội dung | Nguồn |
|---|---|---|
| Đã chốt với khách hàng (có biên bản) | **Không có mục nào.** Không tìm thấy biên bản khảo sát trong `input/`, `output/`, `work/` | 009 mục 5; tìm tên file ngày 27/10 |
| Chỉ đạo nội bộ của bên giao việc | Anh Hoàng Nam Dương, 27/10/2026: giai đoạn này chỉ lập đầu mục việc cần làm cho từng task và UC, kế hoạch và task sơ bộ; đặc tả chi tiết làm khi có thông tin cụ thể | Trao đổi người dùng dán vào phiên; 014 bản 0.2 |
| Do người dùng truyền đạt lại, chưa có văn bản của khách hàng | VNPT-IT có kho dữ liệu; đề nghị hợp tác trọn module từ BA tới test; phần 1 gồm cả biểu đồ, dashboard; stack Angular, Spring Boot, Oracle; mốc 15/11; tuần khảo sát 26 đến 30/10 | 002 mục 1, 11, 12; 003 mục 1, 12 |
| Có trong tài liệu khách hàng (dự thảo) | Chủ đầu tư dự kiến Cục Người có công, nhà thầu Liên danh VNPT-VKX; 153 mục yêu cầu Phụ lục III | 009 mục 1.2 G1; 004 mục 2 |
| Có căn cứ văn bản pháp luật, không cần khách xác nhận | 23 BR "Đã đối chiếu" và tham số mức CB | 011 mục 2, 3 |
| Giả định của BA | Phạm vi toàn ASXH (G2); 7 nguồn API (G5); mốc GĐ1b 30/11 (G7); toàn bộ 36 task và UC; mô hình 22 thực thể, ba lớp dữ liệu, 7 vai trò VT01 đến VT07; 4 BR Dự thảo; ước lượng công BA | 009 mục 1.2; XL-W; 011 mục 3.4; 014 mục 6 |
| Câu hỏi mở | 59 câu Q1 đến Q59; 23 câu P1 đến P3 (đã gộp vào Q38 đến Q49); 11 tài liệu cần xin | XL-W sheet Checklist họp; 009 mục 4.2, 4.3 |

## 3. Khoảng trống và rủi ro

### 3.1. UC và task chưa có đặc tả

| Mục | Hiện trạng | Nguồn |
|---|---|---|
| UC03, UC05, UC08 đến UC20 | Chỉ có thẻ đặc tả, chưa có luồng ngoại lệ, dữ liệu, tiêu chí nghiệm thu đầy đủ | 015 phần B |
| UC02 phần DB02, DB03 | Chỉ có khung | 015 phần A UC02; 014 mục 3.2 |
| T01 đến T11 | Chỉ có khung rút gọn (phạm vi, đầu ra, tiêu chí) | 015 phần C |
| T12 đến T16 | Không có đặc tả, chỉ có một dòng lý do | 014 mục 4 |
| T02, T06 (đường găng demo) | Mức M3 và M2, chưa viết đặc tả hành vi tích hợp, ghép định danh | 014 mục 3.1, 5.3 |

### 3.2. BR chưa truy vết đủ

| Khoảng trống | Chi tiết | Nguồn |
|---|---|---|
| BR chưa có kịch bản kiểm thử | BR-08, BR-10, BR-12, BR-22, BR-30, BR-42 (6 BR) | 011 mục 6, "Khoảng trống truy vết" |
| BR chưa có UC | BR-29 (bộ điều kiện công nhận theo ngày sự kiện) thuộc PL III mục D, chưa có UC trong Excel | 011 mục 6 |
| BR chưa đối chiếu bản gốc | 6 BR Chờ đối chiếu và phần NCC của BR-40. Các BR NCC phụ thuộc NĐ 321/2026, chưa tìm được bản Công báo | 011 mục 3; 010 mục 6 |
| Yêu cầu chưa có UC | PL III mục D (33 mục thủ tục), mục H (chi trả, quà), mục 14 đến 22 (quy trình, biểu mẫu động) | 011 mục 6; 004 mục 4.4 |
| Sổ BR chưa nằm ở `work/` | Danh mục BR và ma trận chỉ có trong 011; skill `ba-quy-tac-truy-vet` quy định chép sang `work/project019_NNN_danh_muc_quy_tac.md` khi người dùng đồng ý | 011 mục 1 |
| Mục THIẾU chưa vào danh sách task | T-THIẾU-02 (thủ tục, biểu mẫu động), T-THIẾU-06 (tạm đình chỉ lan truyền, mới có BR-28), T-THIẾU-07 (chi trả, quà), T-THIẾU-09 (nhóm C). Các mục 01, 03, 04, 05, 08 đã thành T12 đến T16 | 009 mục 1.6; XL-W Task & Usecase |
| 153 mục PL III chưa đánh giá | Cột "Đánh giá phù hợp" 153/153 "Chưa đánh giá" nên sheet Ứng dụng dữ liệu không có số liệu phù hợp | XL-W sheet UC tham khảo PL III |

### 3.3. Thực thể và sơ đồ UML

| Khoảng trống | Chi tiết | Nguồn |
|---|---|---|
| Nhóm C chưa vào sheet | E24 đến E30 chỉ có ở 007 và sơ đồ 6.5; sheet Mô hình dữ liệu ghi "Chưa đưa vào", chờ Q27 | 007 mục 3.3; XL-W sheet Mô hình dữ liệu dòng 35 |
| Nhóm D chưa có sơ đồ lớp và mã | Danh mục dùng chung, bảng chuyển mã (T04); người dùng, vai trò, nhật ký (T10); từ điển dữ liệu (N8) | 007 mục 3.4; sheet UC – Thực thể – UML ghi chú T04, T10 |
| Nguồn Mermaid lệch hình đang dùng | SVG 01 đến 09 đã vẽ lại bằng baoyu-diagram; 8 file `.mmd` trong `work/` không còn là nguồn của hình hiện tại; sơ đồ 09 không có file nguồn | 007 mục 6 |
| Hình trong Excel chưa xem lại lần này | PF-110 ghi đã sửa lỗi ảnh mất chữ; tài liệu này không mở lại 9 ảnh | PF-110 |
| Vai trò người dùng là đề xuất BA | VT01 đến VT07 chưa có tài liệu phân quyền của nguồn | CHECKPOINT; Q56 |

### 3.4. Câu hỏi họp chưa có câu trả lời

Toàn bộ 59 câu chưa hỏi. Các câu làm thay đổi phạm vi hoặc mô hình lõi (P1 theo 009) đều nằm trong số này: Q27, Q28, Q30, Q38, Q39, Q40, Q41, Q42, Q43, Q44 (009 mục 4.2; XL-W sheet Checklist họp). Ngoài ra 11 tài liệu cần xin chưa có tài liệu nào được nhận (009 mục 4.3).

### 3.5. Mâu thuẫn giữa các tài liệu

Ghi cả hai phía kèm nguồn, không chọn bên nào.

| # | Nội dung | Phía 1 | Phía 2 |
|---|---|---|---|
| 1 | Phạm vi nghiệp vụ | Phụ lục III chỉ nói về người có công (004 mục 4.1; 009 G1) | Excel và 002 tính toàn bộ ASXH: TGXH, hộ nghèo, trẻ em, NKT (XL-W Task & Usecase; 002 mục 1) |
| 2 | Bản chất việc giao | Xây module tích hợp và phân tích (002 mục 2, 11; tiêu đề sheet Checklist họp) | Chuyển đổi hệ thống hiện có: thư mục "Migrate ASSH", PL III mục 10, 11, 29, 108 ghi "Nâng cấp" (004 mục 4.1; 009 G3) |
| 3 | Số nguồn | "7 nguồn API" (XL-W T01, T02) | 6 hệ thống, trong đó 3 là đích đẩy lên, cộng 1 nguồn nhập tay (004 mục 4.2; 009 G5). VL-02 tách chiều vào, chiều ra chưa làm: cột M dòng T02 vẫn "38–61, 75–77" |
| 4 | DB01 vào đợt nào | Demo 15/11 gồm DB01 (003 mục 11) | UC02 xếp GĐ1b 30/11 (XL-W Task & Usecase dòng UC02). 014 đề xuất tách, chờ người dùng quyết (014 mục 2, 8) |
| 5 | Phương án đợt 1 | Phương án A: người có công và bộ quy tắc, 2 nguồn chiều vào (009 mục 7.2) | Kế hoạch theo Lộ trình hiện tại: 7 nguồn, T07 và T08 đầy đủ người, hộ, quan hệ (014 mục 5.2; XL-W Lộ trình) |
| 6 | Công BA | 9 đến 12 ngày công (kịch bản A), bố trí 11 đến 15 (kịch bản B) cho tuần khảo sát và đặc tả phần đầu (003 mục 8; 012 mục 3) | 12,5 ngày công đến demo, 21 ngày công đến 30/11 (014 mục 6). 014 tự ghi con số vượt cận trên kịch bản A |
| 7 | Tên pháp nhân | VKX (PL III, tên thư mục `input/`) | XVK (002 mục 11, 003 dòng 3). Đã có Q49 |
| 8 | Lớp dữ liệu E04 DIỆN ĐỐI TƯỢNG | "1. Dữ liệu ETL/API" (XL-W sheet Mô hình hóa thực thể, ô C65) | "3 Tổng hợp (một phần ETL)" (sheet Mô hình dữ liệu ô H8; sheet Nguồn thực thể khối A, E). Đã sửa 28/10/2026: ô C65 sửa theo phía 2 ở XL-W và XL-013 |
| 9 | Lớp dữ liệu E13 ĐỊA BÀN | "1. Dữ liệu ETL/API" (sheet Mô hình hóa thực thể ô C73) | "1 danh mục, 2 ánh xạ" (sheet Mô hình dữ liệu ô H16; Nguồn thực thể khối A). Đã sửa 28/10/2026: ô C73 sửa theo phía 2 ở XL-W và XL-013 |
| 10 | Quy tắc nhiều diện ở UC06 | Sheet UC06 chỉ ghi "Điều 6 khoản 2 NĐ 335/2026" (một mức cao nhất) (XL-W ô J31) | Với NCC từ 01/01/2027 được cộng dồn nhiều diện (BR-25, 011 mục 3.2). Đề xuất sửa ở 009 mục 4.4 điểm 5 chưa áp |
| 11 | Thân nhân NCC theo PL 05/2026 | Sheet Căn cứ pháp lý #37: "Chưa đọc chi tiết điều sửa đổi về thân nhân" (XL-W dòng 42) | BR-23 "Đã đối chiếu" Điều 3 khoản 3 bản VBHN (011 mục 3.2). Đề xuất 009 mục 4.4 điểm 7 chưa áp |
| 12 | Ví dụ E04 | "Bà A: NCT ≥75 hộ nghèo" (XL-W ô E8) | NĐ 335 Điều 5 khoản 5 cần thêm điều kiện "không có người phụng dưỡng" (BR-15; 009 mục 4.4 điểm 8, chưa áp) |
| 13 | Số liệu cũ trong tài liệu | 011 mục 1 và 009 mục 5: 37 câu hỏi, 30 task và UC (014 đã sửa ở bản 0.2) | XL-W hiện có 59 câu, 36 task và UC. Đã sửa 28/10/2026: 009 mục 5 và 011 mục 1 ghi số mới |
| 14 | Mã việc VL trùng | VL-10 đến VL-13 trong 007 lịch sử chính sách (đọc NĐ 321, bảng chuyển đổi diện, câu hỏi truy lĩnh, đưa tham số vào T09) | VL-10 đến VL-13 trong 007 rà soát mô hình (đổi tên HỒ SƠ HƯỞNG, sửa sheet, thêm Q31 đến Q37, thêm PL 05/2026). Hai file cùng số 007, trái quy tắc "một số mới cho mỗi sản phẩm" (WORKSPACE_RULES.md). Đã sửa 28/10/2026: file lịch sử thành 017, mã VL thành VL-18 đến VL-21 |
| 15 | Mục "Quy ước BA" | 4 skill `ba-*` và README yêu cầu đọc mục "Quy ước BA" trong CLAUDE.md | CLAUDE.md hiện không có mục này (CHECKPOINT đã ghi nhận). Đã sửa 28/10/2026: khôi phục mục từ bản 26/10/2026 |
| 16 | Trạng thái câu hỏi truy lĩnh | VL-12 của 007 lịch sử ghi "Chưa làm" | Q32 và Q39 đã có trong checklist. Đã sửa 28/10/2026: VL-20 (mã mới) ghi đã thêm vào checklist |

### 3.6. Rủi ro

| Rủi ro | Ảnh hưởng | Nguồn |
|---|---|---|
| Ngày 15/11/2026 là Chủ nhật | Mốc demo cần xác nhận lại lịch | 003 mục 11; kiểm bằng lịch |
| Đường găng T01 → T07 → T06, T02 → UC01 → DB01 | Mô hình lõi duyệt sau 04/11 thì chỉ còn khoảng 9 ngày làm việc trước demo | 014 mục 5.3 |
| Chưa có quyền đọc dữ liệu thật (Q5 đến Q7) | UC01, T06 chỉ dựa trên giả định | 014 mục 7 |
| Có hệ thống hiện hữu cần chuyển đổi (Q38) | T12 có thể vượt toàn bộ công sức đang ước | 014 mục 7; 009 T-THIẾU-01 |
| Dữ liệu chi trả không đánh dấu truy lĩnh | UC07 báo chi sai hàng loạt cho kỳ 07 đến 09/2026 | 017 kết luận 2; BR-41 |
| Chưa có ước lượng ngày công cho phát triển | Không kiểm được tính khả thi của 15/11 và 30/11 | XL-W cột Ước lượng trống 36/36; 004 mục 5 |
| Có file khóa `~$project019_013_*.xlsx` trong `output/` | XL-013 có thể đang mở trong Excel; ghi đè lúc này dễ hỏng file như PF-105 | Liệt kê thư mục `output/` |
| Profile BA chưa gửi | VNPT-IT đang chờ; thiếu thông tin thật của BA | 012 mục 6 |

## 4. Khuyến nghị việc tiếp theo

Xếp theo thứ tự ưu tiên. Việc 1 mở khóa phần lớn các việc sau.

### 4.1. Chạy buổi khảo sát P1 và ghi biên bản

- **Làm gì:** họp với VNPT-IT theo các câu ưu tiên Cao, hỏi trước 10 câu P1 (Q27, Q28, Q30, Q38 đến Q44), rồi Q5 đến Q7, Q12, Q22, Q32. Ghi biên bản theo mẫu `ba-hop-khao-sat`, cập nhật trạng thái từng câu trong XL-W.
- **Vì sao:** 59/59 câu chưa hỏi (3.4); mâu thuẫn 1, 2, 3, 4 ở mục 3.5 chỉ khách hàng gỡ được; bước 5 của agent BA đang bị chặn (009 mục 5).
- **Đầu ra:** biên bản họp trong `output/`; sheet Checklist họp có trạng thái và câu trả lời; danh sách mục chuyển sang ĐÃ XÁC NHẬN, BỊ BÁC BỎ, CÒN TREO.
- **Người tham gia:** BA1 dẫn, BA2 ghi; VNPT-IT (đầu mối nghiệp vụ và kỹ thuật); nếu được, đại diện chủ đầu tư.
- **Xong khi:** 40 câu Cao có trạng thái khác "Chưa hỏi"; Q27, Q30, Q38 có câu trả lời ghi trong biên bản có ngày và người trả lời.

### 4.2. Xin tài liệu và lập bản đồ nguồn, đích

- **Làm gì:** xin 11 tài liệu ở 009 mục 4.3, trước hết dự thảo hợp đồng dạng file, tài liệu hệ thống hiện hữu, tài liệu API, mẫu danh sách chi trả. Lập bản đồ nguồn và đích theo chiều vào, chiều ra; làm VL-02, VL-04, VL-14.
- **Vì sao:** mâu thuẫn 3 (7 nguồn hay 6 hệ thống); PL III thiếu mục F và E.IV (004 mục 4.3); mapping trường sang E01 đến E32 chưa làm (007 VL-14).
- **Đầu ra:** bản đồ nguồn, danh mục giao tiếp nguồn và đích, mapping trường cho ít nhất một luồng đại diện (skill `ba-du-lieu-nguon`).
- **Người tham gia:** BA2; đội kỹ thuật VNPT-IT; chủ các hệ thống nguồn.
- **Xong khi:** mỗi hệ thống có chiều dữ liệu, phương thức, đơn vị bản ghi (cá nhân hay hộ) và người phụ trách; cột M dòng T02 tách chiều vào, chiều ra.

### 4.3. Chốt phạm vi đợt 1, mốc demo và ước lượng

- **Làm gì:** dựa trên câu trả lời việc 4.1, chọn phương án đợt 1 (A, B hoặc C ở 009 mục 7); quyết DB01 vào GĐ1a hay GĐ1b; xếp giai đoạn cho T12; xác nhận ngày demo (15/11 là Chủ nhật); điền cột Ước lượng cho 36 dòng; xác nhận cơ cấu BA và hoàn thiện profile 012.
- **Vì sao:** mâu thuẫn 4, 5, 6; cột Ước lượng trống 36/36; rủi ro ngày demo; 4 điểm chờ quyết ở 014 mục 8.
- **Đầu ra:** sheet Lộ trình bản 3 có ngày công; biên bản chốt phạm vi; bản 0.2 của 014; profile BA gửi đi.
- **Người tham gia:** người dùng (quyết nội bộ); VNPT-IT; đội kỹ thuật ước lượng phần phát triển và kiểm thử.
- **Xong khi:** 36/36 dòng có giai đoạn và ước lượng; mốc demo có ngày khách hàng xác nhận.

### 4.4. Duyệt mô hình lõi T07 trước 04/11

- **Làm gì:** trình mô hình 22 thực thể và ba lớp dữ liệu; lấy câu trả lời Q31 đến Q37, Q50 đến Q58; quyết giữ hay bỏ nhóm C (Q27); thống nhất đổi tên HỒ SƠ HƯỞNG (VL-10 của 007 rà soát); sửa mâu thuẫn lớp dữ liệu E04, E13 giữa ba sheet.
- **Vì sao:** T07 nằm giữa đường găng (014 mục 5.3); mâu thuẫn 8, 9; nhóm C và D chưa vào mô hình (3.3).
- **Đầu ra:** sheet Mô hình dữ liệu, Nguồn thực thể, Mô hình hóa thực thể khớp nhau; 007 và sơ đồ UML cập nhật; danh sách vai trò thật thay VT01 đến VT07.
- **Người tham gia:** BA1, BA2; VNPT-IT; đội kỹ thuật (thiết kế CSDL vật lý).
- **Xong khi:** bên giao việc duyệt mô hình bằng văn bản hoặc biên bản; ba sheet không còn ô lệch lớp dữ liệu.

### 4.5. Đồng bộ tài liệu nội bộ

- **Làm gì:** sửa số liệu cũ ở 009, 011, 014; áp 4 đề xuất còn treo của 009 mục 4.4 (điểm 5 đến 8); thêm mục "Quy ước BA" vào CLAUDE.md; xử lý trùng số 007 và mã VL (đổi số một file hoặc thêm hậu tố mã VL); xác định lại file nguồn của sơ đồ (`.mmd` hay SVG baoyu).
- **Vì sao:** mâu thuẫn 10 đến 16; skill BA tham chiếu một mục không tồn tại.
- **Đầu ra:** các file đã sửa, mỗi file thêm dòng lịch sử phiên bản; bản sao lưu trước khi sửa trong `tmp/`.
- **Người tham gia:** BA; người dùng duyệt trước khi sửa vì đụng nhiều file.
- **Xong khi:** chạy lại script đếm của tài liệu này không còn số lệch; 4 skill `ba-*` đọc được mục "Quy ước BA". Đóng file XL-013 trong Excel trước khi ghi.

### 4.6. Hoàn thiện truy vết BR

- **Làm gì:** viết kịch bản cho 6 BR chưa có (BR-08, BR-10, BR-12, BR-22, BR-30, BR-42); tìm bản Công báo NĐ 321/2026 để đối chiếu BR-20, BR-21, BR-22 và phần NCC của BR-40; quyết UC cho BR-29; chép danh mục BR và ma trận sang `work/`; đánh giá 153 mục PL III.
- **Vì sao:** khoảng trống ở 3.2.
- **Đầu ra:** `work/project019_NNN_danh_muc_quy_tac.md`, `work/project019_NNN_ma_tran_truy_vet.md`; cột "Đánh giá phù hợp" của sheet UC tham khảo PL III có giá trị.
- **Người tham gia:** BA1; khách hàng xác nhận BR-41 (cách chi truy lĩnh) và 4 BR Dự thảo.
- **Xong khi:** mỗi BR có ít nhất 1 kịch bản; không còn BR "Chờ đối chiếu" trong nhóm dùng cho GĐ1b; 153/153 mục PL III có đánh giá.

### 4.7. Đặc tả phần đầu cho demo sau khảo sát

- **Điều kiện bắt đầu:** chỉ làm sau khi có thông tin cụ thể từ việc 4.1 và 4.2, theo chỉ đạo của anh Dương ngày 27/10 (mục 2.4). Trước đó giữ ở mức đầu mục của 014.
- **Làm gì:** viết đặc tả T02 (một luồng đại diện), T06, hoàn thiện UC01 (ngưỡng chất lượng theo Q59) và UC02 phần DB01 theo dữ liệu thật hoặc bộ dữ liệu mẫu đã duyệt; lập bộ dữ liệu giả và kết quả kỳ vọng (BA-05 đến BA-10).
- **Vì sao:** T02, T06 đang ở M3, M2 và nằm trên đường găng (3.1); mốc M2 06/11.
- **Đầu ra:** đặc tả T02, T06; UC01, UC02 bản 0.2; bộ dữ liệu kiểm thử demo.
- **Người tham gia:** BA2 chính, BA1 duyệt; đội kỹ thuật ước lượng và phát triển.
- **Xong khi:** đội kỹ thuật ước lượng được từ đặc tả; mỗi luồng ngoại lệ có ca kiểm thử.

## 5. Câu hỏi cần khách hàng trả lời trước khi đi tiếp

Mã Q lấy từ XL-W sheet Checklist họp. Câu ghi "mới" chưa có trong checklist.

### 5.1. Phạm vi hợp đồng và bản chất việc giao

1. Q27: Phạm vi là người có công theo Phụ lục III hay toàn bộ an sinh xã hội?
2. Q38: Hệ thống hiện hữu nào đang được nâng cấp hoặc chuyển đổi? Bên mình có nhận chuyển đổi dữ liệu không?
3. Q30: Bên mình nhận phần phân tích dữ liệu hay trọn Phụ lục III, gồm quy trình, biểu mẫu động, thủ tục hành chính?
4. Q44: Mục H (chi trả, quà tri ân) là chức năng phải xây hay chỉ nhận dữ liệu?
5. Q29: Phụ lục III có mục F và E.IV không? Xin bản đầy đủ dạng file.
6. Q49: Tên pháp nhân trong liên danh là VKX hay XVK?

### 5.2. Nguồn dữ liệu và tích hợp

1. Q28, Q37: "7 nguồn API" là những hệ thống nào, chiều vào, chiều ra hay hai chiều; có trùng 7 CSDL thành phần của dự thảo NĐ CSDL ASXH không?
2. Q12 đến Q14: Số CSDL thành phần, loại kết nối, batch hay realtime, đã có công cụ ETL chưa?
3. Q5 đến Q7: Qua VPN truy cập được gì; có bản dump đã che dữ liệu nhạy cảm không?
4. Q15: Đã có danh mục dùng chung, quy tắc làm sạch, xử lý trùng chưa?
5. Q34, Q36: Người không có số định danh được định danh bằng khóa nào; mã hồ sơ ASXH đã được cấp chưa?

### 5.3. Hưởng chế độ, quyết định, chi trả

1. Q31, Q50: Nguồn có lưu quyết định hưởng không; nếu thiếu, cán bộ có nhập tay trong module không?
2. Q32, Q39: Dữ liệu chi trả có tài khoản nhận, ngày chi, phân biệt thường kỳ, truy lĩnh, thu hồi không; khoản chênh tháng 7 đến 9/2026 đã chi truy lĩnh chưa?
3. Q52: Có cần lưu riêng "đang hưởng" (nguồn cấp) và "đáng hưởng" (hệ thống tính) để so sánh không?
4. Q35, Q43: Kết quả xử lý cảnh báo lưu ở module này hay trả về nguồn; quy trình thực tế ai nhập, ai thẩm định, ai quyết định?

### 5.4. Người có công

1. Q42: Từ 01/01/2027, hệ thống có phải giải quyết hồ sơ theo bộ điều kiện cũ cho sự kiện trước mốc không?
2. Q45: Nguồn có ghi loại quan hệ thân nhân theo 5 loại của Pháp lệnh không?
3. Q47: Sự kiện tạm đình chỉ, chấm dứt chế độ (án phạt tù, xuất cảnh trái phép, mất tích) lấy từ nguồn nào?
4. Q33: Nguồn có kết quả giám định kèm ngày và kỳ giám định lại không?

### 5.5. Trợ giúp xã hội

1. Q40: Hồ sơ tiếp nhận trước 05/10/2026 xét diện, hệ số theo NĐ 20/2021 hay NĐ 335/2026?
2. Q41: Khi chuyển nơi cư trú, hệ thống ghi tháng thôi chi nơi cũ và tháng hưởng nơi mới thế nào?
3. Q46: Nguồn có quan hệ người nhận chăm sóc và ngày sinh con của người khuyết tật không?
4. Q48: Tỉnh nào có nghị quyết HĐND về mức chuẩn cao hơn, từ kỳ nào?

### 5.6. Hộ và giảm nghèo

1. Q51: Kết quả rà soát hộ nghèo, cận nghèo lấy qua API từ CSDL của Bộ Nông nghiệp và Môi trường hay cán bộ nhập trong module?

### 5.7. Vai trò, phân quyền, nguồn ghi và chạy lại

1. Q20: Bên mình được làm việc trực tiếp với người dùng cuối không?
2. Q56, Q57: Danh sách vai trò thực tế và mô hình phân quyền hiện có; dữ liệu nào cán bộ được nhập hoặc sửa trực tiếp?
3. Q53, Q58: Ai cấu hình chế độ, tham số, quy tắc; vai trò nào được chạy lại chính thức, vai trò nào chạy mô phỏng?
4. Q54, Q55: Tần suất chạy lại, kỳ đã chi có giữ nguyên không; người dùng có được ghép, tách người bằng tay không?

### 5.8. Đầu ra, nghiệm thu và tiến độ

1. Q16, Q19: Đầu ra là báo cáo cố định, dashboard hay xuất Excel; có biểu mẫu và mẫu tài liệu bắt buộc không?
2. Q18: Ai nghiệm thu, tiêu chí nghiệm thu là gì?
3. Q22: Mốc cứng là ngày nào; GĐ1b là 30/11?
4. Mới: Ngày 15/11/2026 là Chủ nhật; demo vào ngày nào?
5. Mới: Demo 15/11 gồm DB01 (theo báo cáo 003) hay để DB01 sang GĐ1b (theo sheet Task & Usecase)?
6. Q59: Ngưỡng đạt của từng phép đo chất lượng dữ liệu ở UC01 là bao nhiêu?
7. Q23, Q26: Hợp tác trọn gói hay theo man-month; có chấp nhận 1 đến 2 tuần khảo sát trước khi báo giá không?
