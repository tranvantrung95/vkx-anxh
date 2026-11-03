# Lịch sử thay đổi chính sách và các trường dữ liệu cần thiết kế

Ngày lập: 26/10/2026. Người lập: BA project019.

Cập nhật 28/10/2026: đổi số tài liệu từ 007 thành 017 (trước đây trùng số với `project019_007_ra_soat_mo_hinh_du_lieu.md`); đổi mã việc VL-10 đến VL-13 của tài liệu này thành VL-18 đến VL-21 để không trùng mã VL của 007; cập nhật trạng thái VL-20, VL-21.

Mục đích: với mỗi nhóm chính sách trong sheet "Căn cứ pháp lý", ghi lại tham số nào đã thay đổi, thay đổi khi nào, theo văn bản nào. Từ đó suy ra các trường dữ liệu phải có ngay từ thiết kế để hệ thống tính đúng cho từng kỳ, không phải sửa lại sau.

Mức tin cậy của số liệu, ghi ở cột "Nguồn" của từng bảng:

| Ký hiệu | Nghĩa |
|---|---|
| **CB** | Đã đọc toàn văn trên Công báo hoặc văn bản hợp nhất chính thức ngày 26/10/2026 |
| **TV** | Đã đọc toàn văn kèm phụ lục qua trang tổng hợp pháp luật (luatvietnam.vn, hethongphapluat.com) ngày 26/10/2026; chưa đối chiếu với bản ký số trên Công báo |
| **BC** | Theo báo chí, cổng địa phương, trang tổng hợp pháp luật; chưa đọc toàn văn. Trạng thái Chờ đối chiếu |
| **HB** | Theo hiểu biết của BA, chưa tra lại trong đợt này. Trạng thái Chờ đối chiếu |

Không dùng số liệu BC hoặc HB làm tiêu chí nghiệm thu trước khi đối chiếu.

## 1. Kết luận chính

1. **Mức tiền thay đổi gần như mỗi 1 đến 2 năm và hầu hết áp dụng từ ngày 01/7**, đi cùng đợt điều chỉnh lương cơ sở. Các năm 2019, 2023, 2024, 2026 đều có thay đổi.
2. **Văn bản thường ban hành sau ngày áp dụng.** NĐ 335/2026 ban hành 21/8/2026, hiệu lực 05/10/2026 nhưng áp mức mới từ 01/7/2026. NĐ 321/2026 cũng áp từ 01/7/2026. Hệ quả: các tháng 7, 8, 9/2026 chi theo mức cũ rồi **truy lĩnh** phần chênh. Nếu dữ liệu chi trả không đánh dấu khoản truy lĩnh, UC07 (chi sai) sẽ báo nhầm hàng loạt.
3. **Một văn bản có nhiều mốc áp dụng, và đây là khuôn lặp lại.** Nghị định mức hưởng người có công nào cũng tách hai nhóm điều. NĐ 75/2021 áp Điều 4, 5, 12 từ 01/7/2021 và Điều 6 đến 11, 13 từ 01/01/2022. NĐ 321/2026 áp Điều 4, 5, 8, 12 từ 01/7/2026 và Điều 6, 7, 9, 10, 11, 13 từ 01/01/2027. Các nghị định sửa đổi cũng vậy: điều dưỡng theo NĐ 55/2023 áp từ 01/01/2024, theo NĐ 77/2024 áp từ 01/01/2025 (TV).
4. **Mức hưởng hằng tháng người có công là bảng số tiền cụ thể trong phụ lục, không phải công thức.** Văn bản nói các mức điều chỉnh theo mức chuẩn và làm tròn đến nghìn đồng, nhưng số trong phụ lục không trùng khớp phép nhân. Ví dụ thương binh 100%: 6.589.000 nhân 3.012.000/2.055.000 ra 9.657.000, còn phụ lục NĐ 321/2026 ghi 9.656.000 (TV). Hệ thống phải nạp nguyên bảng phụ lục theo từng kỳ. Chỉ các khoản ghi "x lần mức chuẩn" mới tính bằng hệ số: trợ cấp một lần (Phụ lục IV), điều dưỡng, hỗ trợ học tập.
5. **Địa phương được quy định mức cao hơn.** Theo NĐ 335/2026 và NĐ 176/2025, HĐND tỉnh có thể quyết định mức chuẩn cao hơn hoặc hỗ trợ thêm. Tham số cần có phạm vi toàn quốc hoặc theo tỉnh.
6. **Diện đối tượng thay đổi, không chỉ mức tiền.** Từ 01/7/2025, người từ 75 tuổi không có lương hưu chuyển sang trợ cấp hưu trí xã hội theo Luật BHXH 2024. Trong NĐ 335/2026, diện người cao tuổi hưởng trợ giúp xã hội chỉ còn người cao tuổi thuộc hộ nghèo không có người phụng dưỡng.
7. **Tỷ lệ đóng BHXH bắt buộc ổn định ở tổng 32%.** Phần thay đổi trong vài năm gần đây là: giảm đóng tạm thời thời COVID; **căn cứ tính** chuyển từ lương cơ sở sang mức tham chiếu; **tỷ lệ ngân sách hỗ trợ** BHXH tự nguyện tăng từ 01/7/2025. Với module an sinh, các trường quan trọng là căn cứ tính và tỷ lệ hỗ trợ, không phải tỷ lệ đóng của doanh nghiệp.
8. **NĐ 321/2026 đổi cơ cấu, không chỉ tăng mức chuẩn 8%** (TV, mục 2.1.3): thêm diện con liệt sĩ dưới 18 tuổi hưởng 2 lần mức chuẩn; phụ cấp thương binh từ 81% tăng từ khoảng 0,5 lên 1,0 lần mức chuẩn; phụ cấp có vết thương đặc biệt nặng tăng từ khoảng 1,03 lên 2,0 lần. Các diện này cần trường ngày sinh của con và cờ "vết thương đặc biệt nặng".

