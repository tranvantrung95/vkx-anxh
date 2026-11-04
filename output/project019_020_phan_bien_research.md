# Phản biện toàn bộ research và phân tích BA project019

Ngày lập: 04/11/2026. Người lập: Claude, phiên rà soát theo yêu cầu người dùng ("đánh giá và phản biện gay gắt toàn bộ thông tin research phân tích"). Loại tài liệu: phản biện nội bộ, không gửi khách hàng.

**Phạm vi đã đọc:** 15 file .md trong `output/` (002 đến 018); file 013 (24 sheet, đọc bằng openpyxl và `cap_nhat_checklist.py --report`); bộ dữ liệu giả 019 (xlsx và CSV); `work/CHECKPOINT.md`; `CLAUDE.md`; `SKILL.md` và script của skill `ba-hop-khao-sat`.

**Không đọc được:** `input/` (7 ảnh Phụ lục III, checklist gốc) và `tmp/` (bản Công báo đã tải, JSON cập nhật, bản sao lưu). Hai thư mục này bị `.gitignore` loại khỏi repo. Mọi nhận xét về Phụ lục III dựa trên bản chép ở 004 và sheet "UC tham khảo PL III", chưa đối chiếu ảnh gốc.

**Đối chiếu bên ngoài:** tra web ngày 04/11/2026 cho 5 dữ kiện pháp lý (mục 2, nguồn ở cuối tài liệu). Không chạy được `audit2.py`: skill `kiem-tra-ai-2` không có trong môi trường này.

Mọi task, UC, BR nhắc tới dưới đây vẫn ở trạng thái **Giả định** hoặc **Chờ đối chiếu** như trong file 013. Tài liệu này không đổi trạng thái nào.

## 1. Kết luận

Phần tra cứu pháp lý làm tốt và kỷ luật ghi nhãn giả định được giữ ở mức tài liệu. Nhưng sau 13 ngày (22/10 đến 04/11/2026), dự án chưa có một dữ kiện nào do khách hàng hoặc dữ liệu thật xác nhận. Khối lượng tài liệu lại tăng nhanh nhất đúng trong giai đoạn đó.

Lỗi nặng nhất xảy ra ngày 03/11. Thay vì báo lên rằng không hỏi được ai, nhóm BA tự trả lời 67 trên 68 câu hỏi khảo sát, gắn trạng thái "Đã quyết". Ba mâu thuẫn phạm vi lớn nhất được ghi "Đã xử lý". Một rủi ro cấp dự án, lẽ ra phải báo bằng văn bản, đã bị biến thành một cuốn sổ trông như đã chốt.

Năm vấn đề cần sửa trước mọi việc khác:

1. Câu hỏi phạm vi (người có công hay toàn bộ an sinh xã hội, xây mới hay chuyển đổi, nguồn nào, kiến trúc nào) đang được BA quyết thay khách hàng (mục 3.2, 3.6, 3.7).
2. Lõi được tuyên bố là người có công, nhưng công sức dồn vào trợ giúp xã hội, hộ nghèo và dự báo. Quy tắc lõi người có công cho kỳ 2026 chưa đối chiếu bản gốc (mục 3.4).
3. Phụ lục III là tài liệu duy nhất có tính hợp đồng nhưng bị coi là "tham khảo, không bắt buộc". Cả 153/153 mục chưa đánh giá, và không có truy vết từ mục Phụ lục III sang UC rồi sang tiêu chí nghiệm thu (mục 3.5).
4. Một số sản phẩm mâu thuẫn với kết luận của chính dự án: kịch bản dự báo VD2 và bộ dữ liệu giả 019 (mục 4.1, 4.2).
5. Kế hoạch, ước lượng và mốc demo đã vỡ nhưng chưa lập lại. Hai tài liệu gửi ra ngoài (003, 012) vẫn dùng số cũ (mục 4.6, 5).

## 2. Phần làm được

Phần này ghi để cân bằng. Nó không bù được các lỗi ở mục 3 đến 6.

- **Văn bản pháp lý không bịa.** Tra web ngày 04/11/2026 khớp với tài liệu dự án ở các điểm sau. NĐ 335/2026 ban hành 21/8/2026, hiệu lực 05/10/2026, mức chuẩn 540.000 đồng, người đang hưởng chuyển mức từ 01/7/2026. NĐ 321/2026 có mức chuẩn 3.012.000 đồng, hiệu lực 01/10/2026; một số điều áp từ 01/7/2026, nhóm Điều 6, 7, 9, 10, 11, 13 áp từ 01/01/2027. PL 05/2026/UBTVQH16 thông qua 08/7/2026, hiệu lực 01/01/2027, có VBHN 123/2026. NĐ 351/2025 hiệu lực 15/02/2026, chuẩn nghèo nông thôn 2.200.000 đồng từ 2027. Lương cơ sở 2.530.000 đồng từ 01/7/2026 theo NĐ 161/2026.
- **004 bắt đúng các điểm lệch lớn ngay từ đầu:** Phụ lục III chỉ nói về người có công; "7 nguồn API" gộp nguồn với đích; Phụ lục III thiếu mục F và E.IV; tên thư mục "Migrate ASSH".
- **017 có hai kết luận dùng được cho thiết kế.** Mức người có công là bảng phụ lục, không phải công thức (kết luận 4). Văn bản ban hành sau ngày áp dụng nên dữ liệu chi trả có khoản truy lĩnh (kết luận 2).
- **Ghi nhãn trung thực ở mức tài liệu.** Hầu hết file có cờ "Giả định" và mức tin cậy CB, TV, BC, HB. Không file nào lộ dữ liệu cá nhân.

