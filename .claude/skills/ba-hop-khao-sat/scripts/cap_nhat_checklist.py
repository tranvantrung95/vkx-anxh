#!/usr/bin/env python3
"""Đọc hoặc cập nhật file Excel checklist họp BA của project019.

--report               : in câu hỏi và thống kê, không ghi file.
--updates F --out O    : áp cập nhật trong JSON F, ghi ra O (giữ định dạng, công thức, data validation).
Khóa JSON: cau_hoi, task, them_nhom_cau_hoi, sua_van_ban (xem SKILL.md mục C).
"""
import argparse
import json
import shutil
import sys
from collections import Counter
from copy import copy
from datetime import date, datetime
from pathlib import Path

import openpyxl
from openpyxl.styles import Font
from openpyxl.styles.cell_style import StyleArray
from openpyxl.worksheet.cell_range import CellRange, MultiCellRange
from openpyxl.worksheet.datavalidation import DataValidation

SHEET_CAU_HOI = "Checklist họp"
SHEET_TASK = "Task & Usecase"
SHEET_CAN_CU = "Căn cứ pháp lý"
# Từ 03/11/2026 sheet câu hỏi là sổ giả định và quyết định BA: không có đầu mối để hỏi (PF-126)
TRANG_THAI_CAU_HOI = ("Chưa xử lý", "Đã quyết (giả định)", "Đã kiểm chứng")
TRANG_THAI_CU = {"Chưa hỏi": "Chưa xử lý", "Chờ phản hồi": "Chưa xử lý",
                 "Cần làm rõ thêm": "Chưa xử lý", "Đã rõ": "Đã kiểm chứng"}
LOAI_CAU_HOI = ("1 Tra văn bản", "2 Quyết định thiết kế", "3 Phạm vi", "4 Dữ liệu và hệ thống", "5 Nội bộ dự án")
TRANG_THAI_TASK = ("Giả định", "Đã xác nhận", "Điều chỉnh", "Loại bỏ")
UU_TIEN = ("Cao", "Trung bình", "Thấp")
# Cột (1-based) theo cấu trúc file gốc; H đến L thêm khi chuyển sang sổ giả định
CH_NHOM, CH_NOI_DUNG, CH_UU_TIEN, CH_TRANG_THAI, CH_TRA_LOI, CH_NGUOI = 2, 3, 4, 5, 6, 7
COT_SO_GIA_DINH = {"loai": (8, "Loại", 20), "gia_dinh": (9, "Giả định / quyết định của BA", 60),
                   "can_cu": (10, "Căn cứ", 40), "kiem_chung": (11, "Cách kiểm chứng", 40),
                   "anh_huong": (12, "Ảnh hưởng nếu sai", 40)}
CH_LOAI = COT_SO_GIA_DINH["loai"][0]
TK_UOC_LUONG, TK_XAC_NHAN = 11, 12


def index_cau_hoi(ws):
    return {str(c.value): c.row for (c,) in ws.iter_rows(min_col=1, max_col=1) if isinstance(c.value, int)}


def index_task(ws):
    rows = {}
    for (c,) in ws.iter_rows(min_col=1, max_col=1):
        v = c.value
        if isinstance(v, str) and (v[:1] == "T" and v[1:].isdigit() or v[:2] == "UC" and v[2:].isdigit()):
            rows[v] = c.row
    return rows


def report(wb):
    ws = wb[SHEET_CAU_HOI]
    dem = Counter()
    for stt, row in index_cau_hoi(ws).items():
        val = lambda col: ws.cell(row, col).value or ""
        dem[val(CH_TRANG_THAI)] += 1
        print(f"Q{stt} | {val(CH_NHOM)} | {val(CH_UU_TIEN)} | {val(CH_TRANG_THAI)} | {val(CH_NOI_DUNG)}")
    print("\nCâu hỏi theo trạng thái:", dict(dem))
    wt = wb[SHEET_TASK]
    xac_nhan, thieu = Counter(), []
    for ma, row in index_task(wt).items():
        xac_nhan[wt.cell(row, TK_XAC_NHAN).value or ""] += 1
        if wt.cell(row, TK_UOC_LUONG).value in (None, ""):
            thieu.append(ma)
    print("Task/UC theo trạng thái xác nhận:", dict(xac_nhan))
    print(f"Chưa có ước lượng ({len(thieu)}):", ", ".join(thieu))