## 2. Lịch sử theo nhóm chính sách

### 2.1. Người có công: mức chuẩn trợ cấp ưu đãi

#### 2.1.1. Mức chuẩn và mốc áp dụng

| Văn bản | Ban hành / hiệu lực | Mức chuẩn | Mốc áp dụng cho dữ liệu | Thay thế, sửa đổi | Nguồn |
|---|---|---|---|---|---|
| NĐ 58/2019/NĐ-CP | 01/7/2019 | 1.624.000 | 01/7/2019 | | HB |
| NĐ 75/2021/NĐ-CP | 24/7/2021 / 15/9/2021 | 1.624.000 | Điều 4, 5, 12 (mức hưởng, BHYT, xác định danh tính): 01/7/2021. Điều 6 đến 11, 13: 01/01/2022; trước đó các chế độ này vẫn theo NĐ 58/2019, NĐ 31/2013 | Thay NĐ 58/2019 (trừ các chế độ áp từ 2022) | TV (VBHN 834/VBHN-BLĐTBXH, Điều 15) |
| NĐ 55/2023/NĐ-CP | 21/7/2023 / 05/9/2023 | 2.055.000 | Phụ lục I đến IV và Điều 8, Phụ lục VI NĐ 75/2021: 01/7/2023. Điều dưỡng (Điều 6): 01/01/2024 | Sửa NĐ 75/2021 | TV (VBHN 834, chú thích Điều 2 NĐ 55/2023) |
| NĐ 77/2024/NĐ-CP | 01/7/2024 / 01/7/2024 | 2.789.000 | Mức hưởng, Điều 8, Phụ lục VI NĐ 75/2021, Phụ lục IV NĐ 55/2023: 01/7/2024. Điều dưỡng: 01/01/2025 | Sửa NĐ 75/2021; thay Phụ lục I, II, III NĐ 55/2023 | TV (Điều 2, Điều 3) |
| NĐ 321/2026/NĐ-CP | 15/8/2026 / 01/10/2026 | 3.012.000 | Điều 4, 5, 8, 12: 01/7/2026 (riêng giám định ADN theo NQ 26/2026/NQ-CP đến trước 01/8/2027). Điều 6, 7, 9, 10, 11, 13: 01/01/2027; đến hết 31/12/2026 các chế độ này vẫn theo NĐ 75/2021, 55/2023, 77/2024 | NĐ 75/2021, 55/2023, 77/2024 hết hiệu lực từ 01/10/2026, trừ các chế độ áp đến hết 2026 (Điều 15 khoản 4) | TV (Điều 3, Điều 15) |

Hệ quả với dữ liệu:

1. Trong cùng một tháng có thể hai văn bản cùng áp dụng. Ví dụ tháng 11/2026: mức trợ cấp hằng tháng theo NĐ 321/2026, còn điều dưỡng vẫn theo NĐ 77/2024.
2. Thân nhân của 1 liệt sĩ (không phải con dưới 18 tuổi) hưởng 2.789.000 đồng cho tháng 6/2026 và 3.012.000 đồng cho tháng 7/2026. Khoản tháng 7 có thể được chi trong tháng 10/2026 dưới dạng truy lĩnh.

#### 2.1.2. Mức hưởng hằng tháng qua ba kỳ (đồng/tháng)

Trích Phụ lục I, II, III. Nguồn TV: kỳ 2023 lấy từ VBHN 834/VBHN-BLĐTBXH (NĐ 75/2021 hợp nhất NĐ 55/2023); kỳ 2024 lấy từ NĐ 77/2024; kỳ 2026 lấy từ NĐ 321/2026. Cột "Tỷ lệ 2026" bằng mức 2026 chia mức chuẩn 3.012.000.

