# Đặc tả phần đã có căn cứ: quy tắc nghiệp vụ, từ điển dữ liệu, ma trận truy vết (bước 6, agent BA)

Ngày lập: 26/10/2026. Người lập: agent BA project019. Tài liệu đi kèm `output/project019_009_ket_qua_agent_ba.md` (mục 6).

Cập nhật 27/10/2026: thêm mục 3.4 (BR-50 đến BR-53, quy tắc tổng hợp và hiển thị do BA đề xuất khi viết đặc tả `output/project019_015_dac_ta_so_bo_task_uc.md`), kịch bản TC-BR50-01 đến TC-BR53-01 ở mục 5 và 4 dòng ở ma trận mục 6.

## 1. Phạm vi đặc tả và lý do

Chưa có mục nào ở trạng thái ĐÃ XÁC NHẬN: chưa có biên bản khảo sát, cả 59 câu hỏi checklist (Q1 đến Q59) ở trạng thái "Chưa hỏi", cả 36 task và UC (T01 đến T16, UC01 đến UC20) ở trạng thái "Giả định" (đếm lại ngày 28/10/2026; bản 26/10/2026 ghi 37 câu, 30 task và UC).

Mục CÓ CĂN CỨ ổn định nhất là **quy tắc chính sách đọc từ văn bản pháp luật**. Các quy tắc này đúng bất kể nguồn dữ liệu nào có, và đều cần cho T09 (bộ quy tắc cấu hình) dù phạm vi chốt là người có công hay toàn bộ an sinh xã hội. Tài liệu này chỉ đặc tả bốn phần:

1. Danh mục tham số và quy tắc BR-xx (mục 2, 3).
2. Từ điển dữ liệu của ba thực thể chứa tham số và quy tắc: E21 VĂN BẢN PHÁP LÝ, E22 THAM SỐ CHÍNH SÁCH, E23 QUY TẮC (mục 4).
3. Kịch bản kiểm thử ở mức quy tắc, mã TC-BRxx-nn (mục 5).
4. Ma trận truy vết văn bản → BR → UC → kịch bản (mục 6).

**Không đặc tả use case nào.** Mọi UC01 đến UC19 và T01 đến T11 còn "Giả định" về phạm vi, nguồn dữ liệu và người dùng. Danh sách UC chưa đặc tả và điều kiện để đặc tả ở mục 7. Cột UC trong ma trận chỉ cho biết UC nào sẽ dùng BR, không có nghĩa UC đã ổn định.

Quy ước mã theo skill `ba-quy-tac-truy-vet` và `ba-dac-ta-use-case`: tham số `P-` kèm tên, quy tắc `BR-xx`, kịch bản `TC-...`. Trạng thái BR: `Đã đối chiếu` chỉ khi điều khoản được đọc trong bản gốc (CB) có ghi URL và ngày tra; còn lại `Chờ đối chiếu`. Không dùng BR `Chờ đối chiếu` làm tiêu chí nghiệm thu.

Chưa có file sổ BR nào trong `work/` (`ls work/*danh_muc_quy_tac*` rỗng). Tài liệu này là bản đầu của danh mục. Theo quy ước skill, khi người dùng đồng ý thì chép mục 2, 3, 6 sang `work/project019_NNN_danh_muc_quy_tac.md` và `work/project019_NNN_ma_tran_truy_vet.md`.

Nguồn CB dùng trong tài liệu (tra 26/10/2026):

1. [CB-1] NĐ 335/2026/NĐ-CP, Công báo số 500 ngày 05/9/2026: https://congbaocdn.chinhphu.vn/180507251028987904/2026/9/4/470340-1787910774_v1_1788515197_signed.pdf
2. [CB-2] VBHN 123/2026/VBHN-PL-VPQH (Pháp lệnh 02/2020 hợp nhất PL 05/2026): https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/8/2026-123-phap-lenh-uu-dai-nguoi-co-cong-voi-cach-mang-thanh-trang.pdf
3. [CB-3] VBHN 15/2026/VBHN-NĐ-BYT (NĐ 176/2025 hợp nhất), đã đọc trong báo cáo 017 (lịch sử thay đổi chính sách, trước đây đánh số 007): https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/9/15-vbhn-byt.signed.pdf
4. [CP-4] NĐ 321/2026/NĐ-CP, Cổng thông tin Chính phủ (chỉ xác nhận hiệu lực và mức chuẩn).

## 2. Tham số (cấu hình theo thời kỳ)