def fail(msg):
    sys.exit(f"LỖI: {msg}")


def update_cau_hoi(ws, items, ngay):
    rows = index_cau_hoi(ws)
    for stt, u in items.items():
        stt = str(stt).lstrip("Qq")
        if stt not in rows:
            fail(f"không có câu hỏi Q{stt}")
        row = rows[stt]
        if "trang_thai" in u:
            if u["trang_thai"] not in TRANG_THAI_CAU_HOI:
                fail(f"Q{stt}: trạng thái '{u['trang_thai']}' không thuộc {TRANG_THAI_CAU_HOI}")
            ws.cell(row, CH_TRANG_THAI).value = u["trang_thai"]
        if u.get("tra_loi"):
            cu, moi = ws.cell(row, CH_TRA_LOI).value, f"[{ngay}] {u['tra_loi']}"
            ws.cell(row, CH_TRA_LOI).value = f"{cu}\n{moi}" if cu else moi
        if u.get("nguoi_phu_trach"):
            ws.cell(row, CH_NGUOI).value = u["nguoi_phu_trach"]
        if "loai" in u and u["loai"] not in LOAI_CAU_HOI:
            fail(f"Q{stt}: loại '{u['loai']}' không thuộc {LOAI_CAU_HOI}")
        for khoa, (cot, _, _) in COT_SO_GIA_DINH.items():
            if u.get(khoa):
                if ws.cell(5, cot).value is None:
                    fail("sheet chưa có cột sổ giả định; chạy kèm 'chuyen_so_gia_dinh': true")
                ws.cell(row, cot).value = u[khoa]
        yield f"Q{stt}"


def chuyen_so_gia_dinh(ws, bat):
    """Chuyển checklist họp thành sổ giả định và quyết định BA (một lần; chạy lại thì bỏ qua)."""
    if not bat or ws.cell(5, CH_LOAI).value == COT_SO_GIA_DINH["loai"][1]:
        return
    rows = index_cau_hoi(ws)
    cuoi = max(rows.values())
    ws["A1"] = "SỔ GIẢ ĐỊNH VÀ QUYẾT ĐỊNH BA – MODULE TÍCH HỢP & PHÂN TÍCH DỮ LIỆU"
    ws["A3"] = ("Không có đầu mối để hỏi: mỗi câu được BA trả lời bằng tra cứu văn bản hoặc quyết định có căn cứ. "
                "Cột H đến L: loại, giả định hoặc quyết định, căn cứ, cách kiểm chứng, ảnh hưởng nếu sai. "
                "Loại 4 chỉ kiểm chứng được khi đọc source code, CSDL hoặc tài liệu API.")
    for cot, ten, rong in COT_SO_GIA_DINH.values():
        ws.cell(5, cot).value = ten
        ws.cell(5, cot)._style = copy(ws.cell(5, CH_TRA_LOI)._style)
        ws.column_dimensions[ws.cell(5, cot).column_letter].width = rong
        for r in rows.values():
            ws.cell(r, cot)._style = copy(ws.cell(r, CH_TRA_LOI)._style)
    for r in rows.values():
        cu = ws.cell(r, CH_TRANG_THAI).value
        ws.cell(r, CH_TRANG_THAI).value = TRANG_THAI_CU.get(cu, cu)
    for dv in ws.data_validations.dataValidation:
        if str(dv.sqref) == f"E6:E{cuoi}":
            dv.formula1 = '"' + ",".join(TRANG_THAI_CAU_HOI) + '"'
    dv_loai = DataValidation(type="list", formula1='"' + ",".join(LOAI_CAU_HOI) + '"', allow_blank=True)
    dv_loai.add(f"H6:H{cuoi}")
    ws.add_data_validation(dv_loai)
    if ws.auto_filter.ref == f"A5:G{cuoi}":
        ws.auto_filter.ref = f"A5:L{cuoi}"
    # Khối thống kê: thay 4 dòng trạng thái cũ bằng 3 trạng thái mới và số câu loại 4 chưa kiểm chứng
    dong_tk = [r for r in range(cuoi + 1, ws.max_row + 1) if ws.cell(r, 2).value in TRANG_THAI_CU or ws.cell(r, 2).value == "Đã rõ"]
    if len(dong_tk) != 4:
        fail(f"không tìm thấy đủ 4 dòng thống kê trạng thái cũ (thấy {len(dong_tk)})")
    moi = [(t, f'=COUNTIF(E6:E{cuoi},"{t}")') for t in TRANG_THAI_CAU_HOI]
    moi.append(("Loại 4 chưa kiểm chứng", f'=COUNTIFS(H6:H{cuoi},"4*",E6:E{cuoi},"<>Đã kiểm chứng")'))
    for r, (nhan, cong_thuc) in zip(dong_tk, moi):
        ws.cell(r, 2).value, ws.cell(r, 3).value = nhan, cong_thuc
    yield "chuyển sang sổ giả định"