| Diện | Từ 01/7/2023 | Từ 01/7/2024 | Từ 01/7/2026 | Tỷ lệ 2026 |
|---|---|---|---|---|
| Người HĐCM trước 01/01/1945, diện thoát ly (cộng phụ cấp mỗi năm thâm niên) | 2.297.000 + 390.000 | 3.117.000 + 529.000 | 3.366.000 + 571.000 | 1,12 + 0,19 |
| Người HĐCM trước 01/01/1945, diện không thoát ly | 3.899.000 | 5.291.000 | 5.714.000 | 1,90 |
| Thân nhân của 01 liệt sĩ | 2.055.000 | 2.789.000 | 3.012.000 (trừ con dưới 18 tuổi) | 1,0 |
| **Con liệt sĩ chưa đủ 18 tuổi** | không có mục riêng | không có mục riêng | **6.024.000** | **2,0** |
| Thân nhân của 03 liệt sĩ trở lên | 6.165.000 | không trích | 9.036.000 | 3,0 |
| Trợ cấp tuất nuôi dưỡng (cộng thêm) | 1.644.000 | 2.231.000 | 2.410.000 | 0,8 |
| Bà mẹ Việt Nam anh hùng: trợ cấp / phụ cấp | 6.165.000 / 1.722.000 | 8.367.000 / 2.337.000 | 9.036.000 / 2.524.000 | 3,0 / 0,84 |
| **Phụ cấp thương binh, người hưởng chính sách như thương binh, thương binh loại B từ 81%** | 1.031.000 | 1.399.000 | **3.012.000** | **1,0** (trước khoảng 0,5) |
| **Phụ cấp như trên, có vết thương đặc biệt nặng** | 2.113.000 | 2.867.000 | **6.024.000** | **2,0** (trước khoảng 1,03) |
| Phụ cấp bệnh binh từ 81% / có bệnh tật đặc biệt nặng | 1.031.000 / 2.055.000 | không trích | 1.511.000 / 3.012.000 | 0,5 / 1,0 |
| Người phục vụ thương binh hoặc bệnh binh từ 81% đặc biệt nặng | 2.640.000 | 3.582.000 (thương binh) | 3.869.000 (mục 12.2, 12.3) | 1,28 |
| Thương binh 21% / 100% (Phụ lục II, 80 bậc theo từng %) | 1.384.000 / 6.589.000 | 1.878.000 / 8.941.000 | 2.028.000 / 9.656.000 | |
| Thương binh loại B 21% / 100% (Phụ lục III) | 1.144.000 / 5.451.000 | 1.552.000 / 7.397.000 | 1.676.000 / 7.989.000 | |
| Bệnh binh 41% đến 50% | 2.145.000 | 2.911.000 | 3.144.000 | |
| Nhiễm chất độc hóa học 21% đến 40% | 1.562.000 | 2.120.000 | 2.290.000 | |
| Con thương binh 21% đến 60% đang đi học (mục 11.2) | 1.031.000 | 1.399.000 | 1.511.000 | 0,5 |

"Không trích" nghĩa là chưa lấy số từ văn bản trong đợt này, không phải văn bản không có mục đó. Bảng đầy đủ ba kỳ (56 dòng Phụ lục I, 80 bậc Phụ lục II và III, hệ số Phụ lục IV và VI) nằm ở sheet "Tham số NCC" của `work/project019_005_checklist_hop_dang_cap_nhat.xlsx`.

Trợ cấp một lần (Phụ lục IV) giữ nguyên hệ số qua các kỳ (TV):

| Khoản | Hệ số |
|---|---|
| Thân nhân người HĐCM trước 1945 chết chưa hưởng chế độ / người không phải thân nhân | 31,0 / 6,2 lần mức chuẩn |
| Thân nhân người HĐCM 1945 chết chưa hưởng chế độ / người không phải thân nhân | 15,5 / 6,2 lần |
| Truy tặng Bằng Tổ quốc ghi công | 20,0 lần |
| Hỗ trợ báo tử | 1,0 lần |
| Kháng chiến | 0,3 lần mỗi năm thâm niên |

Năm 2026 NĐ 321 ghi đối tượng theo điều, khoản của Pháp lệnh 02/2020, không mô tả bằng lời như trước. Bảng mã đối tượng cần ánh xạ hai cách gọi này.

#### 2.1.3. Thay đổi cơ cấu trong NĐ 321/2026 (TV)

1. **Diện mới:** con liệt sĩ chưa đủ 18 tuổi hưởng 2,0 lần mức chuẩn (mục 3.1); các mục thân nhân 01 và 02 liệt sĩ loại trừ diện này. Mức hưởng đổi khi con đủ 18 tuổi, nên cần ngày sinh của con và quy tắc chuyển mức theo tháng.
2. **Phụ cấp thương binh từ 81%** tăng tỷ lệ: 1,0 lần (trước khoảng 0,5) và 2,0 lần nếu có vết thương đặc biệt nặng (trước khoảng 1,03). Phụ cấp bệnh binh và người nhiễm chất độc hóa học giữ tỷ lệ cũ (0,5 và 1,0).
3. **Người phục vụ** được gom thành mục 12 của Phụ lục I: người phục vụ người có công sống ở gia đình 3.012.000; người phục vụ thương binh hoặc bệnh binh từ 81% đặc biệt nặng 3.869.000.
4. Mục 11 đổi tên thành "theo học tại các cơ sở giáo dục thuộc hệ thống giáo dục quốc dân đến trình độ đại học".
5. Điều dưỡng tập trung: thêm khoản tham quan; trần "các khoản chi khác" giảm từ 15% xuống 10% (áp từ 01/01/2027).
6. Thuật ngữ "từ trần" trong các mục thân nhân đổi thành "chết".

### 2.2. Trợ giúp xã hội (bảo trợ xã hội)