| Mã tham số | Tên | Giá trị | Đơn vị | Áp dụng từ | Áp dụng đến | Căn cứ | Tin cậy |
|---|---|---|---|---|---|---|---|
| P-MUC-CHUAN-TGXH | Mức chuẩn trợ giúp xã hội | 360.000 | đồng/tháng | 01/07/2021 | 30/06/2024 | NĐ 20/2021 | BC, chưa xác minh |
| P-MUC-CHUAN-TGXH | | 500.000 | đồng/tháng | 01/07/2024 | 30/06/2026 | NĐ 76/2024 | BC, chưa xác minh |
| P-MUC-CHUAN-TGXH | | 540.000 | đồng/tháng | 01/07/2026 | | NĐ 335/2026 Điều 4 khoản 2; Điều 32 khoản 3 [CB-1] | CB |
| P-MUC-CHUAN-TGXH-TINH | Mức chuẩn do HĐND tỉnh quyết định cao hơn | theo từng tỉnh | đồng/tháng | theo nghị quyết HĐND | | NĐ 335/2026 Điều 4 khoản 3 điểm a [CB-1] | CB (khung); giá trị chưa có |
| P-HUU-TRI-XH | Trợ cấp hưu trí xã hội | 500.000 | đồng/tháng | 01/07/2025 | 30/06/2026 | NĐ 176/2025 [CB-3] | CB (017) |
| P-HUU-TRI-XH | | 540.000 | đồng/tháng | 01/07/2026 | | NĐ 335/2026 Điều 31, Điều 32 khoản 3 [CB-1] | CB |
| P-MUC-CHUAN-NCC | Mức chuẩn trợ cấp ưu đãi NCC | 2.055.000 | đồng/tháng | 01/07/2023 | 30/06/2024 | NĐ 55/2023 | TV, chưa xác minh |
| P-MUC-CHUAN-NCC | | 2.789.000 | đồng/tháng | 01/07/2024 | 30/06/2026 | NĐ 77/2024 | TV, chưa xác minh |
| P-MUC-CHUAN-NCC | | 3.012.000 | đồng/tháng | 01/07/2026 | | NĐ 321/2026 [CP-4]; mốc áp dụng theo Điều 3 (TV) | Giá trị: CB. Mốc: chưa xác minh |
| P-HS-TGXH-K1-DUOI4 | Hệ số trẻ em Điều 5 khoản 1, dưới 4 tuổi | 2,5 | hệ số | 01/07/2026 | | NĐ 335 Điều 6 khoản 1 điểm a [CB-1] | CB |
| P-HS-TGXH-K1-TU4 | Như trên, từ đủ 4 tuổi | 1,5 | hệ số | 01/07/2026 | | Điều 6 khoản 1 điểm a | CB |
| P-HS-TGXH-K2 | Người từ 16 tuổi đang học (Điều 5 khoản 2) | 1,5 | hệ số | 01/07/2026 | | Điều 6 khoản 1 điểm b | CB |
| P-HS-TGXH-K3-DUOI4 / P-HS-TGXH-K3-4DEN16 | Trẻ em nhiễm HIV hộ nghèo | 2,5 / 2,0 | hệ số | 01/07/2026 | | Điều 6 khoản 1 điểm c | CB |
| P-HS-TGXH-K4 | Đơn thân nghèo, mỗi con đang nuôi | 1,0 | hệ số/con | 01/07/2026 | | Điều 6 khoản 1 điểm d | CB |
| P-HS-TGXH-K5A-60DEN75 / P-HS-TGXH-K5A-TU75 | Người cao tuổi Điều 5 khoản 5 điểm a | 1,5 / 2,0 | hệ số | 01/07/2026 | | Điều 6 khoản 1 điểm đ | CB |
| P-HS-TGXH-K5B | Người cao tuổi Điều 5 khoản 5 điểm b | 3,0 | hệ số | 01/07/2026 | | Điều 6 khoản 1 điểm đ | CB |
| P-HS-TGXH-K6-DBN / -TE-NCT-DBN / -NANG / -TE-NCT-NANG | Người khuyết tật | 2,0 / 2,5 / 1,5 / 2,0 | hệ số | 01/07/2026 | | Điều 6 khoản 1 điểm e | CB |
| P-HS-TGXH-K7K8 | Trẻ dưới 3 tuổi vùng ĐBKK; người nhiễm HIV hộ nghèo | 1,5 | hệ số | 01/07/2026 | | Điều 6 khoản 1 điểm g | CB |
| P-HS-CS-NKT-1CON / P-HS-CS-NKT-2CON | Hỗ trợ chăm sóc NKT mang thai hoặc nuôi con dưới 36 tháng | 1,5 / 2,0 | hệ số | 01/07/2026 | | Điều 17 khoản 2 điểm a | CB |
| P-HS-CS-HO-NKT-DBN | Hộ trực tiếp chăm sóc NKT đặc biệt nặng | 1,0 | hệ số/người | 01/07/2026 | | Điều 17 khoản 2 điểm c | CB |
| P-TUOI-CON-NHO-THANG | Ngưỡng tuổi con nhỏ của NKT | 36 | tháng | 01/07/2026 | | Điều 17 khoản 2 điểm a | CB |
| P-MAI-TANG-TGXH-HS-MIN | Mai táng TGXH, tối thiểu | 20 | lần mức chuẩn | 01/07/2026 | | Điều 11 khoản 2 | CB |
| P-TAM-DUNG-THANG | Số tháng không nhận liên tục thì tạm dừng | 3 | tháng | 05/10/2026 | | Điều 9 khoản 1 điểm a | CB |
| P-NUOI-LS-TUOI / P-NUOI-LS-NAM | Người có công nuôi liệt sĩ: liệt sĩ dưới / thời gian nuôi từ | 18 / 10 | tuổi / năm | 01/07/2021 | | PL 02/2020 Điều 4 khoản 2 [CB-2] | CB |
| P-TUAT-TOI-DA-SUAT | Số suất tuất tối đa của thân nhân hai NCC trở lên | 2 | suất | 01/07/2021 | | PL 02/2020 Điều 6 khoản 5 điểm a [CB-2] | CB |
| P-NGAY-CHUYEN-TIEP-HS-TGXH | Ngày phân định hồ sơ chuyển tiếp TGXH | 05/10/2026 | ngày | | | NĐ 335 Điều 32 khoản 1, Điều 33 | CB |
| P-NGAY-PL05 | Ngày phân định điều kiện công nhận NCC | 01/01/2027 | ngày | | | PL 05/2026 Điều 2 [CB-2] | CB |

Bảng mức hưởng từng diện người có công (Phụ lục I đến IV NĐ 55/2023, NĐ 77/2024, NĐ 321/2026) giữ ở sheet "Tham số NCC" với mã NCC-PL1-xx, NCC-PLIV-xx, NCC-PLVI-xx. Các mã đó là tham số của BR-20 và đều ở mức TV.

## 3. Quy tắc nghiệp vụ

Vai trò theo mô hình lõi: ĐT (người là đối tượng), NH (người hoặc hộ được hưởng), NN (người nhận tiền), NCS (người chăm sóc, nhận nuôi dưỡng), TN (thân nhân).

### 3.1. Trợ giúp xã hội và hưu trí xã hội

