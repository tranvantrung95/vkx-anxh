# Bộ skill BA cho project019

Goal: Người dùng là BA của dự án; tích hợp bộ skill BA riêng (tiếng Việt, gắn bối cảnh ASXH) cho 4 nhóm việc: họp & khảo sát, đặc tả UC/SRS, phân tích dữ liệu nguồn, quy tắc & truy vết.

Acceptance:
- 4 skill trong `.claude/skills/ba-*` có frontmatter hợp lệ, tên khớp thư mục, mọi template/script được tham chiếu đều tồn tại.
- Script cập nhật checklist giữ công thức và data validation, từ chối giá trị sai, không ghi vào `input/`.
- Script profiling không xuất giá trị thô của dữ liệu cá nhân.
- `CLAUDE.md` có mục "Quy ước BA" với bảng định tuyến và mã định danh.

Plan:
- [x] Đọc quy tắc Workspace, checkpoint cũ, PF-098..100; xem cấu trúc Excel (cột, công thức, data validation).
- [x] ba-hop-khao-sat: SKILL.md, agenda, biên bản, scripts/cap_nhat_checklist.py.
- [x] ba-dac-ta-use-case: SKILL.md, mẫu đặc tả UC, khung SRS.
- [x] ba-du-lieu-nguon: SKILL.md, mẫu từ điển & mapping, scripts/profile_nguon.py.
- [x] ba-quy-tac-truy-vet: SKILL.md, danh mục BR, ma trận truy vết, sổ CR.
- [x] CLAUDE.md mục Quy ước BA; README Project facts.

Done + verify (2026-10-23):
- `cap_nhat_checklist.py --report` trên file input: 26 câu "Chưa hỏi", 30 task "Giả định", 30 chưa ước lượng.
- Cập nhật thử ra `tmp/ba_skill_test/out/x.xlsx`: Q12 → Đã rõ, T02 → 8 ngày/Đã xác nhận; lần 2 nối trả lời có ngày và sao lưu bản cũ; công thức C40 và data validation còn nguyên. Trạng thái sai, mã T99, ghi vào input/ đều bị từ chối (exit 1).
- `profile_nguon.py` trên CSV dữ liệu giả: phát hiện trùng khóa, CCCD sai độ dài, ngày sai, mã địa bàn lệch độ dài; chỉ in mẫu đã che. Cột không tồn tại → exit 1.
- Kiểm tra frontmatter/tham chiếu 4 skill: đạt; skill phụ trợ (grilling, docx, xlsx, kiem-tra-ai-2, diagram, markdown-mermaid-writing, domain-modeling, humanizer) đều đã cài.

Current step: Hoàn tất. Skill dự án được nạp khi mở phiên mới tại project019.
Blockers: Không.
Next: Dùng `ba-hop-khao-sat` cho buổi họp kỹ thuật sắp tới (lọc câu Cao, agenda); sau họp cập nhật checklist vào `work/project019_005_checklist_hop_dang_cap_nhat.xlsx (đã tạo 26/10/2026, thêm Q27–Q30, sửa ghi chú GĐ1a)`.

Việc trước (đã xong 23/10/2026): báo cáo phạm vi và nguồn lực `output/project019_003_*` (10 PT, 5 dashboard, 4 KT), bối cảnh `output/project019_002_*`; QA tại `tmp/project019_003_render_dashboard_scope_checked`.

## Rà soát mô hình dữ liệu (26/10/2026)

