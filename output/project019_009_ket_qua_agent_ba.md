# Kết quả agent BA: kiểm chứng bản dựng nghiệp vụ, phạm vi và chuẩn bị khảo sát

Ngày lập: 26/10/2026. Người lập: agent BA project019, chạy theo system prompt `output/project019_008_system_prompt_agent_ba.md` (Phần A).

Bối cảnh: VNPT IT chuyển đổi (migrate) hệ thống an sinh xã hội; bên mình là thành viên liên danh VNPT-VKX. Tài liệu khách hàng duy nhất có chữ là Phụ lục III dự thảo hợp đồng giữa Cục Người có công (Bộ Nội vụ) và Liên danh VNPT-VKX (7 ảnh trong `input/VKX - VNPT IT - Migrate ASSH [26-10-2026 08_54]/`).

Trạng thái chung: bản dựng sơ bộ vẫn là giả thuyết. **Chưa có biên bản khảo sát**, nên không mục nào ở trạng thái ĐÃ XÁC NHẬN. Không dùng tài liệu này như phạm vi đã chốt.

## 0. Cấu trúc sản phẩm

| Nhóm | Nội dung | Vị trí |
|---|---|---|
| 1 | Bảng phân loại bản dựng | Mục 1 của file này |
| 2 | Căn cứ pháp lý và tham số theo kỳ | Tóm tắt ở mục 2; đầy đủ ở `output/project019_010_can_cu_phap_ly_va_tham_so_theo_ky.md` |
| 3 | Bản đồ phạm vi nghiệp vụ | Mục 3 |
| 4 | Checklist khảo sát có xếp ưu tiên | Mục 4 |
| 5 | Đặc tả và ma trận truy vết phần đã ổn định | Tóm tắt ở mục 6; đầy đủ ở `output/project019_011_dac_ta_quy_tac_va_truy_vet.md` |
| 6 | Đề xuất mốc phạm vi | Mục 7 |

Nhóm 2 và nhóm 5 tách file vì mỗi nhóm dài hơn phần còn lại cộng lại.

Đầu vào đã đọc: 7 ảnh Phụ lục III (zip trong `input/` có cùng 7 ảnh, trùng mã băm SHA-1; đã giải nén vào `tmp/zip_vkx_20261026/`); `input/Checklist_hop_ky_thuat_module_tich_hop_du_lieu.xlsx` (7 sheet); `work/project019_005_checklist_hop_dang_cap_nhat.xlsx` (8 sheet); báo cáo 002, 003, 004, 006, 007 (hai file), 008; `work/CHECKPOINT.md`; bốn skill `ba-*`. Không ghi vào `input/`, không sửa `work/project019_005_*.xlsx`.

Ảnh Phụ lục III không chứa họ tên, số định danh hay số điện thoại. Không có thông tin cá nhân nào được chép vào sản phẩm.

## 1. Bảng phân loại bản dựng (bước 1)

### 1.1. Nhãn và mã nguồn

| Nhãn | Nghĩa |
|---|---|
| CÓ CĂN CỨ | Có nguồn cụ thể: điều khoản văn bản pháp luật, hoặc tài liệu khách hàng (Phụ lục III dự thảo) |
| GIẢ ĐỊNH | Nhóm dự án suy ra; không tìm được nguồn |
| THIẾU | Cần cho nghiệp vụ (theo văn bản hoặc tài liệu khách hàng) nhưng bản dựng chưa có |

| Mã nguồn | Tài liệu |
|---|---|
| PL3-n | Phụ lục III dự thảo hợp đồng, mục số n (ảnh trong `input/`) |
| XL:sheet | Sheet của checklist (bản `input/`, nội dung giống bản `work/` trừ phần bổ sung 26/10) |
| 002, 003 | Báo cáo bối cảnh và phạm vi trong `output/` (ghi theo lời người dùng, không phải tài liệu khách hàng) |
| Văn bản | Mức tin cậy CB, TV, BC theo `project019_010` mục 1 |

Mỗi task và UC có hai nhãn. "Nhu cầu" cho biết khách hàng hoặc văn bản có yêu cầu việc này không. "Dữ liệu" cho biết đã chứng minh được nguồn dữ liệu cho việc này chưa. Phụ lục III là dự thảo, nên nhãn CÓ CĂN CỨ dựa trên nó vẫn cần khách hàng xác nhận bản chính thức.

### 1.2. Giả thuyết phạm vi và bối cảnh