| Mã BR | Tên | Vai trò | Logic (NẾU, THÌ) | Tham số | Ưu tiên, ngoại lệ | Căn cứ | Trạng thái | UC dùng |
|---|---|---|---|---|---|---|---|---|
| BR-01 | Mức trợ cấp xã hội hằng tháng | ĐT | NẾU NGƯỜI có DIỆN thuộc Điều 5 khoản k tại kỳ hưởng T THÌ mức = P-MUC-CHUAN-TGXH(T, tỉnh) × hệ số của diện đó tại T | P-MUC-CHUAN-TGXH, P-MUC-CHUAN-TGXH-TINH, P-HS-TGXH-* | Chịu BR-02, BR-03 | NĐ 335 Điều 6 khoản 1; Điều 4 khoản 2, 3 [CB-1] | Đã đối chiếu | T09, UC06, UC07, UC09, UC12 |
| BR-02 | Nhiều hệ số, nhiều văn bản: một mức cao nhất | ĐT | NẾU một NGƯỜI đủ điều kiện nhiều hệ số Điều 6 khoản 1 hoặc nhiều văn bản TGXH tại cùng kỳ THÌ chỉ hưởng mức cao nhất | | BR-03 thắng BR-02 | NĐ 335 Điều 6 khoản 2 câu 1 | Đã đối chiếu | UC06 |
| BR-03 | Ngoại lệ đơn thân nghèo nuôi con | ĐT | NẾU NGƯỜI là đơn thân nghèo nuôi con (Điều 5 khoản 4) VÀ đồng thời thuộc Điều 5 khoản 5, 6 hoặc 8 THÌ hưởng cả chế độ khoản 4 và chế độ khoản 5, 6 hoặc 8 | P-HS-TGXH-K4 | Ngoại lệ của BR-02 | NĐ 335 Điều 6 khoản 2 câu 2 | Đã đối chiếu | UC06, UC10 |
| BR-04 | Thời điểm bắt đầu hưởng TGXH | ĐT, NCS | NẾU Chủ tịch UBND xã ký QUYẾT ĐỊNH trợ cấp hoặc hỗ trợ chăm sóc THÌ tháng bắt đầu hưởng = tháng ký quyết định | | | NĐ 335 Điều 8 khoản 2 | Đã đối chiếu | UC07, UC09 |
| BR-05 | Thôi hưởng và điều chỉnh mức | ĐT | NẾU ĐT chết hoặc không còn đủ điều kiện THÌ thôi hưởng từ tháng ngay sau tháng sự kiện. NẾU ĐT thay đổi điều kiện hưởng THÌ điều chỉnh mức từ tháng thay đổi | | | NĐ 335 Điều 8 khoản 4 | Đã đối chiếu | UC07, UC11 |
| BR-06 | Chuyển nơi cư trú | ĐT | NẾU ĐT đổi nơi cư trú và đề nghị nhận ở nơi mới THÌ nơi cũ quyết định thôi chi trả; nơi mới quyết định hưởng theo mức áp dụng tại địa bàn mới, từ tháng thôi chi trả ở nơi cũ | P-MUC-CHUAN-TGXH-TINH | | NĐ 335 Điều 8 khoản 3 | Đã đối chiếu | UC07, UC11, UC14 |
| BR-07 | Tạm dừng do không nhận | ĐT | NẾU ĐT không nhận chế độ liên tục từ P-TAM-DUNG-THANG tháng trở lên THÌ tạm dừng hưởng | P-TAM-DUNG-THANG | | NĐ 335 Điều 9 khoản 1 điểm a | Đã đối chiếu | UC07 |
| BR-08 | Trường hợp thôi hưởng TGXH | ĐT | NẾU ĐT chết, mất tích; không còn đủ điều kiện Điều 5; chấp hành án phạt tù hoặc có quyết định thôi hưởng; từ chối nhận; hoặc quá 3 tháng sau tạm dừng theo Điều 9 khoản 1 điểm b mà chưa xác định lại THÌ thôi hưởng | | | NĐ 335 Điều 9 khoản 2 | Đã đối chiếu | UC07, UC11 |
| BR-09 | Thôi hỗ trợ nhận chăm sóc, nuôi dưỡng | NCS | NẾU người được chăm sóc hoặc NCS chết, mất tích; người được chăm sóc không còn đủ điều kiện; NCS không còn đủ điều kiện Điều 19, 20; hoặc NCS bị xử phạt, kết án theo Điều 9 khoản 3 điểm d THÌ thôi hỗ trợ kinh phí cho NCS | | Lan truyền qua QUAN HỆ chăm sóc | NĐ 335 Điều 9 khoản 3 | Đã đối chiếu | UC08 |
| BR-10 | Mai táng TGXH | người tổ chức mai táng | NẾU người thuộc Điều 11 khoản 1 chết THÌ hỗ trợ mai táng ≥ P-MAI-TANG-TGXH-HS-MIN × mức chuẩn. NẾU trùng nhiều văn bản THÌ một mức cao nhất | P-MAI-TANG-TGXH-HS-MIN | | NĐ 335 Điều 11 khoản 1, 2 | Đã đối chiếu | UC11, UC12 |
| BR-11 | Hỗ trợ chăm sóc NKT mang thai, nuôi con nhỏ | ĐT | NẾU NKT đặc biệt nặng hoặc nặng đang mang thai hoặc nuôi một con dưới P-TUOI-CON-NHO-THANG tháng THÌ hệ số 1,5; mang thai và nuôi một con, hoặc nuôi từ hai con THÌ 2,0; nhiều hệ số lấy cao nhất; vợ và chồng cùng thuộc diện THÌ một suất | P-HS-CS-NKT-*, P-TUOI-CON-NHO-THANG | Vẫn hưởng khi đang hưởng trợ cấp khoản 6 (Điều 17 khoản 2 điểm b) | NĐ 335 Điều 17 khoản 2 điểm a, b | Đã đối chiếu | UC08, UC10, UC11 |
| BR-12 | Hộ chăm sóc NKT đặc biệt nặng | NH (hộ) | NẾU HỘ trực tiếp chăm sóc, nuôi dưỡng một NKT đặc biệt nặng THÌ hỗ trợ hệ số 1,0 cho mỗi người | P-HS-CS-HO-NKT-DBN | | NĐ 335 Điều 17 khoản 2 điểm c | Đã đối chiếu | UC10, UC12 |
| BR-13 | Chuyển mức cho người đang hưởng từ 01/07/2026 | ĐT | NẾU NGƯỜI đang hưởng theo NĐ 20/2021 hoặc NĐ 176/2025 THÌ từ kỳ 07/2026 mức đúng tính theo NĐ 335. Chênh lệch các kỳ đã chi theo mức cũ là khoản truy lĩnh | P-MUC-CHUAN-TGXH, P-HUU-TRI-XH | | NĐ 335 Điều 32 khoản 3, 4 | Đã đối chiếu (phần "khoản truy lĩnh" là suy luận BA, chờ khách hàng xác nhận cách chi) | UC07, UC12 |
| BR-14 | Hồ sơ TGXH chuyển tiếp | ĐT | NẾU hồ sơ được tiếp nhận trước P-NGAY-CHUYEN-TIEP-HS-TGXH VÀ chưa có quyết định THÌ trình tự, thủ tục theo NĐ 147/2025 (TGXH) hoặc NĐ 176/2025 (hưu trí xã hội); không yêu cầu nộp lại | P-NGAY-CHUYEN-TIEP-HS-TGXH | Diện, hệ số áp cho hồ sơ này: chưa rõ (câu P1-04) | NĐ 335 Điều 33 | Đã đối chiếu (phần thủ tục) | UC02 (tiến độ hồ sơ), UC09 |
| BR-15 | Người cao tuổi hưởng TGXH | ĐT | NẾU NGƯỜI cao tuổi thuộc HỘ nghèo VÀ không có người có nghĩa vụ phụng dưỡng (hoặc người đó đang hưởng trợ cấp xã hội hằng tháng) THÌ thuộc Điều 5 khoản 5 điểm a | P-HS-TGXH-K5A-* | Đối chiếu BR-16 | NĐ 335 Điều 5 khoản 5 | Đã đối chiếu | UC06, UC09, UC13 |
| BR-16 | Hưu trí xã hội và TGXH | ĐT | NẾU NGƯỜI đủ điều kiện hưu trí xã hội VÀ đồng thời thuộc diện trợ cấp xã hội THÌ hưởng mức cao hơn | P-HUU-TRI-XH | | NĐ 335 Điều 31 (sửa NĐ 176/2025) [CB-1, theo 007] | Đã đối chiếu (theo 007) | UC06, UC09 |