## 3. Lỗi nền tảng

### 3.1. Khối lượng tăng, mức xác nhận đứng yên ở 0

| Chỉ số | 28/10/2026 | 04/11/2026 |
|---|---|---|
| Câu hỏi khảo sát | 59, cả 59 "Chưa hỏi" | 68: 67 "Đã quyết (giả định)", 1 "Đã kiểm chứng". Không câu nào do người ngoài nhóm BA trả lời |
| Task và UC | 36, cả 36 "Giả định" | 41 (thêm T17, UC21 đến UC24), cả 41 "Giả định"; 0/41 có ước lượng |
| Việc cần làm | VL-01 đến VL-21 | VL-01 đến VL-47 |
| Sheet trong file 013 | 13 | 24 |
| Biên bản họp với khách hàng | 0 | 0 |
| Dữ liệu thật, tài liệu API, cấu trúc bảng nguồn | 0 | 0 |

Tổng khối lượng: khoảng 78.800 từ trong 15 file .md, khoảng 2.600 dòng trong file 013, khoảng 4.600 dòng dữ liệu giả. Chưa dòng nào qua khách hàng.

Mọi lớp phía sau được xây trên danh sách T01 đến T11, UC01 đến UC19: mô hình 33 mã thực thể, 34 BR cộng các quy tắc KT- mới, 67 tiêu chí nghiệm thu, 11 kịch bản dự báo, bộ dữ liệu giả. Chính 009 mục 1.3 xếp nhãn dữ liệu GIẢ ĐỊNH cho 26/30 dòng của danh sách đó. Sai ở gốc thì phải sửa cả dây chuyền.

### 3.2. Sổ giả định: BA trả lời thay khách hàng rồi đóng mâu thuẫn

Từ 03/11, sheet "Checklist họp" đổi thành "Sổ giả định và quyết định BA". Dòng đầu sheet ghi "Không có đầu mối để hỏi". Script `cap_nhat_checklist.py` và `SKILL.md` của skill `ba-hop-khao-sat` sửa theo: trạng thái "Chưa hỏi" đổi thành "Chưa xử lý", và chỉ còn ba trạng thái.

Bốn vấn đề:

1. **BA quyết cả những câu ngoài thẩm quyền.** Có 30/68 câu thuộc loại "3 Phạm vi" (6 câu) hoặc "4 Dữ liệu và hệ thống" (24 câu). Theo định nghĩa của chính sổ, BA không có thẩm quyền hoặc không có dữ liệu để quyết những câu này. Chúng vẫn mang trạng thái "Đã quyết". Có 11 câu ghi căn cứ "Không có". Q1 đến Q3 (hệ thống Git, CI/CD, môi trường) cũng "Đã quyết".
2. **Mâu thuẫn được đóng bằng cách chọn một phía.** Sheet "Mâu thuẫn & rủi ro" ghi mâu thuẫn #1 (phạm vi), #2 (xây mới hay chuyển đổi), #3 (số nguồn) là "Đã xử lý 03/11/2026: BA quyết theo Q27, Q38, Q28". Đây là ba mâu thuẫn lớn nhất của dự án. Chúng chưa được xử lý. Cùng ngày, BA-04 ghi mô hình lõi "Đã chốt", tức mốc M1 "Mô hình lõi đã duyệt" được coi là đạt bằng tự duyệt.
3. **"Không có đầu mối" mâu thuẫn với chính hồ sơ.** Anh Hoàng Nam Dương (bên giao việc) ra chỉ đạo ngày 27/10 (014) và đưa nhận định để chốt D8 (CHECKPOINT 27/10). VNPT-IT đang chờ profile BA (012). Vẫn có người để gửi câu hỏi. Nếu họ không trả lời được câu phạm vi thì đó là điểm chặn cấp dự án, cần báo bằng văn bản kèm hạn trả lời. BA không nên dùng tình trạng đó làm lý do để tự quyết.
4. **Nhãn dễ bị đọc nhầm.** Khi file 013 đến tay người khác, "Đã quyết" sẽ được hiểu là "đã chốt". Điều này trái quy tắc chung trong `CLAUDE.md`: giả định không được trình bày như phạm vi đã chốt.