| Áp dụng từ | Mức chuẩn (đồng/tháng) | Văn bản | Nguồn |
|---|---|---|---|
| 01/01/2014 | 270.000 | NĐ 136/2013/NĐ-CP | HB |
| 01/7/2021 | 360.000 | NĐ 20/2021/NĐ-CP | BC |
| 01/7/2024 | 500.000 | NĐ 76/2024/NĐ-CP, sửa NĐ 20/2021 | BC |
| 01/7/2026 | 540.000 | NĐ 335/2026/NĐ-CP, Điều 4 khoản 2 và Điều 32 khoản 3 (hiệu lực 05/10/2026; thay NĐ 20/2021 và NĐ 76/2024) | **CB** |

Hệ số trợ cấp xã hội hằng tháng theo NĐ 335/2026 (Điều 6, nguồn **CB**):

| Nhóm (khoản Điều 5) | Điều kiện phân hệ số | Hệ số |
|---|---|---|
| Trẻ em mồ côi, bị bỏ rơi (k1) | dưới 4 tuổi / từ đủ 4 tuổi | 2,5 / 1,5 |
| Người từ 16 tuổi đang học (k2) | | 1,5 |
| Trẻ em nhiễm HIV hộ nghèo (k3) | dưới 4 tuổi / 4 đến dưới 16 tuổi | 2,5 / 2,0 |
| Đơn thân nghèo nuôi con (k4) | mỗi con đang nuôi | 1,0 |
| Người cao tuổi hộ nghèo (k5a) | 60 đến dưới 75 tuổi / từ đủ 75 tuổi | 1,5 / 2,0 |
| Người cao tuổi được nhận chăm sóc tại cộng đồng (k5b) | | 3,0 |
| Người khuyết tật (k6) | đặc biệt nặng / trẻ em hoặc NCT đặc biệt nặng / nặng / trẻ em hoặc NCT nặng | 2,0 / 2,5 / 1,5 / 2,0 |
| Trẻ dưới 3 tuổi hộ nghèo, cận nghèo vùng DTTS đặc biệt khó khăn (k7); người nhiễm HIV hộ nghèo (k8) | | 1,5 |

Quy tắc liên quan (nguồn **CB**):

1. Nhiều hệ số hoặc nhiều văn bản: chỉ hưởng một mức cao nhất. Ngoại lệ: đơn thân nghèo nuôi con thuộc k5, k6, k8 được hưởng cả chế độ k4 (Điều 6 khoản 2).
2. Hỗ trợ chăm sóc (Điều 17):
   1. Người khuyết tật mang thai hoặc nuôi con dưới 36 tháng: 1,5 hoặc 2,0. Vợ chồng cùng khuyết tật chỉ được một suất.
   2. Hộ đang chăm sóc người khuyết tật đặc biệt nặng: 1,0.
   3. Nhận nuôi người khuyết tật đặc biệt nặng: 1,5. Nhận nuôi trẻ em khuyết tật đặc biệt nặng: 2,5.
3. Mai táng: tối thiểu 20 lần mức chuẩn. Trùng nhiều văn bản thì hưởng một mức cao nhất (Điều 11).
4. Mốc thời gian (Điều 8, Điều 9):
   1. Hưởng từ tháng Chủ tịch UBND xã ký quyết định.
   2. Thôi hưởng từ tháng ngay sau tháng chết hoặc không còn đủ điều kiện.
   3. Điều chỉnh mức từ tháng thay đổi điều kiện.
   4. Chuyển nơi cư trú: hưởng ở nơi mới từ tháng thôi chi trả ở nơi cũ.
   5. Tạm dừng khi không nhận liên tục từ 3 tháng.
   6. Hết tạm dừng mà vẫn đủ điều kiện: được hưởng lại từ thời điểm tạm dừng.

### 2.3. Trợ cấp hưu trí xã hội (thuộc Luật BHXH 2024)

| Áp dụng từ | Nội dung | Văn bản | Nguồn |
|---|---|---|---|
| 01/7/2025 | Chế độ mới: từ đủ 75 tuổi, không có lương hưu hoặc có nhưng thấp hơn mức này; hoặc từ đủ 70 đến dưới 75 tuổi thuộc hộ nghèo, cận nghèo. Mức 500.000 đồng/tháng | Luật 41/2024/QH15 Điều 21; NĐ 176/2025/NĐ-CP | **CB** (VBHN 15/2026/VBHN-NĐ-BYT) |
| 01/7/2026 | Mức 540.000 đồng/tháng. Nếu đồng thời thuộc diện trợ cấp xã hội thì hưởng mức cao hơn | NĐ 335/2026 Điều 31 sửa NĐ 176/2025; Điều 32 khoản 3 | **CB** |

Thời điểm hưởng: từ tháng Chủ tịch UBND xã ký quyết định (VBHN 15/2026, Điều 4).

### 2.4. Lương cơ sở và mức tham chiếu

| Áp dụng từ | Lương cơ sở (đồng/tháng) | Văn bản | Nguồn |
|---|---|---|---|
| 01/7/2019 | 1.490.000 | NĐ 38/2019/NĐ-CP | HB |
| 01/7/2023 | 1.800.000 | NĐ 24/2023/NĐ-CP | HB |
| 01/7/2024 | 2.340.000 | NĐ 73/2024/NĐ-CP | BC |
| 01/7/2026 | 2.530.000 | NĐ 161/2026/NĐ-CP (ban hành 15/5/2026) | BC |