### 3.2. Người có công

| Mã BR | Tên | Vai trò | Logic | Tham số | Ưu tiên, ngoại lệ | Căn cứ | Trạng thái | UC dùng |
|---|---|---|---|---|---|---|---|---|
| BR-20 | Mức hằng tháng NCC lấy theo bảng phụ lục | ĐT, TN | NẾU NGƯỜI hưởng trợ cấp, phụ cấp hằng tháng NCC tại kỳ T THÌ mức = giá trị trong bảng phụ lục áp dụng cho kỳ T theo mã diện và tỷ lệ tổn thương; không tính bằng phép nhân mức chuẩn | NCC-PL1-xx, Phụ lục II, III | | NĐ 55/2023, NĐ 77/2024, NĐ 321/2026 Phụ lục I đến III | Chờ đối chiếu (TV) | T09, UC07, UC12 |
| BR-21 | Hai mốc áp dụng của NĐ 321/2026 | ĐT, TN | NẾU chế độ thuộc Điều 4, 5, 8, 12 THÌ áp NĐ 321 từ 07/2026. NẾU thuộc Điều 6, 7, 9, 10, 11, 13 THÌ đến hết 12/2026 áp văn bản cũ, từ 01/2027 áp NĐ 321 | | | NĐ 321/2026 Điều 3, Điều 15 khoản 4 | Chờ đối chiếu (TV) | T09, UC07, UC12 |
| BR-22 | Con liệt sĩ chưa đủ 18 tuổi | TN | NẾU con liệt sĩ chưa đủ 18 tuổi tại kỳ T (từ 07/2026) THÌ áp mục 3.1 Phụ lục I (2,0 lần); tháng sau tháng đủ 18 tuổi chuyển sang mục thân nhân tương ứng | NCC-PL1-08 | | NĐ 321/2026 Phụ lục I mục 3.1 | Chờ đối chiếu (TV); quy tắc chuyển mức theo tháng là suy luận | UC07, UC11 |
| BR-23 | Thân nhân người có công | TN | NẾU QUAN HỆ loại thân nhân NCC tại ngày ≥ P-NGAY-PL05 THÌ chỉ nhận một trong: cha đẻ, mẹ đẻ, vợ hoặc chồng, con (đẻ, nuôi), người có công nuôi liệt sĩ | P-NGAY-PL05 | Trước 01/01/2027: chưa đọc bản gốc chưa sửa | PL 02/2020 Điều 3 khoản 3 (sửa bởi PL 05/2026) [CB-2] | Đã đối chiếu (từ 01/01/2027) | T04, UC04, UC10, UC11 |
| BR-24 | Người có công nuôi liệt sĩ | TN | NẾU một NGƯỜI nuôi liệt sĩ khi liệt sĩ chưa đủ P-NUOI-LS-TUOI tuổi VÀ thời gian nuôi từ P-NUOI-LS-NAM năm THÌ là người có công nuôi liệt sĩ | P-NUOI-LS-TUOI, P-NUOI-LS-NAM | | PL 02/2020 Điều 4 khoản 2 [CB-2] | Đã đối chiếu | UC10 |
| BR-25 | NCC thuộc nhiều diện | ĐT | NẾU NGƯỜI có công thuộc nhiều diện Điều 3 khoản 2 tại ngày ≥ P-NGAY-PL05 THÌ hưởng trợ cấp, phụ cấp của nhiều diện; riêng trợ cấp người phục vụ và ưu đãi Điều 5 khoản 2 THÌ chỉ mức cao nhất | P-NGAY-PL05 | Khác BR-02 của TGXH. Trước 2027 chưa đọc bản gốc | PL 02/2020 Điều 6 khoản 3 (sửa bởi PL 05/2026) [CB-2] | Đã đối chiếu (từ 01/01/2027) | UC06 |
| BR-26 | Trợ cấp tuất của thân nhân | TN | NẾU thân nhân của từ hai NCC trở lên THÌ tối đa P-TUAT-TOI-DA-SUAT suất tuất hằng tháng, trừ ngoại lệ thân nhân liệt sĩ (Điều 6 khoản 5 điểm a đến d). NẾU NCC thuộc nhiều diện THÌ thân nhân hưởng tuất của một diện. Tuất nuôi dưỡng: một suất | P-TUAT-TOI-DA-SUAT | Ngoại lệ điểm b, c với thân nhân liệt sĩ | PL 02/2020 Điều 6 khoản 5, 6 [CB-2] | Đã đối chiếu | UC06, UC10, UC11 |
| BR-27 | Mai táng NCC | người tổ chức mai táng | NẾU NCC hoặc thân nhân thuộc Điều 6 khoản 4 chết THÌ một trợ cấp mai táng; NẾU đồng thời thuộc diện mai táng BHXH THÌ hưởng theo BHXH; trùng chế độ ngân sách khác THÌ một mức cao nhất | | | PL 02/2020 Điều 6 khoản 4 [CB-2] | Đã đối chiếu | UC11, UC12 |
| BR-28 | Tạm đình chỉ, chấm dứt và lan truyền sang thân nhân | ĐT, TN | NẾU NCC hoặc TN chấp hành án phạt tù (không phải tội xâm phạm an ninh quốc gia), xuất cảnh trái phép, mất tích THÌ tạm đình chỉ trong thời gian đó. NẾU thuộc Điều 54 khoản 3, 4, 5 THÌ chấm dứt. NẾU NCC bị tạm đình chỉ vì tội cố ý THÌ TN cũng tạm đình chỉ; NCC bị chấm dứt THÌ TN cũng chấm dứt | | | PL 02/2020 Điều 54 [CB-2] | Đã đối chiếu | UC07, UC11 |
| BR-29 | Bộ điều kiện công nhận theo ngày sự kiện | ĐT | NẾU ngày hy sinh, bị thương, bị bệnh trước 01/07/2021 và không đủ điều kiện hiện hành THÌ xét theo PL 26/2005 sửa bởi PL 04/2012. NẾU trước P-NGAY-PL05 và không đủ điều kiện PL 02/2020 sửa đổi THÌ xét theo PL 26/2005 sửa bởi PL 04/2012 | P-NGAY-PL05 | | PL 02/2020 Điều 58 khoản 1; PL 05/2026 Điều 2 khoản 2 [CB-2] | Đã đối chiếu | UC02 (hồ sơ), PL III mục D |
| BR-30 | Quà Chủ tịch nước | ĐT, TN | NẾU một NGƯỜI thuộc nhiều mức quà trong một đợt THÌ một suất mức cao nhất | mức theo đợt | Văn bản theo đợt | QĐ 01/QĐ-CTN (Tết 2026) | Chờ đối chiếu (BC) | UC02, UC07 |