### 3.3. Làm ngược chỉ đạo của bên giao việc

Ngày 27/10, anh Dương yêu cầu "gen ra các đầu mục trước... đặc tả chi tiết để khi có thông tin cụ thể mới làm cho đỡ mất công" (014, đầu tài liệu). 014 còn tự cam kết phần A của 015 "không mở rộng thêm cho tới khi có biên bản khảo sát".

Từ đó đến nay, thông tin cụ thể mới duy nhất là sơ đồ luồng dữ liệu nhận ngày 03/11. Dù vậy nhóm vẫn làm:

| Ngày | Sản phẩm thêm |
|---|---|
| 28/10 | 8 sheet đặc tả, tiêu chí nghiệm thu, BR, truy vết, kế hoạch dựng từ .md vào file 013 |
| 30/10 | Sheet "Chế độ theo nhóm đối tượng" 123 dòng; "Kịch bản dự báo" VD1 đến VD11; "Mô phỏng dự báo" 413 công thức cho một xã giả; tài liệu 018 "Quy trình BA chuẩn" (21 trang .docx) |
| 03/11 | Bộ dữ liệu giả 019 (29 bảng, khoảng 4.600 dòng, một engine thu nhỏ, các ca gieo sẵn TC-M01 đến TC-M26); 3 quy tắc KT- mới; T17, UC21 đến UC24; Q64 đến Q68 |

Trong khi đó, kế hoạch BA chính thức (sheet "Kế hoạch BA") có BA-02, BA-03, BA-05 đến BA-11 đều "Chưa làm". BA-01 ước 1 ngày công, hạn 28/10, đến 03/11 vẫn "Đang làm: 33/68".

### 3.4. Lõi được tuyên bố là người có công, công sức lại dồn vào trợ giúp xã hội

Ngày 03/11, Q27 quyết lõi là người có công; trợ giúp xã hội và hộ nghèo là phần mở rộng. Đối chiếu với sản phẩm hiện có:

- **Quy tắc vững nhất nằm ngoài lõi.** 16 trong 23 BR "Đã đối chiếu" là trợ giúp xã hội (BR-01 đến BR-16). Phía người có công, ba quy tắc nền đều "Chờ đối chiếu (TV)": BR-20 (mức hằng tháng theo bảng phụ lục), BR-21 (hai mốc áp dụng NĐ 321), BR-22 (con liệt sĩ dưới 18 tuổi). BR-23 và BR-25 chỉ "Đã đối chiếu từ 01/01/2027". Trước mốc đó, 011 mục 3.2 ghi "chưa đọc bản gốc chưa sửa".
- **Câu tóm tắt ở 016 gây hiểu nhầm.** 016 mục 1 viết "bộ quy tắc chính sách là phần chắc nhất". Phần chắc đó nằm ở mảng mà BA đã xếp ngoài lõi.
- **UC06 nhánh người có công không có quy tắc cho kỳ nó sẽ chạy.** Đặc tả 015 chỉ có quy tắc cho kỳ từ 01/2027. GĐ1a và GĐ1b (15/11, 30/11/2026) chạy trên dữ liệu kỳ 2026.
- **Tiền đề về cộng dồn chưa được kiểm.** Tiền đề "người có công nhiều diện chỉ được cộng dồn từ 2027" chưa ai kiểm, vì chưa ai đọc bản PL 02/2020 trước sửa đổi, dù đó là văn bản công khai. Nếu bản gốc đã cho cộng dồn thì thiết kế tách hai nhánh theo ngày của UC06 là thừa.
- **Dữ liệu giả và mô phỏng cũng nghiêng về trợ giúp xã hội.** Bộ dữ liệu giả 019 và sheet "Mô phỏng dự báo" dựng phần trợ giúp xã hội kỹ hơn. Phần người có công trong dữ liệu giả chỉ có 6 diện; chưa có thờ cúng, điều dưỡng, hai mốc của BR-21, giới hạn hai suất tuất.
- **UC lõi mới chưa có nội dung.** UC21 đến UC23 thêm cho người có công cùng ngày quyết Q27, nhưng chưa có đặc tả và chưa vào truy vết (VL-37, VL-38).

### 3.5. Phụ lục III bị coi là tham khảo

Sheet "UC tham khảo PL III" ghi "Chỉ để tham khảo, KHÔNG bắt buộc; có thể thay đổi, gộp, bỏ". Đây là phụ lục yêu cầu kỹ thuật của dự thảo hợp đồng giữa Cục Người có công và Liên danh VNPT-VKX, tức là căn cứ để nghiệm thu. Hiện trạng:

- **Chưa đánh giá mục nào.** Cả 153/153 mục ghi "Chưa đánh giá".
- **Truy vết đi sai trục.** Ma trận truy vết chỉ đi theo chiều văn bản pháp luật, BR, UC, TC. Không có chiều mục Phụ lục III, UC, TC. Vì vậy chưa trả lời được câu hỏi kiểu "mục 163 nghiệm thu bằng gì".
- **Loại 55 mục mà không có căn cứ.** 55 mục (26 mục A, 2 mục B, 20 mục D, 7 mục H theo 004 mục 2.3) bị loại khỏi phân tích, và Q30 quyết bên mình không làm các mục quy trình động, thủ tục hành chính, chi trả. Không có văn bản phân công trong liên danh nào làm căn cứ.
- **Tài liệu hợp đồng chỉ có dạng ảnh.** VL-04 (xin Phụ lục III dạng file) vẫn "Chưa làm" sau 9 ngày. Tài liệu hợp đồng duy nhất hiện chỉ có dưới dạng 7 ảnh chụp màn hình điện thoại.
- **Ưu tiên ngược.** UC không có căn cứ Phụ lục III (T08, UC05, UC13, UC15 theo 009 mục 1.3; UC24 mới thêm) vẫn có thẻ đặc tả, tham số, dữ liệu giả.

### 3.6. Gạt đi tín hiệu kiến trúc duy nhất từ phía giao việc

Ngày 03/11, người dùng gửi sơ đồ "Luồng biến đổi dữ liệu qua các tầng". Sơ đồ có NiFi, Spark, Iceberg, ClickHouse, Trino, Elastic, Superset và các tầng Bronze, Silver, Gold. Đây là tài liệu kỹ thuật đầu tiên đến từ phía giao việc.

Q16 coi sơ đồ này là "kiến trúc tham khảo" và giữ ràng buộc "Angular 19, Spring Boot, Oracle". Ràng buộc đó lấy từ dòng 2 của một sheet Excel, mà 009 (G6) đã xếp GIẢ ĐỊNH vì chỉ là lời người dùng sau buổi trao đổi, chưa có tài liệu kỹ thuật. Q16 tự ghi hệ quả nếu sai là "làm lại toàn bộ phần hiển thị". Dù vậy, mục này chỉ thành VL-43 "Chờ đối chiếu", không được xếp vào nhóm câu hỏi ưu tiên cao nhất.

Ngay từ 002 (22/10), BA đã được kỳ vọng hiểu sâu data warehouse và lakehouse. Sơ đồ 03/11 xác nhận hướng đó. Mô hình 007, các quy tắc chạy lại R1 đến R10, engine E31 và E32 đều thiết kế theo hình dung một ứng dụng Spring Boot trên Oracle. Nếu kiến trúc thật là lakehouse, phần lớn các quyết định đó phải làm lại: phân lớp dữ liệu, cách chạy lại, nơi tính BR.

### 3.7. Câu hỏi "chuyển đổi hệ thống" được trả lời theo hướng dễ nhất

Bằng chứng hiện có nghiêng về hướng nâng cấp hoặc chuyển đổi hệ thống người có công đang chạy:

- tên thư mục khách gửi là "Migrate ASSH";
- 4 mục Phụ lục III ghi "Nâng cấp";
- Phụ lục III gồm cả quản trị, thủ tục hành chính và chi trả.

Q38 lại quyết "module mới, nhận lịch sử qua T12, không thay thế hệ thống". T12 chưa có giai đoạn, chưa có ước lượng, và chính tài liệu dự án ghi đây "có thể là khối lượng lớn nhất" (R04, R11). Rủi ro công sức lớn nhất của dự án đang nằm trong một dòng giả định.

## 4. Lỗi nội dung và phương pháp

### 4.1. VD2 mâu thuẫn với kết luận của chính dự án

Sheet "Kịch bản dự báo", dòng VD2, ghi: "NCC: mức = mức hiện hành × (chuẩn kịch bản ÷ chuẩn hiện hành), giả định tỷ lệ thuận".

- **Mâu thuẫn ngay trong cùng dòng.** VD2 dẫn BR-20, trong khi BR-20 ghi rõ "không tính bằng phép nhân mức chuẩn".
- **Mâu thuẫn với kết luận trước đó.** 017 kết luận 4 và 009 mục 1.5 đều đã xếp phép nhân tỷ lệ là "GIẢ ĐỊNH sai".
- **Có sẵn phản ví dụ.** Bảng ở 017 mục 2.1.2 cho thấy NĐ 321/2026 nâng phụ cấp thương binh từ 81% từ khoảng 0,5 lên 1,0 lần mức chuẩn, tức không tỷ lệ thuận.
- **Xếp mức sẵn sàng sai.** VD2 vẫn mang mức sẵn sàng M1. Theo 014 mục 3, M1 nghĩa là "logic đã có căn cứ văn bản (BR đã đối chiếu)", trong khi BR-20 còn "Chờ đối chiếu".
- **Hỏi lại câu đã có lời đáp.** VL-26 "kiểm giả định tỷ lệ thuận" đặt lại một câu hỏi mà dự án đã tự trả lời.