Từ 01/7/2025, Luật BHXH 2024 dùng **mức tham chiếu**. Khi lương cơ sở chưa bãi bỏ thì mức tham chiếu bằng lương cơ sở (BC). Các khoản tính theo hai đại lượng này:

1. Mức đóng BHYT của nhóm do ngân sách đóng: 4,5% lương cơ sở.
2. Trần đóng BHXH: 20 lần mức tham chiếu, bằng 50.600.000 đồng từ 01/7/2026 (BC).
3. Trợ cấp mai táng BHXH: 10 lần mức tham chiếu (BC).

Mức đóng BHYT mỗi người mỗi tháng của nhóm ngân sách đóng, tính theo công thức 4,5% nhân lương cơ sở (BC):

| Áp dụng từ | Mức đóng |
|---|---|
| 01/7/2019 | 67.050đ |
| 01/7/2023 | 81.000đ |
| 01/7/2024 | 105.300đ |
| 01/7/2026 | 113.850đ |

### 2.5. Bảo hiểm xã hội và bảo hiểm y tế

**BHXH bắt buộc.** Tổng tỷ lệ đóng 32% trên tiền lương làm căn cứ đóng (BC):

| Bên đóng | Tổng | Gồm |
|---|---|---|
| Người lao động | 10,5% | Hưu trí, tử tuất 8%; thất nghiệp 1%; BHYT 1,5% |
| Người sử dụng lao động | 21,5% | Hưu trí, tử tuất 14%; ốm đau, thai sản 3%; tai nạn lao động, bệnh nghề nghiệp 0,5%; thất nghiệp 1%; BHYT 3% |

Các lần giảm đóng tạm thời gần đây (BC):

| Khoản đóng | Mức giảm | Thời gian | Văn bản |
|---|---|---|---|
| Tai nạn lao động, bệnh nghề nghiệp (người sử dụng lao động) | 0% | 01/7/2021 đến 30/6/2022 | NQ 68/NQ-CP |
| Thất nghiệp (người sử dụng lao động) | 0% | 01/10/2021 đến 30/9/2022 | NQ 116/NQ-CP |

Mức 0,3% tai nạn lao động cho doanh nghiệp đủ điều kiện theo NĐ 58/2020 chưa xác nhận được (HB).

**BHXH tự nguyện.** Tỷ lệ đóng 22% trên thu nhập tự chọn; mức thấp nhất là chuẩn nghèo nông thôn. Ngân sách hỗ trợ tính theo % của mức đóng tính trên chuẩn nghèo nông thôn:

| Áp dụng từ | Hộ nghèo | Hộ cận nghèo | Dân tộc thiểu số | Đối tượng khác | Văn bản | Nguồn |
|---|---|---|---|---|---|---|
| 01/01/2018 | 30% | 25% | không có mức riêng | 10% | NĐ 134/2015/NĐ-CP | HB |
| 01/7/2025 | 50% (gồm cả xã đảo, đặc khu) | 40% | 30% | 20% | NĐ 159/2025/NĐ-CP Điều 5 khoản 1 | BC |

Theo NĐ 159/2025: hỗ trợ tối đa 120 tháng; thuộc nhiều nhóm thì hưởng mức cao nhất. Chuẩn nghèo nông thôn dùng làm căn cứ là 1.500.000 đồng đến hết 31/12/2026 (BC).

**BHYT** theo Luật 51/2024/QH15 (hiệu lực 01/7/2025) và NĐ 188/2025/NĐ-CP (BC):

1. Mức đóng 4,5%.
2. Ngân sách đóng 100% cho người có công, hộ nghèo, trẻ dưới 6 tuổi.
3. Hộ cận nghèo được hỗ trợ tối thiểu 70%; hộ cận nghèo ở xã nghèo được 100%.
4. Học sinh, sinh viên được hỗ trợ tối thiểu 50%.
5. Hộ làm nông, lâm, ngư nghiệp có mức sống trung bình được hỗ trợ tối thiểu 30%.
6. Tỷ lệ đóng giảm dần theo thành viên hộ gia đình tự đóng: người thứ 2 đóng 70%, người thứ 3 đóng 60%, người thứ 4 đóng 50%, từ người thứ 5 đóng 40% mức của người thứ nhất.
7. Địa phương có thể hỗ trợ thêm.

### 2.6. Chuẩn nghèo

| Giai đoạn áp dụng | Chuẩn thu nhập nghèo (nông thôn / thành thị, đồng/người/tháng) | Văn bản | Nguồn |
|---|---|---|---|
| 2016 đến 2021 | 700.000 / 900.000 | QĐ 59/2015/QĐ-TTg | HB |
| 2022 đến hết 2026 | 1.500.000 / 2.000.000 | NĐ 07/2021/NĐ-CP (kéo dài hết 2026) | BC |
| Từ 2027 | 2.200.000 / 2.800.000, kèm chỉ số thiếu hụt dịch vụ xã hội | NĐ 351/2025/NĐ-CP (hiệu lực 15/02/2026) | BC |