def update_task(wt, items):
    rows = index_task(wt)
    for ma, u in items.items():
        if ma not in rows:
            fail(f"không có task/UC {ma}")
        row = rows[ma]
        if "uoc_luong" in u:
            val = u["uoc_luong"]
            if isinstance(val, bool) or not isinstance(val, (int, float)) or val < 0:
                fail(f"{ma}: ước lượng phải là số không âm")
            wt.cell(row, TK_UOC_LUONG).value = val
        if "trang_thai_xac_nhan" in u:
            if u["trang_thai_xac_nhan"] not in TRANG_THAI_TASK:
                fail(f"{ma}: trạng thái '{u['trang_thai_xac_nhan']}' không thuộc {TRANG_THAI_TASK}")
            wt.cell(row, TK_XAC_NHAN).value = u["trang_thai_xac_nhan"]
        yield ma


def them_cau_hoi(ws, nhom_moi):
    """Thêm một nhóm câu hỏi mới sau câu cuối; dời khối thống kê xuống và mở rộng công thức, danh sách chọn."""
    if not nhom_moi:
        return
    ten_nhom, cau = nhom_moi.get("ten_nhom"), nhom_moi.get("cau_hoi", [])
    if not ten_nhom or not cau:
        fail("them_nhom_cau_hoi cần 'ten_nhom' và danh sách 'cau_hoi'")
    for c in cau:
        if not c.get("noi_dung") or c.get("uu_tien") not in UU_TIEN:
            fail(f"câu hỏi mới cần 'noi_dung' và 'uu_tien' thuộc {UU_TIEN}")
    stt_cuoi, dong_cuoi = max((int(s), r) for s, r in index_cau_hoi(ws).items())
    tieu_de = [r.min_row for r in ws.merged_cells.ranges if 5 < r.min_row < dong_cuoi]
    so_nhom = len(tieu_de) + 1
    # Khối thống kê nằm dưới câu cuối; dời xuống để chừa chỗ cho dòng tiêu đề nhóm và các câu mới.
    ws.move_range(f"A{dong_cuoi + 1}:G{ws.max_row}", rows=len(cau) + 1)
    hd = dong_cuoi + 1
    for col in range(1, 13):
        ws.cell(hd, col)._style = copy(ws.cell(max(tieu_de), col)._style)
        for i in range(len(cau)):
            ws.cell(hd + 1 + i, col)._style = copy(ws.cell(dong_cuoi, col)._style)
    ws.cell(hd, 1).value = f"{so_nhom}. {ten_nhom}"
    ws.merge_cells(start_row=hd, start_column=1, end_row=hd, end_column=7)
    for i, c in enumerate(cau):
        r = hd + 1 + i
        ws.cell(r, 1).value = stt_cuoi + 1 + i
        ws.cell(r, CH_NHOM).value = ten_nhom
        ws.cell(r, CH_NOI_DUNG).value = c["noi_dung"]
        ws.cell(r, CH_UU_TIEN).value = c["uu_tien"]
        ws.cell(r, CH_TRANG_THAI).value = TRANG_THAI_CAU_HOI[0]
    dong_moi = hd + len(cau)
    for (cell,) in ws.iter_rows(min_row=dong_moi + 1, min_col=3, max_col=3):
        if isinstance(cell.value, str) and cell.value.startswith("="):
            cell.value = (cell.value.replace(f"6:A{dong_cuoi})-{so_nhom - 1}", f"6:A{dong_moi})-{so_nhom}")
                          .replace(f"6:E{dong_cuoi}", f"6:E{dong_moi}")
                          .replace(f"6:H{dong_cuoi}", f"6:H{dong_moi}"))
    for dv in ws.data_validations.dataValidation:
        for cot in "EH":  # trạng thái, loại
            if str(dv.sqref) == f"{cot}6:{cot}{dong_cuoi}":
                dv.sqref = MultiCellRange(f"{cot}6:{cot}{dong_moi}")
    for cot in "GL":
        if ws.auto_filter.ref == f"A5:{cot}{dong_cuoi}":
            ws.auto_filter.ref = f"A5:{cot}{dong_moi}"
    for i in range(len(cau) + 1):
        ws.row_dimensions[hd + i].height = None  # bỏ chiều cao cũ của khối thống kê, để Excel tự giãn
    for i in range(len(cau)):
        yield f"Q{stt_cuoi + 1 + i} (mới)"