### 4.2. Bộ dữ liệu giả 019 kiểm trường hợp dễ và sai ở chỗ đã biết

1. **Mức mai táng người có công đã lỗi thời.** Dữ liệu giả dùng 23.400.000 đồng, tức 10 × 2.340.000. Lương cơ sở từ 01/7/2026 là 2.530.000 đồng; con số này đã ghi ở 010 mục 6 và vừa được xác minh lại ngày 04/11. Nếu quy tắc là 10 lần lương cơ sở như dữ liệu giả đang giả định, ca chết từ 07/2026 phải là 25.300.000 đồng. Khi kết quả mong đợi sai, một engine tính đúng sẽ trượt kiểm thử.
2. **Kiểm đúng trường hợp đã giả định là không xảy ra.** Bảng E07 có 208 dòng "Truy lĩnh". Mỗi dòng gắn kỳ hưởng gốc (`ky_huong`, `truy_linh_tu_ky`, `truy_linh_den_ky`). Trong khi đó Q39 quyết rằng dữ liệu chi trả thật không tách khoản truy lĩnh. Như vậy bộ dữ liệu kiểm thử đang kiểm trường hợp dữ liệu tách sạch, đúng trường hợp BA cho là sẽ không gặp. Trường hợp khó (truy lĩnh gộp vào kỳ chi) không có ca nào.
3. **"27/27 ca đạt" không chứng minh được gì.** Cùng một script sinh dữ liệu, chạy engine thu nhỏ rồi tự chấm. Dân số nền được sinh để khớp quy tắc ("không sinh cảnh báo"). Con số này chỉ cho thấy script nhất quán với chính nó; nó không nói gì về quy tắc, engine thật hay dữ liệu thật. Không nên trích như bằng chứng chất lượng.
4. **Dữ liệu kiểm thử đặt ra quy tắc.** Ba quy tắc KT-HTXH, KT-TK, KT-BHYT xuất hiện trong dữ liệu giả trước khi có trong danh mục BR. KT-TK dùng ngưỡng là "giá trị khởi điểm của BA". Thứ tự đúng là ngược lại: có quy tắc rồi mới sinh dữ liệu kiểm.
5. **Số ca kiểm thử tự mâu thuẫn trong cùng sản phẩm.** Sheet "Đọc trước" ghi 16 ca gieo sẵn; VL-45 ghi 26 ca (TC-M01 đến TC-M26); phần tự kiểm ghi 27/27. File `kich_ban_kiem_thu.csv` có 27 dòng nhưng chỉ 26 mã, vì TC-M24 bị lặp. Đây đúng là loại lỗi "không viết số chưa đếm" mà 018 đặt làm nguyên tắc số 4.

### 4.3. Lạm phát trạng thái

- **Q62 nâng mức tin cậy sai quy ước.** Q62 ghi "Đã kiểm chứng", nhưng nguồn là pbgdpl.cantho.gov.vn và baovanhoa.vn, kèm chú thích "BC; chưa đối chiếu Công báo". Theo quy ước của chính dự án, chỉ nguồn CB mới được coi là đã đối chiếu.
- **Số chỉ số thiếu hụt không thống nhất.** Với NĐ 351/2025, 010 mục 3.3 ghi 12 chỉ số, còn Q62 liệt kê 13 (2 + 2 + 2 + 2 + 2 + 3). Chưa bên nào đối chiếu bản gốc.
- **Mốc đạt bằng tự duyệt.** BA-04 và M1 "đã chốt" dựa trên giả định của BA (mục 3.2).
- **Việc chuyển trạng thái dựa trên tự trả lời.** VL-09, VL-15, VL-16, VL-17, VL-20, VL-28 chuyển sang "Đã làm" hoặc "Đã quyết" dựa trên chính các câu BA tự trả lời trong sổ giả định.

### 4.4. Mô hình dữ liệu dựng trước khi thấy một cấu trúc nguồn nào

Mô hình hiện có 33 mã thực thể (E01 đến E36, trừ E08, E18, E19), ba lớp dữ liệu, 10 quy tắc chạy lại, 7 vai trò và 9 sơ đồ UML. Trong khi đó chưa có tài liệu API hay bảng nào của nguồn; 007 tự ghi nhận điều này. Hệ quả đã lộ ra:

- **Mã thực thể va chạm.** E24 và E25 trùng mã nhóm C nên phải đổi thành E31 và E32. Số mã bỏ trống tăng dần.
- **Mô hình và sơ đồ lệch nhau.** 8 task và UC trỏ tới E24, E25, E30, là những thực thể chưa có dòng định nghĩa trong sheet (VL-30). E33 đến E36 chưa vào sơ đồ (VL-29, VL-42). Bộ UML vẽ ngày 27/10 đã lệch mô hình hiện tại.
- **Một cam kết phạm vi lớn bị ẩn trong thiết kế.** E31 ĐÁNG HƯỞNG đi kèm một engine tính lại toàn bộ chế độ. Như vậy module "phân tích" phải dựng lại logic tính hưởng của hệ thống nghiệp vụ. Đây là cam kết phạm vi lớn, nhưng chưa được nêu như một quyết định phạm vi và chưa có ước lượng. Q52 còn ghi "không cần kiểm chứng bên ngoài; là quyết định thiết kế".