### 3.3. Quy tắc dùng chung theo kỳ

| Mã BR | Tên | Logic | Căn cứ | Trạng thái | UC dùng |
|---|---|---|---|---|---|
| BR-40 | Tính mức đúng theo kỳ hưởng | Mức đúng của kỳ T dùng tham số có `ap_dung_tu ≤ T ≤ ap_dung_den`; không dùng ngày chi, không dùng ngày hiệu lực văn bản | Hệ quả của NĐ 335 Điều 32 khoản 3 và NĐ 321/2026 Điều 3 (mốc áp dụng khác ngày hiệu lực) | Đã đối chiếu cho TGXH; Chờ đối chiếu cho NCC | T09, UC07, UC12, UC17 |
| BR-41 | Đối chiếu chi sai phải gộp truy lĩnh | Số đã chi của kỳ T = khoản thường kỳ của T + các khoản truy lĩnh có `truy_linh_tu_ky ≤ T ≤ truy_linh_den_ky`. Chỉ so số này với mức đúng của T | Suy luận BA từ BR-13, BR-21; chưa có căn cứ dữ liệu nguồn | Chờ đối chiếu (phụ thuộc Q32) | UC07 |
| BR-42 | Phân loại hộ theo kỳ rà soát | Phân loại hộ chỉ có giá trị trong kỳ rà soát và theo chuẩn của kỳ đó: NĐ 07/2021 đến hết 2026, NĐ 351/2025 từ 2027 | NĐ 07/2021, NĐ 351/2025, TT 25/2026 | Chờ đối chiếu (BC) | UC05, UC15, UC17; BR-15 dùng |

### 3.4. Quy tắc tổng hợp và hiển thị (BA đề xuất, 27/10/2026)

Bốn quy tắc này không đọc từ văn bản pháp luật. Chúng lấy từ nguyên tắc chung của báo cáo 003 (mục 2, 6) và mô hình 007 (mục 4.1), nên mang trạng thái `Dự thảo` cho tới khi bên giao việc đồng ý. Theo quy ước, chưa dùng chúng làm tiêu chí nghiệm thu chính thức.

| Mã BR | Tên | Vai trò | Logic (NẾU, THÌ) | Tham số | Ưu tiên, ngoại lệ | Căn cứ | Trạng thái | UC dùng |
|---|---|---|---|---|---|---|---|---|
| BR-50 | Đếm người duy nhất | Mọi vai trò | NẾU đếm số người THÌ đếm số NGƯỜI (E01) khác nhau sau ghép định danh. NẾU bản ghi nguồn (E17) ở trạng thái "không ghép được" hoặc "ghép mờ chờ duyệt" THÌ đếm riêng thành "hồ sơ chưa xác định người", không cộng vào số người | | Một người thuộc nhiều nhóm được đếm ở mỗi nhóm; tổng các nhóm không phải số người | Báo cáo 003 mục 2 (nguyên tắc chung) | Dự thảo | UC01, UC02, UC04 |
| BR-51 | Xét theo ngày chốt | Mọi vai trò | NẾU chỉ tiêu xét tuổi, thành viên hộ, diện hoặc địa bàn cư trú tại ngày chốt D THÌ chỉ lấy bản ghi có `hieu_luc_tu ≤ D` và (`hieu_luc_den` rỗng hoặc `≥ D`); tuổi tính đến D | | Khác BR-40: BR-40 chọn tham số theo kỳ hưởng, BR-51 chọn bản ghi theo ngày chốt báo cáo | Báo cáo 003 mục 2 | Dự thảo | UC02, UC13, UC14 |
| BR-52 | Trạng thái sống chưa xác định | ĐT | NẾU NGƯỜI có trạng thái sống "chưa xác định" THÌ kiểm tra chi sai trả kết quả "chưa đủ dữ liệu", không coi là "còn sống" và không kết luận "chi đúng" | | Áp trước BR-05, BR-08, BR-28 | Tài liệu 007 mục 4.1 | Dự thảo | UC04, UC07 |
| BR-53 | Thiếu dữ liệu khác số 0 | Mọi vai trò | NẾU chỉ tiêu không tính được vì thiếu dữ liệu THÌ hiển thị "chưa có dữ liệu", không hiển thị 0. Nhóm "chưa rõ" (chưa rõ địa bàn, chưa rõ diện) luôn hiển thị | | | Báo cáo 003 mục 6 | Dự thảo | UC01, UC02, UC03 |

Tổng hợp: 34 BR. Đã đối chiếu: 23 (BR-01 đến BR-16, BR-23 đến BR-29). Chờ đối chiếu: 6 (BR-20, BR-21, BR-22, BR-30, BR-41, BR-42). BR-40 tách trạng thái: Đã đối chiếu cho TGXH, Chờ đối chiếu cho NCC. Dự thảo: 4 (BR-50 đến BR-53).

## 4. Từ điển dữ liệu: E21, E22, E23

Mức khái niệm, không phải thiết kế vật lý. Tên trường theo báo cáo 007 mục 3.1.

### 4.1. E21 VĂN BẢN PHÁP LÝ

| Trường | Ý nghĩa | Kiểu | Bắt buộc | Quy tắc kiểm tra |
|---|---|---|---|---|
| so_hieu | Số hiệu, ví dụ 335/2026/NĐ-CP | chuỗi | Có | Duy nhất |
| loai_van_ban | Luật, pháp lệnh, nghị định, thông tư, quyết định, VBHN, dự thảo | danh mục | Có | |
| ngay_ban_hanh | | ngày | Có, trừ dự thảo | |
| ngay_hieu_luc | Ngày văn bản có hiệu lực | ngày | Có, trừ dự thảo | ≥ ngay_ban_hanh |
| ngay_het_hieu_luc | | ngày | Không | > ngay_hieu_luc |
| van_ban_thay_the | Văn bản thay thế toàn bộ | tham chiếu E21 | Không | |
| sua_doi_boi | Danh sách văn bản sửa đổi, kèm điều khoản bị sửa | danh sách | Không | Ví dụ PL 02/2020 ← PL 05/2026 (Điều 3, 5, 6...) |
| la_van_ban_theo_dot | Quyết định ban hành mỗi dịp | có/không | Có | |
| co_quan_ban_hanh, co_quan_chu_tri | | chuỗi | Có | |
| muc_tin_cay | CB, TV, BC, HB | danh mục | Có | Chỉ CB cho phép BR "Đã đối chiếu" |
| url_ban_goc, ngay_tra | Bằng chứng đối chiếu | chuỗi, ngày | Có khi muc_tin_cay = CB | |

