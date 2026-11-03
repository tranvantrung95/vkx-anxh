---
name: ba-hop-khao-sat
description: Chuẩn bị và ghi nhận buổi họp/khảo sát BA của project019 (module tích hợp và phân tích dữ liệu an sinh xã hội). Dùng khi người dùng cần lọc câu hỏi mang đi họp, soạn agenda, ghi biên bản từ ghi chú hoặc transcript, cập nhật trạng thái câu hỏi và task/usecase vào file Excel checklist, hoặc hỏi "sau buổi họp còn gì chưa rõ". Dùng cả khi người dùng chỉ dán ghi chú họp lộn xộn mà không gọi tên skill.
---

# Họp và khảo sát BA

Nguồn sự thật cho câu hỏi và task là file Excel checklist, không phải trí nhớ của agent.

- Bản gốc (chỉ đọc): `input/Checklist_hop_ky_thuat_module_tich_hop_du_lieu.xlsx`
- Bản đang cập nhật: `work/project019_NNN_checklist_hop_dang_cap_nhat.xlsx`. Tìm bằng `ls work/*checklist_hop_dang_cap_nhat*`. Chưa có thì tạo bằng script ở bước C, lấy số NNN kế tiếp theo quy tắc đặt tên của Workspace.

Đọc mục "Quy ước BA" trong `CLAUDE.md` của dự án trước khi bắt đầu.

## A. Trước buổi họp

1. Đọc checklist: `python3 -I .claude/skills/ba-hop-khao-sat/scripts/cap_nhat_checklist.py --in <file> --report`. Lệnh in câu hỏi theo nhóm, ưu tiên, trạng thái và thống kê task.
2. Chọn câu mang đi: ưu tiên Cao trước, rồi câu "Chưa xử lý". Từ 03/11/2026 project019 không có đầu mối để hỏi (PF-126): sheet `Checklist họp` là sổ giả định và quyết định BA, mỗi câu được trả lời bằng tra cứu hoặc quyết định có căn cứ, không mang đi hỏi. Với mỗi câu, ghi một dòng nêu **câu trả lời mở khóa task/UC nào** (đối chiếu sheet `Task & Usecase`). Ví dụ: Q12 (số và loại CSDL nguồn) mở khóa T01, T02, UC01.
3. Soạn agenda bằng `templates/agenda.md`. Đặt câu hỏi chặn GĐ1a (mốc 15/11) lên đầu.
4. Người dùng muốn tập dượt thì gọi skill `grilling`, đóng vai bên giao việc để dò câu hỏi còn thiếu.

## B. Ghi biên bản

Đầu vào: ghi chú rời, transcript hoặc lời kể của người dùng.

1. Tách nội dung thành 4 loại, không trộn:
   - **Trả lời câu hỏi**: gắn mã `Q<STT>` của checklist.
   - **Quyết định** `QD-xx`: điều đã chốt, ghi ai chốt.
   - **Việc cần làm** `VL-xx`: người phụ trách và hạn. Hạn chưa rõ ghi "chưa chốt hạn", không tự đặt.
   - **Vấn đề mở**: phát sinh mới chưa có trong checklist; đề xuất thêm thành câu hỏi mới.
2. Điền `templates/bien_ban_hop.md`. Phân biệt điều được nói trong họp với suy luận của agent; suy luận gắn nhãn "(suy luận – cần xác nhận)".
3. Câu trả lời làm đổi giả định trong sheet `Task & Usecase` hoặc `Căn cứ pháp lý` thì liệt kê ở mục "Ảnh hưởng tới phạm vi" kèm mã T/UC. Nếu phạm vi đã chốt bị đổi, chuyển sang skill `ba-quy-tac-truy-vet` để mở CR.
4. Lưu `output/project019_NNN_bien_ban_hop_<yyyymmdd>.md`. Cần bản Word thì dùng skill `docx`.
5. Soát văn bằng skill `kiem-tra-ai-2` (văn bản hành chính) trước khi bàn giao.

## C. Cập nhật checklist Excel

Không sửa Excel bằng code tự viết. Dùng script sau để giữ định dạng, công thức đếm và danh sách chọn:

```bash
python3 -I .claude/skills/ba-hop-khao-sat/scripts/cap_nhat_checklist.py \
  --in <file nguồn> --out work/project019_NNN_checklist_hop_dang_cap_nhat.xlsx \
  --updates tmp/cap_nhat_<yyyymmdd>.json --date <yyyy-mm-dd>
```

JSON cập nhật:

```json
{
  "cau_hoi": {"12": {"trang_thai": "Đã quyết (giả định)", "tra_loi": "<nội dung>", "nguoi_phu_trach": "<tên>",
                   "loai": "4 Dữ liệu và hệ thống", "gia_dinh": "<giả định hoặc quyết định>", "can_cu": "<căn cứ>",
                   "kiem_chung": "<cách kiểm chứng>", "anh_huong": "<ảnh hưởng nếu sai>"}},
  "task": {"T02": {"uoc_luong": 8, "trang_thai_xac_nhan": "Đã xác nhận"}}
}
```