Quy trình rà soát theo TT 25/2026/TT-BNNMT (BC): rà soát thường xuyên từ 1/1 đến 31/8; rà soát định kỳ từ 1/9 đến 14/12 hằng năm, bắt đầu từ năm 2027.

Hệ quả với dữ liệu:

1. Phân loại hộ (nghèo, cận nghèo, mức sống trung bình) chỉ đúng **trong kỳ rà soát và theo bộ chuẩn của kỳ đó**.
2. Cùng một hộ có thể là hộ nghèo năm 2026 nhưng không còn nghèo năm 2027 dù thu nhập không đổi, vì chuẩn tăng. Các chính sách khác dùng tiêu chí hộ nghèo cũng đổi theo: TGXH k4, k5, k7, k8; hưu trí xã hội cho người từ 70 tuổi; BHYT; BHXH tự nguyện.

### 2.7. Địa bàn

Từ 01/7/2025, mã tỉnh, xã đổi theo QĐ 19/2025/QĐ-TTg và không còn cấp huyện. Danh sách xã, thôn đặc biệt khó khăn được phê duyệt lại cho giai đoạn 2026 đến 2030 theo NĐ 272/2025/NĐ-CP. Hệ số k7 của NĐ 335/2026 phụ thuộc danh sách này (BC).

### 2.8. Chế độ theo đợt

| Chế độ | Quy luật | Ví dụ |
|---|---|---|
| Quà Chủ tịch nước cho người có công | Quyết định riêng cho mỗi dịp Tết và 27/7 | Tết 2026: QĐ 01/QĐ-CTN, 600.000đ hoặc 300.000đ, mỗi người một suất mức cao nhất (BC) |
| Hỗ trợ nhà ở người có công | Theo giai đoạn | QĐ 21/2024/QĐ-TTg, áp dụng đến 31/12/2025 (BC) |

## 3. Các trường dữ liệu cần thiết kế

### 3.1. Bảng tham số chính sách (T09)

Mỗi dòng là một giá trị tham số trong một khoảng thời gian:

| Trường | Ý nghĩa | Lý do (mục 1, 2) |
|---|---|---|
| ma_tham_so | Ví dụ P-MUC-CHUAN-NCC, P-MUC-CHUAN-TGXH, P-LUONG-CO-SO, P-CHUAN-NGHEO-NT | |
| gia_tri, don_vi | Số tiền, hệ số hoặc tỷ lệ | |
| pham_vi, ma_tinh | Toàn quốc hoặc theo tỉnh (mức HĐND tỉnh quyết định cao hơn) | Kết luận 5 |
| ap_dung_tu, ap_dung_den | Mốc áp dụng cho dữ liệu | Kết luận 1, 3 |
| so_hieu_van_ban, dieu_khoan | Văn bản và điều khoản quy định giá trị | |
| ngay_ban_hanh, ngay_hieu_luc_van_ban | Tách khỏi ap_dung_tu | Kết luận 2 |
| van_ban_thay_the | Văn bản thay thế dòng này | |
| trang_thai_doi_chieu | Đã đối chiếu / Chờ đối chiếu / Dự thảo | Quy ước BA |

### 3.2. Bảng hệ số theo chế độ

| Trường | Ý nghĩa |
|---|---|
| ma_che_do, nhom_doi_tuong | Ví dụ TGXH-K6-NKT-DBN |
| dieu_kien_tuoi_tu, dieu_kien_tuoi_den | Ngưỡng tuổi phân hệ số (4, 16, 60, 75; 36 tháng của con) |
| muc_do_khuyet_tat, ty_le_ton_thuong_tu, ty_le_ton_thuong_den | Điều kiện phân hệ số |
| he_so | |
| quy_tac_lam_tron | Ví dụ làm tròn đến nghìn đồng (người có công) |
| ap_dung_tu, ap_dung_den, so_hieu_van_ban, dieu_khoan | |
| nhom_loai_tru, ngoai_le | Quy tắc chỉ hưởng mức cao nhất và ngoại lệ đơn thân |

### 3.3. Hồ sơ hưởng (bổ sung so với sheet "Mô hình dữ liệu")

| Trường | Lý do |
|---|---|
| ngay_ky_quyet_dinh, thang_bat_dau_huong | Hưởng từ tháng ký quyết định |
| thang_ket_thuc_huong, ly_do_thoi_huong, ngay_su_kien | Thôi hưởng từ tháng sau tháng chết, không đủ điều kiện |
| trang_thai (đang hưởng / tạm dừng / thôi hưởng), ngay_tam_dung, ly_do_tam_dung | Tạm dừng 3 tháng, được hưởng lại từ thời điểm tạm dừng |
| ma_xa_chi_tra, thang_chuyen_den | Chuyển nơi cư trú |
| he_so_ap_dung, ma_he_so | Truy được hệ số nào đang dùng |
| muc_huong_theo_quyet_dinh | Đối chiếu với mức tính lại theo tham số |
| can_cu_van_ban | Văn bản căn cứ của quyết định |

### 3.4. Chi trả