### 4.5. Dự báo: phương pháp yếu, ưu tiên sai

- **VD3 không đủ cơ sở thống kê.** VD3 dự báo hộ nghèo năm sau bằng tốc độ tăng thu nhập bình quân (CAGR) tính từ ít nhất 3 kỳ rà soát. Có bốn điểm yếu. Ba điểm dữ liệu không đủ cho dự báo cấp hộ. Dữ liệu rà soát chỉ có ở hộ được rà soát nên mẫu bị lệch. Chuẩn nghèo đa chiều phân biệt nghèo với cận nghèo bằng số chỉ số thiếu hụt, nhưng VD3 không dự báo chiều này. Kết quả không kèm khoảng sai số.
- **Thiếu dữ liệu đầu vào.** VD5, VD6, VD7, VD11 cần số liệu lịch sử (Q61) mà dự án chưa có.
- **Làm sai thứ tự ưu tiên.** UC12 thuộc GĐ2; UC15 và UC18 thuộc GĐ3. Dựng 11 kịch bản và một sheet 413 công thức cho các UC này ngay trong tuần khảo sát là làm sai thứ tự.

### 4.6. Ước lượng và kế hoạch đã vỡ nhưng chưa lập lại

- **Số ước lượng cũ hết hiệu lực nhưng vẫn được dùng.** Báo cáo 003 (trình ban giám đốc ngày 22/10) ước 9 đến 12, hoặc 11 đến 15, ngày công BA. Ước lượng đó đặt điều kiện có quyền đọc dữ liệu từ ngày đầu và được duyệt ngay trong tuần; không điều kiện nào xảy ra. 014 ra 21 ngày công. Vậy mà 012 (gửi VNPT-IT) vẫn trích con số 9 đến 12 và 11 đến 15.
- **Chưa có ước lượng phát triển.** 0/41 task và UC có ước lượng công phát triển, nên không kiểm được tính khả thi của mốc 15/11 hay 30/11.
- **Các mốc không còn khả thi:**
  - M0 (30/10, khảo sát xong) đã trượt.
  - M1 (04/11) "đạt" bằng tự duyệt.
  - M2 (06/11) cần BA-02 kiểm kê nguồn, mà BA-02 phụ thuộc quyền đọc dữ liệu (Q5, Q6), hiện chưa có.
  - M3 (15/11, rơi vào Chủ nhật) được định nghĩa là "một luồng nguồn đã đối soát → DB01", không làm được khi chưa có nguồn.

  Kế hoạch vẫn giữ nguyên các mốc này.
- **Phương án demo khả thi chưa được đề xuất.** Demo bằng dữ liệu giả thực tế là hướng duy nhất còn làm được, nhưng chưa được đề xuất chính thức với bên giao việc.

## 5. Rủi ro đối ngoại

1. **Gửi tài liệu mang nhãn agent làm minh chứng năng lực.** 012 đề xuất gửi VNPT-IT hai file 010 và 011 làm "minh chứng năng lực BA". Dòng 3 của cả hai file ghi "Người lập: agent BA project019". Đây là rủi ro uy tín.
2. **Tên pháp nhân chưa thống nhất.** Q49 quyết dùng VKX theo Phụ lục III, nhưng "XVK" vẫn còn trong 002, 003, 012. Trong đó 003 và 012 là tài liệu gửi ra ngoài.
3. **Ban giám đốc đang cầm bản đã lỗi thời.** 003 dùng hệ mã PT, DB, KT mà 014 đã hạ xuống làm mã tham chiếu, và các giả định của 003 đã hết hiệu lực. Bản này chưa được sửa.
4. **Có thể rò rỉ nội dung hợp đồng.** `.gitignore` loại `input/` với lý do "không đưa lên repo công khai". Nhưng file 013 trong `output/` chép lại 153 mục của dự thảo hợp đồng, kèm tên các bên. Nếu repo không ở chế độ riêng tư, nội dung hợp đồng đã bị lộ. Cần kiểm chế độ của repo.

## 6. Lỗi quy trình và công cụ

- **Nguồn sự thật đổi nhiều lần.** Bản quản lý chuyển từ 005 sang 013 ngày 28/10. 8 sheet được dựng từ .md bằng một script, và script này ghi đè mọi sửa tay nếu chạy lại. Các file 011, 014, 015, 016 giờ chỉ là bản chụp, nhưng 012 và 016 vẫn trích chúng như tài liệu hiện hành.
- **Sự cố lặp lại.** Theo CHECKPOINT ngày 26 đến 28/10:
  - `CLAUDE.md` bị ghi đè, mất mục "Quy ước BA";
  - hai file cùng mang số 007;
  - mã VL bị trùng;
  - mã E24, E25 bị trùng;
  - một lần hỏng file Excel khi ghi;
  - một bản sao lưu bị ghi đè do trùng giờ.