| # | Mục trong bản dựng | Nguồn | Nhãn | Ghi chú |
|---|---|---|---|---|
| G1 | Chủ đầu tư dự kiến là Cục Người có công, Bộ Nội vụ; nhà thầu là Liên danh VNPT-VKX | PL3 tiêu đề | CÓ CĂN CỨ | Số và ngày hợp đồng để trống: dự thảo |
| G2 | Phạm vi là toàn bộ an sinh xã hội (TGXH, giảm nghèo, trẻ em, NCC) | XL:Task & Usecase; 002 | GIẢ ĐỊNH | PL3 chỉ nói về người có công. TGXH do Bộ Y tế chủ trì (NĐ 335/2026 Điều 35, CB); hộ nghèo do Bộ NN&MT (XL:Căn cứ #17 đến 19) |
| G3 | Việc thật là chuyển đổi hệ thống hiện có | Tên thư mục "Migrate ASSH"; PL3-10, 11, 29, 108 ghi "Nâng cấp" | GIẢ ĐỊNH, có dấu hiệu mạnh | Phát hiện mới: bốn mục PL3 dùng chữ "Nâng cấp", tức đã có hệ thống đang chạy |
| G4 | Module chỉ làm tích hợp và phân tích dữ liệu | XL:Checklist họp tiêu đề; 003 | GIẢ ĐỊNH | PL3 gồm cả quản trị, thủ tục hành chính, chi trả (mục A, D, H) |
| G5 | "7 nguồn API" | XL:Task T01, T02 | GIẢ ĐỊNH | PL3-38 đến 61 cho 6 hệ thống, trong đó 3 là đích đẩy lên, và PL3-75 đến 77 là nhập tay (004 mục 4.2) |
| G6 | Công nghệ Angular 19, Spring Boot, Oracle | XL:Checklist họp dòng 2; 002 | GIẢ ĐỊNH | Lời người dùng sau buổi trao đổi; chưa có tài liệu kỹ thuật |
| G7 | Mốc GĐ1a 15/11/2026; GĐ1b 30/11/2026 ("31/11" tạm hiểu là 30/11) | XL:Lộ trình | GIẢ ĐỊNH | Ngày 31/11 không tồn tại; chưa có văn bản nào của khách hàng ghi mốc |
| G8 | Kho dữ liệu VNPT IT đã có | 002 | GIẢ ĐỊNH | Chưa có danh mục bảng hay dữ liệu mẫu |
| G9 | Tên pháp nhân bên mình | PL3: VKX; 002, 003: XVK | THIẾU | Hai cách viết khác nhau, cần xác nhận (P3-01) |

### 1.3. Task nền tảng và use case

| Mã | Tên | Nguồn nhu cầu | Nhãn nhu cầu | Nhãn dữ liệu | Ghi chú kiểm chứng |
|---|---|---|---|---|---|
| T01 | Khảo sát và BA | Phương pháp | CÓ CĂN CỨ | Không áp dụng | Việc bắt buộc của mọi phương án |
| T02 | Tích hợp 7 nguồn qua API | PL3-38 đến 61 | CÓ CĂN CỨ | GIẢ ĐỊNH | Số nguồn và chiều dữ liệu chưa đúng (G5). Có thêm luồng chiều ra PL3-42, 44, 48, 50, 56, 62 đến 67 |
| T03 | Staging và lưu lịch sử | PL3-39, 41, 43 và các mục cùng loại: "theo dõi lịch sử đồng bộ" | CÓ CĂN CỨ | GIẢ ĐỊNH | Lịch sử nghiệp vụ (kỳ hưởng) khác lịch sử đồng bộ; PL3 chỉ nói lịch sử đồng bộ |
| T04 | Chuẩn hóa và danh mục dùng chung | PL3-25 đến 28, 30, 32, 34 | CÓ CĂN CỨ | GIẢ ĐỊNH | Các bộ chủ quản trong T04 (Bộ Y tế, Bộ NN&MT) không có trong PL3 |
| T05 | Ánh xạ địa giới cũ → mới | PL3-29; QĐ 19/2025/QĐ-TTg | CÓ CĂN CỨ | GIẢ ĐỊNH | |
| T06 | Ghép định danh cá nhân | PL3-46, 47, 52, 53; Luật Căn cước 26/2023 | CÓ CĂN CỨ | GIẢ ĐỊNH | Tỷ lệ bản ghi có số định danh chưa biết (Q34) |
| T07 | Mô hình hồ sơ và quan hệ | PL3-117, 118, 124 đến 128; PL 02/2020 Điều 3 khoản 3 | CÓ CĂN CỨ | GIẢ ĐỊNH | Loại thân nhân đã xác minh (BR-23). Quan hệ chăm sóc, hộ chỉ cần nếu có TGXH |
| T08 | Ghép hộ gia đình | XL:Task T08 | GIẢ ĐỊNH | GIẢ ĐỊNH | PL3 không quản lý theo hộ |
| T09 | Bộ quy tắc chính sách cấu hình | PL3-79 đến 84 (tính toán chế độ NCC); NĐ 335/2026 | CÓ CĂN CỨ | CÓ CĂN CỨ (quy tắc từ văn bản) | 30 BR đã lập ở 011. Phần TGXH phụ thuộc G2 |
| T10 | Phân quyền, che dữ liệu, nhật ký | PL3-1, 2, 10 đến 13; Luật 91/2025/QH15 | CÓ CĂN CỨ | Không áp dụng | PL3-10, 11 là "nâng cấp" trên hệ thống có sẵn |
| T11 | Kiểm thử, UAT, tài liệu | Phương pháp | CÓ CĂN CỨ | Không áp dụng | Mẫu tài liệu chưa biết (Q19) |
| UC01 | Đánh giá chất lượng dữ liệu | PL3-52 đến 55, 72 đến 74, 148, 149 | CÓ CĂN CỨ | GIẢ ĐỊNH | |
| UC02 | Dashboard thống kê | PL3-163 đến 192 | CÓ CĂN CỨ | GIẢ ĐỊNH | PL3 có 30 biểu đồ cụ thể, đều về NCC. Chiều "vai trò người chăm sóc" và "hộ" là GIẢ ĐỊNH |
| UC03 | Báo cáo theo biểu mẫu | PL3-136 đến 162, 193 đến 197; TT 18/2025/TT-BNV | CÓ CĂN CỨ | GIẢ ĐỊNH | Chưa có biểu mẫu |
| UC04 | Hồ sơ 360° theo số định danh | PL3-108 đến 128 | CÓ CĂN CỨ (phần NCC và thân nhân) | GIẢ ĐỊNH | Chiều "đang chăm sóc ai" là GIẢ ĐỊNH |
| UC05 | Hồ sơ 360° theo hộ | XL:Task UC05 | GIẢ ĐỊNH | GIẢ ĐỊNH | |
| UC06 | Nhiều diện, quy tắc mức cao nhất | PL3-132; NĐ 335 Điều 6 khoản 2 | CÓ CĂN CỨ | GIẢ ĐỊNH | **Sai một phần:** với NCC từ 01/01/2027, người nhiều diện hưởng cộng dồn trợ cấp, phụ cấp (PL 02/2020 sửa đổi Điều 6 khoản 3). Không áp quy tắc "mức cao nhất" cho NCC |
| UC07 | Chi sai theo trạng thái | PL3-62, 63, 66 đến 71, 130 đến 134; NĐ 335 Điều 8, 9; PL Điều 54 | CÓ CĂN CỨ | GIẢ ĐỊNH | Thiếu xử lý truy lĩnh (xem 1.6, T-THIẾU-03) |
| UC08 | Chi sai theo vai trò liên quan | NĐ 335 Điều 9 khoản 3, Điều 17 | CÓ CĂN CỨ (quy tắc TGXH) | GIẢ ĐỊNH | Chỉ có nghĩa khi phạm vi gồm TGXH. Ngưỡng "nhận chăm sóc quá nhiều đối tượng" là GIẢ ĐỊNH |
| UC09 | Đủ điều kiện chưa hưởng | PL3-109, 201 | CÓ CĂN CỨ | GIẢ ĐỊNH | Cần danh sách đầy đủ người đủ điều kiện, nguồn chưa rõ |
| UC10 | Người liên quan chưa hưởng | PL3-124 đến 128, 201; NĐ 335 Điều 17 | CÓ CĂN CỨ | GIẢ ĐỊNH | |
| UC11 | Chuyển đổi chế độ theo sự kiện | PL3-79, 102 đến 106, 190, 191 | CÓ CĂN CỨ | GIẢ ĐỊNH | "Hộ thoát nghèo → mọi thành viên mất chính sách theo hộ" là khái quát hóa, GIẢ ĐỊNH |
| UC12 | Dự toán ngân sách, mô phỏng | PL3-147, 155, 156, 172 đến 174, 199 | CÓ CĂN CỨ | GIẢ ĐỊNH | |
| UC13 | Danh sách dễ tổn thương khi khẩn cấp | XL:Task UC13 | GIẢ ĐỊNH | GIẢ ĐỊNH | Không có trong PL3 |
| UC14 | Bản đồ mật độ | PL3-188, 189 | CÓ CĂN CỨ (NCC) | GIẢ ĐỊNH | |
| UC15 | Mô phỏng chuẩn nghèo 2027 | XL:Task UC15; NĐ 351/2025 (BC) | GIẢ ĐỊNH | GIẢ ĐỊNH | Ngoài PL3 |
| UC16 | Phân tích liên ngành | PL3-114, 153, 154, 168 đến 171 (BHYT, giáo dục NCC) | CÓ CĂN CỨ một phần | GIẢ ĐỊNH | Phần "trẻ hộ nghèo không đi học" là GIẢ ĐỊNH |
| UC17 | Đánh giá hiệu quả chính sách | PL3-200, 201 | CÓ CĂN CỨ một phần | GIẢ ĐỊNH | Thoát nghèo, tái nghèo không có trong PL3 |
| UC18 | Dự báo nguồn lực | PL3-177, 178, 198 | CÓ CĂN CỨ một phần | GIẢ ĐỊNH | |
| UC19 | API cung cấp dữ liệu | PL3-48 đến 51, 56, 57, 62 đến 67 | CÓ CĂN CỨ | GIẢ ĐỊNH | |

### 1.4. Đối tượng hưởng trong bản dựng

| Đối tượng | Nguồn trong bản dựng | Nguồn kiểm chứng | Nhãn |
|---|---|---|---|
| 12 diện người có công | XL:Căn cứ #14 | PL 02/2020 Điều 3 khoản 2 điểm a đến m (CB, bản sửa 2026) | CÓ CĂN CỨ |
| Thân nhân NCC: cha mẹ, vợ chồng, con, người nuôi liệt sĩ | XL:Căn cứ #14; T07 | PL 02/2020 Điều 3 khoản 3, Điều 4 khoản 2 (CB) | CÓ CĂN CỨ |
| Người thờ cúng liệt sĩ | 007 E06 | PL3-80; NĐ 131/2021 Điều 28 khoản 6 (BC) | CÓ CĂN CỨ (nhu cầu); điều khoản chưa xác minh |
| Thanh niên xung phong | XL:Căn cứ #29 | PL3-110; QĐ 40/2011 (BC) | CÓ CĂN CỨ |
| Người phục vụ NCC | XL:Tham số NCC | NĐ 321/2026 Phụ lục I mục 12 (TV) | CÓ CĂN CỨ |
| Trẻ em mồ côi, bị bỏ rơi; người từ 16 tuổi đang học | XL:T09 | NĐ 335 Điều 5 khoản 1, 2 (CB) | CÓ CĂN CỨ (nếu phạm vi gồm TGXH) |
| Người cao tuổi hưởng TGXH | XL:Mô hình ví dụ "NCT ≥75 hộ nghèo" | NĐ 335 Điều 5 khoản 5 (CB): phải thuộc hộ nghèo và không có người phụng dưỡng | CÓ CĂN CỨ; ví dụ trong sheet thiếu điều kiện phụng dưỡng |
| Người khuyết tật nặng, đặc biệt nặng | XL:T04, UC06 đến UC10 | NĐ 335 Điều 5 khoản 6 (CB) | CÓ CĂN CỨ |
| Đơn thân nghèo nuôi con; trẻ em nhiễm HIV; người nhiễm HIV hộ nghèo; trẻ dưới 3 tuổi vùng ĐBKK | XL:T09 | NĐ 335 Điều 5 khoản 3, 4, 7, 8 (CB) | CÓ CĂN CỨ |
| Người hưởng hưu trí xã hội | 006 #35 | Luật 41/2024, NĐ 176/2025 (CB qua VBHN 15/2026) | CÓ CĂN CỨ; bản dựng gốc THIẾU, đã bổ sung ở sheet bản `work/` |
| Người nhận chăm sóc, nuôi dưỡng; hộ chăm sóc NKT | XL:T07, UC08, UC10 | NĐ 335 Điều 17, 19, 20 (CB) | CÓ CĂN CỨ |
| Hộ nghèo, cận nghèo | XL:T08, UC05, UC15 | NĐ 07/2021, NĐ 351/2025 (BC) | CÓ CĂN CỨ (văn bản); chưa xác minh số liệu |
| "Hoàn cảnh khó khăn", "diện chính sách", "dân sự" | 002 | Không có | GIẢ ĐỊNH; chưa có định nghĩa |
| Nhóm bảo hiểm thất nghiệp, người cai nghiện | 007 (7 CSDL thành phần dự thảo) | Dự thảo NĐ CSDL ASXH (BC) | THIẾU trong bản dựng; chưa rõ có thuộc phạm vi |

### 1.5. Quy tắc tính toán trong bản dựng

| Quy tắc trong bản dựng | Vị trí | Kiểm chứng | Nhãn |
|---|---|---|---|
| Mức chuẩn TGXH 540.000đ | XL:Task UC12; Căn cứ #9 | NĐ 335 Điều 4 khoản 2 (CB) | CÓ CĂN CỨ |
| Mức chuẩn NCC 3.012.000đ | XL:Task UC12; Căn cứ #16 | NĐ 321/2026, Cổng Chính phủ (CB về giá trị) | CÓ CĂN CỨ; mốc áp dụng chưa xác minh |
| Nhiều diện chỉ hưởng một mức cao nhất, trừ đơn thân | XL:T09, UC06 | NĐ 335 Điều 6 khoản 2 (CB) | CÓ CĂN CỨ cho TGXH. Không đúng cho NCC từ 2027 (BR-25) |
| Mai táng ≥ 20 lần mức chuẩn | XL:UC11 | NĐ 335 Điều 11 khoản 2 (CB) | CÓ CĂN CỨ (chỉ TGXH; NCC theo BHXH, BR-27) |
| Hộ chăm sóc NKT đặc biệt nặng hệ số 1,0 | XL:UC10 | NĐ 335 Điều 17 khoản 2 điểm c (CB) | CÓ CĂN CỨ |
| NKT mang thai, nuôi con dưới 36 tháng 1,5 đến 2,0; vợ chồng cùng NKT một suất | XL:UC08, UC10 | NĐ 335 Điều 17 khoản 2 điểm a (CB) | CÓ CĂN CỨ |
| Sai hệ số do qua mốc 4, 16 tuổi | XL:UC07 | NĐ 335 Điều 6 khoản 1 (CB) | CÓ CĂN CỨ. Bản dựng THIẾU mốc 60, 75 tuổi (k5) và 18 tuổi (con liệt sĩ, NĐ 321) |
| Người có công mất thì thân nhân hưởng tuất | XL:UC10, UC11 | PL 02/2020 Điều 6 khoản 5 (CB) | CÓ CĂN CỨ; bản dựng THIẾU giới hạn tối đa 2 suất |
| Tham số theo thời kỳ, không viết cứng | XL:T09; Lộ trình | NĐ 335 Điều 32; NĐ 321 (hai mốc) | CÓ CĂN CỨ |
| Một tài khoản nhận cho nhiều người là bất thường | XL:Ứng dụng dữ liệu N2 | Không có văn bản; PL3-64 chỉ nói "tài khoản người hưởng sai" | GIẢ ĐỊNH (dấu hiệu rủi ro, không phải quy tắc pháp lý) |
| Ghép mờ khi thiếu số định danh | XL:T06 | Không có | GIẢ ĐỊNH |
| Hộ rà soát nghèo khác hộ cư trú | XL:T08 | Không có | GIẢ ĐỊNH |
| Mức NCC tính bằng mức chuẩn nhân tỷ lệ | Ngầm định trong XL:T09 "diện → hệ số → mức chuẩn" | NĐ 321 phụ lục là bảng số tiền, không khớp phép nhân (007 kết luận 4, TV) | GIẢ ĐỊNH sai; dùng bảng phụ lục (BR-20) |

### 1.6. Mục THIẾU trong bản dựng

| Mã | Mục thiếu | Căn cứ cho thấy cần | Ảnh hưởng |
|---|---|---|---|
| T-THIẾU-01 | Chuyển đổi dữ liệu từ hệ thống hiện có (migrate) | G3; PL3-10, 11, 29, 108 | Có thể là khối lượng lớn nhất nếu đúng; không có task nào |
| T-THIẾU-02 | Thủ tục hành chính (PL3 mục D, 33 mục), quy trình và biểu mẫu động (PL3-14 đến 22) | PL3 | Chưa ước lượng (004 mục 4.4) |
| T-THIẾU-03 | Truy lĩnh, truy thu theo kỳ hưởng | NĐ 335 Điều 32 khoản 3, 4 (CB); NĐ 321 áp từ 01/7/2026, ban hành 15/8/2026 | UC07 báo sai hàng loạt nếu thiếu |
| T-THIẾU-04 | Chuyển tiếp hồ sơ đang giải quyết (NĐ 335 Điều 33; PL 05/2026 Điều 2) | CB | Hồ sơ giai đoạn chuyển tiếp xét sai bộ quy tắc |
| T-THIẾU-05 | Di chuyển hồ sơ NCC giữa tỉnh, chuyển nơi cư trú TGXH | PL3-102 đến 105; NĐ 335 Điều 8 khoản 3 (CB) | Bản ghi trùng giữa hai tỉnh; UC07 hiểu nhầm chi trùng |
| T-THIẾU-06 | Tạm đình chỉ, chấm dứt và lan truyền sang thân nhân | PL Điều 54 (CB) | UC07 bỏ sót trường hợp phải dừng chi |
| T-THIẾU-07 | Chi trả theo kỳ và quà tri ân (PL3 mục H) | PL3-202 đến 208 | Không rõ là nguồn hay chức năng phải xây |
| T-THIẾU-08 | Mức TGXH theo tỉnh do HĐND quyết định | NĐ 335 Điều 4 khoản 3 (CB) | Tính sai mức đúng ở tỉnh có mức riêng |
| T-THIẾU-09 | Cơ sở nuôi dưỡng, điều dưỡng, nghĩa trang, mộ liệt sĩ | PL3-33, 35, 58 đến 61, 157 đến 159, 175 | Đã đề xuất nhóm C ở 007, chưa vào bản dựng |

### 1.7. Tổng hợp

| Nhóm | Số mục | CÓ CĂN CỨ | GIẢ ĐỊNH | THIẾU |
|---|---|---|---|---|
| Giả thuyết phạm vi (1.2) | 9 | 1 | 7 | 1 |
| Task, UC: nhãn nhu cầu (1.3) | 30 | 26 (6 trong đó chỉ một phần: UC04, UC08, UC14, UC16, UC17, UC18) | 4 (T08, UC05, UC13, UC15) | 0 |
| Task, UC: nhãn dữ liệu (1.3) | 30 | 1 (T09) | 26 | 0 (3 mục không áp dụng: T01, T10, T11) |
| Đối tượng hưởng (1.4) | 14 | 12 | 1 | 1 |
| Quy tắc tính (1.5) | 13 | 9 | 4 | 0 |
| Mục thiếu (1.6) | 9 | | | 9 |

Kết luận bước 1: phần lớn **nhu cầu** có căn cứ nhờ Phụ lục III và văn bản pháp luật. Gần như toàn bộ **dữ liệu** vẫn là giả định. Rủi ro lớn nhất không nằm ở UC đã liệt kê, mà ở các mục thiếu: chuyển đổi hệ thống cũ, truy lĩnh, chuyển tiếp và thủ tục hành chính.

## 2. Căn cứ pháp lý và tham số theo kỳ (bước 2, tóm tắt)

Bảng đầy đủ: `output/project019_010_can_cu_phap_ly_va_tham_so_theo_ky.md`. Điểm chính:

1. **Đã đối chiếu bản gốc** NĐ 335/2026 (Công báo số 500 ngày 05/9/2026) và Pháp lệnh 02/2020 hợp nhất Pháp lệnh 05/2026 (VBHN 123/2026, Văn phòng Quốc hội xác thực 05/8/2026). Xác nhận hiệu lực và mức chuẩn NĐ 321/2026 qua Cổng thông tin Chính phủ.
2. **Sửa sai:** chuyển tiếp hồ sơ của NĐ 335 nằm ở Điều 33; Điều 32 khoản 3 đến 5 là chuyển mức cho người đang hưởng. Sheet "Căn cứ pháp lý" dòng #9 ghi "Điều 32".
3. **Mới:** Pháp lệnh sửa đổi (từ 01/01/2027) định nghĩa thân nhân gồm năm loại; người có công nhiều diện hưởng cộng dồn trợ cấp, phụ cấp; có quy tắc lan truyền tạm đình chỉ, chấm dứt sang thân nhân (Điều 54); điều kiện công nhận có ba bộ tùy ngày sự kiện.
4. **Mới:** NĐ 63/2024 (liên thông khai tử, mai táng) đã được sửa bởi NĐ 301/2026, chưa có trong sheet.
5. Bảng "kỳ nào áp dụng văn bản nào" từ 01/2024 đến 2027 ở mục 5 của 010. Ví dụ tháng 11/2026: trợ cấp NCC theo NĐ 321/2026 nhưng điều dưỡng theo NĐ 77/2024.
6. Còn 11 nhóm số liệu "chưa xác minh" (010 mục 6), nặng nhất là bảng mức hưởng NCC ba kỳ và hai mốc áp dụng NĐ 321/2026 (chỉ có bản trang tổng hợp).

## 3. Bản đồ phạm vi nghiệp vụ (bước 3)

Phạm vi khảo sát là **toàn bộ nghiệp vụ của khách hàng**, không thu hẹp theo bản demo 15/11 (quy tắc PF-099 của Workspace). Bản đồ dưới đây ghi cả phần chưa có trong Excel.

### 3.1. Nhóm nghiệp vụ theo lĩnh vực

Ký hiệu ô: mục PL3 hoặc điều khoản làm căn cứ; mã T/UC đang phủ; "Chưa có" là bản dựng chưa có.

| Nhóm nghiệp vụ | Người có công | Trợ giúp xã hội, hưu trí xã hội | Giảm nghèo | Bản dựng đang phủ |
|---|---|---|---|---|
| Tiếp nhận | PL3-38 đến 41 (đồng bộ hồ sơ từ HT TTHC Bộ Nội vụ); PL3-75 đến 77 (nhập hồ sơ BQP/BCA) | NĐ 335 Điều 7, 8 khoản 1: nộp qua Cổng DVC quốc gia, bưu chính, Một cửa | TT 25/2026 (rà soát) | T02 (một phần); không có UC tiếp nhận |
| Xét duyệt | PL3-78 đến 101 (giải quyết, trình, ký số, phê duyệt, phát hành) | NĐ 335 Điều 8 khoản 2: Chủ tịch UBND xã quyết định trong 7 ngày làm việc | Rà soát thường xuyên, định kỳ | Chưa có (T-THIẾU-02) |
| Tính chế độ | PL3-79 đến 84 | NĐ 335 Điều 6, 17 | | T09 |
| Chi trả | PL3-135, 136, 146, 192, 202 đến 204 | NĐ 335 Điều 8 khoản 2 (tổ chức chi trả) | | UC07, UC12 (đọc); chức năng chi trả: chưa có (T-THIẾU-07) |
| Điều chỉnh | PL3-102 đến 107 (đổi nơi thường trú, di chuyển hồ sơ, sửa thông tin) | NĐ 335 Điều 8 khoản 3, 4 | Đổi phân loại hộ theo kỳ | UC11 (phát hiện); quy trình: chưa có (T-THIẾU-05) |
| Tạm dừng, thôi hưởng | PL3-28, 68 đến 71, 130 đến 134; PL Điều 54 | NĐ 335 Điều 9 | | UC07, UC11 (phát hiện) |
| Truy lĩnh, truy thu | Không có mục PL3 riêng; NĐ 321 áp từ 01/7/2026 | NĐ 335 Điều 32 khoản 3, 4 | | Chưa có (T-THIẾU-03) |
| Quà, chế độ theo đợt | PL3-161, 162, 180 đến 182, 205 đến 208 | | | UC02 (thống kê); quản lý quà: chưa có |
| Ưu đãi không bằng tiền (BHYT, giáo dục, nhà ở, đất, vay vốn, thuế) | PL3-114 đến 123, 153, 154, 168 đến 171 | | | UC16 (một phần) |
| Điều dưỡng, phương tiện trợ giúp, cơ sở nuôi dưỡng | PL3-35, 108, 115, 116, 157 đến 160, 175 đến 179 | NĐ 335: chăm sóc tại cơ sở TGXH | | Chưa có (T-THIẾU-09) |
| Liệt sĩ, mộ, nghĩa trang | PL3-33, 58 đến 61 | | | Chưa có |
| Báo cáo, thống kê, dashboard | PL3-136 đến 197 | | | UC02, UC03 |
| Hỗ trợ ra quyết định | PL3-198 đến 201 | | UC15, UC17 | UC12, UC17, UC18 |
| Chất lượng dữ liệu, đối soát | PL3-52 đến 55, 72 đến 74, 148, 149 | | | UC01 |
| Quản trị (nhật ký, phân quyền, danh mục) | PL3-1 đến 35 | | | T04, T05, T10 (một phần) |

### 3.2. Người dùng theo cấp

Từ 01/7/2025 không còn cấp huyện (NĐ 128/2025, NĐ 129/2025, BC; QĐ 19/2025/QĐ-TTg chỉ có mã tỉnh, xã). Cột "Huyện" của khung chuẩn được thay bằng ghi chú.

| Cấp | Đơn vị | Vai trò dự kiến | Nguồn | Nhãn |
|---|---|---|---|---|
| Trung ương | Cục Người có công, Bộ Nội vụ | Chủ đầu tư; quản trị, báo cáo toàn quốc | PL3 tiêu đề | CÓ CĂN CỨ |
| Trung ương | Bộ Y tế | Chủ trì TGXH | NĐ 335 Điều 35 (CB) | CÓ CĂN CỨ (nếu G2 đúng) |
| Trung ương | Bộ NN&MT | CSDL hộ nghèo | XL:Căn cứ #17 đến 19 (BC) | GIẢ ĐỊNH |
| Trung ương | Cơ quan quản lý NCC thuộc BQP, BCA | Trao đổi hồ sơ, nhập tay | PL3-75 đến 77 | CÓ CĂN CỨ |
| Tỉnh | Sở Nội vụ, UBND tỉnh | Giải quyết hồ sơ NCC, báo cáo tỉnh | NĐ 128, 129/2025 (BC) | GIẢ ĐỊNH (cần quy trình thực tế, P1-07) |
| Tỉnh | HĐND tỉnh | Quyết định mức TGXH cao hơn | NĐ 335 Điều 4 khoản 3 (CB) | CÓ CĂN CỨ (nguồn tham số, không phải người dùng hệ thống) |
| Tỉnh | Cơ sở nuôi dưỡng, điều dưỡng NCC; cơ sở TGXH | Báo cáo đối tượng tại cơ sở | PL3-35, 157; NĐ 335 Điều 32 khoản 5 | CÓ CĂN CỨ |
| Huyện | Không còn | | | |
| Xã | Chủ tịch UBND xã, công chức phụ trách | Quyết định TGXH, rà soát danh sách chi | NĐ 335 Điều 8, Điều 32 khoản 4 (CB) | CÓ CĂN CỨ (TGXH); vai trò xã với NCC GIẢ ĐỊNH |
| Người dân | Đối tượng, thân nhân | Tra cứu qua VNeID | Dự thảo NĐ CSDL ASXH (BC) | GIẢ ĐỊNH |
| Nội bộ | Thanh tra, tài chính | Dùng cảnh báo chi sai | XL:UC06 đến UC08 | GIẢ ĐỊNH |

### 3.3. Hệ thống liên quan

| Hệ thống | Chiều dữ liệu theo PL3 | Nguồn | Nhãn |
|---|---|---|---|
| Hệ thống hiện hữu được nâng cấp hoặc chuyển đổi | Nguồn chuyển đổi | G3 | GIẢ ĐỊNH; tên chưa biết |
| HT giải quyết TTHC Bộ Nội vụ | Hai chiều | PL3-38 đến 45 | CÓ CĂN CỨ |
| CSDL quốc gia về dân cư | Vào (xác thực) | PL3-46, 47; NĐ 335 Điều 8 khoản 2 | CÓ CĂN CỨ |
| Trung tâm dữ liệu quốc gia | Ra | PL3-48, 49 | CÓ CĂN CỨ |
| CSDL quốc gia về ASXH | Hai chiều | PL3-50 đến 55 | CÓ CĂN CỨ |
| Trung tâm điều hành thông minh IOC | Ra | PL3-56, 57 | CÓ CĂN CỨ |
| CSDL liệt sĩ, mộ, nghĩa trang liệt sĩ | Chưa rõ | PL3-58 đến 61 | CÓ CĂN CỨ |
| Hệ thống nhận "người hưởng sai", "tài khoản người hưởng sai" qua API | Ra | PL3-62 đến 67 | CÓ CĂN CỨ; đơn vị nhận chưa biết |
| Cổng Dịch vụ công quốc gia | Vào (hồ sơ TGXH) | NĐ 335 Điều 8 khoản 1 (CB) | CÓ CĂN CỨ nếu có TGXH |
| Liên thông khai tử, mai táng phí (hộ tịch) | Vào (sự kiện mất) | NĐ 63/2024 sửa bởi NĐ 301/2026; NĐ 335 Điều 11 | CÓ CĂN CỨ; chưa đọc NĐ 301/2026 |
| Nền tảng chia sẻ, điều phối dữ liệu | Kênh kết nối bắt buộc chậm nhất 31/12/2026 | NĐ 278/2025 (BC) | GIẢ ĐỊNH |
| CSDL hộ nghèo (csdlhn.mae.gov.vn) | Vào | XL:Căn cứ #19 (BC) | GIẢ ĐỊNH |
| BHXH (BHYT, hưu trí xã hội) | Chưa rõ | PL3-114, 154 | GIẢ ĐỊNH |
| Ngân hàng, bưu điện chi trả | Chưa rõ | Đề án 06 (chi không dùng tiền mặt) | GIẢ ĐỊNH |

## 4. Checklist khảo sát có xếp ưu tiên (bước 4)

### 4.1. Cách xếp

Ưu tiên theo khối lượng phải làm lại nếu đoán sai:

1. **P1**: sai thì đổi phạm vi, mô hình lõi T07 hoặc bộ quy tắc T09. Hỏi trước, trong buổi đầu.
2. **P2**: sai thì phải sửa một nhóm UC hoặc một nhóm thực thể.
3. **P3**: sai thì sửa cục bộ.

Cột "Q" ghi mã câu hỏi đã có trong checklist bản `work/`, hoặc mã sẽ có nếu áp file đề xuất `tmp/project019_009_de_xuat_cap_nhat_checklist.json` (Q38 đến Q49). File này đã chạy thử trên bản sao `tmp/thu_de_xuat_009/thu.xlsx`, không áp vào `work/`.

### 4.2. Danh sách câu hỏi

| Mã | Ưu tiên | Câu hỏi | Q | Mở khóa | Lý do rủi ro |
|---|---|---|---|---|---|
| P1-01 | P1 | Phạm vi là người có công hay toàn bộ ASXH? Bên mình nhận trọn Phụ lục III hay chỉ phần phân tích? Nếu có TGXH (Bộ Y tế chủ trì) thì dữ liệu lấy theo thỏa thuận nào? | Q27, Q30 | Mọi T, UC; BR-01 đến 16 | Quyết định một nửa BR và UC08, UC10, UC13, UC15 có cần không |
| P1-02 | P1 | Hệ thống hiện hữu nào được nâng cấp hoặc chuyển đổi? Dữ liệu từ năm nào, khối lượng, ai đối soát sau chuyển đổi? | Q38 (mới); Q27 | T-THIẾU-01, T02, T03, T06 | Có thể là khối việc lớn nhất, hiện không có task |
| P1-03 | P1 | Khoản chênh tháng 7 đến 9/2026 đã chi truy lĩnh chưa? Dữ liệu chi trả có tách kỳ hưởng với ngày chi, có truy thu, thu hồi không? | Q39 (mới); Q32 | UC07, UC12; BR-13, BR-41 | Thiếu thì UC07 báo chi sai hàng loạt cho mọi người hưởng NCC và TGXH |
| P1-04 | P1 | Hồ sơ TGXH tiếp nhận trước 05/10/2026 chưa có quyết định được xét diện, hệ số theo văn bản nào? Người đang hưởng theo NĐ 20/2021 không còn thuộc diện NĐ 335 xử lý thế nào? | Q40 (mới) | BR-14, BR-15, UC07, UC09 | Văn bản chỉ nói thủ tục; sai thì cả lô hồ sơ chuyển tiếp bị đánh giá sai |
| P1-05 | P1 | Chuyển nơi cư trú, di chuyển hồ sơ NCC giữa tỉnh được ghi thế nào? Một người có thể có bản ghi đang hưởng ở hai tỉnh không? | Q41 (mới) | BR-06, UC07, UC11, UC14, E12 | Ảnh hưởng khóa và lịch sử của T06, T07 |
| P1-06 | P1 | Từ 01/01/2027 hệ thống có phải giải quyết hồ sơ theo ba bộ điều kiện (Điều 58, PL 05 Điều 2)? Có dự thảo nghị định thay NĐ 131/2021 không? Ai cung cấp danh mục diện, thân nhân phiên bản mới? | Q42 (mới) | BR-23, BR-25, BR-29; T04, T09 | Danh mục diện và quan hệ của T07 có hai phiên bản; chỉ còn hơn 2 tháng |
| P1-07 | P1 | Quy trình thực tế (ai nhập, ai thẩm định, ai quyết định ở Cục, Sở, xã) có khác văn bản không? Xin sơ đồ quy trình và quy chế phối hợp | Q43 (mới); Q20, Q21 | T10, PL3 mục D, UC02 | Phân quyền và luồng duyệt dựng theo văn bản có thể sai với thực tế |
| P1-08 | P1 | "7 nguồn" là những hệ thống nào, chiều nào? Có trùng 7 CSDL thành phần của dự thảo NĐ CSDL ASXH không? | Q28, Q37; Q12 | T02, T04, UC01 | Ước lượng T02 và mốc GĐ1a phụ thuộc trực tiếp |
| P1-09 | P1 | Mục H (chi trả, quà) bên mình xây chức năng hay chỉ nhận dữ liệu? Nếu xây, có gồm truy lĩnh, truy thu, thu hồi? | Q44 (mới); Q30 | T-THIẾU-07, E07 | Đổi E07 từ thực thể đọc sang thực thể ghi |
| P2-01 | P2 | Người không có số định danh được định danh bằng khóa nào ở từng nguồn? | Q34 | T06, E01 | |
| P2-02 | P2 | Nguồn có loại quan hệ thân nhân theo năm loại của Pháp lệnh và giấy tờ căn cứ không? Người thờ cúng ghi ở đâu? | Q45 (mới) | BR-23, BR-24, BR-26; UC10 | |
| P2-03 | P2 | Nguồn TGXH có quan hệ nhận chăm sóc và ngày sinh con của NKT không? | Q46 (mới) | BR-09, BR-11, BR-12; UC08, UC10 | |
| P2-04 | P2 | Sự kiện án phạt tù, xuất cảnh trái phép, mất tích nhận từ nguồn nào? | Q47 (mới) | BR-28; UC07, UC11 | |
| P2-05 | P2 | Địa phương đang xử lý ngoại lệ (đơn thân nghèo; tuất nhiều suất; NCC nhiều diện) bằng tay hay có trong hệ thống cũ? | (hỏi miệng, không thêm Q) | BR-03, BR-25, BR-26; UC06 | Ngoại lệ là nơi dữ liệu thực tế hay lệch văn bản |
| P2-06 | P2 | Tỉnh nào có mức TGXH do HĐND quyết định cao hơn, từ kỳ nào? | Q48 (mới) | BR-01, P-MUC-CHUAN-TGXH-TINH | |
| P2-07 | P2 | Nguồn có quyết định hưởng (số, ngày ký, loại) và kết quả giám định kèm ngày không? | Q31, Q33 | BR-04, BR-05; E09, E11 | |
| P2-08 | P2 | Dữ liệu lịch sử giữ từ năm nào, có snapshot theo kỳ không? | Q17 | T03, UC07 kỳ cũ, UC17 | |
| P2-09 | P2 | Báo cáo dùng biểu mẫu TT 18/2025/TT-BNV hay mẫu riêng của Cục? Định nghĩa "người đang hưởng" tại ngày chốt? | Q16, Q19 | UC02, UC03 | |
| P2-10 | P2 | Kết quả xử lý cảnh báo lưu ở đâu; mã hồ sơ ASXH đã cấp chưa? | Q35, Q36 | E16, UC19 | |
| P3-01 | P3 | Tên pháp nhân bên mình là VKX hay XVK? | Q49 (mới) | Tài liệu bàn giao | |
| P3-02 | P3 | Phụ lục III có mục F, E.IV không? Xin bản file | Q29 | Đối chiếu đủ yêu cầu | |
| P3-03 | P3 | Hạ tầng, mã nguồn, môi trường, ATTT | Q1 đến Q11, Q8 | T02, T10, T11 | Kỹ thuật, không gây làm lại nghiệp vụ |
| P3-04 | P3 | Thương mại, nghiệm thu, CR | Q18, Q22 đến Q26 | Lộ trình | |

### 4.3. Tài liệu cần xin

| # | Tài liệu | Phục vụ | Ưu tiên |
|---|---|---|---|
| 1 | Dự thảo hợp đồng đầy đủ dạng file (gồm Phụ lục III và các phụ lục khác) | P1-01, P3-02 | P1 |
| 2 | Tài liệu hệ thống hiện hữu: danh mục bảng, từ điển dữ liệu, sơ đồ quan hệ, khối lượng | P1-02 | P1 |
| 3 | Hồ sơ TKCS, TKKT của dự án (nếu có) | P1-01, P1-08 | P1 |
| 4 | Tài liệu API hoặc mô tả giao tiếp của từng nguồn | P1-08 | P1 |
| 5 | Mẫu danh sách chi trả một kỳ, kèm khoản truy lĩnh kỳ 10/2026, đã ẩn danh | P1-03 | P1 |
| 6 | Sơ đồ quy trình đang vận hành: giải quyết hồ sơ NCC, di chuyển hồ sơ, TGXH tại xã | P1-05, P1-07 | P1 |
| 7 | Dữ liệu mẫu đã ẩn danh của mỗi nguồn (một tỉnh, một kỳ) | P2-01 đến P2-04, UC01 | P2 |
| 8 | Danh mục dùng chung đang dùng: loại đối tượng, lý do chấm dứt, lý do từ chối, đơn vị | T04 | P2 |
| 9 | Biểu mẫu báo cáo đang nộp (Cục, Sở) | P2-09 | P2 |
| 10 | Nghị quyết HĐND tỉnh về mức TGXH; danh sách xã ĐBKK theo xã mới | P2-06, hệ số k7 | P2 |
| 11 | Quyết định tặng quà các đợt 2025 đến 2026 và danh sách nhận quà mẫu | BR-30 | P3 |

### 4.4. Đề xuất thay đổi checklist (chưa áp)

File: `tmp/project019_009_de_xuat_cap_nhat_checklist.json`. Áp bằng skill `ba-hop-khao-sat` khi người dùng đồng ý.

1. Thêm nhóm "Chuyển tiếp, truy lĩnh, chuyển vùng (agent BA 26/10/2026)" gồm 12 câu Q38 đến Q49 (mục 4.2).
2. Sheet "Căn cứ pháp lý" dòng #9, cột Ghi chú: thay "Chuyển tiếp tại Điều 32" bằng "chuyển mức tại Điều 32 khoản 3 đến 5; chuyển tiếp hồ sơ tại Điều 33", kèm nguồn Công báo.
3. Thêm dòng #38: NĐ 301/2026/NĐ-CP sửa NĐ 63/2024 (nhóm A).
4. Nối dòng nguồn tra cứu ngày 26/10/2026.

Đề xuất chưa có trong file JSON (cần người dùng quyết vì đụng nội dung sheet khác):

5. Sheet "Task & Usecase" UC06: ghi chú "Quy tắc mức cao nhất chỉ áp cho TGXH; NCC từ 01/01/2027 hưởng cộng dồn (PL 02/2020 sửa đổi Điều 6 khoản 3)".
6. Sheet "Task & Usecase" UC07: thêm "Đối chiếu theo kỳ hưởng, gộp truy lĩnh" vào cột Căn cứ / Giả định.
7. Sheet "Căn cứ pháp lý" dòng #37: thay "Chưa đọc chi tiết điều sửa đổi về thân nhân" bằng nội dung Điều 3 khoản 3 đã xác minh.
8. Sheet "Mô hình dữ liệu" ví dụ E04 "Bà A: NCT ≥75 hộ nghèo": thêm "không có người phụng dưỡng" cho đúng NĐ 335 Điều 5 khoản 5.
9. Sheet "Lộ trình": đổi "31/11" thành "30/11 (chờ xác nhận)" nếu khách hàng chưa trả lời Q22.

## 5. Cập nhật bản dựng theo biên bản (bước 5): bị chặn

Chưa thực hiện được. Lý do: không có biên bản khảo sát nào sau buổi họp.

Bằng chứng: tìm trong `input/`, `output/`, `work/` các tên chứa `bien_ban`, `khao_sat`, `hop` chỉ thấy hai file checklist và mẫu `.claude/skills/ba-hop-khao-sat/templates/bien_ban_hop.md`. Tại ngày 26/10/2026, checklist bản `work/` có 37 câu, cả 37 ở trạng thái "Chưa hỏi", cột trả lời và người phụ trách trống. Sheet "Task & Usecase" có 30 dòng, cả 30 ở trạng thái "Giả định". Cập nhật 28/10/2026 (đếm lại bằng openpyxl): checklist có 59 câu (Q1 đến Q59), cả 59 "Chưa hỏi"; sheet "Task & Usecase" có 36 dòng (T01 đến T16, UC01 đến UC20), cả 36 "Giả định".

Cần để mở khóa: biên bản hoặc ghi chú buổi họp với khách hàng (dán vào phiên mới, hoặc đặt vào `input/`). Khi có, dùng skill `ba-hop-khao-sat` mục B để ghi biên bản và cập nhật trạng thái ĐÃ XÁC NHẬN, BỊ BÁC BỎ, CÒN TREO cho các mục ở mục 1.

## 6. Đặc tả phần đã ổn định (bước 6, tóm tắt)

Đầy đủ: `output/project019_011_dac_ta_quy_tac_va_truy_vet.md`.

1. Không mục nào ĐÃ XÁC NHẬN. Phần CÓ CĂN CỨ ổn định là quy tắc chính sách từ văn bản, nên chỉ đặc tả phần này.
2. 30 quy tắc BR-01 đến BR-42: 23 ở trạng thái Đã đối chiếu (bản gốc NĐ 335/2026, VBHN 123/2026, VBHN 15/2026), 6 Chờ đối chiếu, BR-40 tách trạng thái theo lĩnh vực. Mỗi tham số mã P- có mốc áp dụng từ và đến.
3. Từ điển dữ liệu E21 VĂN BẢN, E22 THAM SỐ, E23 QUY TẮC.
4. 23 kịch bản kiểm thử mức quy tắc, dữ liệu giả.
5. Ma trận văn bản → BR → UC → kịch bản. Khoảng trống: PL3 mục D, H, PL3-14 đến 22 chưa có UC; 6 BR chưa có kịch bản.
6. Không đặc tả UC nào; danh sách UC chưa đặc tả và điều kiện ở mục 7 của 011.

## 7. Đề xuất mốc phạm vi (bước 7)

Đây là đề xuất để khách hàng và bên giao việc quyết, không phải quyết định của agent. Mọi phương án đều giữ T01 khảo sát toàn phạm vi.

### 7.1. Ba phương án cho đợt 1 (GĐ1a 15/11, GĐ1b 30/11)

| | Phương án A: Nền tảng người có công + bộ quy tắc | Phương án B: Toàn ASXH theo Lộ trình hiện tại | Phương án C: Phân tích trên kho hiện có |
|---|---|---|---|
| Đợt 1 gồm | T01; T02 cho 2 nguồn vào đã xác nhận trong PL3 (HT TTHC Bộ Nội vụ, CSDL dân cư); T03; T05; T06; T07 phần NCC và thân nhân; T09 với 23 BR đã đối chiếu; T10 tối thiểu; UC01; UC02 theo các biểu đồ PL3-163, 184, 185, 187 | GĐ1a và GĐ1b như sheet "Lộ trình": 17 task, UC; 7 nguồn; T07 và T08 đầy đủ người đến hộ đến quan hệ | T01; UC01, UC02, UC03 trên kho VNPT IT đang có (002, 003: PT01, PT02, DB01); không xây connector mới |
| Để sau | TGXH, giảm nghèo (UC05, UC08, UC10 phần TGXH, UC13, UC15 đến UC18); luồng chiều ra (PL3-48 đến 57, 62 đến 67); mục D, H | GĐ2, GĐ3 | Tích hợp (mục B PL3), chuyển đổi, quy tắc chi sai |
| Điều kiện | Q27 hoặc Q30 xác nhận NCC là phạm vi chính | Q27 xác nhận toàn ASXH; có tài liệu 7 nguồn trước 01/11 | Khách hàng chấp nhận demo không có tích hợp |
| Rủi ro | Nếu phạm vi là toàn ASXH: T07 phải mở rộng hộ và quan hệ chăm sóc (mô hình 007 đã tính trước nên phần làm lại vừa phải). Nếu việc thật là migrate: vẫn thiếu task chuyển đổi | Phạm vi Excel rộng hơn PL3; nguồn Bộ Y tế, Bộ NN&MT không có trong hợp đồng dự thảo; GĐ1a có 3 task mức Cao trong 20 ngày; chưa có ước lượng ngày công | Không đáp ứng PL3 mục B; nếu việc thật là migrate thì demo không chứng minh được năng lực chuyển đổi; dễ bị coi là thu hẹp phạm vi |
| Giá trị cho khách hàng | Bám tài liệu duy nhất khách hàng viết; bộ quy tắc NCC và TGXH đã sẵn để cấu hình | Phủ tất cả nhóm đã thảo luận 22/10 | Có sản phẩm nhìn thấy nhanh nhất |

### 7.2. Đề xuất của agent

Đề xuất trình **phương án A** làm mặc định cho buổi khảo sát, kèm hai điều kiện:

1. Nếu P1-02 xác nhận việc thật là chuyển đổi hệ thống, thêm một luồng "chuyển đổi dữ liệu" (T-THIẾU-01) vào đợt 1, ít nhất ở mức kiểm kê và đối soát mẫu. Không phương án nào ở trên có luồng này.
2. Nếu P1-01 xác nhận toàn ASXH, giữ khung phương án A nhưng chuyển T07 sang mô hình đầy đủ của 007 (nhóm A và B) và đưa BR-01 đến BR-16 vào nghiệm thu GĐ1b.

Lý do chọn A: Phụ lục III là tài liệu khách hàng duy nhất; BR cho cả hai lĩnh vực đã sẵn; A giữ được mốc 15/11 với số connector ít nhất. Rủi ro chung của mọi phương án: mốc 15/11 còn 20 ngày, chưa có ước lượng ngày công nào (cột ước lượng trống ở 30/30 dòng).

## 8. File tạo trong lượt chạy

| File | Nội dung |
|---|---|
| `output/project019_009_ket_qua_agent_ba.md` | File này |
| `output/project019_010_can_cu_phap_ly_va_tham_so_theo_ky.md` | Nhóm 2 |
| `output/project019_011_dac_ta_quy_tac_va_truy_vet.md` | Nhóm 5 |
| `tmp/project019_009_de_xuat_cap_nhat_checklist.json` | Đề xuất cập nhật checklist, chưa áp |
| `tmp/thu_de_xuat_009/thu.xlsx` | Bản chạy thử đề xuất, không phải sản phẩm |
| `tmp/van_ban_20261026/` | Bản lưu NĐ 335/2026 (Công báo), VBHN 123/2026 và văn bản trích |
| `tmp/zip_vkx_20261026/` | Ảnh giải nén từ zip, trùng thư mục ảnh trong `input/` |
| `tmp/tien_do_agent_ba.md` | File tiến độ |