### 4.2. E22 THAM SỐ CHÍNH SÁCH

| Trường | Ý nghĩa | Kiểu | Bắt buộc | Quy tắc kiểm tra |
|---|---|---|---|---|
| ma_tham_so | Ví dụ P-MUC-CHUAN-TGXH | chuỗi | Có | |
| gia_tri | | số | Có | > 0 |
| don_vi | đồng/tháng, hệ số, lần mức chuẩn, tháng, năm, suất | danh mục | Có | |
| pham_vi | toàn quốc / tỉnh | danh mục | Có | |
| ma_tinh | Mã tỉnh theo QĐ 19/2025 | mã E13 | Khi pham_vi = tỉnh | |
| ap_dung_tu | Mốc áp dụng cho dữ liệu | ngày | Có | Không bắt buộc bằng ngày hiệu lực văn bản (BR-40) |
| ap_dung_den | | ngày | Không | Hai dòng cùng ma_tham_so, pham_vi, ma_tinh không được chồng khoảng thời gian |
| van_ban, dieu_khoan | Căn cứ | tham chiếu E21, chuỗi | Có | dieu_khoan phải tới cấp khoản hoặc điểm |
| ma_che_do, ma_dien | Chế độ, diện áp dụng | tham chiếu E20, E04 | Có cho hệ số | |
| dieu_kien_tuoi_tu, dieu_kien_tuoi_den, don_vi_tuoi | Ngưỡng tuổi (4, 16, 60, 75 năm; 36 tháng) | số, danh mục | Không | tu < den |
| quy_tac_lam_tron | Ví dụ đến nghìn đồng | danh mục | Không | |
| trang_thai_doi_chieu | Đã đối chiếu, Chờ đối chiếu, Dự thảo | danh mục | Có | Theo muc_tin_cay của van_ban |

### 4.3. E23 QUY TẮC

| Trường | Ý nghĩa | Kiểu | Bắt buộc | Quy tắc kiểm tra |
|---|---|---|---|---|
| ma_br | BR-xx | chuỗi | Có | Duy nhất |
| ten | | chuỗi | Có | |
| vai_tro_ap_dung | ĐT, NH, NN, NCS, TN | danh sách | Có | |
| dieu_kien | Biểu thức NẾU | văn bản có cấu trúc | Có | Chỉ dùng tên thực thể của mô hình lõi |
| ket_qua | Biểu thức THÌ | văn bản có cấu trúc | Có | |
| tham_so_dung | | danh sách mã E22 | Không | Mọi mã phải tồn tại trong E22 |
| thang_br, ngoai_le_cua | Quan hệ ưu tiên | tham chiếu E23 | Không | Không tạo vòng |
| van_ban, dieu_khoan | | tham chiếu E21, chuỗi | Có | |
| ap_dung_tu, ap_dung_den | | ngày | Có | |
| trang_thai | Dự thảo, Chờ đối chiếu, Đã đối chiếu, Đã xác nhận, Hết hiệu lực | danh mục | Có | |

### 4.4. Thuộc tính ở thực thể khác mà các BR cần

Chỉ liệt kê, không đặc tả, vì chưa biết nguồn nào có. Điều kiện dữ liệu này nằm trong checklist khảo sát (009 mục 4).

| BR | Thực thể.thuộc tính cần | Câu hỏi checklist |
|---|---|---|
| BR-04, BR-05 | E09 QUYẾT ĐỊNH.ngày ký, loại; E15 SỰ KIỆN.ngày xảy ra | Q31 |
| BR-06 | E12 CƯ TRÚ.từ ngày, đến ngày; E09 quyết định thôi chi trả | P1-05 (mới) |
| BR-07 | E07 CHI TRẢ.kết quả chi theo kỳ | Q32 |
| BR-09, BR-11, BR-12 | E06 QUAN HỆ loại chăm sóc, nhận nuôi dưỡng; ngày sinh con | Q31, P2-03 (mới) |
| BR-13, BR-41 | E07 CHI TRẢ.kỳ hưởng, loại khoản, truy lĩnh từ, đến kỳ | Q32, P1-03 (mới) |
| BR-14 | E30 HỒ SƠ TTHC.ngày tiếp nhận | P1-04 (mới) |
| BR-23, BR-24, BR-26 | E06 QUAN HỆ loại thân nhân, căn cứ, thời gian nuôi | Q34, P2-02 (mới) |
| BR-28 | E15 SỰ KIỆN loại án phạt tù, xuất cảnh, mất tích; nguồn | P2-04 (mới) |
| BR-29 | E15 SỰ KIỆN.ngày hy sinh, bị thương, bị bệnh | P1-06 (mới) |

## 5. Kịch bản kiểm thử mức quy tắc

Dữ liệu trong bảng là **dữ liệu giả**. Kịch bản của BR "Chờ đối chiếu" không dùng làm tiêu chí nghiệm thu. Khi UC được đặc tả, mỗi kịch bản chuyển thành TC-UCxx-nn.