| Trường | Lý do |
|---|---|
| ky_huong (tháng/năm thuộc về) | Khác với ngày chi |
| ngay_chi | |
| loai_khoan_chi: thường kỳ / truy lĩnh / truy thu / một lần | Phân biệt khoản chênh do văn bản ban hành muộn |
| truy_linh_tu_ky, truy_linh_den_ky | |
| muc_chuan_tai_ky, he_so_tai_ky | Lưu giá trị dùng để tính tại thời điểm chi |
| so_tien, phuong_thuc, ma_tai_khoan_da_che | |

Quy tắc kiểm tra chi sai (UC07) phải so số tiền **theo kỳ hưởng** với tham số áp dụng cho kỳ đó, sau khi cộng khoản truy lĩnh của cùng kỳ.

### 3.5. Thuộc tính người và hộ phục vụ tính toán

| Trường | Lý do |
|---|---|
| ngay_sinh (đủ ngày, tháng) | Hệ số đổi khi qua 4, 16, 60, 75 tuổi; hưu trí xã hội từ 70, 75 tuổi |
| ngay_mat, nguon_ngay_mat (hộ tịch, CSDL dân cư) | Thôi hưởng, mai táng, tuất |
| muc_do_khuyet_tat, ngay_xac_dinh | Hệ số k6 |
| ty_le_ton_thuong_co_the (theo từng %) | Phụ lục II, III có 80 bậc từ 21% đến 100% |
| co_vet_thuong_dac_biet_nang, co_benh_tat_dac_biet_nang | Phụ cấp 2,0 lần (thương binh) hoặc 1,0 lần (bệnh binh) từ 01/7/2026 |
| loai_doi_tuong_ncc, dieu_khoan_phap_lenh | Ánh xạ cách gọi theo lời (NĐ 75/2021) và theo điều, khoản Pháp lệnh 02/2020 (NĐ 321/2026) |
| dang_huong_luong_huu_bhxh, muc_luong_huu_bhxh | Điều kiện hưu trí xã hội, k8 |
| phan_loai_ho, chuan_ngheo_ap_dung, nam_ra_soat, ky_ra_soat | Kết quả hộ nghèo chỉ đúng trong kỳ và theo chuẩn |
| ma_dia_ban_cu, ma_dia_ban_moi, ngay_hieu_luc_ma | Mã đổi từ 01/7/2025 |
| thuoc_vung_dbkk, giai_doan_vung | Hệ số k7 |

### 3.6. BHYT và BHXH tự nguyện (nếu có trong phạm vi, UC16)

| Trường | Lý do |
|---|---|
| ma_doi_tuong_bhyt, ty_le_nsnn_ho_tro, can_cu_tinh (lương cơ sở / mức tham chiếu), han_the | Mức đóng đổi theo lương cơ sở; tỷ lệ hỗ trợ theo nhóm |
| nhom_ho_tro_bhxh_tn, ty_le_ho_tro, chuan_ngheo_nong_thon_can_cu, so_thang_da_ho_tro | Tỷ lệ đổi từ 01/7/2025; trần 120 tháng |

## 4. Việc cần làm

| Mã | Việc | Trạng thái |
|---|---|---|
| VL-18 | Đọc NĐ 321/2026, NĐ 55/2023, NĐ 77/2024 để chốt bảng 2.1 | Xong ngày 26/10/2026 qua trang tổng hợp (TV). Còn lại: đối chiếu bản ký số Công báo; trích đủ Phụ lục II, III (80 bậc) và Phụ lục VI vào bảng tham số |
| VL-19 | Đối chiếu NĐ 20/2021 với NĐ 335/2026 để lập bảng chuyển đổi diện người cao tuổi và hệ số cho dữ liệu cũ | Chưa làm |
| VL-20 | Hỏi bên giao việc: dữ liệu chi trả ở các nguồn có phân biệt khoản truy lĩnh và kỳ hưởng không (thêm vào checklist) | Đã thêm vào checklist (Q32, Q39); chờ buổi khảo sát |
| VL-21 | Đưa bảng tham số 3.1 và 3.2 vào đặc tả T09 (skill `ba-quy-tac-truy-vet`), mỗi tham số một mã dạng P-MUC-CHUAN-NCC | Một phần: `output/project019_011_dac_ta_quy_tac_va_truy_vet.md` mục 2 đã có tham số P-; chưa chép sổ sang `work/` |

## 5. Nguồn

Công báo, văn bản chính thức (CB):