def sua_van_ban(wb, items):
    """Thay một đoạn văn bản trong một ô; đoạn cũ phải xuất hiện đúng một lần."""
    for it in items:
        sheet, o, cu, moi = it.get("sheet"), it.get("o"), it.get("cu"), it.get("moi")
        if sheet not in wb.sheetnames or not (o and cu and moi):
            fail(f"sua_van_ban cần sheet hợp lệ và đủ 'o', 'cu', 'moi': {it}")
        cell = wb[sheet][o]
        if not isinstance(cell.value, str) or cell.value.count(cu) != 1:
            fail(f"{sheet}!{o}: không tìm thấy đúng một lần đoạn '{cu}'")
        cell.value = cell.value.replace(cu, moi)
        yield f"{sheet}!{o}"


def _chup_dong(ws, r, so_cot):
    return {
        "cells": [(ws.cell(r, c).value, copy(ws.cell(r, c)._style)) for c in range(1, so_cot + 1)],
        "height": ws.row_dimensions[r].height,
    }


def cap_nhat_can_cu(wb, spec):
    """Sửa dòng theo cột '#', thêm dòng vào cuối nhóm A/B/C…, thêm cột cuối, nối dòng nguồn tra cứu.

    Sheet được dựng lại từ dòng tiêu đề nhóm đầu tiên để giữ định dạng và gộp ô của tiêu đề nhóm.
    """
    if not spec:
        return
    ws = wb[SHEET_CAN_CU]
    cot_cuoi = ws.max_column + (1 if spec.get("them_cot") else 0)
    hop_le = {openpyxl.utils.get_column_letter(c) for c in range(1, cot_cuoi + 1)}
    dong_dau = min(m.min_row for m in ws.merged_cells.ranges)
    dong_tieu_de = dong_dau - 1
    do_rong = [ws.column_dimensions[openpyxl.utils.get_column_letter(c)].width or 10 for c in range(1, cot_cuoi + 1)]
    do_rong[-1] = spec.get("do_rong_cot", 22) if spec.get("them_cot") else do_rong[-1]

    def uoc_chieu_cao(d):
        # Excel không tự giãn dòng có chữ xuống dòng khi mở file, nên ước theo độ dài chữ / độ rộng cột.
        so_dong_chu = max(-(-len(str(v)) // max(int(w * 1.1), 1)) for (v, _), w in zip(d["cells"], do_rong) if v is not None)
        return max(15.0, 12.0 * so_dong_chu + 3)
    rows = [_chup_dong(ws, r, cot_cuoi) for r in range(dong_dau, ws.max_row + 1)]
    ket_bang = next(i for i, d in enumerate(rows) if i and d["cells"][0][0] is None)
    bang, cuoi = rows[:ket_bang], rows[ket_bang:]
    if spec.get("them_cot"):  # cột mới mượn định dạng của cột liền trước trên từng dòng bảng
        for d in bang:
            d["cells"][-1] = (d["cells"][-1][0], copy(d["cells"][-2][1]))
    so_dong = {d["cells"][0][0]: d for d in bang if isinstance(d["cells"][0][0], int)}
    style_thuong = [copy(s) for _, s in rows[1]["cells"]]
    dong_cam = spec.get("dong_mau_cam")
    if dong_cam is not None and dong_cam not in so_dong:
        fail(f"dong_mau_cam: không có văn bản # {dong_cam}")
    style_cam = [copy(s) for _, s in so_dong[dong_cam]["cells"]] if dong_cam is not None else style_thuong
    xoa = set(spec.get("xoa", []))
    if not xoa <= set(so_dong):
        fail(f"xoa: không có văn bản # {sorted(xoa - set(so_dong))}")
    bang = [d for d in bang if d["cells"][0][0] not in xoa]

    def ghi(d, o, bo_to_cam):
        for col, val in o.items():
            if col not in hop_le:
                fail(f"cột '{col}' không hợp lệ (có {sorted(hop_le)})")
            idx = openpyxl.utils.column_index_from_string(col) - 1
            d["cells"][idx] = (val, d["cells"][idx][1])
        if bo_to_cam:
            d["cells"] = [(v, copy(s)) for (v, _), s in zip(d["cells"], style_thuong)]

    for so, u in spec.get("cap_nhat", {}).items():
        if int(so) not in so_dong:
            fail(f"không có văn bản # {so} trong sheet {SHEET_CAN_CU}")
        d = so_dong[int(so)]
        ghi(d, u.get("o", {}), u.get("bo_to_cam"))
        d["height"] = uoc_chieu_cao(d)
        yield f"CCPL#{so}"

    them_theo_nhom = {}
    for it in spec.get("them", []):
        so = it.get("o", {}).get("A")
        if not isinstance(so, int) or so in so_dong:
            fail(f"dòng mới cần cột A là số # chưa dùng: {so}")
        mau = style_cam if it.get("to_cam") else style_thuong
        d = {"cells": [(None, copy(s)) for s in mau], "height": None}
        ghi(d, it["o"], False)
        d["height"] = uoc_chieu_cao(d)
        so_dong[so] = d
        them_theo_nhom.setdefault(it.get("nhom"), []).append(d)
        yield f"CCPL#{so} (mới)"

    moi, nhom = [], None
    for d in bang:
        dau = d["cells"][0][0]
        if isinstance(dau, str):  # tiêu đề nhóm "A. …"
            moi += them_theo_nhom.pop(nhom, [])
            nhom = dau.split(".")[0].strip()
        moi.append(d)
    moi += them_theo_nhom.pop(nhom, [])
    if them_theo_nhom:
        fail(f"không có nhóm {sorted(them_theo_nhom)} trong sheet {SHEET_CAN_CU}")
    for dong in spec.get("nguon_tra_cuu", []):
        cuoi.append({"cells": [(dong, copy(cuoi[-1]["cells"][0][1]))] + [(None, copy(s)) for _, s in cuoi[-1]["cells"][1:]], "height": cuoi[-1]["height"]})

    for m in [m for m in ws.merged_cells.ranges if m.min_row >= dong_dau]:
        ws.unmerge_cells(str(m))
    for i, d in enumerate(moi + cuoi):
        r = dong_dau + i
        for c, (val, st) in enumerate(d["cells"], start=1):
            ws.cell(r, c).value, ws.cell(r, c)._style = val, st
        ws.row_dimensions[r].height = d["height"]
        if i < len(moi) and isinstance(d["cells"][0][0], str):
            ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=cot_cuoi)
    for r in range(dong_dau + len(moi) + len(cuoi), dong_dau + len(rows)):  # dòng thừa sau khi xóa
        for c in range(1, cot_cuoi + 1):
            ws.cell(r, c).value, ws.cell(r, c)._style = None, StyleArray()
        ws.row_dimensions[r].height = None
    for so in sorted(xoa):
        yield f"CCPL#{so} (xóa)"
    if spec.get("them_cot"):
        tieu_de = ws.cell(dong_tieu_de, cot_cuoi)
        tieu_de.value, tieu_de._style = spec["them_cot"], copy(ws.cell(dong_tieu_de, cot_cuoi - 1)._style)
        ws.column_dimensions[openpyxl.utils.get_column_letter(cot_cuoi)].width = spec.get("do_rong_cot", 22)
        yield f"CCPL cột mới '{spec['them_cot']}'"
    for k, v in spec.get("o_rieng", {}).items():
        ws[k].value = v
        yield f"CCPL!{k}"


def them_sheet(wb, spec):
    """Tạo sheet bảng tham số gồm nhiều khối; mượn định dạng tiêu đề, nhóm, dòng của sheet Căn cứ pháp lý."""
    if not spec:
        return
    ten, khoi = spec.get("ten"), spec.get("khoi", [])
    if not ten or not khoi:
        fail("them_sheet cần 'ten' và danh sách 'khoi'")
    if ten in wb.sheetnames:
        if not spec.get("ghi_de"):
            fail(f"sheet '{ten}' đã có; đặt 'ghi_de': true để tạo lại")
        del wb[ten]
    mau = wb[SHEET_CAN_CU]
    st = {"tieu_de": mau["A1"]._style, "mo_ta": mau["A2"]._style, "cot": mau["B4"]._style,
          "nhom": mau["A5"]._style, "dong": mau["E6"]._style}
    ws = wb.create_sheet(ten)
    ws["A1"], ws["A1"]._style = spec.get("tieu_de", ten), copy(st["tieu_de"])
    ws["A2"], ws["A2"]._style = spec.get("mo_ta", ""), copy(st["mo_ta"])
    for i, w in enumerate(spec.get("do_rong_cot", []), start=1):
        ws.column_dimensions[openpyxl.utils.get_column_letter(i)].width = w
    r = 4
    for k in khoi:
        cot, dong = k.get("cot", []), k.get("dong", [])
        if not cot:
            fail(f"khối '{k.get('tieu_de')}' thiếu 'cot'")
        ws.cell(r, 1).value, ws.cell(r, 1)._style = k.get("tieu_de", ""), copy(st["nhom"])
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=len(cot))
        r += 1
        if k.get("ghi_chu"):
            ws.cell(r, 1).value, ws.cell(r, 1)._style = k["ghi_chu"], copy(st["mo_ta"])
            r += 1
        for c, v in enumerate(cot, start=1):
            ws.cell(r, c).value, ws.cell(r, c)._style = v, copy(st["cot"])
        r += 1
        for d in dong:
            o = d.get("o", [])
            if len(o) > len(cot):
                fail(f"khối '{k.get('tieu_de')}': dòng có {len(o)} ô, nhiều hơn {len(cot)} cột")
            for c in range(1, len(cot) + 1):
                cell = ws.cell(r, c)
                cell._style = copy(st["nhom"] if d.get("nhom") else st["dong"])
                cell.value = o[c - 1] if c <= len(o) else None
                if isinstance(cell.value, (int, float)) and not isinstance(cell.value, bool):
                    cell.number_format = "#,##0" if float(cell.value).is_integer() else "0.0"
            r += 1
        r += 1
    ws.freeze_panes = "A4"
    yield f"sheet '{ten}' ({sum(len(k.get('dong', [])) for k in khoi)} dòng)"