Done: `output/project019_007_ra_soat_mo_hinh_du_lieu.md` + 7 SVG trong `output/project019_007_uml/` (nguồn Mermaid: `work/project019_007_uml/*.mmd`). 8 thực thể cũ (6 cần sửa), đề xuất thêm 10 (nhóm B) + 7 (nhóm C, phụ thuộc Q27); ma trận thực thể × UC; vai trò NGƯỜI × UC; phát hiện Pháp lệnh 05/2026/UBTVQH16 (hiệu lực 01/01/2027).
Verify: mmdc dựng đủ 7 sơ đồ (cần `-p` trỏ chrome-headless-shell 149 trong ~/.cache/puppeteer vì mmdc tìm bản 131).
Next: VL-10..VL-15 chờ người dùng đồng ý (sửa sheet Mô hình dữ liệu, thêm 7 câu hỏi, thêm PL 05/2026 vào Căn cứ pháp lý).
Lưu ý: các skill ba-* tham chiếu mục "Quy ước BA" trong CLAUDE.md nhưng CLAUDE.md hiện không còn mục này.
Cập nhật 26/10/2026: đã áp VL-11..VL-13 vào `work/project019_005_*.xlsx` (Mô hình dữ liệu 20 thực thể nhóm A+B; Q31–Q37; PL 05/2026 dòng #37). Sao lưu trước khi sửa: `tmp/project019_005_checklist_hop_dang_cap_nhat_truoc_007_20261026_092920.xlsx`. Chưa đổi tên HỒ SƠ HƯỞNG ở sheet Task & Usecase (T07, VL-10 chờ bên giao việc).

## Lượt chạy agent BA (26/10/2026, bổ sung)

Done: `output/project019_009_ket_qua_agent_ba.md` (phân loại bản dựng, phạm vi, checklist P1–P3, mốc phạm vi), `output/project019_010_can_cu_phap_ly_va_tham_so_theo_ky.md`, `output/project019_011_dac_ta_quy_tac_va_truy_vet.md`. Tiến độ: `tmp/tien_do_agent_ba.md`.
Phát hiện: chuyển tiếp hồ sơ NĐ 335 ở Điều 33 (sheet #9 ghi Điều 32); PL 05/2026 cho NCC nhiều diện hưởng cộng dồn (UC06 không dùng "mức cao nhất" cho NCC); NĐ 63/2024 đã sửa bởi NĐ 301/2026; PL III mục 10, 11, 29, 108 ghi "Nâng cấp" (có hệ thống hiện hữu).
Blockers: bước 5 chờ biên bản khảo sát.
Next: người dùng duyệt đề xuất `tmp/project019_009_de_xuat_cap_nhat_checklist.json` (Q38–Q49, CCPL#9, CCPL#38) rồi áp bằng skill ba-hop-khao-sat; mang câu P1 đi họp.

## Rà soát phạm vi và căn cứ pháp lý theo T/UC (26/10/2026, bổ sung)

Done: sheet "Căn cứ pháp lý" thêm cột J "Phạm vi đối tượng" (Lõi NCC / Mở rộng TGXH, hộ nghèo / Chung / Ngoài phân tích), 11 văn bản mới (#39–#49), cập nhật ghi chú #10, 11, 13, 15, 19, 24, 25, 27, 38. Sao lưu: `tmp/project019_005_checklist_hop_dang_cap_nhat_truoc_20261026_152332.xlsx`. JSON: `tmp/cap_nhat_ccpl_pham_vi_20261026.json`.
Sự cố: lần lưu đầu lỗi (script nối dòng nguồn tra cứu gán sai kiểu định dạng) làm hỏng file làm việc; đã khôi phục từ bản sao lưu ngay trước đó, sửa `cap_nhat_checklist.py` (dòng nguồn tra cứu; lưu qua file `.tam` rồi đổi tên).
Chờ người dùng: dòng 24–25 là hàng Excel (Luật NKT, VBHN 11) hay số # (Luật Giao dịch điện tử, Luật Lưu trữ); xóa hay giữ #24, #25.
Cập nhật 26/10/2026: theo yêu cầu người dùng, đã xóa #24 (Luật Giao dịch điện tử) và #25 (Luật Lưu trữ) khỏi sheet Căn cứ pháp lý (người dùng xác nhận "số # cột A"); sao lưu `tmp/project019_005_checklist_hop_dang_cap_nhat_truoc_20261026_152850.xlsx`. Script `cap_nhat_checklist.py` thêm khóa `xoa` trong `can_cu_phap_ly`.

## Profile BA gửi VNPT-IT (27/10/2026)

Yêu cầu: VNPT-IT xin profile các BA dự kiến (domain đặc thù: hiểu sâu dữ liệu, xác định use case khai thác, viết đầu bài cho phát triển).
Done: `output/project019_012_profile_ba_gui_vnpt_it.md` và `.docx` (thư trả lời nháp, 3 năng lực và minh chứng, cơ cấu 2+1 BA theo báo cáo 003, mẫu profile, danh mục sản phẩm mẫu). Rà văn phong audit2: 0 lỗi bắt buộc.
Blockers: workspace không có thông tin thật của BA nào; các ô [ĐIỀN] chờ người dùng cung cấp, kèm sự đồng ý của từng BA.
Next: điền profile, chốt BA 3, chọn sản phẩm mẫu gửi kèm, xác định người nhận và người ký.

## Nguồn dữ liệu của thực thể và chạy lại (27/10/2026)
- Thêm sheet "Nguồn thực thể" vào work/project019_005_checklist_hop_dang_cap_nhat.xlsx: phân 20 thực thể theo 3 lớp (ETL, cấu hình, tổng hợp) từ nhận định người dùng chuyển, 12 chuỗi ảnh hưởng (B), 10 quy tắc chạy lại (R1–R10), 8 điều chỉnh đề xuất cho mô hình (D1–D8, chưa áp vào sheet Mô hình dữ liệu).
- Cần chốt 3 thực thể: E05 (đang hưởng hay đáng hưởng), E09, E14. 4 thực thể nhận định chưa nêu: E10, E13, E16, E17.
- Thêm Q50–Q55 vào Checklist họp (nhóm "Nguồn ghi dữ liệu và chạy lại"). Sao lưu: tmp/project019_005_checklist_hop_dang_cap_nhat_truoc_20261027_100538.xlsx. JSON: tmp/cap_nhat_nguon_thuc_the_20261027.json.
- Cùng ngày, theo yêu cầu người dùng ("áp đi, vì đây là bản mô tả giả định"): đã áp D1–D7 vào sheet "Mô hình dữ liệu" (thêm E24 ĐÁNG HƯỞNG, E25 LẦN TÍNH; sửa E04, E05, E07, E13, E16, E20; dời khối ghi chú xuống 2 hàng). D8 chưa chốt, chờ Q50, Q51. Sao lưu: tmp/project019_005_checklist_hop_dang_cap_nhat_truoc_20261027_101035.xlsx.
- Chưa cập nhật: output/project019_007_ra_soat_mo_hinh_du_lieu.md và sơ đồ work/project019_007_uml/*.mmd chưa có E24, E25.
- 27/10/2026, theo yêu cầu "cập nhật luôn output/project019_007 và các sơ đồ UML": phát hiện E24, E25 đã là CƠ SỞ, LƯỢT CHĂM SÓC TẠI CƠ SỞ (nhóm C của 007), nên đổi hai thực thể mới thành E31 ĐÁNG HƯỞNG, E32 LẦN TÍNH ở cả Excel (sheet Mô hình dữ liệu, Nguồn thực thể) và 007.
- 007: thêm mục 3.5 (ba lớp dữ liệu), hàng E31/E32 ở mục 3.2, 4.2, 4.3, VL-16; sửa hàng E04, E05, E07, E13, E16, E20. Sơ đồ .mmd sửa 01, 02, 03, 04, 07; dựng lại 5 SVG trong output/project019_007_uml/ (06 và 05 không đổi). Sao lưu bản cũ: tmp/sao_luu_007_*/ (md, mmd, svg_cu).
- 27/10/2026, bổ sung theo ghi chú người dùng "UML là liên kết giữa thực thể, còn nguồn dữ liệu là ai thêm/sửa": sheet "Nguồn thực thể" thêm khối E (ai thêm/sửa 22 thực thể: ETL/API hay người dùng, vai trò, duyệt) và F (10 tác nhân: ETL, Engine, VT01–VT07, hệ thống ngoài/người dân); sheet "Mô hình dữ liệu" thêm cột H "Lớp dữ liệu", I "Ai thêm hoặc sửa"; checklist thêm Q56–Q58. 007 thêm mục 3.6, sơ đồ 6.8 (work/project019_007_uml/08_nguon_du_lieu_tac_nhan.mmd + SVG), VL-17. Vai trò VT01–VT07 là đề xuất BA, chưa có tài liệu phân quyền của nguồn.
- Lưu ý: một bản sao lưu Excel bị ghi đè do trùng giờ (tmp/..._truoc_20261027_102342.xlsx); bản _102341 còn nguyên.
- 27/10/2026, "sửa đi" (người dùng chọn không ưu tiên): chốt D8 theo nhận định của bên giao việc, E09 và E14 là lớp 2 (cán bộ VT05 nhập, VT04 duyệt, có phiên bản), ETL/API chỉ là ngoại lệ nếu nguồn có lưu; vẫn giả định, chờ Q50, Q51. Cập nhật sheet "Nguồn thực thể", cột F, H, I của "Mô hình dữ liệu", 007 (3.5, 3.6, VL-16, VL-17), sơ đồ 08 (SVG dựng lại). Giữ nguyên 7 vai trò VT01–VT07 theo yêu cầu. Sao lưu: tmp/sao_luu_007_d8_*/ và tmp/project019_005_..._truoc_20261027_1032xx.xlsx.

## Truy vết Task/UC → thực thể → sơ đồ UML (27/10/2026)
- Thêm sheet "UC – Thực thể – UML" (30 dòng: 11 task, 19 UC) vào work/project019_005_checklist_hop_dang_cap_nhat.xlsx, đặt sau sheet "Mô hình dữ liệu"; thêm mục 4.4 vào output/project019_007_ra_soat_mo_hinh_du_lieu.md (bảng xuôi và bảng ngược sơ đồ → T/UC).
- Nguồn: ma trận 4.2, cột G sheet Mô hình dữ liệu, danh sách sơ đồ mục 6. Bổ sung T01–T05, T10, T11, UC03 (4.2 chưa có); UC09 thêm E06 (Đ), T09 thêm E32 (Đ).
- Chỗ trống: nhóm D (T04, T10) chưa có sơ đồ lớp. Đã chép sheet sang output/project019_013_checklist_kem_so_do_uml.xlsx (sao lưu tmp/project019_013_..._truoc_20261027_114854_78531.xlsx; 10 ảnh, 12 sheet cũ giữ nguyên).
- Sao lưu: tmp/project019_005_checklist_hop_dang_cap_nhat_truoc_20261027_114726_74958.xlsx; tmp/anh_xa_uc_uml_20261027/ (script, 007 bản cũ). Kiểm: 11 sheet cũ không đổi giá trị, data validation giữ nguyên.

## Việc cần làm, đặc tả sơ bộ, kế hoạch (27/10/2026)
- Tạo output/project019_014_viec_can_lam_va_ke_hoach_so_bo.md: bảng đối chiếu mã 003 (TH, PT, DB, KT) ↔ T/UC; việc BA và dev cho 30 T/UC, mức sẵn sàng M1 6 / M2 12 / M3 12 (bản 0.1, 30 dòng; bản 0.2 có 36 dòng: M1 8 / M2 15 / M3 13); đề xuất T12–T16, UC20; mốc M0–M5; 17 task BA-01..BA-17 (21 ngày công đến 30/11, 12,5 đến demo 15/11).
- Tạo output/project019_015_dac_ta_so_bo_task_uc.md: đặc tả đầy đủ UC01, UC02 (DB01), UC04, UC06, UC07 theo mẫu skill ba-dac-ta-use-case (40 TC); thẻ đặc tả 14 UC còn lại + UC20; khung T01–T11; đề xuất BR-50..BR-53.
- Kiểm: mọi BR của 5 UC phần A có TC, mọi luồng ngoại lệ có TC; số M1/M2/M3 và tổng ngày công đếm bằng script. audit2 vẫn KHÔNG ĐẠT: còn gạch đầu dòng theo mẫu đặc tả, câu liệt kê phép đo 31–36 từ, chuỗi mã nhiều dấu phẩy.
- Chưa làm: thêm BR-50..53 vào danh mục 011 và ma trận truy vết; thêm Q59; thêm T12–T16, UC20 vào sheet Task & Usecase (chờ người dùng quyết, mục 8 của 014).
- 27/10/2026, theo yêu cầu người dùng: thêm Q59 (nhóm 12 "Chất lượng dữ liệu") bằng cap_nhat_checklist.py; chèn T12–T16 sau T11 và nhóm C8 + UC20 cuối sheet Task & Usecase (tô xanh lá, Giả định; T12 chưa có giai đoạn, chờ Q38). Dời 27 dòng, gộp lại ô tiêu đề nhóm, mở danh sách chọn I, L và vùng lọc tới dòng 51, công thức sheet Lộ trình đổi $44 → $51. Sao lưu: tmp/project019_005_checklist_hop_dang_cap_nhat_truoc_20261027_133431.xlsx (trước Q59), tmp/..._truoc_them_task_20261027_133459_15993.xlsx. Script: tmp/anh_xa_uc_uml_20261027/them_task.py.
- 011: thêm mục 3.4 BR-50..53 (Dự thảo), TC-BR50-01..TC-BR53-01, 4 dòng ma trận; tổng 34 BR. Sửa câu tương ứng ở 014, 015.
- Chưa cập nhật: sheet "UC – Thực thể – UML" và file 013 chưa có T12–T16, UC20; Lộ trình chưa tính lại trong Excel (không có LibreOffice để kiểm công thức).
- 27/10/2026: sheet "UC – Thực thể – UML" dựng lại với 36 dòng (thêm T12–T16, UC20; E30 vào nhóm sơ đồ 6.5) ở file làm việc và 013. Chép Checklist họp, Lộ trình (công thức $51), Task & Usecase từ file làm việc sang 013: giá trị, kiểu, ô gộp, danh sách chọn khớp; 9 sheet còn lại và 10 ảnh giữ nguyên. Sao lưu: tmp/project019_005_..._truoc_20261027_133829_20388.xlsx, tmp/project019_013_..._truoc_chep_sheet_20261027_133841_20881.xlsx, tmp/project019_013_..._truoc_20261027_133842_20882.xlsx. Mục 4.4 của 007 đã dựng lại 36 dòng cùng ngày (bản cũ: tmp/anh_xa_uc_uml_20261027/007_truoc_44_*.md).

## Đồng bộ tài liệu sau rà soát (28/10/2026)
- Sao lưu trước khi sửa: tmp/sao_luu_dong_bo_20261028_134514_78792/ (12 file, có SHA256SUMS).
- Số liệu cũ: 009 mục 5 ghi số 26/10 kèm số đếm lại 28/10 (59 câu, 36 T/UC); 011 mục 1 sửa 59/36; 014 BA-01 tới Q59 (bản 0.3); 015 dẫn BR-50..53, UC01 ghi Q59 (bản 0.2); 016 ghi 014 bản 0.3 và đánh dấu mâu thuẫn đã xử lý.
- Trùng số 007: file lịch sử chính sách đổi thành output/project019_017_lich_su_thay_doi_chinh_sach_va_truong_du_lieu.md; VL-10..13 của file đó thành VL-18..21 (VL-20 ghi đã có Q32, Q39; VL-21 một phần qua 011 mục 2). Dẫn chiếu sửa ở 010, 011, 012 (.md và .docx), 016. Dẫn chiếu "007" còn lại trỏ tới 007 rà soát mô hình.
- CLAUDE.md: khôi phục mục "Quy ước BA" từ bản 26/10 (lấy từ lịch sử phiên), thêm mã TC-BR, Exx, quy tắc VL đánh số liên tục toàn dự án.
- Excel làm việc: sheet "Mô hình hóa thực thể" C65 (E04) và C73 (E13) sửa theo cột H sheet "Mô hình dữ liệu"; sửa thẳng XML sheet8, chỉ 2 ô đổi, 12 sheet, 1 ảnh, 4 data validation giữ nguyên.
- Cùng ngày, sau khi người dùng đóng Excel: chép C65, C73 sang output/project019_013_checklist_kem_so_do_uml.xlsx cùng cách (sao lưu vào cùng thư mục tmp). Kiểm: chỉ 2 ô khác bản sao lưu; 13 sheet, 10 ảnh, 4 data validation giữ nguyên; 12 sheet chung với file làm việc khớp 100% từng ô.
- Chưa làm: ảnh UML trong sheet "Mô hình hóa thực thể" chưa xem lại xem có ghi lớp của E04, E13 không.
Next: xem lại ảnh UML sheet "Mô hình hóa thực thể" (lớp dữ liệu E04, E13); họp khảo sát theo câu P1.

## File 013 là bản quản lý duy nhất (28/10/2026)
- Người dùng chọn: chỉ dùng output/project019_013_checklist_kem_so_do_uml.xlsx; work/project019_005_* dừng cập nhật. Ghi trong CLAUDE.md mục "Nguồn sự thật".
- Thêm 8 sheet (trước sheet "Sơ đồ UML"): Đặc tả UC (36 dòng: 5 đầy đủ, 15 thẻ, 11 khung task, 5 chưa có đặc tả T12–T16; mức sẵn sàng M1 8, M2 15, M3 13), Tiêu chí nghiệm thu (40 TC-UC, 27 TC-BR, cột kết quả kiểm có danh sách chọn), Quy tắc BR (34), Tham số BR (27), Ma trận truy vết (19), Kế hoạch BA (17 việc, công thức tổng 21 ngày công, 6 mốc, cột trạng thái), Việc cần làm (VL-01..21), Mâu thuẫn & rủi ro (16 mâu thuẫn, 6 đã xử lý; 13 rủi ro).
- Script: tmp/dong_bo_013_20261028/dung_sheet_013.py (chạy lại sẽ dựng lại 8 sheet từ .md, ghi đè sửa tay; chỉ dùng khi chưa sửa trên Excel). Sao lưu: tmp/sao_luu_013_truoc_them_sheet_20261028_140041_90929/.
- Kiểm: 13 sheet cũ không đổi ô nào so với bản sao lưu; 10 ảnh, 4 data validation cũ giữ nguyên.
Next: sửa đặc tả và trạng thái trực tiếp trên 013; sau buổi khảo sát cập nhật Checklist họp, Đặc tả UC, Kế hoạch BA.

## Chế độ theo nhóm đối tượng và dự báo theo khu vực (30/10/2026)
- Kế hoạch đã duyệt: ~/.claude/plans/d-a-v-o-c-c-c-n-wild-charm.md. Script: tmp/du_bao_20261030/dung_sheet_du_bao.py (từ chối chạy lại nếu sheet đã có; từ chối khi có file khóa ~$). Sao lưu: tmp/du_bao_20261030/sao_luu_013_truoc_093952_95358/.
- File 013 thêm 3 sheet: "Chế độ theo nhóm đối tượng" (123 dòng: TGXH 47, NCC 77 gồm PL I, PL II/III, PL IV/VI, tuất, mai táng, quà; hộ nghèo 6; cột Phạm vi theo Q27), "Kịch bản dự báo" (VD1–VD11), "Mô phỏng dự báo" (xã A giả: khối A tham số ô vàng, B 22 nhóm tháng sau, C 30 hộ giả dự báo chuẩn nghèo 2027, D tổng hợp tách chênh lệch theo VD; 413 công thức).
- Cập nhật: Đặc tả UC dòng UC12 (mở rộng dự báo theo khu vực), UC15, UC18; Tiêu chí nghiệm thu TC-UC12-01..06; Việc cần làm VL-22..26; Checklist họp nhóm "Dự báo theo khu vực" Q60–Q63 (qua cap_nhat_checklist.py).
- Kiểm: 21 sheet cũ chỉ đổi ở các dòng có chủ đích (Checklist họp nhóm mới, Đặc tả UC 14 ô); 10 ảnh giữ nguyên; công thức không trỏ ô rỗng. Không có công cụ tính công thức: số đối chứng Python (tháng hiện tại 319.845.000, tháng sau 334.353.000, chênh 14.508.000 = VD2 16.020.000 + VD1 −3.372.000 + VD5 −1.740.000 + VD6 3.600.000; hộ nghèo 5 → 15 hộ; mai táng 12.000.000) ghi ở TC-UC12-04, 06; người dùng mở Excel để so.
- Giả định: mức NCC tỷ lệ thuận mức chuẩn (VL-26); dải "cận ngưỡng" 10% không phải hộ cận nghèo theo luật (VL-22); kịch bản mức chuẩn TGXH 600.000 là minh họa.
Next: người dùng mở file kiểm số khối D khớp TC-UC12-04; hỏi Q60–Q63 trong buổi khảo sát.


## Quy trình BA chuẩn (30/10/2026)
- Tạo output/project019_018_quy_trinh_ba_chuan.md: 12 bước (0 đến 11), mỗi bước có mục tiêu, đầu vào, cách làm, câu hỏi gợi ý, đầu ra kèm bộ cột, cổng kiểm, lỗi thường gặp (PF-099..PF-110); phân vai; mã định danh, cột khóa; vòng lặp; bản đồ áp vào project019.
- Bộ cột đối chiếu tiêu đề thật của 24 sheet trong 013. Cột và bảng đánh dấu (+) là đề xuất, chưa thêm vào 013 (Các bên liên quan, Nguồn tích hợp, Thuật ngữ, Từ điển dữ liệu, Danh mục, Chất lượng dữ liệu, Vai trò và phân quyền, Phi chức năng, Chỉ tiêu, Bàn giao, Sổ CR).
- audit2: ĐẠT.
- Next: người dùng duyệt; tùy chọn xuất .docx, thêm bảng (+) vào 013 qua cap_nhat_checklist.py, hoặc đóng gói thành skill BA dùng chung.
- 30/10/2026: xuất output/project019_018_quy_trinh_ba_chuan.docx (21 trang A4, Times New Roman, 35 bảng có viền, hàng tiêu đề lặp lại, sơ đồ mạch chính dọc 21 cm). Script: tmp/xuat_018_20261030/build_docx.py (pandoc + python-docx; ảnh sơ đồ dựng bằng mmdc). Đã xem bản PDF do Word xuất. Sơ đồ đổi LR → TB ở cả .md. Sửa "hợp nhất" → "phù hợp" ở mục 1 (PF-121).