1. [NĐ 335/2026/NĐ-CP, Công báo](https://congbaocdn.chinhphu.vn/180507251028987904/2026/9/4/470340-1787910774_1788515182_signed.docx)
2. [VBHN 15/2026/VBHN-NĐ-BYT](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/9/15-vbhn-byt.signed.pdf)

Toàn văn qua trang tổng hợp (TV):

1. [NĐ 321/2026/NĐ-CP, luatvietnam.vn](https://luatvietnam.vn/lao-dong/nghi-dinh-321-2026-nd-cp-quy-dinh-tro-cap-phu-cap-cho-nguoi-co-cong-voi-cach-mang-444621-d1.html)
2. [NĐ 77/2024/NĐ-CP, hethongphapluat.com](https://hethongphapluat.com/du-thao-nghi-dinh-sua-doi-nghi-dinh-75-2021-nd-cp-ve-quy-dinh-muc-huong-tro-cap-phu-cap-va-cac-che-do-uu-dai-nguoi-co-cong-voi-cach-mang-da-duoc-sua-doi-theo-nghi-dinh-55-2023-nd-cp.html) (đường dẫn có chữ "du-thao" nhưng nội dung là văn bản số 77/2024/NĐ-CP ngày 01/7/2024)
3. [VBHN 834/VBHN-BLĐTBXH năm 2024 (NĐ 75/2021 hợp nhất NĐ 55/2023), hethongphapluat.com](https://hethongphapluat.com/van-ban-hop-nhat-834-vbhn-bldtbxh-nam-2024-hop-nhat-nghi-dinh-quy-dinh-muc-huong-tro-cap-phu-cap-va-cac-che-do-uu-dai-nguoi-co-cong-voi-cach-mang-do-bo-lao-dong-thuong-binh-va-xa-hoi-ban-hanh.html)

Báo chí, trang tổng hợp (BC):

1. Người có công:
   1. [luatvietnam.vn: NĐ 321/2026](https://luatvietnam.vn/linh-vuc-khac/nghi-dinh-321-2026-nd-cp-quy-dinh-muc-tro-cap-phu-cap-nguoi-co-cong-nhu-the-nao-883-113559-article.html)
   2. [nhandan.vn](https://nhandan.vn/nhung-quy-dinh-moi-ve-che-do-uu-dai-nguoi-co-cong-voi-cach-mang-post991849.html)
   3. [hdndtuyenquang.gov.vn](https://hdndtuyenquang.gov.vn/van-ban-nghi-quyet/van-ban-moi!/nghi-dinh-321-2026-nd-cp-tiep-tuc-hoan-thien-chinh-sach-uu-dai-cham-lo-tot-hon-nguoi-co-cong-voi-cach-mang-9240.html)
   4. [thuvienphapluat.vn: mức chuẩn tăng 26%](https://thuvienphapluat.vn/lao-dong-tien-luong/muc-chuan-tro-cap-uu-dai-nguoi-co-cong-voi-cach-mang-tang-hon-26-co-dung-khong-7419.html)
   5. [baovanhoa.vn: NĐ 77/2024](https://baovanhoa.vn/doi-song/muc-chuan-tro-cap-uu-dai-nguoi-co-cong-tang-cao-nhat-20-nam-qua-98126.html)
2. Trợ giúp xã hội: [hcc.nghean.gov.vn](https://hcc.nghean.gov.vn/tin-tong-hop/chinh-phu-nang-muc-chuan-tro-giup-xa-hoi-1417.html), [tapchicongthuong.vn](https://tapchicongthuong.vn/tu-1-7-tang-muc-chuan-tro-giup-xa-hoi-123182.htm)
3. Lương cơ sở, mức tham chiếu:
   1. [tapchicongthuong.vn: lương cơ sở 2026](https://tapchicongthuong.vn/chinh-thuc-tang-luong-co-so-len-2-530-000-dong-thang-tu-01-7-2026-518417.htm)
   2. [vneconomy.vn](https://vneconomy.vn/muc-tien-cac-khoan-bao-hiem-tang-theo-luong-co-so-tu-17.htm)
   3. [thuvienphapluat.vn: mức đóng tối đa](https://thuvienphapluat.vn/hoi-dap-phap-luat/muc-dong-bhxh-toi-da-tu-ngay-0172026-la-bao-nhieu-138091227.html)
4. BHXH:
   1. [joboko.com](https://vn.joboko.com/blog/muc-dong-bao-hiem-xa-hoi-nwi5821)
   2. [luatvietnam.vn: mức đóng 2026](https://luatvietnam.vn/bao-hiem/tu-2026-muc-dong-bhxh-bhyt-bhtn-cua-nld-va-nsdld-duoc-tinh-nhu-the-nao-563-106906-article.html)
   3. [lsvn.vn: NQ 116](https://lsvn.vn/doanh-nghiep-nho-va-vua-duoc-giam-muc-dong-bao-hiem-that-nghiep-bang-0-trong-bao-lau1632729748.html)
   4. [luatvietnam.vn: chính sách 01/7/2021](https://luatvietnam.vn/bao-hiem/chinh-sach-moi-ve-bao-hiem-xa-hoi-tu-01-7-2021-563-31346-article.html)
   5. [luatvietnam.vn: NĐ 159/2025](https://luatvietnam.vn/tin-van-ban-moi/tang-manh-muc-ho-tro-dong-bhxh-tu-nguyen-cho-ho-ngheo-can-ngheo-tu-01-7-2025-186-102748-article.html)
5. BHYT: [luatvietnam.vn: mức đóng BHYT từ 01/7/2025](https://luatvietnam.vn/bao-hiem/muc-dong-muc-ho-tro-dong-bhty-tu-01-7-2025-563-102202-article.html)
6. Chuẩn nghèo: [thuvienphapluat.vn: NĐ 351/2025](https://thuvienphapluat.vn/phap-luat-nha-dat/toan-van-nghi-dinh-3512025ndcp-ve-chuan-ngheo-da-chieu-giai-doan-20262030-13468.html), [baovanhoa.vn](https://baovanhoa.vn/doi-song/tieu-chi-do-luong-chuan-ngheo-da-chieu-quoc-gia-giai-doan-20262030-194176.html)