| Mã | Cho (dữ liệu giả) | Khi | Thì | BR |
|---|---|---|---|---|
| TC-BR01-01 | Người khuyết tật đặc biệt nặng, 40 tuổi, tỉnh không có mức HĐND riêng | Tính mức đúng kỳ 08/2026 | 540.000 × 2,0 = 1.080.000đ | BR-01, BR-40 |
| TC-BR01-02 | Như trên, kỳ 05/2026 | Tính mức đúng | Dùng mức chuẩn kỳ 05/2026 (500.000đ, chưa xác minh) × hệ số theo văn bản kỳ đó; không dùng 540.000đ | BR-40 |
| TC-BR01-03 | Tỉnh X có nghị quyết HĐND mức chuẩn 600.000đ từ 01/2027 | Tính mức kỳ 02/2027 cho người ở tỉnh X | Dùng 600.000đ | BR-01 |
| TC-BR02-01 | Trẻ em 3 tuổi mồ côi (hệ số 2,5) đồng thời khuyết tật đặc biệt nặng (hệ số 2,5) | Tính mức | Một mức 2,5; cảnh báo nếu dữ liệu chi trả có hai khoản | BR-02 |
| TC-BR03-01 | Người khuyết tật nặng, đơn thân nghèo nuôi 2 con dưới 16 tuổi | Tính mức | Hưởng cả hệ số 1,5 (khoản 6) và 2 × 1,0 (khoản 4); không gắn cảnh báo trùng | BR-03 |
| TC-BR05-01 | Đối tượng chết ngày 20/09/2026 | Xác định kỳ cuối được hưởng | Kỳ 09/2026 là kỳ cuối; chi kỳ 10/2026 là chi sai | BR-05 |
| TC-BR06-01 | Đối tượng thôi chi trả ở xã A từ 11/2026, chuyển xã B ở tỉnh khác | Xác định kỳ đầu ở xã B | 11/2026, theo mức áp dụng tại tỉnh của xã B | BR-06 |
| TC-BR07-01 | Đối tượng không nhận tiền các kỳ 10, 11, 12/2026 | Kiểm tra trạng thái | Phải có quyết định tạm dừng; nếu vẫn lập danh sách chi kỳ 01/2027 thì gắn cảnh báo | BR-07 |
| TC-BR09-01 | NCS nhận nuôi trẻ em mồ côi; NCS chết ngày 05/12/2026 | Kiểm tra hỗ trợ kinh phí của NCS | Thôi hỗ trợ cho NCS; trẻ cần quyết định mới | BR-09 |
| TC-BR11-01 | Hai vợ chồng cùng khuyết tật nặng, nuôi một con 20 tháng tuổi | Tính hỗ trợ chăm sóc | Một suất hệ số 1,5 | BR-11 |
| TC-BR11-02 | NKT nặng nuôi con, con đủ 36 tháng vào tháng 03/2027 | Kiểm tra kỳ 04/2027 | Không còn hưởng hệ số nuôi con nhỏ | BR-11 |
| TC-BR13-01 | Đối tượng đang hưởng theo NĐ 20/2021, kỳ 07 đến 09/2026 đã chi theo 500.000đ, quyết định mới ký 10/2026 | Đối chiếu chi kỳ 07/2026 | Mức đúng theo 540.000đ; khoản chênh phải là truy lĩnh, không phải chi thiếu nếu đã chi truy lĩnh | BR-13, BR-41 |
| TC-BR14-01 | Hồ sơ TGXH tiếp nhận 01/10/2026, quyết định 20/10/2026 | Ghi nhận căn cứ thủ tục | Căn cứ thủ tục NĐ 147/2025; người nộp không có yêu cầu nộp lại | BR-14 |
| TC-BR15-01 | Người 72 tuổi, hộ nghèo, có con đang sống cùng và không hưởng trợ cấp xã hội | Kiểm tra diện | Không thuộc Điều 5 khoản 5 điểm a; xét hưu trí xã hội (BR-16) | BR-15, BR-16 |
| TC-BR16-01 | Người 76 tuổi không có lương hưu, đồng thời NKT nặng (hệ số NCT là NKT nặng 2,0) | Tính mức kỳ 08/2026 | So 540.000đ (hưu trí xã hội) với 1.080.000đ (TGXH), hưởng mức cao hơn | BR-16 |
| TC-BR23-01 | Quan hệ "cháu nội" khai là thân nhân liệt sĩ, ngày tính 02/2027 | Kiểm tra loại quan hệ | Không thuộc thân nhân; từ chối hoặc cảnh báo | BR-23 |
| TC-BR24-01 | Người nuôi liệt sĩ từ khi liệt sĩ 8 tuổi đến 15 tuổi (7 năm) | Kiểm tra người có công nuôi liệt sĩ | Không đủ điều kiện (dưới 10 năm) | BR-24 |
| TC-BR25-01 | Người vừa là thương binh, vừa là bệnh binh, kỳ 03/2027 | Kiểm tra trùng | Được hưởng trợ cấp của cả hai diện; trợ cấp người phục vụ chỉ một mức cao nhất | BR-25 |
| TC-BR26-01 | Vợ của ba người có công đã mất (không phải liệt sĩ) | Đếm suất tuất hằng tháng | Tối đa 2 suất; suất thứ ba gắn cảnh báo | BR-26 |
| TC-BR27-01 | NCC chết, đồng thời thuộc diện mai táng BHXH | Kiểm tra mai táng | Một trợ cấp, theo BHXH | BR-27 |
| TC-BR28-01 | Thương binh bị phạt tù có thời hạn vì tội cố ý từ 06/2027 | Kiểm tra trạng thái thân nhân | Thương binh và thân nhân cùng tạm đình chỉ trong thời gian chấp hành án | BR-28 |
| TC-BR29-01 | Hồ sơ người bị thương năm 1990, nộp năm 2027, không đủ điều kiện PL 02/2020 sửa đổi | Chọn bộ điều kiện | Xét theo PL 26/2005 sửa bởi PL 04/2012 | BR-29 |
| TC-BR40-01 | Thân nhân 01 liệt sĩ, kỳ 11/2026, được điều dưỡng tại nhà trong năm 2026 | Tính mức đúng | Trợ cấp theo NĐ 321/2026; điều dưỡng theo NĐ 77/2024 (chưa xác minh) | BR-21, BR-40 |
| TC-BR50-01 | Nguồn có 1.000 bản ghi; 900 bản ghi ghép vào 870 người, 100 bản ghi không ghép được | Đếm số người | 870 người và 100 hồ sơ chưa xác định người; không báo 970 hay 1.000 | BR-50 |
| TC-BR51-01 | Diện NKT của một người hết hiệu lực 30/09/2026 | Đếm NKT tại ngày chốt 15/10/2026 | Người này không được đếm | BR-51 |
| TC-BR52-01 | Đối tượng có trạng thái sống "chưa xác định", kỳ 10/2026 vẫn chi | Kiểm tra chi sai | Kết quả "chưa đủ dữ liệu"; không phải "chi đúng", không phải "chi sai" | BR-52 |
| TC-BR53-01 | Nguồn hộ chưa đồng bộ lần nào | Hiển thị số hộ | "Chưa có dữ liệu", không hiển thị 0 | BR-53 |

## 6. Ma trận truy vết

Cột "Trạng thái UC" lấy từ sheet "Task & Usecase". Chưa có YC-xx từ bên giao việc vì chưa có biên bản; nguồn yêu cầu ghi là văn bản pháp luật hoặc mục Phụ lục III dự thảo.

