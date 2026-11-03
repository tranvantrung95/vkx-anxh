---
name: ba-dac-ta-use-case
description: Viết đặc tả use case, tiêu chí nghiệm thu và tổng hợp SRS cho project019 (module tích hợp và phân tích dữ liệu an sinh xã hội, các mã T01–T11, UC01–UC19). Dùng khi người dùng nhờ đặc tả một UC, viết luồng xử lý, tiêu chí nghiệm thu, wireframe mô tả màn hình/dashboard, ghép SRS, hoặc rà một đặc tả có thiếu sót không. Dùng cả khi người dùng chỉ nói "viết UC07" hay "làm SRS phần dashboard".
---

# Đặc tả use case và SRS

Đọc mục "Quy ước BA" trong `CLAUDE.md` của dự án trước khi bắt đầu.

## Nguồn phải đọc trước khi viết một UC

1. Dòng của UC trong sheet `Task & Usecase` của checklist đang cập nhật (`work/*checklist_hop_dang_cap_nhat*.xlsx`, chưa có thì dùng bản trong `input/`). Lấy mô tả, trục phân tích, dữ liệu/phụ thuộc, giai đoạn và cột "Căn cứ / Giả định".
2. Sheet `Mô hình dữ liệu`: thực thể nào UC đọc/ghi.
3. Danh mục quy tắc BR-xx (skill `ba-quy-tac-truy-vet`). UC dùng quy tắc chưa có trong danh mục thì tạo BR mới qua skill đó, không viết điều kiện chính sách trực tiếp trong luồng.
4. Báo cáo phạm vi `output/project019_003_*.md` và biên bản họp gần nhất trong `output/*bien_ban_hop*`.

## Quy trình

1. **Xác định trạng thái UC.** Trạng thái xác nhận còn "Giả định" thì đặt cờ ở đầu đặc tả: "Bản nháp dựa trên giả định, chưa được bên giao việc xác nhận".
2. **Liệt kê lỗ hổng trước khi viết.** Gồm dữ liệu chưa biết nguồn nào có, quy tắc chưa rõ điều khoản, tác nhân và quyền chưa rõ. Lỗ hổng nhiều thì gọi skill `grilling` để hỏi người dùng từng câu. Phần nào chỉ bên giao việc trả lời được thì ghi vào mục "Câu hỏi mở" và đề xuất thêm vào checklist.
3. **Viết theo `templates/dac_ta_use_case.md`.** Các yêu cầu bắt buộc:
   - Luồng chính đánh số. Luồng thay thế và luồng ngoại lệ tham chiếu bước của luồng chính (ví dụ `3a`).
   - Mỗi điều kiện nghiệp vụ dẫn chiếu `BR-xx`, không viết con số chính sách trần trong luồng.
   - Dữ liệu ghi theo thực thể và thuộc tính của mô hình lõi (NGƯỜI, HỘ, HỒ SƠ HƯỞNG...), kèm nguồn trong 7 nguồn.
   - Với UC có dữ liệu cá nhân: ghi quyền xem theo vai trò và địa bàn, trường cần che, và việc ghi nhật ký tra cứu (T10, Luật 91/2025).
4. **Tiêu chí nghiệm thu** dạng Cho/Khi/Thì, mã `TC-UCxx-nn`. Mỗi BR mà UC dùng phải có ít nhất 1 tiêu chí. Mỗi luồng ngoại lệ phải có 1 tiêu chí. Dữ liệu ví dụ trong tiêu chí là dữ liệu giả, ghi rõ "dữ liệu giả".
5. **Màn hình/dashboard** (nếu có): mô tả bộ lọc, chỉ tiêu và cách tính, biểu đồ, drill-down, xuất file. Cần hình thì gọi skill `diagram` (luồng) hoặc `markdown-mermaid-writing` (sequence/activity).
6. **Ghép SRS** theo `templates/srs_khung.md` khi người dùng yêu cầu. Nếu bên giao việc có mẫu bắt buộc (câu hỏi Q19 của checklist), mẫu đó thay thế khung này.
7. **Tự rà trước khi giao**: không còn ô `<...>`; mọi BR và TC đều có mã; mọi thực thể đều có trong mô hình; mọi giả định nằm ở mục giả định. Soát văn bằng skill `kiem-tra-ai-2`.
8. **Cập nhật truy vết**: báo skill `ba-quy-tac-truy-vet` thêm các dòng UC ↔ BR ↔ TC vào ma trận.

## Đầu ra

- Một UC: `output/project019_NNN_dac_ta_<ucxx>_<ten_ngan>.md`. Bản Word dùng skill `docx`.
- SRS: `output/project019_NNN_srs_<pham_vi>.docx` kèm bản Markdown cùng tên.
- Sửa UC đã có thì sửa trong file cũ và ghi lịch sử phiên bản, không tạo số mới.