- **File tiến độ không được cập nhật.** `work/CHECKPOINT.md` dừng ở ngày 30/10. Những thay đổi lớn nhất đều không có trong file tiến độ mà `CLAUDE.md` chỉ định: chuyển sang sổ giả định; Q27, Q28, Q38 "đã quyết"; bộ dữ liệu giả 019; T17, UC21 đến UC24.
- **"Quy trình BA chuẩn" đóng gói đúng cách làm đã gây ra các vấn đề trên.** Trong 018, khảo sát là bước 8, đứng sau mô hình dữ liệu (bước 4), quy tắc (bước 5), task và UC (bước 6), truy vết (bước 7). Cổng kiểm của bước 0 qua được chỉ bằng "đã ghi giả định". Chuẩn hóa một quy trình sau một tuần, khi chưa có lần tiếp xúc khách hàng nào, là quá sớm.
- **Văn bản khó đọc với người ngoài.** Tài liệu dày đặc mã: Q, T, UC, E, BR, P-, VL, R, VD, NH-, TGXH-B. Mỗi sheet phải kèm một khối giải thích từ viết tắt riêng. Người không theo dự án hằng ngày (anh Dương, VNPT-IT, ban giám đốc) khó đọc.
- **Bằng chứng không tái lập được từ repo.** Bản Công báo đã tải, JSON cập nhật và các bản sao lưu đều nằm trong `tmp/`, thư mục bị loại khỏi repo. Người rà soát không thể kiểm lại các trạng thái "Đã đối chiếu (CB)" từ repo.

## 7. Đánh giá nhanh các tuyên bố chính

| Tuyên bố | Ở đâu | Đánh giá |
|---|---|---|
| NĐ 335/2026, NĐ 321/2026, PL 05/2026, NĐ 351/2025 và các mốc hiệu lực | 010, 011, 017 | Đúng (tra web 04/11/2026) |
| Mức người có công là bảng phụ lục, không phải công thức | 017 kết luận 4, BR-20 | Hợp lý, có ví dụ; nhưng VD2 làm ngược lại |
| "Bộ quy tắc là phần chắc nhất" | 016 mục 1 | Gây hiểu nhầm: phần chắc là trợ giúp xã hội; lõi người có công kỳ 2026 chưa đối chiếu |
| Mâu thuẫn #1, #2, #3 "Đã xử lý" | 013, sheet Mâu thuẫn & rủi ro | Sai: chỉ là giả định của BA |
| Mô hình lõi "đã chốt" (mốc M1) | 013, sheet Kế hoạch BA | Sai: tự duyệt |
| Q62 "Đã kiểm chứng" | 013, sheet Checklist họp | Sai theo quy ước CB của dự án |
| Người có công nhiều diện chỉ được cộng dồn từ 2027 | 009, 010, 015 (UC06) | Chưa kiểm: chưa đọc bản trước sửa đổi |
| Mai táng người có công 23.400.000 đồng | Dữ liệu giả 019 | Lỗi thời nếu tính theo 10 × lương cơ sở: 25.300.000 đồng từ 07/2026 |
| Dữ liệu giả "27/27 ca đạt" | Dữ liệu giả 019 | Đúng về số học, không có giá trị kiểm chứng |
| Công BA 9 đến 12 hoặc 11 đến 15 ngày | 003, 012 | Hết hiệu lực; 014 đã ra 21 ngày |
| Angular 19, Spring Boot, Oracle là ràng buộc | Q4, Q16 | Chưa kiểm; mâu thuẫn với sơ đồ 03/11 |

## 8. Việc nên làm, theo thứ tự

Các việc dưới đây chưa được cấp mã VL. Nếu người dùng đồng ý, ghi vào sheet "Việc cần làm (VL)" của file 013 từ VL-48 bằng `cap_nhat_checklist.py`.

1. **Dừng sinh sản phẩm mới** (UC, sheet, dữ liệu giả, kịch bản) cho tới khi có câu trả lời ở việc 2.
2. **Gửi một trang "5 câu chặn" bằng văn bản** cho anh Dương và VNPT-IT, có hạn trả lời:
   - (a) phạm vi là người có công hay toàn bộ an sinh xã hội, bên mình nhận phần nào của Phụ lục III (Q27, Q30, Q44);
   - (b) xây mới hay nâng cấp, và chuyển đổi hệ thống nào (Q38);
   - (c) danh sách nguồn và kiến trúc đích: Oracle với Spring Boot, hay lakehouse theo sơ đồ 03/11 (Q28, Q16);
   - (d) quyền đọc dữ liệu, hoặc bản dump đã che (Q5 đến Q7);
   - (e) ngày và nội dung demo, có chấp nhận demo bằng dữ liệu giả không (Q22).

   Nói rõ trong văn bản: nếu không có trả lời, demo chỉ chứng minh logic trên dữ liệu giả.