| Văn bản, điều | Nguồn yêu cầu (YC) | BR | T/UC | Kịch bản | Giai đoạn đề xuất | Trạng thái UC |
|---|---|---|---|---|---|---|
| NĐ 335 Điều 4, 6 | PL III 79 đến 84 (tính toán chế độ, chỉ NCC); sheet T09 | BR-01, BR-02, BR-03 | T09, UC06, UC07, UC09, UC12 | TC-BR01-01..03, TC-BR02-01, TC-BR03-01 | GĐ1b | Giả định |
| NĐ 335 Điều 8 khoản 2 đến 4 | Sheet T09, UC07 | BR-04, BR-05, BR-06 | UC07, UC09, UC11, UC14 | TC-BR05-01, TC-BR06-01 | GĐ1b, GĐ2 | Giả định |
| NĐ 335 Điều 9 | Sheet UC07, UC08 | BR-07, BR-08, BR-09 | UC07, UC08, UC11 | TC-BR07-01, TC-BR09-01 | GĐ1b, GĐ2 | Giả định |
| NĐ 335 Điều 11 | Sheet UC11 | BR-10 | UC11, UC12 | Chưa có | GĐ2 | Giả định |
| NĐ 335 Điều 17 | Sheet UC08, UC10 | BR-11, BR-12 | UC08, UC10, UC12 | TC-BR11-01, TC-BR11-02 | GĐ2 | Giả định |
| NĐ 335 Điều 32, 33 | Văn bản (chuyển tiếp) | BR-13, BR-14 | UC07, UC12, UC02 | TC-BR13-01, TC-BR14-01 | GĐ1b | Giả định |
| NĐ 335 Điều 5 khoản 5; Điều 31 | Sheet UC06, UC09 | BR-15, BR-16 | UC06, UC09, UC13 | TC-BR15-01, TC-BR16-01 | GĐ1b, GĐ2 | Giả định |
| NĐ 321/2026 Phụ lục, Điều 3, 15 | PL III 111 đến 113, 135, 147 | BR-20, BR-21, BR-22 | T09, UC07, UC11, UC12 | TC-BR40-01 | GĐ1b | Giả định |
| PL 02/2020 Điều 3 khoản 3, Điều 4 khoản 2 (sửa 2026) | PL III 124 đến 128 | BR-23, BR-24 | T04, UC04, UC10 | TC-BR23-01, TC-BR24-01 | GĐ1b, GĐ2 | Giả định |
| PL 02/2020 Điều 6 khoản 3 đến 6 | PL III 132 (cảnh báo trùng chế độ) | BR-25, BR-26, BR-27 | UC06, UC10, UC11 | TC-BR25-01, TC-BR26-01, TC-BR27-01 | GĐ1b | Giả định |
| PL 02/2020 Điều 54 | PL III 28 (lý do chấm dứt), 133, 134 | BR-28 | UC07, UC11 | TC-BR28-01 | GĐ1b | Giả định |
| PL 02/2020 Điều 58; PL 05/2026 Điều 2 | PL III mục D (giải quyết hồ sơ) | BR-29 | Chưa có UC (mục D chưa thuộc Excel) | TC-BR29-01 | Chưa xếp | Không có UC |
| QĐ 01/QĐ-CTN | PL III 161, 162, 180 đến 182, 205 đến 208 | BR-30 | UC02, UC07 | Chưa có | GĐ2 | Giả định |
| Suy luận từ BR-13, BR-21 | Sheet UC07; 017 kết luận 2 | BR-40, BR-41 | T09, UC07, UC12, UC17 | TC-BR01-02, TC-BR13-01, TC-BR40-01 | GĐ1b | Giả định |
| NĐ 07/2021, NĐ 351/2025, TT 25/2026 | Sheet T08, UC15 | BR-42 | UC05, UC15, UC17 | Chưa có | GĐ2, GĐ3 | Giả định |
| Báo cáo 003 mục 2 (nguyên tắc chung) | Đặc tả 015 UC01, UC02, UC04 | BR-50 | UC01, UC02, UC04 | TC-BR50-01; TC-UC01-02, TC-UC02-01, TC-UC04-07 | GĐ1a, GĐ1b | Giả định |
| Báo cáo 003 mục 2 | Đặc tả 015 UC02 | BR-51 | UC02, UC13, UC14 | TC-BR51-01; TC-UC02-02 | GĐ1a, GĐ1b, GĐ2 | Giả định |
| Tài liệu 007 mục 4.1 | Đặc tả 015 UC04, UC07 | BR-52 | UC04, UC07 | TC-BR52-01; TC-UC04-04, TC-UC07-07 | GĐ1b | Giả định |
| Báo cáo 003 mục 6 | Đặc tả 015 UC01, UC02 | BR-53 | UC01, UC02, UC03 | TC-BR53-01; TC-UC01-03, TC-UC02-03, TC-UC02-04 | GĐ1a, GĐ2 | Giả định |

### Khoảng trống truy vết

1. **YC chưa có UC:** PL III mục D (33 mục thủ tục hành chính) và mục H (chi trả, quà tri ân); PL III 14 đến 22 (quy trình, biểu mẫu động); di chuyển hồ sơ NCC giữa tỉnh (PL III 102 đến 105) chỉ được phủ một phần bởi UC11, UC14; xử lý truy lĩnh không có UC riêng.
2. **BR chưa có kịch bản:** BR-08, BR-10, BR-12, BR-22, BR-30, BR-42.
3. **UC "Đã xác nhận" còn BR "Chờ đối chiếu":** không có, vì chưa UC nào được xác nhận.

## 7. Mục chưa đặc tả (chỉ liệt kê)

| Mã | Lý do chưa đặc tả | Điều kiện để đặc tả |
|---|---|---|
| T01 đến T08, T10, T11 | Phụ thuộc số nguồn, phương thức kết nối, nền tảng có sẵn | Trả lời Q12 đến Q15, Q28, Q37; tài liệu API |
| T09 | Quy tắc đã có (mục 3), nhưng phạm vi lĩnh vực và nơi cấu hình chưa chốt | Trả lời Q27, Q30 |
| UC01 | Cần biết nguồn và quyền truy cập dữ liệu | Q6, Q7, Q12 |
| UC02, UC03 | Biểu mẫu báo cáo bắt buộc chưa có; TT 18/2025/TT-BNV chưa xem biểu mẫu NCC | Q16, Q19; biểu mẫu khách hàng |
| UC04, UC05 | Phân quyền, che dữ liệu, nguồn quan hệ chưa rõ | Q20, Q31, Q34 |
| UC06 đến UC08 | Cần dữ liệu chi trả có kỳ hưởng và truy lĩnh | Q32, P1-03 |
| UC09 đến UC11 | Cần dữ liệu "đủ điều kiện" và sự kiện vòng đời | Q31, Q33, P1-05 |
| UC12 đến UC19 | GĐ2, GĐ3; phạm vi chưa chốt | Q27, Q30 và kết quả UC01 |