def them_dong(wb, specs):
    """Chèn dòng mới ngay sau dòng `sau_dong` của một sheet, chép kiểu từ `mau_dong` (mặc định chính dòng đó)."""
    for sp in specs or []:
        sheet, sau, dong = sp.get("sheet"), sp.get("sau_dong"), sp.get("dong")
        if sheet not in wb.sheetnames or not isinstance(sau, int) or sau < 1 or not dong:
            fail(f"them_dong cần sheet hợp lệ, 'sau_dong' (số nguyên) và 'dong': {sheet}")
        ws = wb[sheet]
        if any(len(v) > ws.max_column for v in dong):
            fail(f"them_dong: {sheet} có {ws.max_column} cột, dòng mới dài hơn")
        if any(r.min_row > sau for r in ws.merged_cells.ranges):
            fail(f"them_dong: {sheet} có ô gộp bên dưới dòng {sau}, chưa hỗ trợ chèn")
        mau, n = sp.get("mau_dong", sau), len(dong)
        ws.insert_rows(sau + 1, n)
        for i, vals in enumerate(dong):
            r = sau + 1 + i
            for col in range(1, ws.max_column + 1):
                ws.cell(r, col)._style = copy(ws.cell(mau, col)._style)
            for col, v in enumerate(vals, 1):
                ws.cell(r, col).value = v
        for r in range(sau + 1, ws.max_row + 1):
            ws.row_dimensions[r].height = None  # insert_rows không dời chiều cao dòng; để Excel tự giãn
        if ws.auto_filter.ref:
            vung = CellRange(ws.auto_filter.ref)
            if vung.min_row <= sau <= vung.max_row:  # dòng chèn nằm trong vùng lọc thì mở rộng vùng lọc
                vung.expand(down=n)
                ws.auto_filter.ref = vung.coord
        for dv in ws.data_validations.dataValidation:  # danh sách chọn phủ dòng chèn thì phủ cả dòng mới
            vung_moi = []
            for v in dv.sqref.ranges:
                v = CellRange(v.coord)
                if v.min_row <= sau <= v.max_row:
                    v.expand(down=n)
                vung_moi.append(v.coord)
            dv.sqref = MultiCellRange(" ".join(vung_moi))
        yield f"{sheet}: +{n} dòng sau dòng {sau}"


