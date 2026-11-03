---
name: ba-quy-tac-truy-vet
description: Quản lý quy tắc nghiệp vụ gắn căn cứ pháp lý, ma trận truy vết và yêu cầu thay đổi (CR) cho project019 (chính sách trợ giúp xã hội, người có công, giảm nghèo). Dùng khi người dùng cần chuyển điều khoản văn bản (NĐ 335/2026, NĐ 321/2026, NĐ 351/2025, Pháp lệnh 02/2020...) thành quy tắc BR-xx cấu hình được, kiểm tra quy tắc còn hiệu lực, xem yêu cầu nào đã có UC/test, đánh giá ảnh hưởng khi văn bản hoặc phạm vi thay đổi, hoặc lập phiếu change request.
---

# Quy tắc nghiệp vụ, truy vết và thay đổi

Đọc mục "Quy ước BA" trong `CLAUDE.md` của dự án trước khi bắt đầu.

Có 3 sổ đăng ký. Mỗi sổ là một file trong `work/`, tìm bằng `ls work/*danh_muc_quy_tac* work/*ma_tran_truy_vet* work/*so_cr*`. Chưa có thì tạo từ mẫu, lấy số NNN kế tiếp.

## A. Danh mục quy tắc (BR-xx), mẫu `templates/danh_muc_quy_tac.md`

1. **Nguồn**: sheet `Căn cứ pháp lý` của checklist. Mỗi BR phải dẫn tới điều, khoản, điểm cụ thể. Chỉ ghi tên văn bản là chưa đủ.
2. **Kiểm tra văn bản trước khi dùng**:
   - BR chỉ được `Đã đối chiếu` khi điều khoản nó dẫn đã được đọc toàn văn: cột "Kiểm tra" ghi "Đã kiểm tra nội dung các Điều" và có đúng điều đó, hoặc BA vừa đối chiếu và ghi URL, ngày tra. Các giá trị khác ("Đã kiểm tra số hiệu", "Cần BA đối chiếu toàn văn", ô trống) đều cho trạng thái `Chờ đối chiếu`. Không dùng BR `Chờ đối chiếu` làm tiêu chí nghiệm thu.
   - Văn bản là DỰ THẢO thì BR mang trạng thái `Dự thảo`.
   - Cần tra lại toàn văn thì dùng WebSearch/WebFetch, ghi URL và ngày tra vào cột căn cứ. Không trích dài quá 15 từ.
3. **Viết quy tắc để cấu hình được (T09)**:
   - Tách **tham số** (mức chuẩn, hệ số, ngưỡng tuổi, chuẩn nghèo) khỏi **logic**.
   - Tham số ghi cùng hiệu lực từ–đến. Không viết cứng con số trong logic.
   - Logic viết dạng NẾU … THÌ …, dùng đúng tên thực thể của mô hình lõi.
   - Ghi rõ vai trò áp dụng: đối tượng, người được hưởng, người nhận tiền, người chăm sóc, thân nhân.
4. **Quy tắc xung đột** (ví dụ nhiều diện chỉ hưởng mức cao nhất, trừ ngoại lệ đơn thân theo Điều 6 khoản 2 NĐ 335/2026): ghi thứ tự ưu tiên và ngoại lệ thành BR riêng, tham chiếu chéo.
5. **Quy tắc chuyển tiếp**: khi chuẩn cũ và chuẩn mới cùng tồn tại (NĐ 07/2021 áp dụng tới hết 2026, NĐ 351/2025 áp dụng từ 2027), mỗi chuẩn là một bộ tham số có hiệu lực riêng.

## B. Ma trận truy vết, mẫu `templates/ma_tran_truy_vet.md`

- Chuỗi truy vết: `YC-xx` (yêu cầu từ bên giao việc hoặc văn bản) → `UCxx`/`Txx` → `BR-xx` → `TC-UCxx-nn` → trạng thái.
- Mỗi lần có đặc tả UC mới (skill `ba-dac-ta-use-case`) thì thêm các dòng tương ứng.
- Khi người dùng hỏi về độ phủ, báo 3 danh sách:
  - YC chưa có UC.
  - BR chưa có TC.
  - UC ở trạng thái "Đã xác nhận" mà còn BR `Chờ đối chiếu`.

## C. Change request, mẫu `templates/phieu_cr.md`

1. Mở CR khi phạm vi đã chốt bị đổi. Các trường hợp: biên bản họp ghi nhận thay đổi, văn bản pháp lý mới hoặc sửa đổi, bên giao việc thêm hoặc bớt UC.
2. **Phân tích ảnh hưởng** bằng cách lần theo ma trận: BR bị đổi → UC dùng BR → TC → giai đoạn và mốc trong sheet `Lộ trình`. Ghi ước lượng ngày công tăng hoặc giảm, hoặc ghi "chưa ước lượng".
3. CR chỉ chuyển `Đã duyệt` khi người dùng xác nhận có người duyệt phía bên giao việc. Agent không tự duyệt.
4. Sau khi duyệt: cập nhật BR, ma trận, đặc tả UC liên quan và trạng thái task trong checklist (qua skill `ba-hop-khao-sat`).

## Kết thúc

- Soát văn bằng skill `kiem-tra-ai-2`.
- Báo người dùng: số BR theo trạng thái, các khoảng trống truy vết, CR đang mở.