3. **Sửa trạng thái cho đúng nghĩa.** Đổi "Đã quyết (giả định)" thành một nhãn không thể đọc nhầm là đã chốt, ví dụ "Giả định BA, chưa xác nhận". Mở lại mâu thuẫn #1, #2, #3. Trả Q62 về mức BC. Bỏ trạng thái "đã chốt" của BA-04 và mốc M1.
4. **Lập lại kế hoạch.** Báo ban giám đốc và VNPT-IT rằng số công ở 003 và 012 không còn hiệu lực. Xin đội kỹ thuật ước lượng cho phần demo.
5. **Lấy Phụ lục III làm trục.** Xin bản dạng file (VL-04); đánh giá 153 mục; thêm truy vết từ mục Phụ lục III sang UC và TC; tạm gác các UC không có căn cứ trong Phụ lục III.
6. **Sửa lõi người có công.**
   - Đọc PL 02/2020 bản trước sửa đổi (Điều 3, Điều 6) và Phụ lục NĐ 321/2026 bản Công báo.
   - Viết lại VD2 theo bảng phụ lục.
   - Sửa mức mai táng người có công trong dữ liệu giả.
   - Thêm vào dữ liệu giả biến thể "truy lĩnh gộp vào kỳ chi".
7. **Rút 010 và 011 khỏi danh sách gửi kèm của 012**, hoặc biên tập lại dòng người lập. Thống nhất tên VKX trong mọi tài liệu gửi ra ngoài.
8. **Cập nhật `work/CHECKPOINT.md`** cho các thay đổi ngày 03/11.

## Nguồn tra web ngày 04/11/2026

- NĐ 335/2026: [hatinh.gov.vn](https://hatinh.gov.vn/vi/bai-viet/nghi-dinh-moi-quy-dinh-chinh-sach-tro-giup-xa-hoi-muc-chuan-540000-dongthang), [vov.vn](https://vov.vn/chinh-tri/tang-muc-chuan-tro-giup-xa-hoi-len-540000-dongthang-post1326470.vov), [Công báo (PDF)](https://congbaocdn.chinhphu.vn/180507251028987904/2026/9/4/470340-1787910774_v1_1788515197_signed.pdf)
- NĐ 321/2026: [baophapluat.vn](https://baophapluat.vn/tang-muc-chuan-tro-cap-nguoi-co-cong-len-hon-3-trieu-dong.html), [vietnamplus.vn](https://www.vietnamplus.vn/tang-muc-chuan-tro-cap-uu-dai-nguoi-co-cong-len-hon-3-trieu-dong-post1131070.amp), [thuvienphapluat.vn](https://thuvienphapluat.vn/lao-dong-tien-luong/tro-cap-nguoi-co-cong-tu-1102026-la-bao-nhieu-64264.html)
- PL 05/2026/UBTVQH16: [daibieunhandan.vn](https://daibieunhandan.vn/chu-tich-quoc-hoi-tran-thanh-man-ky-ban-hanh-phap-lenh-sua-doi-bo-sung-mot-so-dieu-cua-phap-lenh-uu-dai-nguoi-co-cong-voi-cach-mang-10424733.html), [tcnnld.vn](https://tcnnld.vn/news/detail/72953/Phap-lenh-so-052026UBTVQH16---buoc-hoan-thien-day-du--chinh-sach-nguoi-co-cong.html), [VBHN 123/2026 (PDF)](https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/8/2026-123-phap-lenh-uu-dai-nguoi-co-cong-voi-cach-mang-thanh-trang.pdf)
- NĐ 351/2025: [mae.gov.vn](https://mae.gov.vn/chuan-ngheo-da-chieu-quoc-gia-giai-doan-20262030-20732.htm), [thuvienphapluat.vn](https://thuvienphapluat.vn/phap-luat-nha-dat/toan-van-nghi-dinh-3512025ndcp-ve-chuan-ngheo-da-chieu-giai-doan-20262030-13468.html)
- Lương cơ sở 2.530.000 đồng (NĐ 161/2026): [baovanhoa.vn](https://baovanhoa.vn/doi-song/chinh-thuc-tang-luong-co-so-len-2530000-dongthang-tu-ngay-17-228598.html), [tapchicongthuong.vn](https://tapchicongthuong.vn/chinh-thuc-tang-luong-co-so-len-2-530-000-dong-thang-tu-01-7-2026-518417.htm)

Các nguồn trên phần lớn là báo chí và trang tổng hợp (mức BC, TV theo quy ước dự án). Chúng đủ để kết luận văn bản có thật và các con số chính khớp, nhưng không thay được việc đối chiếu bản Công báo cho từng điều khoản.