Thêm nhóm câu hỏi mới (đánh số tiếp, trạng thái `Chưa xử lý`; script tự dời khối thống kê, mở rộng công thức đếm, danh sách chọn và vùng lọc) hoặc sửa một đoạn chữ trong một ô:

```json
{
  "them_nhom_cau_hoi": {"ten_nhom": "<tên nhóm>", "cau_hoi": [{"noi_dung": "<câu hỏi>", "uu_tien": "Cao"}]},
  "sua_van_ban": [{"sheet": "Lộ trình", "o": "A12", "cu": "<đoạn cũ>", "moi": "<đoạn mới>"}]
}
```

Sheet `Căn cứ pháp lý` (khóa `can_cu_phap_ly`): `cap_nhat` sửa ô theo số `#` (cột chữ A..I, `bo_to_cam` bỏ tô cam khi đã có số hiệu); `them` thêm dòng vào cuối nhóm A/B/C/D/E (`to_cam` tô cam như dòng `dong_mau_cam`); `them_cot` thêm cột cuối; `nguon_tra_cuu` nối dòng nguồn; `o_rieng` ghi ô cố định như `A2`. Script dựng lại bảng, giữ gộp ô tiêu đề nhóm và ước chiều cao dòng. Mẫu: `tmp/cap_nhat_ccpl_20261026.json`.

Sheet bảng tham số mới (khóa `them_sheet`): `ten`, `tieu_de`, `mo_ta`, `do_rong_cot`, `khoi` (mỗi khối có `tieu_de`, `ghi_chu`, `cot`, `dong` gồm `o` và cờ `nhom`). Script từ chối nếu sheet đã có, trừ khi đặt `ghi_de: true`. Mẫu: `tmp/cap_nhat_tham_so_ncc_20261026.json`.

Chèn dòng vào bảng có sẵn (khóa `them_dong`, danh sách): mỗi mục có `sheet`, `sau_dong` (số dòng Excel), `dong` (danh sách các dòng, mỗi dòng là danh sách giá trị theo cột) và tùy chọn `mau_dong` (dòng chép kiểu, mặc định là `sau_dong`). Dùng cho thực thể mới ở sheet `Mô hình dữ liệu` hay việc `VL-xx` mới. Script từ chối nếu có ô gộp bên dưới dòng chèn, mở rộng vùng lọc và danh sách chọn nếu `sau_dong` nằm trong vùng đó (công thức ở sheet khác tham chiếu tới vùng cũ thì phải sửa bằng `sua_van_ban`), và để Excel tự giãn chiều cao dòng.

Bảng từ viết tắt cuối sheet (khóa `ghi_chu_viet_tat`): `{"<tên sheet>": ["MÃ: nghĩa", ...]}`. Script ghi tiêu đề "TỪ VIẾT TẮT TRONG SHEET" cách dữ liệu và ảnh một dòng, mỗi mục một dòng ở cột A. Chạy lại thì xóa bảng cũ từ dòng tiêu đề trở xuống rồi ghi lại, không chèn dòng nên không làm lệch công thức tham chiếu giữa các sheet. Mẫu: `tmp/cap_nhat_20261103_viet_tat.json`.

- Ưu tiên câu mới: `Cao`, `Trung bình`, `Thấp`. `sua_van_ban` từ chối nếu đoạn cũ không xuất hiện đúng một lần trong ô.
- Trạng thái câu hỏi: `Chưa xử lý`, `Đã quyết (giả định)`, `Đã kiểm chứng`. Loại (cột H): `1 Tra văn bản`, `2 Quyết định thiết kế`, `3 Phạm vi`, `4 Dữ liệu và hệ thống`, `5 Nội bộ dự án`. Các khóa `loai`, `gia_dinh`, `can_cu`, `kiem_chung`, `anh_huong` ghi đè cột H đến L.
- Khóa `"chuyen_so_gia_dinh": true` chuyển sheet từ checklist họp sang sổ giả định (thêm cột H đến L, đổi trạng thái cũ, danh sách chọn, khối thống kê); đã chạy cho file 013 ngày 03/11/2026, chạy lại thì bỏ qua.
- Trạng thái xác nhận task: `Giả định`, `Đã xác nhận`, `Điều chỉnh`, `Loại bỏ`.
- Script từ chối giá trị ngoài danh sách, mã không tồn tại, ước lượng âm, và `--out` nằm trong `input/`. Nếu `--out` đã tồn tại, script sao lưu bản cũ vào `tmp/` trước khi ghi.
- `tra_loi` được nối vào nội dung cũ với tiền tố `[ngày]`, không xóa câu trả lời trước.
- Đọc tóm tắt script in ra và báo người dùng số câu theo từng trạng thái.

## D. Kết thúc

Báo người dùng: số câu đã rõ, câu Cao còn mở, các VL-xx kèm người phụ trách, các T/UC bị ảnh hưởng. Có bất đồng hoặc giả định sai gây làm lại thì ghi PF bằng `~/Workspace/project006/work/tools/pf_log.py`.
