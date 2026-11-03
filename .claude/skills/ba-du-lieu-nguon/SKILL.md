---
name: ba-du-lieu-nguon
description: Phân tích dữ liệu nguồn cho project019 (7 nguồn API an sinh xã hội của các bộ khác nhau). Dùng khi người dùng có tài liệu API, file dữ liệu mẫu/dump, danh mục mã của một nguồn và cần lập từ điển dữ liệu, mapping trường nguồn sang mô hình lõi NGƯỜI–HỘ–HỒ SƠ HƯỞNG–QUAN HỆ, đánh giá chất lượng "đúng–đủ–sạch–sống" (UC01), kiểm tra tỷ lệ có CCCD, hoặc trả lời "nguồn này dùng được cho UC nào".
---

# Phân tích dữ liệu nguồn

Đọc mục "Quy ước BA" trong `CLAUDE.md` của dự án trước khi bắt đầu.

**An toàn dữ liệu (bắt buộc).** Dữ liệu nguồn chứa dữ liệu cá nhân nhạy cảm (sức khỏe, khuyết tật, số định danh). Không in, trích dẫn hay ghi giá trị thô vào tài liệu, chat hoặc nhật ký. Chỉ ghi thống kê và mẫu định dạng đã che. File dữ liệu thật đặt trong `input/` và không được sao ra ngoài dự án. Nếu bên giao việc cấm mang dữ liệu ra khỏi môi trường của họ (Q8), chỉ làm trên tài liệu mô tả, không xin file.

## Quy trình cho một nguồn

1. **Nhận diện nguồn.** Ghi: tên, cơ quan chủ quản, phương thức (API/DB/file), xác thực, giới hạn gọi, full hay incremental, tần suất cập nhật. Ghi thêm đơn vị dữ liệu: theo **cá nhân** hay theo **hộ**. Đây là câu hỏi then chốt của T01.
2. **Profiling** khi có file mẫu:

   ```bash
   python3 -I .claude/skills/ba-du-lieu-nguon/scripts/profile_nguon.py <file.csv|xlsx> \
     --ten-nguon "<tên>" --key <cột khóa> --cccd <cột số định danh> \
     --date <cột ngày>[,<cột ngày>] --ma-dia-ban <cột mã xã/tỉnh> \
     --out work/project019_NNN_profiling_<ten_nguon>.md
   ```

   Script chỉ xuất thống kê và mẫu đã che. Nếu bản Excel có nhiều sheet thì chọn bằng `--sheet`.
3. **Từ điển dữ liệu và mapping** theo `templates/tu_dien_va_mapping.md`:
   - Mỗi trường nguồn ánh xạ về một thực thể và thuộc tính của mô hình lõi (sheet `Mô hình dữ liệu`), hoặc ghi "không dùng" kèm lý do.
   - Mã danh mục riêng của nguồn (diện, mức độ khuyết tật, loại quan hệ) đưa vào bảng chuyển mã sang danh mục dùng chung (T04).
   - Mã địa bàn phải xác định là mã trước hay sau sắp xếp 2025 (T05, QĐ 19/2025/QĐ-TTg).
4. **Đánh giá theo "đúng–đủ–sạch–sống"** (Đề án 06), mỗi tiêu chí có chỉ số đo được:
   - Đúng: tỷ lệ CCCD đúng định dạng 12 số, ngày hợp lệ, mã danh mục khớp.
   - Đủ: tỷ lệ trống của các trường bắt buộc cho UC; độ phủ theo tỉnh.
   - Sạch: trùng theo khóa, mâu thuẫn giữa trường (ví dụ trạng thái "mất" nhưng vẫn có kỳ chi).
   - Sống: ngày cập nhật gần nhất, độ trễ so với thực tế.
   - **Quan hệ**: tỷ lệ hồ sơ xác định được người nhận, người chăm sóc, hộ. Đây là điều kiện của UC08, UC10, UC11.
5. **Kết luận khả dụng theo UC**: ma trận nguồn × UC với giá trị Đủ / Thiếu trường … / Không có. Nguồn nào thiếu dữ liệu chi trả hoặc quan hệ thì ghi rõ UC bị chặn và đề xuất câu hỏi mới cho checklist.
6. **Bàn giao**: `output/project019_NNN_tu_dien_mapping_<ten_nguon>.md`. Cần tổng hợp nhiều nguồn trong một bảng tính thì dùng skill `xlsx`. Cập nhật kết quả liên quan vào checklist qua skill `ba-hop-khao-sat`.

## Không làm

- Không suy ra chất lượng từ tài liệu API khi chưa có dữ liệu. Phần đó ghi "chưa kiểm chứng".
- Không tự ghép định danh hay ghép hộ trên dữ liệu thật trong máy cá nhân. Việc đó là T06/T08 trên môi trường dự án.
