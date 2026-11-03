# CLAUDE.md

Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.

---

## Quy ước BA (project019)

Khôi phục ngày 28/10/2026 từ bản 26/10/2026 (mục này bị mất khi CLAUDE.md được ghi đè); đã cập nhật số câu hỏi, mã TC-BR, Exx và quy tắc đánh số VL.

Người dùng giữ vai trò **BA** của module tích hợp và phân tích dữ liệu an sinh xã hội (7 nguồn API; Angular 19, Spring Boot, Oracle; theo pattern source có sẵn). Việc BA đi qua bộ skill trong `.claude/skills/`. Mục 1–4 phía trên áp dụng cho code; với tài liệu BA, "giả định nêu rõ" và "không làm ngoài yêu cầu" vẫn giữ nguyên.

### Định tuyến việc BA → skill

| Việc | Skill chính | Skill hỗ trợ |
|---|---|---|
| Lọc câu hỏi, agenda, biên bản họp, cập nhật checklist Excel | `ba-hop-khao-sat` | `grilling` (tập dượt), `docx`, `kiem-tra-ai-2` |
| Đặc tả UC, tiêu chí nghiệm thu, mô tả dashboard, ghép SRS | `ba-dac-ta-use-case` | `grilling`, `diagram`, `markdown-mermaid-writing`, `docx` |
| Từ điển dữ liệu, mapping về mô hình lõi, profiling, chất lượng "đúng–đủ–sạch–sống" | `ba-du-lieu-nguon` | `xlsx` |
| Quy tắc BR-xx từ văn bản pháp lý, ma trận truy vết, CR | `ba-quy-tac-truy-vet` | WebSearch/WebFetch (đối chiếu văn bản) |
| Thuật ngữ, khái niệm miền, quyết định thiết kế cần lưu | `domain-modeling` | |
| Văn xuôi bàn giao (báo cáo, email, biên bản) | `kiem-tra-ai-2` | `humanizer` |

### Nguồn sự thật

- **Bản gốc duy nhất từ 28/10/2026 (người dùng chọn): `output/project019_013_checklist_kem_so_do_uml.xlsx`.** Mọi cập nhật checklist, task/UC, đặc tả UC, tiêu chí nghiệm thu, BR, tham số, truy vết, kế hoạch BA, việc VL, mâu thuẫn và rủi ro ghi vào file này (24 sheet; thêm "Chế độ theo nhóm đối tượng", "Kịch bản dự báo", "Mô phỏng dự báo" ngày 30/10/2026). Skill `ba-*` nhắc `work/*checklist_hop_dang_cap_nhat*.xlsx` thì hiểu là file 013. `work/project019_005_checklist_hop_dang_cap_nhat.xlsx` dừng cập nhật (khớp 013 ở 12 sheet chung ngày 28/10/2026), chỉ giữ để tra lịch sử.
- Các file `.md` trong `output/` (011, 014, 015, 016…) là bản chụp tại ngày lập; nội dung đặc tả, BR, kế hoạch sửa tiếp ở sheet tương ứng của 013, không sửa song song ở `.md`.
- Bản gốc khách hàng: `input/Checklist_hop_ky_thuat_module_tich_hop_du_lieu.xlsx` (chỉ đọc).
- Phụ lục III dự thảo hợp đồng (Cục Người có công – Liên danh VNPT-VKX, 208 mục yêu cầu): chỉ có dạng 7 ảnh chụp trong `input/VKX - VNPT IT - Migrate ASSH [...]/` (trùng nội dung với file zip cùng tên). Sheet "UC tham khảo PL III" của Excel đã chép 153 mục liên quan dữ liệu.
- Phạm vi đã đề xuất: `output/project019_003_bao_cao_use_case_va_nhan_su_ba_vnpt_it.md`. Bối cảnh bài toán: `output/project019_002_bai_toan_ba_du_lieu_an_sinh.md`. Phân tích input và các điểm lệch phạm vi chưa giải quyết (người có công hay toàn bộ ASXH, nguồn hay đích của "7 nguồn API"): `output/project019_004_phan_tich_input.md`.
- Tiến độ và việc kế tiếp: `work/CHECKPOINT.md`.
- `graphify-out/` (đồ thị tri thức, có bản Markdown của Excel trong `converted/`) và `.codegraph/` là chỉ mục sinh tự động, không phải nguồn sự thật.