TIEU_DE_VIET_TAT = "TỪ VIẾT TẮT TRONG SHEET"
EMU_MOI_DONG = 9525 * 20  # dòng mặc định cao 20 px, 1 px = 9525 EMU


def _dong_cuoi_anh(anh):
    """Dòng Excel cuối cùng mà ảnh phủ tới (ước lượng với neo một ô)."""
    neo = anh.anchor
    if hasattr(neo, "to") and neo.to is not None:
        return neo.to.row + 1
    return neo._from.row + 1 + -(-neo.ext.height // EMU_MOI_DONG)


def ghi_chu_viet_tat(wb, spec):
    """Ghi bảng từ viết tắt ở cuối mỗi sheet, dưới dữ liệu và ảnh; chạy lại thì thay bảng cũ."""
    for sheet, dong in (spec or {}).items():
        if sheet not in wb.sheetnames or not dong or not all(isinstance(d, str) for d in dong):
            fail(f"ghi_chu_viet_tat cần sheet hợp lệ và danh sách chuỗi: {sheet}")
        ws = wb[sheet]
        cu = [r for r in range(1, ws.max_row + 1)
              if isinstance(ws.cell(r, 1).value, str) and ws.cell(r, 1).value.startswith(TIEU_DE_VIET_TAT)]
        if cu:
            ws.delete_rows(cu[0], ws.max_row - cu[0] + 1)
        dau = max([ws.max_row] + [_dong_cuoi_anh(a) for a in ws._images]) + 2
        ws.cell(dau, 1, TIEU_DE_VIET_TAT).font = Font(bold=True)
        for i, noi_dung in enumerate(dong, 1):
            ws.cell(dau + i, 1, noi_dung)  # không xuống dòng: chữ tràn sang các ô trống bên phải
        yield f"{sheet}: {len(dong)} từ viết tắt"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="src", required=True)
    ap.add_argument("--out")
    ap.add_argument("--updates")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--date", default=date.today().isoformat(), help="yyyy-mm-dd, ghi kèm câu trả lời")
    a = ap.parse_args()

    wb = openpyxl.load_workbook(Path(a.src))
    if a.report:
        report(wb)
        return
    if not (a.updates and a.out):
        fail("cần --updates và --out (hoặc dùng --report)")
    try:
        datetime.strptime(a.date, "%Y-%m-%d")
    except ValueError:
        fail("--date phải có dạng yyyy-mm-dd")
    out = Path(a.out).resolve()
    if "input" in out.parts:
        fail("không ghi vào thư mục input/; bản gốc chỉ đọc")
    updates = json.loads(Path(a.updates).read_text(encoding="utf-8"))
    unknown = set(updates) - {"cau_hoi", "task", "them_nhom_cau_hoi", "sua_van_ban", "can_cu_phap_ly", "them_sheet", "them_dong", "ghi_chu_viet_tat",
                           "chuyen_so_gia_dinh"}
    if unknown:
        fail(f"khóa không hợp lệ: {sorted(unknown)}")
    # Kiểm tra toàn bộ trước khi ghi: fail() thoát trước wb.save nên không có ghi dở.
    changes = list(chuyen_so_gia_dinh(wb[SHEET_CAU_HOI], updates.get("chuyen_so_gia_dinh")))
    changes += list(update_cau_hoi(wb[SHEET_CAU_HOI], updates.get("cau_hoi", {}), a.date))
    changes += list(update_task(wb[SHEET_TASK], updates.get("task", {})))
    changes += list(them_cau_hoi(wb[SHEET_CAU_HOI], updates.get("them_nhom_cau_hoi")))
    changes += list(sua_van_ban(wb, updates.get("sua_van_ban", [])))
    changes += list(cap_nhat_can_cu(wb, updates.get("can_cu_phap_ly")))
    changes += list(them_sheet(wb, updates.get("them_sheet")))
    changes += list(them_dong(wb, updates.get("them_dong")))
    changes += list(ghi_chu_viet_tat(wb, updates.get("ghi_chu_viet_tat")))
    if out.exists():
        tmp = out.parent.parent / "tmp"
        tmp.mkdir(exist_ok=True)
        moc = f"{datetime.now():%Y%m%d_%H%M%S}"
        backup, so = tmp / f"{out.stem}_truoc_{moc}{out.suffix}", 1
        while backup.exists():  # hai lần chạy cùng một giây không được ghi đè bản sao lưu trước
            so += 1
            backup = tmp / f"{out.stem}_truoc_{moc}_{so}{out.suffix}"
        shutil.copy2(out, backup)
        print("Đã sao lưu bản cũ:", backup)
    tam = out.with_name(out.name + ".tam")  # lưu ra file tạm rồi đổi tên: lỗi khi lưu không làm hỏng bản đang có
    wb.save(tam)
    tam.replace(out)
    print(f"Đã cập nhật {len(changes)} mục: {', '.join(changes)}")
    report(openpyxl.load_workbook(out))


if __name__ == "__main__":
    main()