### Lệnh thường dùng

Chạy Python với `-I` (theo quy ước của các skill). File `~$*.xlsx` cạnh một file Excel (trong `input/`, `work/` hay `output/`) nghĩa là người dùng đang mở file đó; không ghi vào file đang mở.

```bash
# Đọc checklist: câu hỏi theo trạng thái, task chưa ước lượng
python3 -I .claude/skills/ba-hop-khao-sat/scripts/cap_nhat_checklist.py --in <file.xlsx> --report

# Cập nhật checklist từ JSON (khóa: cau_hoi, task, them_nhom_cau_hoi, sua_van_ban; xem SKILL.md mục C)
python3 -I .claude/skills/ba-hop-khao-sat/scripts/cap_nhat_checklist.py --in <nguồn> --out work/<file>.xlsx --updates tmp/<file>.json --date yyyy-mm-dd

# Profiling dữ liệu nguồn (chỉ in thống kê và mẫu đã che)
python3 -I .claude/skills/ba-du-lieu-nguon/scripts/profile_nguon.py <file.csv|xlsx> --ten-nguon <tên> --key <cột> --cccd <cột> --date <cột,cột> --ma-dia-ban <cột>

# Soát văn bản bàn giao, phải ra ĐẠT
python3 ~/.claude/skills/kiem-tra-ai-2/scripts/audit2.py <file.md>

# Sinh lại báo cáo 003 (.docx + .md vào output/)
python3 work/project019_003_build_report.py
```

Không sửa Excel bằng openpyxl tự viết: chỉ dùng `cap_nhat_checklist.py`, vì script giữ công thức đếm, danh sách chọn, vùng lọc và từ chối ghi vào `input/`. Thiếu chức năng thì mở rộng script đó và cập nhật `SKILL.md` của skill. Khi ghi đè, script tự sao lưu bản cũ vào `tmp/`.

Sổ BA dài hạn trong `work/`: danh mục quy tắc, ma trận truy vết, sổ CR.

### Mã định danh

| Mã | Nghĩa | Ví dụ |
|---|---|---|
| `Q<STT>` | Câu hỏi trong checklist | Q12 |
| `Txx`, `UCxx` | Task, use case (theo sheet Task & Usecase) | T07, UC06 |
| `YC-xx` | Yêu cầu từ bên giao việc hoặc văn bản | YC-03 |
| `BR-xx`, `P-...` | Quy tắc nghiệp vụ, tham số cấu hình | BR-05, P-MUC-CHUAN-TGXH |
| `TC-UCxx-nn`, `TC-BRxx-nn` | Tiêu chí nghiệm thu mức UC, kịch bản mức quy tắc | TC-UC07-02, TC-BR13-01 |
| `Exx` | Thực thể trong mô hình dữ liệu; mã đã cấp không dùng lại (E08, E18, E19 bỏ trống) | E05 |
| `QD-xx`, `VL-xx` | Quyết định, việc cần làm trong biên bản hoặc báo cáo. `VL-xx` đánh số liên tục trong toàn dự án, không đánh lại theo từng file (đã dùng tới VL-47) | QD-01, VL-14 |
| `CR-xx` | Yêu cầu thay đổi | CR-01 |

### Quy tắc chung

- Mọi task/UC/BR còn trạng thái "Giả định" hoặc "Chờ đối chiếu" phải mang nhãn đó trong tài liệu bàn giao. Không trình bày như phạm vi đã chốt.
- Không dùng số liệu giả như kết quả thật; dữ liệu ví dụ ghi rõ "dữ liệu giả".
- Không in, trích hay ghi giá trị thô của dữ liệu cá nhân (số định danh, họ tên, tình trạng sức khỏe); chỉ ghi thống kê và mẫu đã che.
- Tên file sản phẩm theo `project019_NNN_ten_ngan.ext`, lấy NNN kế tiếp bằng `ls output work | grep -o 'project019_[0-9]*' | sort -u | tail -1`.
