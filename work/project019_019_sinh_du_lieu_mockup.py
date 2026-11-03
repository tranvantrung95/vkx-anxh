#!/usr/bin/env python3
"""Sinh bộ DỮ LIỆU GIẢ (mockup) theo mô hình dữ liệu lõi project019.

Căn cứ: các sheet Mô hình dữ liệu, Mô hình hóa thực thể, Quy tắc BR, Tham số BR,
Tham số NCC, Kịch bản dự báo, Task & Usecase của
output/project019_013_checklist_kem_so_do_uml.xlsx (đọc ngày 03/11/2026).
Mọi tên người, số định danh, tài khoản, địa bàn đều bịa.

Bộ dữ liệu có hai phần:
- Dân số nền (ngẫu nhiên, hạt giống cố định): dữ liệu nguồn khớp kết quả tính, không sinh cảnh báo.
- Các ca gieo sẵn TC-Mxx: dữ liệu nguồn lệch có chủ đích. Engine thu nhỏ trong script tính
  E31 (đáng hưởng), so với E05/E07 (đang hưởng) để sinh E16; cuối script tự kiểm từng ca.

Chạy: python3 -I work/project019_019_sinh_du_lieu_mockup.py
"""
import csv
import random
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parent.parent
OUT_XLSX = ROOT / "output" / "project019_019_du_lieu_mockup.xlsx"
OUT_CSV = ROOT / "output" / "project019_019_du_lieu_mockup_csv"
R = random.Random(19)
NGAY_CHOT = date(2026, 10, 31)
KY = ["2026-07", "2026-08", "2026-09", "2026-10"]
SO_HO_NEN = 110
CAU_HINH = "CH-2026.10.1"
BAN_CHUP = "BC-20261031"
LT_CT, LT_VD1, LT_VD2 = "LT-20261031-CT", "LT-20261101-MP-VD1", "LT-20261101-MP-VD2"
MUC_VD2 = 600_000
NGUONG_TK_NGUOI = 3  # một tài khoản nhận cho từ 3 đối tượng thuộc từ 2 hộ trở lên thì cảnh báo
CD_TGXH = {"CD01", "CD02", "CD03"}  # TGXH hằng tháng
CD_NCC = {"CD04", "CD05", "CD06", "CD07", "CD08", "CD10", "CD11"}
MOT_LAN = {"CD09", "CD10", "CD11"}
KY_CHUYEN = "2026-10"  # kỳ đầu chi theo mức NĐ 335 (hiệu lực 05/10/2026); kỳ trước đó truy lĩnh (Điều 32 khoản 3, 4)
NGAY_MUC_CU = date(2026, 6, 30)

# ---------------------------------------------------------------- tiện ích


def ky_dau(ky):
    y, m = map(int, ky.split("-"))
    return date(y, m, 1)


def ky_cuoi(ky):
    d = ky_dau(ky)
    return date(d.year + d.month // 12, d.month % 12 + 1, 1) - timedelta(days=1)


def ky_truoc(ky):
    return (ky_dau(ky) - timedelta(days=1)).strftime("%Y-%m")


def tuoi(dob, d):
    return d.year - dob.year - ((d.month, d.day) < (dob.month, dob.day))


def sinh_nhat(dob, n):
    return date(dob.year + n, dob.month, dob.day)  # ngày sinh luôn ≤ 28 nên không vướng 29/02


def ngay_sinh(a):
    m, d = R.randint(1, 12), R.randint(1, 28)
    return date(NGAY_CHOT.year - a - (1 if m > NGAY_CHOT.month else 0), m, d)


def ngay_bat_ky(y1, y2):
    return date(R.randint(y1, y2), R.randint(1, 12), R.randint(1, 28))


def tien(x):
    return f"{x:,}".replace(",", ".")


_dem = defaultdict(int)


def ma(prefix, w):
    _dem[prefix] += 1
    return f"{prefix}{_dem[prefix]:0{w}d}"


# ---------------------------------------------------------------- dữ liệu cấu hình (lớp 2)

TINH = ("T99", "Tỉnh Mẫu (giả)")
XA = {"X99001": "Xã An Bình (giả)", "X99002": "Xã Hòa Lạc (giả)", "X99003": "Xã Tân Phú (giả)"}
XA_CU = [("X99101", "Xã An Bình cũ (giả)", "X99001"), ("X99102", "Xã Bình Minh cũ (giả)", "X99001"),
         ("X99103", "Xã Hòa Lạc cũ (giả)", "X99002"), ("X99104", "Xã Tân Phú cũ (giả)", "X99003"),
         ("X99105", "Xã Phú Mỹ cũ (giả)", "X99003")]

VAN_BAN = [  # ma, so_hieu, trich_yeu, hieu_luc_tu, hieu_luc_den, thay_the, ghi_chu
    ("VB01", "335/2026/NĐ-CP", "Chính sách trợ giúp xã hội", date(2026, 10, 5), None,
     "NĐ 20/2021, NĐ 76/2024", "Hiệu lực 05/10/2026 (Điều 32 khoản 1, Công báo số 500); người đang hưởng chuyển mức từ 01/07/2026 (khoản 3, 4)"),
    ("VB02", "321/2026/NĐ-CP", "Mức hưởng trợ cấp, phụ cấp ưu đãi người có công", None, None,
     "NĐ 55/2023, NĐ 77/2024", "Ngày hiệu lực chưa đối chiếu (TV); mockup áp toàn bộ mục dùng ở đây từ 07/2026"),
    ("VB03", "176/2025/NĐ-CP", "Trợ cấp hưu trí xã hội", date(2025, 7, 1), None, "", "Điều 31 NĐ 335/2026 sửa"),
    ("VB04", "76/2024/NĐ-CP", "Điều chỉnh mức chuẩn trợ giúp xã hội", date(2024, 7, 1), date(2026, 6, 30), "", "Mức 500.000"),
    ("VB05", "02/2020/UBTVQH14", "Pháp lệnh Ưu đãi người có công với cách mạng (VBHN 123/2026)", date(2021, 7, 1), None, "", ""),
    ("VB06", "07/2021/NĐ-CP", "Chuẩn nghèo đa chiều", date(2021, 3, 15), date(2026, 12, 31), "", "Áp dụng đến hết 2026 (BR-42)"),
    ("VB07", "19/2025/QĐ-TTg", "Bảng danh mục và mã số đơn vị hành chính", date(2025, 7, 1), None, "", "Căn cứ ánh xạ mã cũ → mới (T05)"),
]

CHE_DO = [  # ma, ten, nhom, hinh_thuc, don_vi, ma_van_ban
    ("CD01", "Trợ cấp xã hội hằng tháng", "TGXH", "Tiền hằng tháng", "Người", "VB01"),
    ("CD02", "Hỗ trợ hộ trực tiếp chăm sóc NKT đặc biệt nặng", "TGXH", "Tiền hằng tháng", "Hộ", "VB01"),
    ("CD03", "Trợ cấp hưu trí xã hội", "TGXH", "Tiền hằng tháng", "Người", "VB03"),
    ("CD04", "Trợ cấp ưu đãi hằng tháng NCC", "NCC", "Tiền hằng tháng", "Người", "VB02"),
    ("CD05", "Phụ cấp hằng tháng NCC", "NCC", "Tiền hằng tháng", "Người", "VB02"),
    ("CD06", "Trợ cấp người phục vụ NCC sống ở gia đình", "NCC", "Tiền hằng tháng", "Người", "VB02"),
    ("CD07", "Trợ cấp tuất hằng tháng thân nhân liệt sĩ", "NCC", "Tiền hằng tháng", "Người", "VB05"),
    ("CD08", "Trợ cấp tuất nuôi dưỡng hằng tháng", "NCC", "Tiền hằng tháng", "Người", "VB05"),
    ("CD09", "Hỗ trợ chi phí mai táng TGXH", "TGXH", "Một lần", "Người", "VB01"),
    ("CD10", "Trợ cấp mai táng NCC", "NCC", "Một lần", "Người", "VB05"),
    ("CD11", "Trợ cấp một lần khi thân nhân liệt sĩ đang hưởng tuất chết", "NCC", "Một lần", "Người", "VB05"),
]
LOAI_QD_MOT_LAN = {"CD09": "Hỗ trợ chi phí mai táng", "CD10": "Trợ cấp mai táng", "CD11": "Trợ cấp một lần"}

D0726 = date(2026, 7, 1)
THAM_SO = [  # ma, ten, ma_che_do, gia_tri, don_vi, tu, den, ma_vb, dieu_khoan
    ("P-MUC-CHUAN-TGXH", "Mức chuẩn TGXH", "CD01;CD02", 500_000, "đồng/tháng", date(2024, 7, 1), date(2026, 6, 30), "VB04", ""),
    ("P-MUC-CHUAN-TGXH", "Mức chuẩn TGXH", "CD01;CD02", 540_000, "đồng/tháng", D0726, None, "VB01", "Điều 4 khoản 2; Điều 32 khoản 3"),
    ("P-HUU-TRI-XH", "Trợ cấp hưu trí xã hội", "CD03", 500_000, "đồng/tháng", date(2025, 7, 1), date(2026, 6, 30), "VB03", ""),
    ("P-HUU-TRI-XH", "Trợ cấp hưu trí xã hội", "CD03", 540_000, "đồng/tháng", D0726, None, "VB01", "Điều 31"),
    ("P-HS-TGXH-K1-DUOI4", "Hệ số trẻ em Điều 5 khoản 1, dưới 4 tuổi", "CD01", 2.5, "hệ số", D0726, None, "VB01", "Điều 6 khoản 1 điểm a"),
    ("P-HS-TGXH-K1-TU4", "Hệ số trẻ em Điều 5 khoản 1, từ đủ 4 tuổi", "CD01", 1.5, "hệ số", D0726, None, "VB01", "Điều 6 khoản 1 điểm a"),
    ("P-HS-TGXH-K2", "Hệ số người từ 16 tuổi đang học (Điều 5 khoản 2)", "CD01", 1.5, "hệ số", D0726, None, "VB01", "Điều 6 khoản 1 điểm b"),
    ("P-HS-TGXH-K4", "Hệ số đơn thân nghèo, mỗi con đang nuôi", "CD01", 1.0, "hệ số/con", D0726, None, "VB01", "Điều 6 khoản 1 điểm d"),
    ("P-MAI-TANG-TGXH-HS-MIN", "Hỗ trợ mai táng TGXH, tối thiểu", "CD09", 20, "lần mức chuẩn", D0726, None, "VB01", "Điều 11 khoản 2"),
    ("P-MAI-TANG-NCC", "Trợ cấp mai táng NCC (GIẢ ĐỊNH mockup: 10 × lương cơ sở 2.340.000; chưa có trong sheet, VL-23)", "CD10", 23_400_000, "đồng", D0726, None, "VB05", "Điều 6 khoản 4; Điều 16 khoản 12"),
    ("P-TN-1LAN-THANG", "Trợ cấp một lần khi thân nhân liệt sĩ chết: số tháng trợ cấp hiện hưởng", "CD11", 3, "tháng", D0726, None, "VB05", "Điều 16 khoản 11"),
    ("NCC-PL1-11", "Thân nhân của 3 liệt sĩ trở lên", "CD07", 9_036_000, "đồng/tháng", D0726, None, "VB02", "Phụ lục I mục 3.4"),
    ("NCC-PL1-12", "Tuất nuôi dưỡng: thân nhân liệt sĩ sống cô đơn", "CD08", 2_410_000, "đồng/tháng", D0726, None, "VB02", "Phụ lục I mục 3.5"),
    ("P-HS-TGXH-K5A-60DEN75", "Hệ số NCT Điều 5 khoản 5 điểm a, 60 đến dưới 75", "CD01", 1.5, "hệ số", D0726, None, "VB01", "Điều 6 khoản 1 điểm đ"),
    ("P-HS-TGXH-K5A-TU75", "Hệ số NCT Điều 5 khoản 5 điểm a, từ 75", "CD01", 2.0, "hệ số", D0726, None, "VB01", "Điều 6 khoản 1 điểm đ"),
    ("P-HS-TGXH-K6-DBN", "Hệ số NKT đặc biệt nặng", "CD01", 2.0, "hệ số", D0726, None, "VB01", "Điều 6 khoản 1 điểm e"),
    ("P-HS-TGXH-K6-TE-NCT-DBN", "Hệ số NKT đặc biệt nặng là trẻ em hoặc NCT", "CD01", 2.5, "hệ số", D0726, None, "VB01", "Điều 6 khoản 1 điểm e"),
    ("P-HS-TGXH-K6-NANG", "Hệ số NKT nặng", "CD01", 1.5, "hệ số", D0726, None, "VB01", "Điều 6 khoản 1 điểm e"),
    ("P-HS-TGXH-K6-TE-NCT-NANG", "Hệ số NKT nặng là trẻ em hoặc NCT", "CD01", 2.0, "hệ số", D0726, None, "VB01", "Điều 6 khoản 1 điểm e"),
    ("P-HS-CS-HO-NKT-DBN", "Hệ số hộ chăm sóc NKT đặc biệt nặng", "CD02", 1.0, "hệ số/người", D0726, None, "VB01", "Điều 17 khoản 2 điểm c"),
    ("P-TAM-DUNG-THANG", "Số tháng không nhận liên tục thì tạm dừng", "CD01;CD02;CD03", 3, "tháng", date(2026, 10, 5), None, "VB01", "Điều 9 khoản 1 điểm a"),
    ("NCC-PL1-08", "Con liệt sĩ chưa đủ 18 tuổi", "CD07", 6_024_000, "đồng/tháng", D0726, None, "VB02", "Phụ lục I mục 3.1"),
    ("NCC-PL1-09", "Thân nhân của 01 liệt sĩ", "CD07", 3_012_000, "đồng/tháng", D0726, None, "VB02", "Phụ lục I mục 3.2"),
    ("NCC-PL1-10", "Thân nhân của 02 liệt sĩ", "CD07", 6_024_000, "đồng/tháng", D0726, None, "VB02", "Phụ lục I mục 3.3"),
    ("NCC-PL1-14", "Bà mẹ Việt Nam anh hùng, trợ cấp", "CD04", 9_036_000, "đồng/tháng", D0726, None, "VB02", "Phụ lục I mục 4"),
    ("NCC-PL1-14-PC", "Bà mẹ Việt Nam anh hùng, phụ cấp", "CD05", 2_524_000, "đồng/tháng", D0726, None, "VB02", "Phụ lục I mục 4"),
    ("NCC-PL1-38", "Nhiễm chất độc hóa học, tổn thương 41% đến 60%", "CD04", 3_825_000, "đồng/tháng", D0726, None, "VB02", "Phụ lục I"),
    ("NCC-PL1-39", "Nhiễm chất độc hóa học, tổn thương 61% đến 80%", "CD04", 5_361_000, "đồng/tháng", D0726, None, "VB02", "Phụ lục I"),
    ("NCC-PL1-54", "Người phục vụ NCC sống ở gia đình", "CD06", 3_012_000, "đồng/tháng", D0726, None, "VB02", "Phụ lục I mục 12.1"),
]

QUY_TAC = [  # ma, ten, ma_che_do, dieu_kien, can_cu, trang_thai
    ("BR-01", "Mức trợ cấp xã hội hằng tháng", "CD01", "Mức = mức chuẩn kỳ T × hệ số diện tại T", "NĐ 335 Điều 6 khoản 1", "Đã đối chiếu"),
    ("BR-02", "Nhiều hệ số: một mức cao nhất", "CD01", "Nhiều diện cùng kỳ thì chỉ hưởng mức cao nhất", "NĐ 335 Điều 6 khoản 2", "Đã đối chiếu"),
    ("BR-03", "Ngoại lệ đơn thân nghèo nuôi con", "CD01", "Đơn thân nghèo (khoản 4) đồng thời thuộc khoản 5, 6, 8: hưởng cả hai", "NĐ 335 Điều 6 khoản 2 câu 2", "Đã đối chiếu"),
    ("BR-05", "Thôi hưởng, điều chỉnh mức", "CD01;CD03", "Chết: thôi từ tháng sau tháng chết. Đổi điều kiện: điều chỉnh từ tháng thay đổi", "NĐ 335 Điều 8 khoản 4", "Đã đối chiếu"),
    ("BR-06", "Chuyển nơi cư trú", "CD01;CD03", "Nơi cũ thôi chi, nơi mới hưởng từ tháng thôi chi", "NĐ 335 Điều 8 khoản 3", "Đã đối chiếu"),
    ("BR-07", "Tạm dừng do không nhận", "CD01;CD02;CD03", "Không nhận liên tục từ P-TAM-DUNG-THANG tháng thì tạm dừng", "NĐ 335 Điều 9 khoản 1 điểm a", "Đã đối chiếu"),
    ("BR-08", "Thôi hưởng TGXH", "CD01", "Chết, mất tích, không còn đủ điều kiện Điều 5...", "NĐ 335 Điều 9 khoản 2", "Đã đối chiếu"),
    ("BR-09", "Thôi hỗ trợ chăm sóc", "CD02", "Người được chăm sóc chết thì thôi hỗ trợ chăm sóc", "NĐ 335 Điều 9 khoản 3", "Đã đối chiếu"),
    ("BR-10", "Mai táng TGXH", "CD09", "Đối tượng Điều 11 khoản 1 chết: hỗ trợ ≥ 20 × mức chuẩn; trùng văn bản (kể cả BHXH) thì một mức cao nhất", "NĐ 335 Điều 11 khoản 1, 2", "Đã đối chiếu"),
    ("BR-27", "Mai táng NCC", "CD10", "NCC, thân nhân đang hưởng hằng tháng chết: một trợ cấp mai táng; thuộc diện mai táng BHXH thì hưởng theo BHXH", "PL 02/2020 Điều 6 khoản 4", "Đã đối chiếu"),
    ("BR-28", "Chấm dứt trợ cấp NCC", "CD04;CD07;CD08", "NCC, thân nhân chết: thôi trợ cấp hằng tháng (thời điểm theo NĐ 131/2021 Điều 118)", "PL 02/2020 Điều 54", "Đã đối chiếu"),
    ("BR-41", "Đối chiếu chi phải gộp truy lĩnh", "CD01;CD02;CD03", "Số đã chi kỳ T = thường kỳ T + truy lĩnh của kỳ gốc T; so với mức quyết định của T", "Suy luận BA từ BR-13; NĐ 335 Điều 32 khoản 3, 4", "Chờ đối chiếu"),
    ("BR-12", "Hộ chăm sóc NKT đặc biệt nặng", "CD02", "Hộ trực tiếp chăm sóc NKT ĐBN: hệ số 1,0 mỗi người", "NĐ 335 Điều 17 khoản 2 điểm c", "Đã đối chiếu"),
    ("BR-13", "Chuyển mức từ 01/07/2026", "CD01", "Người đang hưởng theo NĐ 20/2021, NĐ 176/2025: từ 07/2026 tính theo NĐ 335", "NĐ 335 Điều 32 khoản 3, 4", "Đã đối chiếu"),
    ("BR-16", "Hưu trí xã hội và TGXH", "CD01;CD03", "Đủ cả hai thì hưởng mức cao hơn", "NĐ 335 Điều 31", "Đã đối chiếu (theo 007)"),
    ("BR-20", "Mức NCC theo bảng phụ lục", "CD04;CD05;CD06", "Mức = giá trị bảng phụ lục của kỳ T theo mã diện", "NĐ 321/2026 Phụ lục I", "Chờ đối chiếu (TV)"),
    ("BR-22", "Con liệt sĩ chưa đủ 18 tuổi", "CD04", "Dưới 18: mục 3.1; tháng sau tháng đủ 18 chuyển mục thân nhân tương ứng", "NĐ 321/2026 Phụ lục I mục 3.1", "Chờ đối chiếu (TV)"),
    ("BR-52", "Trạng thái sống chưa xác định", "Mọi chế độ", "Không kết luận chi đúng; trả 'chưa đủ dữ liệu'", "Tài liệu 007 mục 4.1", "Dự thảo"),
    ("KT-HTXH", "Điều kiện hưu trí xã hội (rút gọn cho mockup)", "CD03", "Từ 75 tuổi, không có lương hưu hoặc trợ cấp BHXH hằng tháng, không hưởng trợ cấp NCC hằng tháng", "NĐ 176/2025 (chưa trích điều)", "Giả định mockup, chưa có trong sheet Quy tắc BR"),
    ("KT-TK", "Một tài khoản nhận cho nhiều đối tượng khác hộ", "Mọi chế độ", f"Một tài khoản nhận cho từ {NGUONG_TK_NGUOI} đối tượng thuộc từ 2 hộ trở lên", "Đề xuất BA (UC08)", "Giả định mockup, chưa có trong sheet Quy tắc BR"),
    ("KT-TUAT-ND", "Tuất nuôi dưỡng thân nhân liệt sĩ sống cô đơn", "CD08", "Thân nhân liệt sĩ hưởng tuất hằng tháng, sống một mình và không có người phụng dưỡng (rút gọn khái niệm 'sống cô đơn')", "PL 02/2020 Điều 16 khoản 4", "Giả định mockup, chưa có trong sheet Quy tắc BR (VL-39)"),
    ("KT-TUAT-1L", "Trợ cấp một lần khi thân nhân liệt sĩ chết", "CD11", "Thân nhân đang hưởng tuất hằng tháng chết: 3 tháng trợ cấp tuất hiện hưởng (chưa cộng tuất nuôi dưỡng)", "PL 02/2020 Điều 16 khoản 11", "Giả định mockup, chưa có trong sheet Quy tắc BR (VL-39)"),
    ("KT-BHYT", "Người hưởng trợ cấp hằng tháng chưa có thẻ BHYT", "CD01;CD03;CD04;CD07", "Đang đáng hưởng tại kỳ chốt mà không có thẻ BHYT còn hạn", "Đề xuất BA (UC16)", "Giả định mockup, chưa có trong sheet Quy tắc BR"),
]


def gia_tri(ma_ts, d):
    for t in THAM_SO:  # BR-40: chọn tham số theo ngày thuộc kỳ, không theo ngày chi
        if t[0] == ma_ts and t[5] <= d and (t[6] is None or d <= t[6]):
            return t[3]
    raise KeyError(f"Thiếu tham số {ma_ts} tại {d}")


# ---------------------------------------------------------------- lớp 1: người, hộ, quan hệ

HO = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Vũ", "Đặng", "Bùi", "Đỗ", "Hồ", "Ngô", "Dương", "Lý"]
DEM = {"Nam": ["Văn", "Hữu", "Đức", "Minh", "Quang", "Công", "Xuân"], "Nữ": ["Thị", "Thị", "Thị", "Ngọc", "Thu", "Thanh", "Hồng"]}
TEN = {"Nam": ["An", "Bình", "Cường", "Dũng", "Hải", "Hùng", "Khoa", "Long", "Nam", "Phúc", "Quân", "Sơn", "Tài", "Thắng", "Toàn", "Việt"],
       "Nữ": ["Anh", "Chi", "Dung", "Hà", "Hạnh", "Hoa", "Hương", "Lan", "Linh", "Mai", "Nga", "Nhung", "Oanh", "Thảo", "Trang", "Yến"]}

VC = "Có vợ hoặc chồng"
nguoi, ho = {}, {}
thanh_vien, quan_he, giam_dinh, bhxh, ngoai_ns = [], [], [], [], []
huong, chi_tra, quyet_dinh, tai_khoan = [], [], [], []
cu_tru_doi = []  # (ma_nguoi, xa_cu, xa_moi, ngay)
cccd_da_dung = set()
ca_kiem_thu = []


def tao_nguoi(gioi, dob, ho_dem=None, **tt):
    while True:
        so = "099" + f"{R.randrange(10**9):09d}"
        if so not in cccd_da_dung:
            cccd_da_dung.add(so)
            break
    p = dict(ma=ma("NG", 6), cccd=so, ho_ten=f"{ho_dem or R.choice(HO)} {R.choice(DEM[gioi])} {R.choice(TEN[gioi])}",
             ngay_sinh=dob, gioi_tinh=gioi, dan_toc="Kinh" if R.random() < 0.85 else R.choice(["Tày", "Mường", "Thái", "Khmer"]),
             trang_thai="Còn sống", ngay_mat=None, nguon_tu_vong=None, nkt=None, ty_le=None, ncc=None, ngay_cn=None,
             con_ls=False, phuc_vu_cho=None, luong_huu=False, phung_duong=False, liet_si=False,
             hon_nhan=None, cha_me=None, dang_hoc=False, don_than=False,
             khong_suy=False, khong_bhyt=False, tc=None)
    p.update(tt)
    nguoi[p["ma"]] = p
    return p


def bo_qua(obj, cd):
    """khong_suy: True bỏ qua mọi chế độ, hoặc tập mã chế độ không suy từ kết quả tính (nguồn lệch có chủ đích)."""
    v = obj["khong_suy"]
    return v is True or (isinstance(v, set) and cd in v)


def con_trong_ho(h, d):
    return [nguoi[tv["ma_nguoi"]] for tv in thanh_vien if tv["ma_ho"] == h["ma"] and tv["quan_he_chu_ho"] == "Con"
            and tv["tu_ngay"] <= d and (tv["den_ngay"] is None or d <= tv["den_ngay"])]


def tao_cha_me_da_mat(nam):
    return [tao_nguoi(g, ngay_sinh(R.randint(30, 40) + 2026 - nam), trang_thai="Đã mất", ngay_mat=ngay_bat_ky(nam, nam),
                      nguon_tu_vong="CSDL dân cư (giả)", hon_nhan="Có vợ hoặc chồng") for g in ("Nam", "Nữ")]


def mo_coi(p, cha_me):
    p["cha_me"] = [x["ma"] for x in cha_me]
    for x in cha_me:
        lien_ket(p, x, "Con đẻ", "Hộ tịch (giả)", p["ngay_sinh"])
    return p


def tao_ho(xa, phan_loai="Không nghèo", tc=None):
    h = dict(ma=ma("HO", 5), xa=xa, chu_ho=None, ngay_lap=date(R.randint(1995, 2024), R.randint(1, 12), 1),
             phan_loai=phan_loai, tc=tc, khong_suy=False)
    ho[h["ma"]] = h
    return h


def vao_ho(h, p, qh, tu=None, den=None):
    if qh == "Chủ hộ":
        h["chu_ho"] = p["ma"]
    thanh_vien.append(dict(ma_ho=h["ma"], ma_nguoi=p["ma"], quan_he_chu_ho=qh, la_chu_ho="Có" if qh == "Chủ hộ" else "Không",
                           tu_ngay=tu or max(h["ngay_lap"], p["ngay_sinh"]), den_ngay=den, nguon="CSDL dân cư (giả)"))
    return p


def ho_cua(p, d):
    for tv in thanh_vien:
        if tv["ma_nguoi"] == p["ma"] and tv["tu_ngay"] <= d and (tv["den_ngay"] is None or d <= tv["den_ngay"]):
            return ho[tv["ma_ho"]]
    return None


def thanh_vien_luc(h, d):
    return [nguoi[tv["ma_nguoi"]] for tv in thanh_vien
            if tv["ma_ho"] == h["ma"] and tv["tu_ngay"] <= d and (tv["den_ngay"] is None or d <= tv["den_ngay"])]


def lien_ket(p1, p2, loai, can_cu, tu, nguon="ETL/API"):
    quan_he.append(dict(ma_qh=ma("QH", 4), ma_nguoi_1=p1["ma"], ma_nguoi_2=p2["ma"], loai=loai, can_cu=can_cu,
                        hieu_luc_tu=tu, hieu_luc_den=None, nguon=nguon))


def ghi_giam_dinh(p, loai, gia_tri_gd, hoi_dong, nguon):
    giam_dinh.append(dict(ma_gd=ma("GD", 4), ma_nguoi=p["ma"], loai_chi_so=loai, gia_tri=gia_tri_gd,
                          ngay_giam_dinh=ngay_bat_ky(2015, 2025), hoi_dong=hoi_dong, ky_giam_dinh_lai=None, nguon=nguon))


def nkt(p, muc):
    p["nkt"] = muc
    ghi_giam_dinh(p, "Mức độ khuyết tật", muc, "Hội đồng xác định mức độ khuyết tật xã (giả)", "CSDL TGXH, NKT (giả)")
    return p


def tao_liet_si(nam, tuoi_hy_sinh):
    return tao_nguoi("Nam", date(nam - tuoi_hy_sinh, R.randint(1, 12), R.randint(1, 28)), trang_thai="Đã mất",
                     ngay_mat=date(nam, R.randint(1, 12), R.randint(1, 28)), liet_si=True,
                     nguon_tu_vong="CSDL người có công (giấy báo tử liệt sĩ, giả)")


def cong_nhan_ncc(p, dien, nam):
    p["ncc"], p["ngay_cn"] = dien, ngay_bat_ky(nam, nam)


def sinh_dan_so_nen():
    can_pd = []
    for _ in range(SO_HO_NEN):
        xa = R.choice(list(XA))
        kieu = R.choices(["tre", "gia2", "nhieu_the_he", "gia1"], [45, 20, 25, 10])[0]
        x = R.random()
        ng, cn = (0.40, 0.55) if kieu == "gia1" else (0.12, 0.22)
        h = tao_ho(xa, "Nghèo" if x < ng else "Cận nghèo" if x < cn else "Không nghèo")
        hd = R.choice(HO)
        if kieu == "tre":
            a = R.randint(25, 50)
            vao_ho(h, tao_nguoi("Nam", ngay_sinh(a), hd, hon_nhan=VC), "Chủ hộ")
            vao_ho(h, tao_nguoi("Nữ", ngay_sinh(max(20, a + R.randint(-5, 3))), hon_nhan=VC), "Vợ")
            for _ in range(R.randint(0, 3)):
                vao_ho(h, tao_nguoi(R.choice(["Nam", "Nữ"]), ngay_sinh(R.randint(0, min(17, a - 20))), hd), "Con")
        elif kieu == "gia2":
            a = R.randint(60, 88)
            ong = vao_ho(h, tao_nguoi("Nam", ngay_sinh(a), hd, hon_nhan=VC), "Chủ hộ")
            ba = vao_ho(h, tao_nguoi("Nữ", ngay_sinh(max(58, a - R.randint(0, 6))), hon_nhan=VC), "Vợ")
            if R.random() < 0.5:
                can_pd += [ong, ba]
        elif kieu == "nhieu_the_he":
            a = R.randint(35, 55)
            chu = vao_ho(h, tao_nguoi("Nam", ngay_sinh(a), hd, hon_nhan=VC), "Chủ hộ")
            vao_ho(h, tao_nguoi("Nữ", ngay_sinh(a - R.randint(0, 5)), hon_nhan=VC), "Vợ")
            for _ in range(R.randint(1, 3)):
                vao_ho(h, tao_nguoi(R.choice(["Nam", "Nữ"]), ngay_sinh(R.randint(0, 20)), hd), "Con")
            gioi = "Nữ" if R.random() < 0.6 else "Nam"
            gia = vao_ho(h, tao_nguoi(gioi, ngay_sinh(R.randint(a + 22, min(95, a + 40))), hd, hon_nhan="Góa"), "Mẹ" if gioi == "Nữ" else "Cha")
            gia["phung_duong"] = True
            lien_ket(chu, gia, "Phụng dưỡng (con đẻ)", "Hộ tịch (giả)", gia["ngay_sinh"] + timedelta(days=365 * 60))
        else:
            gioi = "Nữ" if R.random() < 0.7 else "Nam"
            p = vao_ho(h, tao_nguoi(gioi, ngay_sinh(R.randint(62, 95)), hon_nhan="Góa"), "Chủ hộ")
            if R.random() < 0.5:
                can_pd.append(p)
    nguoi_lon = [p for p in nguoi.values() if 30 <= tuoi(p["ngay_sinh"], NGAY_CHOT) <= 55]
    for p in can_pd:  # con sống ở hộ khác vẫn có nghĩa vụ phụng dưỡng
        con = R.choice([c for c in nguoi_lon if ho_cua(c, NGAY_CHOT)["ma"] != ho_cua(p, NGAY_CHOT)["ma"]])
        p["phung_duong"] = True
        lien_ket(con, p, "Phụng dưỡng (con đẻ, khác hộ)", "Hộ tịch (giả)", date(2010, 1, 1))
    for p in list(nguoi.values()):
        if R.random() < 0.04:
            nkt(p, R.choices(["Đặc biệt nặng", "Nặng", "Nhẹ"], [30, 45, 25])[0])
        if tuoi(p["ngay_sinh"], NGAY_CHOT) >= 60 and R.random() < 0.35:
            p["luong_huu"] = True
    gan_ncc_nen()
    sinh_tre_em_don_than()
    chon_tu_vong_nen()


def sinh_tre_em_don_than():
    """Trẻ em mồ côi cả cha mẹ (Điều 5 khoản 1, 2) và đơn thân nghèo nuôi con (khoản 4), ca thường."""
    for xa, pl, ong_ba, tuoi_chau, hoc in [("X99001", "Nghèo", [("Nữ", 68)], [2, 9], False),
                                           ("X99002", "Cận nghèo", [("Nam", 72), ("Nữ", 70)], [13], False),
                                           ("X99003", "Không nghèo", [("Nam", 45), ("Nữ", 43)], [17], True)]:
        h = tao_ho(xa, pl)
        hd = R.choice(HO)
        for i, (g, a) in enumerate(ong_ba):
            vao_ho(h, tao_nguoi(g, ngay_sinh(a), hd, hon_nhan="Góa" if len(ong_ba) == 1 else VC), "Chủ hộ" if i == 0 else "Vợ")
        cha_me = tao_cha_me_da_mat(2025)
        for t in tuoi_chau:
            vao_ho(h, mo_coi(tao_nguoi(R.choice(["Nam", "Nữ"]), ngay_sinh(t), hd, dang_hoc=hoc), cha_me), "Cháu")
    for xa, pl, g, a, hn, cac_con in [("X99001", "Nghèo", "Nữ", 32, "Ly hôn", [(5, False), (10, False)]),
                                      ("X99002", "Cận nghèo", "Nam", 40, "Góa", [(7, False)]),
                                      ("X99003", "Nghèo", "Nữ", 45, "Chưa kết hôn", [(17, True), (12, False)])]:
        h = tao_ho(xa, pl)
        vao_ho(h, tao_nguoi(g, ngay_sinh(a), hon_nhan=hn, don_than=True), "Chủ hộ")
        for t, hoc in cac_con:
            vao_ho(h, tao_nguoi(R.choice(["Nam", "Nữ"]), ngay_sinh(t), dang_hoc=hoc), "Con")


def chon_tu_vong_nen():
    """Hai ca chết thường trong kỳ: nguồn đã dừng trợ cấp và chi mai táng, trợ cấp một lần đúng."""
    def co_nguoi_cung_ho(p):
        h = ho_cua(p, NGAY_CHOT)
        return h and len(thanh_vien_luc(h, NGAY_CHOT)) >= 2 and h["phan_loai"] == "Không nghèo"
    htxh = [p for p in nguoi.values() if tuoi(p["ngay_sinh"], NGAY_CHOT) >= 76 and not p["luong_huu"] and not p["ncc"]
            and not p["nkt"] and not p["liet_si"] and co_nguoi_cung_ho(p)]
    vo_ls = [p for p in nguoi.values() if p["ncc"] == "NCC-TN-1LS" and not p["con_ls"] and co_nguoi_cung_ho(p)]
    for ds, ngay in [(htxh, date(2026, 9, 14)), (vo_ls, date(2026, 8, 3))]:
        if ds:
            p = R.choice(ds)
            p["trang_thai"], p["ngay_mat"], p["nguon_tu_vong"] = "Đã mất", ngay, "CSDL dân cư (giả)"


def ung_vien(gioi, a1, a2):
    return [p for p in nguoi.values() if p["gioi_tinh"] == gioi and a1 <= tuoi(p["ngay_sinh"], NGAY_CHOT) <= a2
            and not p["nkt"] and not p["ncc"] and not p["liet_si"] and ho_cua(p, NGAY_CHOT)["phan_loai"] == "Không nghèo"]


def gan_ncc_nen():
    for i, p in enumerate(R.sample(ung_vien("Nữ", 75, 95), 6)):
        ls = [tao_liet_si(R.choice([1968, 1972, 1979]), R.randint(19, 28))]
        if i == 0:
            ls.append(tao_liet_si(1979, 19))
        cong_nhan_ncc(p, "NCC-TN-2LS" if i == 0 else "NCC-TN-1LS", 1995)
        for s, qh in zip(ls, ["vợ liệt sĩ", "mẹ liệt sĩ"]):
            lien_ket(p, s, f"Thân nhân NCC: {qh}", "Giấy chứng nhận gia đình liệt sĩ (giả)", p["ngay_cn"])
    for p in R.sample(ung_vien("Nam", 70, 85), 3):
        cong_nhan_ncc(p, "NCC-CDHH", 2012)
        p["ty_le"] = R.choice([50, 70])
        ghi_giam_dinh(p, "Tỷ lệ tổn thương cơ thể (%)", p["ty_le"], "Hội đồng giám định y khoa tỉnh (giả)", "CSDL người có công (giả)")
    h = tao_ho("X99003")  # con liệt sĩ dưới 18 sống với mẹ (ca thường, không lệch)
    vao_ho(h, tao_nguoi("Nữ", ngay_sinh(38)), "Chủ hộ")
    con = vao_ho(h, tao_nguoi("Nam", ngay_sinh(12)), "Con")
    ls = tao_liet_si(2022, 34)
    cong_nhan_ncc(con, "NCC-TN-1LS", 2022)
    con["con_ls"] = True
    lien_ket(con, ls, "Thân nhân NCC: con liệt sĩ", "Giấy chứng nhận gia đình liệt sĩ (giả)", con["ngay_cn"])


# ---------------------------------------------------------------- engine thu nhỏ (lớp 3)


def song(p, ky):
    """True: còn sống trong kỳ; False: đã mất trước kỳ; None: chưa xác định (BR-52)."""
    if p["trang_thai"] == "Chưa xác định":
        return None
    return p["ngay_mat"] is None or p["ngay_mat"] >= ky_dau(ky)


def tgxh(code, ky):
    ts = "P-HS-TGXH-" + code
    hs = gia_tri(ts, ky_dau(ky))
    return ("CD01", "TGXH-" + code, ts, hs, round(hs * gia_tri("P-MUC-CHUAN-TGXH", ky_dau(ky))), "BR-01")


def song_co_don(p, ky):
    h = ho_cua(p, ky_cuoi(ky))
    khac = [x for x in thanh_vien_luc(h, ky_cuoi(ky)) if x is not p and song(x, ky)] if h else []
    return not khac and not p["phung_duong"]


def ncc_muc(p, ky):
    """[(cd, ma_tham_so, quy_tac)] theo diện NCC của người tại kỳ."""
    if p["ncc"] == "NCC-BMVNAH":
        return [("CD04", "NCC-PL1-14", "BR-20"), ("CD05", "NCC-PL1-14-PC", "BR-20")]
    if p["ncc"] == "NCC-CDHH":
        return [("CD04", "NCC-PL1-38" if p["ty_le"] <= 60 else "NCC-PL1-39", "BR-20")]
    if p["con_ls"]:
        out = [("CD07", "NCC-PL1-08" if sinh_nhat(p["ngay_sinh"], 18) >= ky_dau(ky) else "NCC-PL1-09", "BR-22")]
    else:
        out = [("CD07", "NCC-PL1-10" if p["ncc"] == "NCC-TN-2LS" else "NCC-PL1-09", "BR-20")]
        if song_co_don(p, ky):  # PL Điều 16 khoản 4
            out.append(("CD08", "NCC-PL1-12", "KT-TUAT-ND"))
    return out


def mot_lan_khi_chet(p, ky, out):
    """Khoản một lần phát sinh trong kỳ chết: mai táng (BR-10, BR-27) và trợ cấp một lần (PL Điều 16 khoản 11)."""
    if not (p["ngay_mat"] and ky_dau(ky) <= p["ngay_mat"] <= ky_cuoi(ky)):
        return []
    cds, them = {x[0] for x in out}, []
    if not p["luong_huu"]:  # có lương hưu thì mai táng BHXH là mức cao nhất, ngân sách không chi
        if cds & {"CD01", "CD03"}:
            hs = gia_tri("P-MAI-TANG-TGXH-HS-MIN", ky_dau(ky))
            them.append(("CD09", "TGXH-MAI-TANG", "P-MAI-TANG-TGXH-HS-MIN", hs, round(hs * gia_tri("P-MUC-CHUAN-TGXH", ky_dau(ky))), "BR-10"))
        if cds & {"CD04", "CD07"}:
            them.append(("CD10", "NCC-MAI-TANG", "P-MAI-TANG-NCC", None, gia_tri("P-MAI-TANG-NCC", ky_dau(ky)), "BR-27"))
        them = [max(them, key=lambda x: x[4])] if them else []  # trùng văn bản: một mức cao nhất
    tuat = [x for x in out if x[0] == "CD07"]
    if tuat:
        n = gia_tri("P-TN-1LAN-THANG", ky_dau(ky))
        them.append(("CD11", "NCC-TN-CHET", "P-TN-1LAN-THANG", n, n * tuat[0][4], "KT-TUAT-1L"))
    return them


def dien_ca_nhan(p, ky):
    """Mọi diện của một người tại kỳ, chưa áp BR-02: [(cd, dien, ts, he_so, muc, quy_tac)]."""
    if p["liet_si"]:
        return []
    d = ky_cuoi(ky)
    a, h, out = tuoi(p["ngay_sinh"], d), ho_cua(p, d), []
    if p["nkt"] in ("Đặc biệt nặng", "Nặng"):
        te_nct = a < 16 or a >= 60
        code = {("Đặc biệt nặng", True): "K6-TE-NCT-DBN", ("Đặc biệt nặng", False): "K6-DBN",
                ("Nặng", True): "K6-TE-NCT-NANG", ("Nặng", False): "K6-NANG"}[(p["nkt"], te_nct)]
        out.append(tgxh(code, ky))
    if a >= 60 and h and h["phan_loai"] == "Nghèo" and not p["phung_duong"]:
        out.append(tgxh("K5A-TU75" if a >= 75 else "K5A-60DEN75", ky))
    if p["cha_me"] and all(nguoi[x]["ngay_mat"] and nguoi[x]["ngay_mat"] < ky_dau(ky) for x in p["cha_me"]):
        if sinh_nhat(p["ngay_sinh"], 16) >= ky_dau(ky):  # dưới 16: thôi từ tháng sau tháng đủ 16 (BR-05)
            out.append(tgxh("K1-DUOI4" if a < 4 else "K1-TU4", ky))
        elif p["dang_hoc"] and a < 22:  # giả định học liên tục đến dưới 22 tuổi
            out.append(tgxh("K2", ky))
    if p["don_than"] and h and h["chu_ho"] == p["ma"] and h["phan_loai"] in ("Nghèo", "Cận nghèo"):
        con = [c for c in con_trong_ho(h, d) if song(c, ky)
               and (sinh_nhat(c["ngay_sinh"], 16) >= ky_dau(ky) or (c["dang_hoc"] and tuoi(c["ngay_sinh"], d) < 22))]
        if con:
            hs = gia_tri("P-HS-TGXH-K4", ky_dau(ky)) * len(con)
            out.append(("CD01", "TGXH-K4", "P-HS-TGXH-K4", hs, round(hs * gia_tri("P-MUC-CHUAN-TGXH", ky_dau(ky))), "BR-01"))
    if p["ncc"]:
        for cd, ts, br in ncc_muc(p, ky):
            out.append((cd, p["ncc"], ts, None, gia_tri(ts, ky_dau(ky)), br))
    if p["phuc_vu_cho"] and song(nguoi[p["phuc_vu_cho"]], ky):
        out.append(("CD06", "NCC-NGUOI-PHUC-VU", "NCC-PL1-54", None, gia_tri("NCC-PL1-54", ky_dau(ky)), "BR-20"))
    co_tgxh = any(x[0] == "CD01" for x in out)
    if a >= 75 and not co_tgxh and not p["luong_huu"] and not p["ncc"]:  # BR-16: TGXH luôn cao hơn hưu trí XH
        out.append(("CD03", "HTXH-TU75", "P-HUU-TRI-XH", None, gia_tri("P-HUU-TRI-XH", ky_dau(ky)), "KT-HTXH"))
    return out + mot_lan_khi_chet(p, ky, out)


def giai_thich(ts, hs, muc, ky):
    if hs is not None and ts.startswith("P-HS-TGXH"):
        return f"{str(hs).replace('.', ',')} × {tien(gia_tri('P-MUC-CHUAN-TGXH', ky_dau(ky)))} = {tien(muc)}"
    return f"{ts} = {tien(muc)}"


def gop_cd01(items, ky):
    """BR-02: nhiều hệ số lấy mức cao nhất; BR-03: phần đơn thân nghèo (K4) cộng thêm."""
    cd01 = [x for x in items if x[0] == "CD01"]
    if len(cd01) < 2:
        return items
    k4 = [x for x in cd01 if x[1] == "TGXH-K4"]
    khac = [x for x in cd01 if x[1] != "TGXH-K4"]
    cao = max(khac, key=lambda x: x[4])
    br = "BR-01" + ("; BR-02" if len(khac) > 1 else "")
    if k4:
        k = k4[0]
        gop = ("CD01", f"{cao[1]} + TGXH-K4", f"{cao[2]} + P-HS-TGXH-K4", cao[3], cao[4] + k[4], br + "; BR-03")
    else:
        gop = cao[:5] + (br,)
    return [x for x in items if x[0] != "CD01"] + [gop]


def giai_thich_dong(cd, dien, ts, hs, muc, br, ky):
    mc = tien(gia_tri("P-MUC-CHUAN-TGXH", ky_dau(ky)))
    if "BR-03" in br:
        return f"Mức cao nhất của diện khác + {tien(muc - round(hs * gia_tri('P-MUC-CHUAN-TGXH', ky_dau(ky))))} phần đơn thân (BR-03) = {tien(muc)}"
    if cd == "CD09":
        return f"{hs} × {mc} = {tien(muc)} (một lần)"
    if cd == "CD11":
        return f"{hs} tháng × trợ cấp tuất hiện hưởng = {tien(muc)} (một lần)"
    return giai_thich(ts, hs, muc, ky) + (" (mức cao nhất, BR-02)" if "BR-02" in br else "")


def tinh_dang_huong():
    e31, dien_moi_ky = {}, defaultdict(set)
    for p in nguoi.values():
        for ky in KY:
            s = song(p, ky)
            if s is False:
                continue
            items = dien_ca_nhan(p, ky)
            for it in items:
                if it[0] not in MOT_LAN | {"CD06", "CD08"}:
                    dien_moi_ky[(p["ma"], it[1])].add(ky)
            items = gop_cd01(items, ky)
            for cd, dien, ts, hs, muc, br in items:
                e31[("Người", p["ma"], cd, ky)] = dict(
                    loai_doi_tuong="Người", ma_doi_tuong=p["ma"], ma_che_do=cd, ky=ky, ma_dien_ap_dung=dien,
                    ma_tham_so=ts, he_so=hs, muc_dang_huong=muc if s else None, so_phai_chi=muc if s else None,
                    ma_quy_tac=br + ("; BR-16" if cd == "CD03" else ""),
                    trang_thai_tinh="Đã tính" if s else "Chưa đủ dữ liệu (BR-52)",
                    giai_thich=giai_thich_dong(cd, dien, ts, hs, muc, br, ky) if s else "Trạng thái sống chưa xác định, không kết luận")
    for h in ho.values():
        for ky in KY:
            tv = thanh_vien_luc(h, ky_cuoi(ky))
            dbn = [p for p in tv if p["nkt"] == "Đặc biệt nặng" and song(p, ky)]
            if dbn and len([p for p in tv if song(p, ky)]) >= 2:
                hs = gia_tri("P-HS-CS-HO-NKT-DBN", ky_dau(ky))
                muc = round(hs * gia_tri("P-MUC-CHUAN-TGXH", ky_dau(ky)) * len(dbn))
                e31[("Hộ", h["ma"], "CD02", ky)] = dict(
                    loai_doi_tuong="Hộ", ma_doi_tuong=h["ma"], ma_che_do="CD02", ky=ky, ma_dien_ap_dung="TGXH-HO-CS-NKT-DBN",
                    ma_tham_so="P-HS-CS-HO-NKT-DBN", he_so=hs, muc_dang_huong=muc, so_phai_chi=muc, ma_quy_tac="BR-12",
                    trang_thai_tinh="Đã tính", nkt_dbn=dbn[0]["ma"],
                    giai_thich=f"1,0 × {tien(gia_tri('P-MUC-CHUAN-TGXH', ky_dau(ky)))} × {len(dbn)} NKT ĐBN = {tien(muc)}")
    return e31, dien_moi_ky


# ---------------------------------------------------------------- lớp 1: hưởng chế độ, chi trả (dữ liệu nguồn)

tk_cua = {}


def tao_tk(ma_ng, tc=None):
    loai = R.choice(["Ngân hàng giả A", "Ngân hàng giả B", "Ví điện tử giả C"])
    t = dict(ma_tk=ma("TK", 4), ma_nguoi_chu=ma_ng, loai="Ví điện tử" if loai.startswith("Ví") else "Tài khoản ngân hàng",
             to_chuc=loai, so_tk_che="******" + f"{R.randrange(10**4):04d}",
             hieu_luc_tu=date(R.randint(2018, 2025), R.randint(1, 12), 1), hieu_luc_den=None, nguon="Đơn vị chi trả (giả)", tc=tc)
    tai_khoan.append(t)
    return t


def tk_mac_dinh(ma_ng):
    if ma_ng not in tk_cua:
        tk_cua[ma_ng] = tao_tk(ma_ng) if R.random() < 0.5 else None
    return tk_cua[ma_ng]


def nguoi_nhan_mac_dinh(loai_dt, ma_dt):
    if loai_dt == "Hộ":
        return ho[ma_dt]["chu_ho"]
    p = nguoi[ma_dt]
    if tuoi(p["ngay_sinh"], NGAY_CHOT) < 18 or p["nkt"] == "Đặc biệt nặng":
        h = ho_cua(p, NGAY_CHOT)
        if h and h["chu_ho"] != p["ma"]:
            return h["chu_ho"]
    return p["ma"]


def them_qd(ma_huong, loai, ngay, xa, cd, ly_do):
    ncc = cd in ("CD04", "CD05", "CD06")
    quyet_dinh.append(dict(
        ma_qd=ma("QD", 5), ma_huong=ma_huong, so_hieu=f"{R.randint(100, 999)}/QĐ-{'SNV' if ncc else 'UBND'}", ngay_ky=ngay,
        co_quan="Sở Nội vụ Tỉnh Mẫu (giả)" if ncc else f"UBND {XA[xa]}", loai=loai, hieu_luc_tu=ngay, ly_do=ly_do,
        nguon="Nhập bổ sung (VT05 nhập, VT04 duyệt)" if R.random() < 0.1 else "ETL/API"))


def muc_truoc_chuyen(cd, muc):
    """Mức chi kỳ 07 đến 09/2026 khi xã chưa quyết định theo NĐ 335: cùng hệ số, mức chuẩn cũ."""
    ts = "P-HUU-TRI-XH" if cd == "CD03" else "P-MUC-CHUAN-TGXH"
    return round(muc * gia_tri(ts, NGAY_MUC_CU) / gia_tri(ts, D0726))


def them_huong(loai_dt, ma_dt, cd, muc, tu_ky, den_ky, xa, dien, he_so=None, nguoi_dt=None, nguoi_nhan=None,
               ly_do=None, ngay_huong=None, loai_qd="Hưởng", tk="mac_dinh", truy_linh="tu_dong", trang_thai=None):
    """Một bản ghi hưởng (E05), quyết định (E09) và các kỳ chi (E07).

    truy_linh: "tu_dong" (TGXH hằng tháng: kỳ trước KY_CHUYEN chi mức cũ, kỳ KY_CHUYEN truy lĩnh từng kỳ gốc),
    None (chi đúng mức quyết định mọi kỳ), "thieu:<kỳ>" (thiếu truy lĩnh kỳ đó), "trung:<kỳ>" (truy lĩnh kỳ đó hai lần).
    """
    mot_lan = cd in MOT_LAN
    nhan = nguoi_nhan or nguoi_nhan_mac_dinh(loai_dt, ma_dt)
    t = tk_mac_dinh(nhan) if tk == "mac_dinh" else tk
    ngay_huong = ngay_huong or (ngay_bat_ky(2019, 2025) if tu_ky == KY[0] else ky_dau(tu_ky))
    if truy_linh == "tu_dong":
        truy_linh = "du" if cd in CD_TGXH else None
    h = dict(ma_huong=ma("HCD", 6), ma_che_do=cd, ma_nguoi_doi_tuong=nguoi_dt or ma_dt, loai_doi_tuong_huong=loai_dt,
             ma_doi_tuong_huong=ma_dt, ma_nguoi_nhan=nhan, hinh_thuc="Một lần" if mot_lan else "Tiền hằng tháng",
             ma_dien_theo_nguon=dien, he_so=he_so, muc_theo_qd=muc, hieu_luc_tu=ngay_huong,
             hieu_luc_den=ky_cuoi(den_ky) if den_ky else None, ma_dia_ban_chi_tra=xa,
             trang_thai=trang_thai or ("Đã chi một lần" if mot_lan else "Đang hưởng" if den_ky is None
                                       else "Thôi hưởng" if ly_do and "Điều chỉnh" not in ly_do else "Đã điều chỉnh"),
             ly_do_cham_dut=ly_do, nguon="ETL/API", tu_ky=tu_ky, den_ky=den_ky)
    huong.append(h)
    them_qd(h["ma_huong"], loai_qd, ngay_huong, xa, cd, "Đủ điều kiện hưởng" if loai_qd != "Điều chỉnh" else "Thay đổi điều kiện hưởng")
    if den_ky and ly_do and "Điều chỉnh" not in ly_do and den_ky != KY[-1]:
        them_qd(h["ma_huong"], "Thôi hưởng", ky_dau(KY[KY.index(den_ky) + 1]), xa, cd, ly_do)
    cu = muc_truoc_chuyen(cd, muc) if truy_linh else muc
    cac_ky = [k for k in KY if tu_ky <= k <= (den_ky or KY[-1])]
    goc = [k for k in cac_ky if k < KY_CHUYEN] if truy_linh and cu != muc else []
    if goc:
        them_qd(h["ma_huong"], "Điều chỉnh mức (NĐ 335/2026 Điều 32 khoản 4)", date(2026, 10, 15), xa, cd,
                "Chuyển sang mức NĐ 335/2026 từ 07/2026, truy lĩnh phần chênh")
    tl = list(goc)
    if truy_linh and ":" in truy_linh:
        kieu, k = truy_linh.split(":")
        tl = [x for x in tl if x != k] if kieu == "thieu" else tl + [k]

    def chi(ky_chi, ky_huong, loai, tien_chi):
        chi_tra.append(dict(
            ma_chi_tra=ma("CT", 7), ma_huong=h["ma_huong"], ky_chi=ky_chi, ky_huong=ky_huong, loai_khoan=loai,
            truy_linh_tu_ky=ky_huong if loai == "Truy lĩnh" else None, truy_linh_den_ky=ky_huong if loai == "Truy lĩnh" else None,
            so_thuc_chi=tien_chi, ngay_chi=ky_dau(ky_chi) + timedelta(days=9), ma_nguoi_nhan=nhan,
            ma_tai_khoan=t["ma_tk"] if t else None, hinh_thuc_chi="Chuyển khoản" if t else "Tiền mặt qua bưu điện",
            don_vi_chi_tra=f"Bưu điện {XA[xa]}", ket_qua="Đã chi"))
    for ky in cac_ky:
        chi(ky, ky, "Một lần" if mot_lan else "Thường kỳ", cu if ky in goc else muc)
    for k in sorted(tl):
        chi(KY_CHUYEN, k, "Truy lĩnh", muc - cu)
    return h


def nguoi_to_chuc_mai_tang(p):
    h = ho_cua(p, p["ngay_mat"])
    if h and h["chu_ho"] != p["ma"]:
        return h["chu_ho"]
    for q in quan_he:
        if q["ma_nguoi_2"] == p["ma"] and q["loai"].startswith(("Phụng dưỡng", "Người tổ chức mai táng")):
            return q["ma_nguoi_1"]
    khac = [x for x in thanh_vien_luc(h, p["ngay_mat"]) if x is not p] if h else []
    return khac[0]["ma"] if khac else p["ma"]


def suy_huong_nen(e31):
    """Dân số nền: nguồn đã cập nhật đúng, mỗi đoạn mức không đổi là một bản ghi hưởng."""
    nhom = defaultdict(dict)
    for (lt, mdt, cd, ky), r in e31.items():
        if r["muc_dang_huong"] is not None:
            nhom[(lt, mdt, cd)][ky] = r
    for (lt, mdt, cd), theo_ky in sorted(nhom.items()):
        if bo_qua(nguoi[mdt] if lt == "Người" else ho[mdt], cd):
            continue
        if cd in MOT_LAN:
            p = nguoi[mdt]
            ky, r = next(iter(theo_ky.items()))
            them_huong(lt, mdt, cd, r["muc_dang_huong"], ky, ky, ho_cua(p, p["ngay_mat"])["xa"], r["ma_dien_ap_dung"], r["he_so"],
                       nguoi_nhan=nguoi_to_chuc_mai_tang(p), ngay_huong=p["ngay_mat"] + timedelta(days=5), loai_qd=LOAI_QD_MOT_LAN[cd])
            continue
        doan = []
        for ky in KY:
            r = theo_ky.get(ky)
            if not r:
                continue
            if doan and doan[-1][1] == ky_truoc(ky) and doan[-1][2] == r["muc_dang_huong"] and doan[-1][3] == r["ma_dien_ap_dung"]:
                doan[-1][1] = ky
            else:
                doan.append([ky, ky, r["muc_dang_huong"], r["ma_dien_ap_dung"], r["he_so"]])
        for i, (tu, den, muc, dien, hs) in enumerate(doan):
            cuoi = i == len(doan) - 1
            den_out = None if (cuoi and den == KY[-1]) else den
            ly_do = None
            if den_out:
                if not cuoi:
                    ly_do = "Điều chỉnh mức (BR-05)"
                elif lt == "Người" and nguoi[mdt]["ngay_mat"]:
                    ly_do = "Đối tượng chết (BR-05)"
                elif lt == "Hộ":
                    ly_do = "Người được chăm sóc chết (BR-09)"
                else:
                    ly_do = "Không còn đủ điều kiện"
            if lt == "Người":
                xa = ho_cua(nguoi[mdt], ky_dau(tu))["xa"]
                nguoi_dt = mdt
            else:
                xa, nguoi_dt = ho[mdt]["xa"], theo_ky[tu]["nkt_dbn"]
            them_huong(lt, mdt, cd, muc, tu, den_out, xa, dien, hs, nguoi_dt=nguoi_dt, ly_do=ly_do,
                       loai_qd="Điều chỉnh" if i > 0 else "Hưởng")


# ---------------------------------------------------------------- ca gieo sẵn


def ca(ma_tc, ten, du_lieu, loai, quy_tac, doi_tuong, cd, ky_tu, ky_den, so_tien, uc):
    ca_kiem_thu.append(dict(ma_tc=ma_tc, ten=ten, du_lieu_gieo=du_lieu, loai_mong_doi=loai, quy_tac_mong_doi=quy_tac,
                            ma_doi_tuong=doi_tuong, ma_che_do=cd, ky_tu=ky_tu, ky_den=ky_den, so_tien_mong_doi=so_tien, uc=uc))


def ho_don(xa, pl, gioi, dob, tc, **tt):
    h = tao_ho(xa, pl, tc)
    p = vao_ho(h, tao_nguoi(gioi, dob, tc=tc, **tt), "Chủ hộ")
    return h, p


def gieo_ca():
    # TC-M01 chi sau ngày mất
    _, p = ho_don("X99001", "Nghèo", "Nữ", ngay_sinh(80), "TC-M01", khong_suy=True, trang_thai="Đã mất",
                  ngay_mat=date(2026, 8, 15), nguon_tu_vong="CSDL dân cư (giả)")
    them_huong("Người", p["ma"], "CD01", 1_080_000, "2026-07", None, "X99001", "TGXH-K5A-TU75", 2.0)
    chau = vao_ho(tao_ho("X99001"), tao_nguoi("Nam", ngay_sinh(48), tc="TC-M01", hon_nhan=VC), "Chủ hộ")
    lien_ket(chau, p, "Người tổ chức mai táng (cháu)", "Tờ khai đề nghị hỗ trợ mai táng (giả)", date(2026, 8, 16))
    them_huong("Người", p["ma"], "CD09", 10_800_000, "2026-08", "2026-08", "X99001", "TGXH-MAI-TANG", 20, nguoi_nhan=chau["ma"],
               ngay_huong=date(2026, 8, 20), loai_qd="Hỗ trợ chi phí mai táng")
    ca("TC-M01", "Chi sau ngày mất", "NCT 80 tuổi hộ nghèo, mất 15/08/2026; nguồn chi trả vẫn chi 09, 10/2026",
       "Chi sau ngày mất", "BR-05; BR-08", p["ma"], "CD01", "2026-09", "2026-10", 2_160_000, "UC07")
    # TC-M02 sai mức: nguồn còn mức chuẩn cũ 500.000
    _, p = ho_don("X99002", "Nghèo", "Nam", ngay_sinh(66), "TC-M02", khong_suy=True)
    them_huong("Người", p["ma"], "CD01", 750_000, "2026-07", None, "X99002", "TGXH-K5A-60DEN75", 1.5, truy_linh=None)
    ca("TC-M02", "Chưa chuyển mức theo NĐ 335", "NCT 66 tuổi hộ nghèo; xã chưa quyết định chuyển mức: nguồn vẫn 1,5 × 500.000 = 750.000 đến kỳ 10/2026, không có truy lĩnh",
       "Sai mức", "BR-13", p["ma"], "CD01", "2026-07", "2026-10", 240_000, "UC07")
    # TC-M03 trùng chế độ cùng xã
    _, p = ho_don("X99003", "Nghèo", "Nữ", ngay_sinh(65), "TC-M03", khong_suy=True)
    nkt(p, "Nặng")
    them_huong("Người", p["ma"], "CD01", 1_080_000, "2026-07", None, "X99003", "TGXH-K6-TE-NCT-NANG", 2.0)
    them_huong("Người", p["ma"], "CD01", 810_000, "2026-07", None, "X99003", "TGXH-K5A-60DEN75", 1.5)
    ca("TC-M03", "Hưởng hai mức TGXH cùng lúc", "NKT nặng 65 tuổi hộ nghèo; nguồn có 2 bản ghi trợ cấp (2,0 và 1,5)",
       "Trùng chế độ", "BR-02", p["ma"], "CD01", "2026-07", "2026-10", 3_240_000, "UC06")
    # TC-M04 bỏ sót TGXH, hộ nhận hỗ trợ ngoài ngân sách
    h, p = ho_don("X99001", "Nghèo", "Nữ", ngay_sinh(78), "TC-M04", khong_suy=True)
    ngoai_ns.append(dict(ma_ht=ma("HT", 3), loai_doi_tuong="Hộ", ma_doi_tuong=h["ma"], loai="Quỹ hỗ trợ", nguon_kinh_phi="Quỹ Vì người nghèo (giả)",
                         don_vi_cap="Ủy ban MTTQ xã (giả)", gia_tri=2_000_000, ngay_cap=date(2026, 2, 5), trang_thai="Đã cấp", nguon="Mặt trận Tổ quốc (giả)"))
    ca("TC-M04", "Đủ điều kiện TGXH nhưng chưa hưởng", "NCT 78 tuổi, hộ nghèo, không người phụng dưỡng; không có bản ghi hưởng",
       "Bỏ sót", "BR-01", p["ma"], "CD01", "2026-07", "2026-10", 4_320_000, "UC09")
    # TC-M05 bỏ sót hưu trí xã hội
    _, p = ho_don("X99002", "Không nghèo", "Nam", ngay_sinh(80), "TC-M05", khong_suy=True)
    ca("TC-M05", "Đủ điều kiện hưu trí xã hội nhưng chưa hưởng", "Người 80 tuổi, không lương hưu, không thuộc diện TGXH",
       "Bỏ sót", "KT-HTXH", p["ma"], "CD03", "2026-07", "2026-10", 2_160_000, "UC09")
    # TC-M06 hưu trí xã hội khi đang có lương hưu
    _, p = ho_don("X99003", "Không nghèo", "Nữ", ngay_sinh(77), "TC-M06", khong_suy=True, luong_huu=True)
    them_huong("Người", p["ma"], "CD03", 540_000, "2026-07", None, "X99003", "HTXH-TU75")
    ca("TC-M06", "Hưởng hưu trí xã hội khi có lương hưu", "Người 77 tuổi có lương hưu BHXH (E33) vẫn nhận hưu trí xã hội",
       "Chi khi không đủ điều kiện", "KT-HTXH", p["ma"], "CD03", "2026-07", "2026-10", 2_160_000, "UC07")
    # TC-M07 một tài khoản nhận cho 4 người ở 4 hộ (xử lý sau suy_huong_nen)
    chu = vao_ho(tao_ho("X99002"), tao_nguoi("Nam", ngay_sinh(45), tc="TC-M07"), "Chủ hộ")
    tk = tao_tk(chu["ma"], tc="TC-M07")
    for xa in ["X99001", "X99001", "X99002", "X99003"]:
        _, p = ho_don(xa, "Không nghèo", R.choice(["Nam", "Nữ"]), ngay_sinh(R.randint(30, 50)), "TC-M07")
        nkt(p, "Nặng")
        p["tk_chung"] = tk
    ca("TC-M07", "Một tài khoản nhận cho nhiều người khác hộ", "4 NKT nặng ở 4 hộ, cả 4 nhận vào tài khoản của một người ngoài hộ",
       "Tài khoản nhận bất thường", "KT-TK", tk["ma_tk"], "", "2026-07", "2026-10", 12_960_000, "UC08")
    # TC-M08 chuyển cư trú, hai xã cùng chi
    _, p = ho_don("X99001", "Không nghèo", "Nam", ngay_sinh(42), "TC-M08", khong_suy=True)
    nkt(p, "Nặng")
    ngay_chuyen = date(2026, 9, 10)
    thanh_vien[-1]["den_ngay"] = ngay_chuyen - timedelta(days=1)
    h_moi = tao_ho("X99002", tc="TC-M08")
    vao_ho(h_moi, p, "Chủ hộ", tu=ngay_chuyen)
    cu_tru_doi.append((p["ma"], "X99001", "X99002", ngay_chuyen))
    them_huong("Người", p["ma"], "CD01", 810_000, "2026-07", None, "X99001", "TGXH-K6-NANG", 1.5)
    them_huong("Người", p["ma"], "CD01", 810_000, "2026-10", None, "X99002", "TGXH-K6-NANG", 1.5)
    ca("TC-M08", "Chuyển cư trú, nơi cũ chưa thôi chi", "NKT nặng chuyển từ X99001 sang X99002 ngày 10/09/2026; nơi mới hưởng từ 10/2026, nơi cũ vẫn chi",
       "Trùng nơi chi", "BR-06", p["ma"], "CD01", "2026-10", "2026-10", 810_000, "UC07")
    # TC-M09 qua mốc 75 tuổi, nguồn chưa điều chỉnh
    _, p = ho_don("X99003", "Nghèo", "Nữ", date(1951, 9, 12), "TC-M09", khong_suy=True)
    them_huong("Người", p["ma"], "CD01", 810_000, "2026-07", None, "X99003", "TGXH-K5A-60DEN75", 1.5)
    ca("TC-M09", "Đủ 75 tuổi, chưa điều chỉnh hệ số", "NCT hộ nghèo đủ 75 tuổi ngày 12/09/2026; nguồn giữ 1,5",
       "Chuyển đổi chế độ", "BR-05", p["ma"], "CD01", "2026-09", "2026-10", 540_000, "UC11")
    # TC-M10 con liệt sĩ đủ 18 tuổi
    h = tao_ho("X99001", tc="TC-M10")
    me = vao_ho(h, tao_nguoi("Nữ", ngay_sinh(45), tc="TC-M10"), "Chủ hộ")
    con = vao_ho(h, tao_nguoi("Nam", date(2008, 8, 20), tc="TC-M10", khong_suy=True, con_ls=True), "Con")
    ls = tao_liet_si(2014, 30)
    cong_nhan_ncc(con, "NCC-TN-1LS", 2014)
    lien_ket(con, ls, "Thân nhân NCC: con liệt sĩ", "Giấy chứng nhận gia đình liệt sĩ (giả)", con["ngay_cn"])
    them_huong("Người", con["ma"], "CD07", 6_024_000, "2026-07", None, "X99001", "NCC-TN-1LS", nguoi_nhan=me["ma"])
    ca("TC-M10", "Con liệt sĩ đủ 18 tuổi, chưa chuyển mức", "Con liệt sĩ đủ 18 tuổi ngày 20/08/2026 (giả định đang đi học); nguồn giữ mục 3.1",
       "Chuyển đổi chế độ", "BR-22", con["ma"], "CD07", "2026-09", "2026-10", 6_024_000, "UC11")
    # TC-M11 hộ chăm sóc NKT ĐBN, NKT đã mất
    h = tao_ho("X99002", tc="TC-M11")
    h["khong_suy"] = True
    chu = vao_ho(h, tao_nguoi("Nữ", ngay_sinh(62), tc="TC-M11"), "Chủ hộ")
    con = vao_ho(h, nkt(tao_nguoi("Nam", ngay_sinh(40), tc="TC-M11", trang_thai="Đã mất", ngay_mat=date(2026, 7, 20),
                                  nguon_tu_vong="CSDL dân cư (giả)"), "Đặc biệt nặng"), "Con")
    them_huong("Hộ", h["ma"], "CD02", 540_000, "2026-07", None, "X99002", "TGXH-HO-CS-NKT-DBN", 1.0, nguoi_dt=con["ma"], nguoi_nhan=chu["ma"])
    ca("TC-M11", "Hỗ trợ hộ chăm sóc vẫn chi sau khi NKT mất", "NKT đặc biệt nặng mất 20/07/2026; trợ cấp của NKT đã dừng nhưng hỗ trợ hộ vẫn chi",
       "Chi khi người được chăm sóc đã mất", "BR-09", h["ma"], "CD02", "2026-08", "2026-10", 1_620_000, "UC07")
    # TC-M12 trạng thái sống chưa xác định
    _, p = ho_don("X99003", "Không nghèo", "Nam", ngay_sinh(40), "TC-M12", khong_suy=True, trang_thai="Chưa xác định")
    nkt(p, "Nặng")
    them_huong("Người", p["ma"], "CD01", 810_000, "2026-07", None, "X99003", "TGXH-K6-NANG", 1.5)
    ca("TC-M12", "Trạng thái sống chưa xác định", "NKT nặng, nguồn dân cư ghi 'chưa xác định'; vẫn chi 4 kỳ",
       "Chưa đủ dữ liệu", "BR-52", p["ma"], "CD01", "2026-07", "2026-10", 3_240_000, "UC07")
    # TC-M13 không nhận liên tục (xử lý sau suy_huong_nen)
    _, p = ho_don("X99001", "Không nghèo", "Nữ", ngay_sinh(50), "TC-M13")
    nkt(p, "Nặng")
    p["khong_nhan"] = True
    ca("TC-M13", "Không nhận liên tục từ 3 tháng", "NKT nặng không nhận tiền kỳ 07 đến 10/2026; nguồn vẫn ghi đang hưởng",
       "Cần tạm dừng", "BR-07", p["ma"], "CD01", "2026-07", "2026-10", 3_240_000, "UC07")
    # TC-M14 chưa có thẻ BHYT
    _, p = ho_don("X99002", "Không nghèo", "Nam", ngay_sinh(35), "TC-M14", khong_bhyt=True)
    nkt(p, "Đặc biệt nặng")
    ca("TC-M14", "Đang hưởng trợ cấp nhưng chưa có thẻ BHYT", "NKT đặc biệt nặng hưởng trợ cấp đúng nhưng không có thẻ BHYT trong E33",
       "Chưa có thẻ BHYT", "KT-BHYT", p["ma"], "CD01", "2026-10", "2026-10", 0, "UC16")
    # TC-M15 ghép mờ, không ghép được (kiểm tra ở E17, không sinh cảnh báo)
    ca("TC-M15", "Bản ghi nguồn ghép mờ và không ghép được", "2 bản ghi nguồn: một lệch ngày sinh (ghép mờ chờ VT02 duyệt), một thiếu số định danh",
       "Không sinh cảnh báo; BR-50 đếm riêng 2 bản ghi", "BR-50", "", "", "", "", 0, "UC01")
    # TC-M16 Bà mẹ Việt Nam anh hùng và người phục vụ (ca đúng)
    h = tao_ho("X99001", tc="TC-M16")
    con_trai = vao_ho(h, tao_nguoi("Nam", ngay_sinh(66), tc="TC-M16"), "Chủ hộ")
    con_dau = vao_ho(h, tao_nguoi("Nữ", ngay_sinh(62), tc="TC-M16"), "Vợ")
    me = vao_ho(h, tao_nguoi("Nữ", ngay_sinh(97), tc="TC-M16", phung_duong=True), "Mẹ")
    cong_nhan_ncc(me, "NCC-BMVNAH", 1995)
    for nam in (1968, 1972):
        lien_ket(me, tao_liet_si(nam, R.randint(19, 24)), "Thân nhân NCC: mẹ liệt sĩ", "Giấy chứng nhận gia đình liệt sĩ (giả)", me["ngay_cn"])
    lien_ket(con_trai, me, "Phụng dưỡng (con đẻ)", "Hộ tịch (giả)", date(1990, 1, 1))
    con_dau["phuc_vu_cho"] = me["ma"]
    lien_ket(con_dau, me, "Người phục vụ NCC", "Quyết định trợ cấp người phục vụ (giả)", date(2010, 3, 1))
    ca("TC-M16", "Bà mẹ Việt Nam anh hùng và người phục vụ (ca đúng)",
       "BMVNAH 97 tuổi: trợ cấp 9.036.000, phụ cấp 2.524.000; người phục vụ 3.012.000 (NĐ 321/2026 mục 12.1)",
       "Không sinh cảnh báo", "BR-20", me["ma"], "CD04;CD05;CD06", "2026-07", "2026-10", 0, "UC04")
    gieo_ca_mo_rong()


def gieo_ca_mo_rong():
    """Ca gieo sẵn cho trẻ em, đơn thân nghèo, mai táng, tuất thân nhân liệt sĩ, truy lĩnh."""
    # TC-M17 trẻ mồ côi đủ 4 tuổi, nguồn giữ hệ số 2,5
    h = tao_ho("X99002", "Nghèo", tc="TC-M17")
    vao_ho(h, tao_nguoi("Nữ", ngay_sinh(64), tc="TC-M17", hon_nhan="Góa", phung_duong=True), "Chủ hộ")
    be = vao_ho(h, mo_coi(tao_nguoi("Nữ", date(2022, 8, 15), tc="TC-M17", khong_suy=True), tao_cha_me_da_mat(2024)), "Cháu")
    them_huong("Người", be["ma"], "CD01", 1_350_000, "2026-07", None, "X99002", "TGXH-K1-DUOI4", 2.5)
    ca("TC-M17", "Trẻ mồ côi đủ 4 tuổi, chưa đổi hệ số", "Trẻ mồ côi cả cha mẹ đủ 4 tuổi ngày 15/08/2026; nguồn giữ hệ số 2,5",
       "Chuyển đổi chế độ", "BR-05", be["ma"], "CD01", "2026-08", "2026-10", 1_620_000, "UC11")
    # TC-M18 trẻ mồ côi đủ 16 tuổi, không đi học, nguồn vẫn chi
    h = tao_ho("X99003", "Không nghèo", tc="TC-M18")
    vao_ho(h, tao_nguoi("Nam", ngay_sinh(50), tc="TC-M18", hon_nhan=VC), "Chủ hộ")
    em = vao_ho(h, mo_coi(tao_nguoi("Nam", date(2010, 7, 25), tc="TC-M18", khong_suy=True), tao_cha_me_da_mat(2020)), "Cháu")
    them_huong("Người", em["ma"], "CD01", 810_000, "2026-07", None, "X99003", "TGXH-K1-TU4", 1.5)
    ca("TC-M18", "Trẻ mồ côi đủ 16 tuổi, không đi học, vẫn chi", "Trẻ mồ côi đủ 16 tuổi ngày 25/07/2026, không đi học; thôi từ 08/2026 nhưng nguồn vẫn chi",
       "Chuyển đổi chế độ", "BR-05", em["ma"], "CD01", "2026-08", "2026-10", 2_430_000, "UC11")
    # TC-M19 đơn thân nghèo là NKT nặng, thiếu phần đơn thân (BR-03)
    h = tao_ho("X99001", "Nghèo", tc="TC-M19")
    me = vao_ho(h, nkt(tao_nguoi("Nữ", ngay_sinh(35), tc="TC-M19", hon_nhan="Ly hôn", don_than=True, khong_suy=True), "Nặng"), "Chủ hộ")
    vao_ho(h, tao_nguoi("Nam", ngay_sinh(6), tc="TC-M19"), "Con")
    them_huong("Người", me["ma"], "CD01", 810_000, "2026-07", None, "X99001", "TGXH-K6-NANG", 1.5)
    ca("TC-M19", "Đơn thân nghèo là NKT nặng, thiếu phần đơn thân", "Mẹ đơn thân hộ nghèo, NKT nặng, nuôi 1 con 6 tuổi; nguồn chỉ có trợ cấp NKT 1,5",
       "Bỏ sót phần cộng thêm", "BR-03", me["ma"], "CD01", "2026-07", "2026-10", 2_160_000, "UC06")
    # TC-M20 NKT đặc biệt nặng cao tuổi chết, chưa hỗ trợ mai táng
    h = tao_ho("X99002", "Không nghèo", tc="TC-M20")
    vao_ho(h, tao_nguoi("Nam", ngay_sinh(45), tc="TC-M20", hon_nhan=VC), "Chủ hộ")
    ba = vao_ho(h, nkt(tao_nguoi("Nữ", ngay_sinh(72), tc="TC-M20", hon_nhan="Góa", phung_duong=True, khong_suy={"CD09"},
                                 trang_thai="Đã mất", ngay_mat=date(2026, 9, 20), nguon_tu_vong="CSDL dân cư (giả)"), "Đặc biệt nặng"), "Mẹ")
    ca("TC-M20", "Đối tượng TGXH chết, chưa hỗ trợ mai táng", "NKT đặc biệt nặng 72 tuổi mất 20/09/2026; trợ cấp đã dừng đúng nhưng chưa có hỗ trợ mai táng",
       "Bỏ sót", "BR-10", ba["ma"], "CD09", "2026-09", "2026-09", 10_800_000, "UC11")
    # TC-M21 NCC có lương hưu chết: ngân sách vẫn chi mai táng NCC dù BHXH đã chi
    h = tao_ho("X99003", "Không nghèo", tc="TC-M21")
    ong = vao_ho(h, tao_nguoi("Nam", ngay_sinh(78), tc="TC-M21", hon_nhan=VC, luong_huu=True, trang_thai="Đã mất",
                              ngay_mat=date(2026, 8, 12), nguon_tu_vong="CSDL dân cư (giả)"), "Chủ hộ")
    vo = vao_ho(h, tao_nguoi("Nữ", ngay_sinh(75), tc="TC-M21", hon_nhan=VC), "Vợ")
    cong_nhan_ncc(ong, "NCC-CDHH", 2010)
    ong["ty_le"] = 50
    ghi_giam_dinh(ong, "Tỷ lệ tổn thương cơ thể (%)", 50, "Hội đồng giám định y khoa tỉnh (giả)", "CSDL người có công (giả)")
    them_huong("Người", ong["ma"], "CD10", 23_400_000, "2026-08", "2026-08", "X99003", "NCC-MAI-TANG", nguoi_nhan=vo["ma"],
               ngay_huong=date(2026, 8, 18), loai_qd="Trợ cấp mai táng")
    ca("TC-M21", "Chi mai táng NCC khi đã hưởng mai táng BHXH", "Người nhiễm chất độc hóa học có lương hưu mất 12/08/2026; BHXH chi mai táng (E33) và ngân sách vẫn chi",
       "Chi khi không đủ điều kiện", "BR-27", ong["ma"], "CD10", "2026-08", "2026-08", 23_400_000, "UC07")
    # TC-M22 vợ liệt sĩ sống cô đơn, chưa có tuất nuôi dưỡng
    _, p = ho_don("X99001", "Không nghèo", "Nữ", ngay_sinh(83), "TC-M22", hon_nhan="Góa", khong_suy={"CD08"})
    cong_nhan_ncc(p, "NCC-TN-1LS", 1990)
    lien_ket(p, tao_liet_si(1972, 24), "Thân nhân NCC: vợ liệt sĩ", "Giấy chứng nhận gia đình liệt sĩ (giả)", p["ngay_cn"])
    ca("TC-M22", "Vợ liệt sĩ sống cô đơn chưa có tuất nuôi dưỡng", "Vợ liệt sĩ 83 tuổi sống một mình, không người phụng dưỡng; nguồn chỉ có tuất hằng tháng",
       "Bỏ sót", "KT-TUAT-ND", p["ma"], "CD08", "2026-07", "2026-10", 9_640_000, "UC23")
    # TC-M23 mẹ hai liệt sĩ, nguồn trả mức thân nhân một liệt sĩ
    h = tao_ho("X99002", "Không nghèo", tc="TC-M23")
    me = vao_ho(h, tao_nguoi("Nữ", ngay_sinh(90), tc="TC-M23", hon_nhan="Góa", phung_duong=True, khong_suy={"CD07"}), "Chủ hộ")
    con_gai = vao_ho(h, tao_nguoi("Nữ", ngay_sinh(60), tc="TC-M23", hon_nhan=VC), "Con")
    cong_nhan_ncc(me, "NCC-TN-2LS", 1985)
    for nam in (1968, 1972):
        lien_ket(me, tao_liet_si(nam, R.randint(19, 23)), "Thân nhân NCC: mẹ liệt sĩ", "Giấy chứng nhận gia đình liệt sĩ (giả)", me["ngay_cn"])
    lien_ket(con_gai, me, "Phụng dưỡng (con đẻ)", "Hộ tịch (giả)", date(1990, 1, 1))
    them_huong("Người", me["ma"], "CD07", 3_012_000, "2026-07", None, "X99002", "NCC-TN-1LS")
    ca("TC-M23", "Mẹ hai liệt sĩ hưởng mức thân nhân một liệt sĩ", "Mẹ của 2 liệt sĩ; nguồn trả NCC-PL1-09 thay vì NCC-PL1-10",
       "Sai mức", "BR-20", me["ma"], "CD07", "2026-07", "2026-10", 12_048_000, "UC07")
    # TC-M24 vợ liệt sĩ chết: tuất vẫn chi kỳ sau, chưa có trợ cấp một lần
    h = tao_ho("X99003", "Không nghèo", tc="TC-M24")
    con_trai = vao_ho(h, tao_nguoi("Nam", ngay_sinh(58), tc="TC-M24", hon_nhan=VC), "Chủ hộ")
    vo = vao_ho(h, tao_nguoi("Nữ", ngay_sinh(85), tc="TC-M24", hon_nhan="Góa", phung_duong=True, khong_suy={"CD07", "CD11"},
                             trang_thai="Đã mất", ngay_mat=date(2026, 9, 10), nguon_tu_vong="CSDL dân cư (giả)"), "Mẹ")
    cong_nhan_ncc(vo, "NCC-TN-1LS", 1990)
    lien_ket(vo, tao_liet_si(1968, 25), "Thân nhân NCC: vợ liệt sĩ", "Giấy chứng nhận gia đình liệt sĩ (giả)", vo["ngay_cn"])
    lien_ket(con_trai, vo, "Phụng dưỡng (con đẻ)", "Hộ tịch (giả)", date(1990, 1, 1))
    them_huong("Người", vo["ma"], "CD07", 3_012_000, "2026-07", None, "X99003", "NCC-TN-1LS")
    ca("TC-M24", "Thân nhân liệt sĩ chết: tuất vẫn chi", "Vợ liệt sĩ mất 10/09/2026; nguồn vẫn chi tuất kỳ 10/2026",
       "Chi sau ngày mất", "BR-28", vo["ma"], "CD07", "2026-10", "2026-10", 3_012_000, "UC07")
    ca("TC-M24", "Thân nhân liệt sĩ chết: chưa có trợ cấp một lần", "Cùng người: mai táng NCC đã chi đúng, trợ cấp một lần 3 tháng chưa chi",
       "Bỏ sót", "KT-TUAT-1L", vo["ma"], "CD11", "2026-09", "2026-09", 9_036_000, "UC23")
    # TC-M25, TC-M26 truy lĩnh theo NĐ 335 Điều 32
    _, p = ho_don("X99001", "Không nghèo", "Nam", ngay_sinh(38), "TC-M25", hon_nhan=VC, khong_suy=True)
    nkt(p, "Đặc biệt nặng")
    them_huong("Người", p["ma"], "CD01", 1_080_000, "2026-07", None, "X99001", "TGXH-K6-DBN", 2.0, truy_linh="thieu:2026-09")
    ca("TC-M25", "Truy lĩnh thiếu một kỳ", "NKT đặc biệt nặng: kỳ 07 đến 09 chi 1.000.000, kỳ 10 truy lĩnh 07 và 08, thiếu kỳ 09",
       "Truy lĩnh thiếu", "BR-41", p["ma"], "CD01", "2026-09", "2026-09", 80_000, "UC07")
    _, p = ho_don("X99002", "Không nghèo", "Nữ", ngay_sinh(44), "TC-M26", hon_nhan=VC, khong_suy=True)
    nkt(p, "Nặng")
    them_huong("Người", p["ma"], "CD01", 810_000, "2026-07", None, "X99002", "TGXH-K6-NANG", 1.5, truy_linh="trung:2026-07")
    ca("TC-M26", "Truy lĩnh trùng một kỳ", "NKT nặng: truy lĩnh kỳ 07/2026 được chi hai lần trong kỳ 10",
       "Truy lĩnh thừa", "BR-41", p["ma"], "CD01", "2026-07", "2026-07", 60_000, "UC07")


def hau_xu_ly_ca():
    for p in nguoi.values():
        if not (p.get("tk_chung") or p.get("khong_nhan")):
            continue
        ma_h = {h["ma_huong"] for h in huong if h["ma_doi_tuong_huong"] == p["ma"]}
        for c in chi_tra:
            if c["ma_huong"] not in ma_h:
                continue
            if p.get("tk_chung"):
                c["ma_tai_khoan"], c["hinh_thuc_chi"] = p["tk_chung"]["ma_tk"], "Chuyển khoản"
            else:
                c["ket_qua"], c["so_thuc_chi"], c["ngay_chi"] = "Không nhận", 0, None


# ---------------------------------------------------------------- sự kiện, cảnh báo


def sinh_su_kien(e31):
    sk = []
    dau, cuoi = ky_dau(KY[0]), NGAY_CHOT
    co_huong = {h["ma_nguoi_doi_tuong"] for h in huong} | {k[1] for k in e31 if k[0] == "Người"}
    for p in nguoi.values():
        if p["ngay_mat"] and dau <= p["ngay_mat"] <= cuoi:
            sk.append(("Chết", p["ma"], p["ngay_mat"], p["nguon_tu_vong"]))
        if p["ma"] not in co_huong:
            continue
        for n in [4, 16, 60, 75] + ([18] if p["con_ls"] else []):
            d = sinh_nhat(p["ngay_sinh"], n)
            if dau <= d <= cuoi:
                sk.append((f"Đủ {n} tuổi", p["ma"], d, "Engine (ngày sinh E01)"))
    for ma_ng, cu, moi, d in cu_tru_doi:
        sk.append((f"Chuyển cư trú {cu} → {moi}", ma_ng, d, "CSDL cư trú (giả)"))
    return [dict(ma_su_kien=ma("SK", 4), loai=l, ma_nguoi=m, ngay_xay_ra=d, ngay_ghi_nhan=min(d + timedelta(days=R.randint(2, 20)), NGAY_CHOT),
                 nguon=n, trang_thai="Đã xác nhận") for l, m, d, n in sorted(sk, key=lambda x: x[2])]


def phan_loai(k, ky, act, dang, dung, chi, dh, su_kien):
    lt, mdt, cd = k
    if not act:
        return "Bỏ sót", "BỎ SÓT", dh["ma_quy_tac"].split(";")[0], dung
    doi = lt == "Người" and any(s["ma_nguoi"] == mdt and s["loai"].startswith("Đủ") and s["ngay_xay_ra"] <= ky_cuoi(ky) for s in su_kien)
    qt_doi = "BR-22" if cd == "CD07" else "BR-05"
    if dung == 0:
        if lt == "Hộ":
            return "Chi khi người được chăm sóc đã mất", "CHI SAI", "BR-09", chi
        if song(nguoi[mdt], ky) is False:
            return "Chi sau ngày mất", "CHI SAI", "BR-28" if cd in CD_NCC else "BR-05; BR-08", chi
        if doi:
            return "Chuyển đổi chế độ", "CHUYỂN ĐỔI", qt_doi, chi
        return "Chi khi không đủ điều kiện", "CHI SAI", {"CD03": "KT-HTXH", "CD09": "BR-10", "CD10": "BR-27"}.get(cd, "BR-08"), chi
    if len(act) > 1:
        if len({h["ma_dia_ban_chi_tra"] for h in act}) > 1:
            return "Trùng nơi chi", "CHI SAI", "BR-06", chi - dung
        return "Trùng chế độ", "CHI SAI", "BR-02", chi - dung
    if dang < dung and "BR-03" in dh["ma_quy_tac"] and not any("K4" in (h["ma_dien_theo_nguon"] or "") for h in act):
        return "Bỏ sót phần cộng thêm", "BỎ SÓT", "BR-03", dung - dang
    if doi:
        return "Chuyển đổi chế độ", "CHUYỂN ĐỔI", qt_doi, abs(dang - dung)
    return "Sai mức", "CHI SAI", "BR-13" if cd in CD_TGXH else "BR-20", abs(dang - dung)


UC_THEO_LOAI = {"Trùng chế độ": "UC06", "Bỏ sót phần cộng thêm": "UC06", "Tài khoản nhận bất thường": "UC08",
                "Bỏ sót": "UC09", "Chuyển đổi chế độ": "UC11", "Chưa có thẻ BHYT": "UC16"}


def uc_cua(loai, cd):
    if loai == "Bỏ sót":
        return "UC23" if cd in ("CD07", "CD08", "CD11") else "UC11" if cd in ("CD09", "CD10") else "UC10" if cd == "CD02" else "UC09"
    return UC_THEO_LOAI.get(loai, "UC07")


def phat_hien(e31, su_kien):
    theo_khoa = defaultdict(list)
    for h in huong:
        theo_khoa[(h["loai_doi_tuong_huong"], h["ma_doi_tuong_huong"], h["ma_che_do"])].append(h)
    chi_idx = defaultdict(list)  # theo kỳ hưởng gốc: thường kỳ + truy lĩnh của kỳ đó (BR-41)
    for c in chi_tra:
        chi_idx[(c["ma_huong"], c["ky_huong"])].append(c)
    gom = {}

    def ghi(loai, nhom, qt, lt, mdt, cd, ky, so_tien, ma_huong, chieu=""):
        g = gom.setdefault((loai, lt, mdt, cd), dict(loai=loai, nhom=nhom, qt=qt, lt=lt, mdt=mdt, cd=cd, ky=[], tien=0, huong=set(), chieu=chieu))
        g["ky"].append(ky)
        g["tien"] += so_tien
        g["huong"] |= set(ma_huong)

    for k in sorted({x[:3] for x in e31} | set(theo_khoa)):
        for ky in KY:
            dh = e31.get(k + (ky,))
            act = [h for h in theo_khoa.get(k, []) if h["tu_ky"] <= ky <= (h["den_ky"] or KY[-1])]
            chi = sum(c["so_thuc_chi"] for h in act for c in chi_idx[(h["ma_huong"], ky)])
            mh = [h["ma_huong"] for h in act]
            if dh and dh["muc_dang_huong"] is None:
                if act:
                    ghi("Chưa đủ dữ liệu", "KHÁC", "BR-52", *k, ky, chi, mh)
                continue
            dang, dung = sum(h["muc_theo_qd"] for h in act), dh["muc_dang_huong"] if dh else 0
            if dang == dung:
                continue
            loai, nhom, qt, so_tien = phan_loai(k, ky, act, dang, dung, chi, dh, su_kien)
            ghi(loai, nhom, qt, *k, ky, so_tien, mh, "Thừa" if dang > dung else "Thiếu")
    for h in huong:  # BR-41: số đã chi theo kỳ gốc phải bằng mức quyết định
        if h["hinh_thuc"] != "Tiền hằng tháng":
            continue
        for ky in KY:
            dong = chi_idx[(h["ma_huong"], ky)]
            if not dong or any(c["ket_qua"] != "Đã chi" for c in dong):
                continue
            da_chi = sum(c["so_thuc_chi"] for c in dong)
            if da_chi == h["muc_theo_qd"]:
                continue
            co_tl = any(c["loai_khoan"] == "Truy lĩnh" for c in dong)
            if da_chi < h["muc_theo_qd"]:
                loai = "Truy lĩnh thiếu" if ky < KY_CHUYEN else "Chi lệch quyết định"
            else:
                loai = "Truy lĩnh thừa" if co_tl else "Chi lệch quyết định"
            ghi(loai, "CHI SAI", "BR-41", h["loai_doi_tuong_huong"], h["ma_doi_tuong_huong"], h["ma_che_do"], ky,
                abs(da_chi - h["muc_theo_qd"]), [h["ma_huong"]], "Thiếu" if da_chi < h["muc_theo_qd"] else "Thừa")
    nguong = gia_tri("P-TAM-DUNG-THANG", NGAY_CHOT)
    for h in huong:  # BR-07
        khong = sorted({c["ky_huong"] for c in chi_tra if c["ma_huong"] == h["ma_huong"] and c["ket_qua"] == "Không nhận"})
        if len(khong) >= nguong and h["trang_thai"] == "Đang hưởng":
            for ky in khong:
                ghi("Cần tạm dừng", "CHI SAI", "BR-07", h["loai_doi_tuong_huong"], h["ma_doi_tuong_huong"], h["ma_che_do"], ky, h["muc_theo_qd"], [h["ma_huong"]])
    vao_tk = defaultdict(list)  # KT-TK
    for c in chi_tra:
        if c["ma_tai_khoan"]:
            vao_tk[c["ma_tai_khoan"]].append(c)
    hmap = {h["ma_huong"]: h for h in huong}
    for tk, ds in vao_tk.items():
        dt = {hmap[c["ma_huong"]]["ma_doi_tuong_huong"] for c in ds}
        so_ho = {ho_cua(nguoi[d], NGAY_CHOT)["ma"] if d in nguoi else d for d in dt}
        if len(dt) >= NGUONG_TK_NGUOI and len(so_ho) >= 2:
            for c in ds:
                ghi("Tài khoản nhận bất thường", "CHI SAI", "KT-TK", "Tài khoản", tk, "", c["ky_chi"], c["so_thuc_chi"], [c["ma_huong"]])
    co_the = {b["ma_nguoi"] for b in bhxh if b["loai"] == "Thẻ BHYT" and (b["den_ngay"] is None or b["den_ngay"] >= NGAY_CHOT)}
    for (lt, mdt, cd, ky), r in e31.items():  # KT-BHYT
        if ky == KY[-1] and lt == "Người" and cd in ("CD01", "CD03", "CD04", "CD07") and r["muc_dang_huong"] and mdt not in co_the:
            ghi("Chưa có thẻ BHYT", "KHÁC", "KT-BHYT", lt, mdt, cd, ky, 0, [])
    return gom


def lap_canh_bao(gom, su_kien):
    out = []
    for g in sorted(gom.values(), key=lambda g: (g["nhom"], g["loai"], g["mdt"])):
        ky = sorted(set(g["ky"]))
        uc = uc_cua(g["loai"], g["cd"])
        tc = (nguoi[g["mdt"]]["tc"] if g["lt"] == "Người" else ho[g["mdt"]]["tc"] if g["lt"] == "Hộ"
              else next(t["tc"] for t in tai_khoan if t["ma_tk"] == g["mdt"]))
        sk = [s["ma_su_kien"] for s in su_kien if s["ma_nguoi"] == g["mdt"]]
        out.append(dict(
            ma_canh_bao=ma("CB", 4), nhom=g["nhom"], loai=g["loai"], chieu_lech=g["chieu"], ma_quy_tac=g["qt"],
            loai_doi_tuong=g["lt"], ma_doi_tuong=g["mdt"], ma_che_do=g["cd"], ky_tu=ky[0], ky_den=ky[-1], so_ky=len(ky),
            so_tien_anh_huong=g["tien"], ma_huong_lien_quan="; ".join(sorted(g["huong"])), ma_su_kien_lien_quan="; ".join(sk),
            ma_lan_tinh=LT_CT, ngay_phat_hien=NGAY_CHOT, trang_thai="Mới", vai_tro_xu_ly="VT06" if uc in ("UC06", "UC07", "UC08") else "VT05",
            uc=uc, ket_qua_xu_ly=None, ma_tc_mockup=tc))
    for cb in out:  # minh họa vòng đời xử lý (UC20)
        if cb["ma_tc_mockup"] == "TC-M01":
            cb["trang_thai"], cb["ket_qua_xu_ly"] = "Đang xác minh", "VT06 đã gửi xã xác minh giấy chứng tử (giả)"
        if cb["ma_tc_mockup"] == "TC-M06":
            cb["trang_thai"], cb["ket_qua_xu_ly"] = "Xác nhận đúng", "Đã có quyết định thôi hưởng, chờ thu hồi (giả)"
    return out


# ---------------------------------------------------------------- dữ liệu phụ: BHXH, rà soát hộ, hoàn cảnh hộ, nguồn


def sinh_bhxh(e31):
    huong_hang_thang = {k[1] for k, r in e31.items() if k[0] == "Người" and r["muc_dang_huong"]} | \
                       {h["ma_doi_tuong_huong"] for h in huong if h["loai_doi_tuong_huong"] == "Người"}
    for p in nguoi.values():
        if p["liet_si"] or (p["ngay_mat"] and p["ngay_mat"] < D0726):
            continue
        mso = "99" + f"{R.randrange(10**8):08d}"
        if p["luong_huu"]:
            bhxh.append(dict(ma_bh=ma("BH", 4), ma_nguoi=p["ma"], loai="Lương hưu", ma_so_bhxh=mso, nhom_doi_tuong="",
                             muc_huong=R.randrange(3_000_000, 9_000_000, 1000), tu_ngay=sinh_nhat(p["ngay_sinh"], 60),
                             den_ngay=p["ngay_mat"], trang_thai="Thôi hưởng (chết)" if p["ngay_mat"] else "Đang hưởng", nguon="CSDL BHXH (giả)"))
            if p["ngay_mat"]:
                bhxh.append(dict(ma_bh=ma("BH", 4), ma_nguoi=p["ma"], loai="Trợ cấp mai táng BHXH", ma_so_bhxh=mso, nhom_doi_tuong="",
                                 muc_huong=gia_tri("P-MAI-TANG-NCC", D0726), tu_ngay=p["ngay_mat"] + timedelta(days=7), den_ngay=None,
                                 trang_thai="Đã chi", nguon="CSDL BHXH (giả); mức giả định 10 × lương cơ sở"))
        if p["khong_bhyt"]:
            continue
        if p["ma"] in huong_hang_thang:
            nhom = "Ngân sách đóng: người hưởng trợ cấp hằng tháng"
        elif p["luong_huu"]:
            nhom = "Quỹ BHXH đóng: người hưởng lương hưu"
        elif R.random() < 0.6:
            nhom = "Hộ gia đình tự đóng"
        else:
            continue
        bhxh.append(dict(ma_bh=ma("BH", 4), ma_nguoi=p["ma"], loai="Thẻ BHYT", ma_so_bhxh=mso, nhom_doi_tuong=nhom, muc_huong=None,
                         tu_ngay=date(2026, 1, 1), den_ngay=date(2026, 12, 31), trang_thai="Còn hạn", nguon="CSDL BHXH (giả)"))


def ra_soat_ho():
    out = []
    for h in ho.values():
        pl = h["phan_loai"]
        tn = R.randrange(700_000, 1_500_000, 10_000) if pl != "Không nghèo" else R.randrange(1_600_000, 6_000_000, 10_000)
        th = R.randint(3, 6) if pl == "Nghèo" else R.randint(0, 2)
        out.append(dict(ma_rs=ma("RS", 4), ma_ho=h["ma"], ky_ra_soat="Định kỳ cuối năm 2025, áp dụng năm 2026", phan_loai=pl,
                        thu_nhap_binh_quan=tn, so_chieu_thieu_hut=th, chuan_ngheo_ap_dung="NĐ 07/2021 (nông thôn)", nguon="CSDL hộ nghèo (giả)"))
    return out


def hoan_canh_ho():
    out = []
    for h in ho.values():
        if h["phan_loai"] == "Không nghèo":
            continue
        tv = thanh_vien_luc(h, NGAY_CHOT)
        out.append(dict(ma_hc=ma("HC", 3), ma_ho=h["ma"], thoi_diem=date(2025, 12, 15),
                        nha_o=R.choice(["Nhà tạm", "Bán kiên cố, xuống cấp", "Bán kiên cố"]),
                        tai_san_chinh=R.choice(["Không có", "Xe máy cũ", "Ruộng 1 sào"]),
                        nguon_thu_nhap_chinh=R.choice(["Làm thuê", "Nông nghiệp", "Trợ cấp", "Không có"]),
                        so_nguoi_phu_thuoc=sum(1 for p in tv if not 16 <= tuoi(p["ngay_sinh"], NGAY_CHOT) < 60),
                        tiep_can_dich_vu=R.choice(["Thiếu nước sạch", "Thiếu nhà vệ sinh", "Đủ"]), nguon="CSDL hộ nghèo (giả)"))
    return out


NGUON = [  # ma, ten, co_quan, don_vi
    ("NGUON-DC", "CSDL quốc gia về dân cư", "Bộ Công an (giả định)", "Cá nhân, hộ cư trú"),
    ("NGUON-NCC", "CSDL người có công", "Bộ Nội vụ (giả định)", "Cá nhân"),
    ("NGUON-TGXH", "CSDL trợ giúp xã hội, NKT", "Bộ Y tế (giả định)", "Cá nhân"),
    ("NGUON-HN", "CSDL hộ nghèo, cận nghèo", "Bộ NN&MT", "Hộ rà soát"),
    ("NGUON-BHXH", "CSDL BHXH, BHYT", "BHXH Việt Nam (giả định)", "Cá nhân"),
    ("NGUON-CT", "Đơn vị chi trả", "Bưu điện, ngân hàng (giả định)", "Cá nhân, hộ"),
    ("NGUON-MTTQ", "Mặt trận Tổ quốc, quỹ hỗ trợ", "Ủy ban MTTQ (giả định)", "Cá nhân, hộ"),
]


def ban_ghi_nguon(ra_soat):
    ldb = {n[0]: f"LDB-{n[0][6:]}-20261031" for n in NGUON}
    bg = []

    def them(ng, loai, ma_ng=None, ma_h=None, pp="Số định danh", tin=1.0, tt="Đã ghép", tc=None):
        bg.append(dict(ma_bgn=ma("BGN", 6), ma_nguon=ng, ma_lan_dong_bo=ldb[ng], khoa_nguon=f"{ng[6:]}-{R.randrange(10**6):06d}",
                       loai_don_vi=loai, ma_nguoi=ma_ng, ma_ho=ma_h, phuong_phap_ghep=pp, do_tin_cay=tin, trang_thai_ghep=tt, ma_tc_mockup=tc))
    for p in nguoi.values():
        if not p["liet_si"]:
            them("NGUON-DC", "Cá nhân", p["ma"])
    ncc_ng = {p["ma"] for p in nguoi.values() if p["ncc"] or p["liet_si"] or p["phuc_vu_cho"]}
    tgxh_ng = {h["ma_nguoi_doi_tuong"] for h in huong if h["ma_che_do"] in CD_TGXH} | {r["ma_nguoi"] for r in giam_dinh if r["loai_chi_so"].startswith("Mức")}
    for m in sorted(ncc_ng):
        them("NGUON-NCC", "Cá nhân", m)
    for m in sorted(tgxh_ng):
        them("NGUON-TGXH", "Cá nhân", m)
    for r in ra_soat:
        if r["phan_loai"] != "Không nghèo":
            them("NGUON-HN", "Hộ", ma_h=r["ma_ho"], pp="Mã hộ và số định danh chủ hộ")
    for m in sorted({b["ma_nguoi"] for b in bhxh}):
        them("NGUON-BHXH", "Cá nhân", m)
    for x in ngoai_ns:
        them("NGUON-MTTQ", "Hộ", ma_h=x["ma_doi_tuong"], pp="Mã hộ")
    mo = R.choice([p for p in nguoi.values() if p["tc"] is None and not p["liet_si"] and tuoi(p["ngay_sinh"], NGAY_CHOT) >= 60])
    them("NGUON-TGXH", "Cá nhân", mo["ma"], pp="Họ tên, ngày sinh lệch 1 năm, địa bàn", tin=0.82, tt="Ghép mờ chờ duyệt", tc="TC-M15")
    them("NGUON-NCC", "Cá nhân", None, pp="Không có số định danh; họ tên trùng 3 người", tin=0.0, tt="Không ghép được", tc="TC-M15")
    so = defaultdict(int)
    for b in bg:
        so[b["ma_nguon"]] += 1
    so["NGUON-CT"] = len(chi_tra)
    lan = [dict(ma_lan_dong_bo=ldb[n[0]], ma_nguon=n[0], thoi_diem=datetime(2026, 10, 31, 22, 0),
                kieu="Toàn phần" if n[0] in ("NGUON-HN", "NGUON-DC") else "Tăng dần",
                so_ban_ghi=so[n[0]], so_loi=1 if n[0] == "NGUON-NCC" else 0, ma_ban_chup=BAN_CHUP) for n in NGUON]
    return bg, lan


# ---------------------------------------------------------------- dự báo (E36)


def xa_cua(lt, mdt):
    if lt == "Hộ":
        return ho[mdt]["xa"]
    h = ho_cua(nguoi[mdt], NGAY_CHOT)
    return h["xa"] if h else None


def kich_ban_du_bao(e31):
    out, ky, cuoi = [], KY[-1], date(2027, 10, 31)
    muc_ht = gia_tri("P-MUC-CHUAN-TGXH", ky_dau(ky))
    for xa in XA:
        dt = [(k, r) for k, r in e31.items() if k[3] == ky and r["muc_dang_huong"] and k[2] in CD_TGXH and xa_cua(k[0], k[1]) == xa]
        co_so = sum(r["muc_dang_huong"] for _, r in dt)
        moi = sum(round(r["muc_dang_huong"] * MUC_VD2 / muc_ht) for _, r in dt)
        out.append(dict(ma_kich_ban=f"KB-VD2-{xa}", ma_vd="VD2", ten="Đổi mức chuẩn TGXH lên 600.000 đồng", loai_thay_doi="Mức tiền",
                        ma_dia_ban=xa, ky_du_bao="2026-11", tham_so_nhap="P-MUC-CHUAN-TGXH = 600.000 (bản nháp)",
                        nhom="CD01, CD02, CD03", so_nguoi=len({k[1] for k, _ in dt}), kinh_phi_co_so=co_so, kinh_phi_kich_ban=moi,
                        chenh_lech=moi - co_so, ma_lan_tinh=LT_VD2, loai="Mô phỏng", ghi_chu="Giữ nguyên hệ số; không ghi vào kết quả chính thức (R10)"))
        du_75 = [p for p in nguoi.values() if not p["liet_si"] and song(p, ky) and NGAY_CHOT < sinh_nhat(p["ngay_sinh"], 75) <= cuoi
                 and xa_cua("Người", p["ma"]) == xa]
        chuyen = [p for p in du_75 if e31.get(("Người", p["ma"], "CD01", ky), {}).get("ma_dien_ap_dung") == "TGXH-K5A-60DEN75"]
        moi_htxh = [p for p in du_75 if not p["luong_huu"] and not p["ncc"] and ("Người", p["ma"], "CD01", ky) not in e31]
        tang = len(chuyen) * round(0.5 * muc_ht) + len(moi_htxh) * gia_tri("P-HUU-TRI-XH", ky_dau(ky))
        out.append(dict(ma_kich_ban=f"KB-VD1-{xa}", ma_vd="VD1", ten="Biến động do tuổi trong 12 tháng tới", loai_thay_doi="Số người, nhóm hệ số",
                        ma_dia_ban=xa, ky_du_bao="2026-11 đến 2027-10", tham_so_nhap="Ngưỡng 75 tuổi; mức chuẩn giữ 540.000",
                        nhom="CD01 (1,5 → 2,0), CD03 (mới)", so_nguoi=len(chuyen) + len(moi_htxh), kinh_phi_co_so=None, kinh_phi_kich_ban=None,
                        chenh_lech=tang, ma_lan_tinh=LT_VD1, loai="Mô phỏng",
                        ghi_chu=f"{len(chuyen)} người chuyển hệ số, {len(moi_htxh)} người vào hưu trí xã hội; chênh lệch là kinh phí tăng mỗi tháng khi đủ tuổi"))
    return out


# ---------------------------------------------------------------- dòng xuất


def dong_e04(dien_moi_ky):
    ten = {"NCC-BMVNAH": "Bà mẹ Việt Nam anh hùng", "NCC-TN-1LS": "Thân nhân 01 liệt sĩ", "NCC-TN-2LS": "Thân nhân 02 liệt sĩ",
           "NCC-CDHH": "Người hoạt động kháng chiến nhiễm chất độc hóa học", "HTXH-TU75": "Hưu trí xã hội (từ 75 tuổi)",
           "TGXH-K1-DUOI4": "Trẻ em mồ côi cả cha mẹ, dưới 4 tuổi", "TGXH-K1-TU4": "Trẻ em mồ côi cả cha mẹ, từ 4 tuổi",
           "TGXH-K2": "Từ 16 tuổi đang học, trước đó thuộc khoản 1", "TGXH-K4": "Đơn thân hộ nghèo, cận nghèo nuôi con"}
    out = []
    for p in nguoi.values():
        if p["ncc"]:
            out.append(dict(ma_dien_dt=ma("DDT", 5), ma_nguoi=p["ma"], ma_dien=p["ncc"], ten_dien=ten[p["ncc"]],
                            can_cu="Quyết định công nhận (giả)", ngay_cong_nhan=p["ngay_cn"], cach_sinh="Công nhận từ nguồn",
                            phien_ban_quy_tac=None, hieu_luc_tu=p["ngay_cn"], hieu_luc_den=None, nguon="CSDL người có công (giả)"))
    for (m, dien), kys in sorted(dien_moi_ky.items()):
        if dien.startswith("NCC"):
            continue
        kys = sorted(kys)
        out.append(dict(ma_dien_dt=ma("DDT", 5), ma_nguoi=m, ma_dien=dien, ten_dien=ten.get(dien, dien.replace("TGXH-", "TGXH ")),
                        can_cu="Suy từ E01, E11, E14, E06, E33", ngay_cong_nhan=None, cach_sinh="Suy ra theo quy tắc",
                        phien_ban_quy_tac=CAU_HINH, hieu_luc_tu=ky_dau(kys[0]),
                        hieu_luc_den=None if kys[-1] == KY[-1] else ky_cuoi(kys[-1]), nguon="Engine (cửa sổ tính 07 đến 10/2026)"))
    return out


def dong_e31(e31):
    out = []
    for k in sorted(e31):
        r = {c: v for c, v in e31[k].items() if c != "nkt_dbn"}
        out.append(dict(ma_dh=ma("DH", 6), **r, ma_lan_tinh=LT_CT))
    return out


def dong_e12():
    out = []
    doi = {m: (cu, moi, d) for m, cu, moi, d in cu_tru_doi}

    def them(m, xa, tu, den):
        out.append(dict(ma_cu_tru=ma("CTR", 6), ma_nguoi=m, ma_dia_ban=xa, loai="Thường trú", tu_ngay=tu, den_ngay=den, nguon="CSDL cư trú (giả)"))
    for p in nguoi.values():
        if p["liet_si"]:
            continue
        if p["ma"] in doi:
            cu, moi, d = doi[p["ma"]]
            them(p["ma"], cu, date(2000, 1, 1), d - timedelta(days=1))
            them(p["ma"], moi, d, None)
            continue
        h = ho_cua(p, p["ngay_mat"] or NGAY_CHOT)
        if h:  # cha mẹ đã mất của trẻ mồ côi không thuộc hộ nào trong bộ dữ liệu
            them(p["ma"], h["xa"], max(p["ngay_sinh"], date(2000, 1, 1)), p["ngay_mat"])
    return out


def danh_sach_sheet(e04, e12, e31_rows, e16, ra_soat, hoan_canh, bgn, lan, kb, su_kien):
    nguoi_rows = [dict(ma_nguoi=p["ma"], so_dinh_danh_gia=p["cccd"], ho_ten_gia=p["ho_ten"], ngay_sinh=p["ngay_sinh"], gioi_tinh=p["gioi_tinh"],
                       dan_toc=p["dan_toc"], tinh_trang_hon_nhan=p["hon_nhan"] or ("Chưa kết hôn" if tuoi(p["ngay_sinh"], NGAY_CHOT) < 18 else "Chưa rõ"),
                       dang_hoc="Có" if p["dang_hoc"] else None, trang_thai_song=p["trang_thai"], ngay_mat=p["ngay_mat"], nguon_xac_nhan_tu_vong=p["nguon_tu_vong"],
                       ma_tc_mockup=p["tc"]) for p in nguoi.values()]
    ho_rows = [dict(ma_ho=h["ma"], loai_ho="Hộ cư trú", ma_chu_ho=h["chu_ho"], ma_dia_ban=h["xa"], ngay_lap=h["ngay_lap"], nguon="CSDL dân cư (giả)",
                    ma_tc_mockup=h["tc"]) for h in ho.values()]
    huong_rows = [{k: v for k, v in h.items() if k not in ("tu_ky", "den_ky")} for h in huong]
    tk_rows = [{k: v for k, v in t.items() if k != "tc"} | {"ma_tc_mockup": t["tc"]} for t in tai_khoan]
    db = [dict(ma_dia_ban=TINH[0], ten=TINH[1], cap="Tỉnh", ma_cap_tren=None, hieu_luc_tu=date(2025, 7, 1), nguon="Danh mục ĐVHC (giả)")] + \
         [dict(ma_dia_ban=m, ten=t, cap="Xã", ma_cap_tren=TINH[0], hieu_luc_tu=date(2025, 7, 1), nguon="Danh mục ĐVHC (giả)") for m, t in XA.items()]
    ax = [dict(ma_anh_xa=f"AX{i + 1:02d}", ma_cu=c, ten_cu=t, ma_moi=m, ngay_ap_dung=date(2025, 7, 1), ma_van_ban="VB07",
               phien_ban="AX-2025.1", nguoi_soan="VT02", nguoi_duyet="VT04") for i, (c, t, m) in enumerate(XA_CU)]
    vb = [dict(ma_van_ban=v[0], so_hieu=v[1], trich_yeu=v[2], hieu_luc_tu=v[3], hieu_luc_den=v[4], van_ban_bi_thay_the=v[5], ghi_chu=v[6]) for v in VAN_BAN]
    cd = [dict(ma_che_do=c[0], ten=c[1], nhom_chinh_sach=c[2], hinh_thuc=c[3], don_vi_tinh=c[4], ma_van_ban=c[5], hieu_luc_tu=D0726,
               hieu_luc_den=None, phien_ban=CAU_HINH) for c in CHE_DO]
    ts = [dict(ma_tham_so=t[0], ten=t[1], ma_che_do=t[2], gia_tri=t[3], don_vi=t[4], ap_dung_tu=t[5], ap_dung_den=t[6], ma_van_ban=t[7],
               dieu_khoan=t[8], phien_ban=CAU_HINH) for t in THAM_SO]
    qt = [dict(ma_quy_tac=q[0], ten=q[1], ma_che_do=q[2], dieu_kien=q[3], can_cu=q[4], trang_thai=q[5], ap_dung_tu=D0726, phien_ban=CAU_HINH) for q in QUY_TAC]
    lt = [dict(ma_lan_tinh=LT_CT, thoi_diem=datetime(2026, 10, 31, 23, 0), pham_vi="Tỉnh T99, CD01 đến CD06, kỳ 07 đến 10/2026", ma_ban_chup=BAN_CHUP,
               phien_ban_cau_hinh=CAU_HINH, kich_ban="Chính thức", nguoi_kich_hoat="VT01", so_dang_huong=len(e31_rows), so_canh_bao=len(e16)),
          dict(ma_lan_tinh=LT_VD2, thoi_diem=datetime(2026, 11, 1, 9, 0), pham_vi="3 xã, kỳ 11/2026", ma_ban_chup=BAN_CHUP,
               phien_ban_cau_hinh=CAU_HINH + " + nháp VD2", kich_ban="Mô phỏng", nguoi_kich_hoat="VT07", so_dang_huong=None, so_canh_bao=None),
          dict(ma_lan_tinh=LT_VD1, thoi_diem=datetime(2026, 11, 1, 9, 30), pham_vi="3 xã, 11/2026 đến 10/2027", ma_ban_chup=BAN_CHUP,
               phien_ban_cau_hinh=CAU_HINH, kich_ban="Mô phỏng", nguoi_kich_hoat="VT07", so_dang_huong=None, so_canh_bao=None)]
    nguon = [dict(ma_nguon=n[0], ten=n[1], co_quan=n[2], don_vi_du_lieu=n[3], chieu="Vào", ghi_chu="Tên nguồn là giả định BA") for n in NGUON]
    return [
        ("E01 Người", "e01_nguoi", nguoi_rows), ("E02 Hộ", "e02_ho", ho_rows), ("E03 Thành viên hộ", "e03_thanh_vien_ho", thanh_vien),
        ("E04 Diện đối tượng", "e04_dien_doi_tuong", e04), ("E05 Hưởng chế độ", "e05_huong_che_do", huong_rows),
        ("E06 Quan hệ", "e06_quan_he", quan_he), ("E07 Chi trả", "e07_chi_tra", chi_tra), ("E09 Quyết định", "e09_quyet_dinh", quyet_dinh),
        ("E10 Tài khoản nhận", "e10_tai_khoan_nhan", tk_rows), ("E11 Giám định", "e11_ket_qua_giam_dinh", giam_dinh),
        ("E12 Cư trú", "e12_cu_tru", e12), ("E13 Địa bàn", "e13_dia_ban", db), ("E13 Ánh xạ địa bàn", "e13_anh_xa_dia_ban", ax),
        ("E14 Rà soát hộ", "e14_ket_qua_ra_soat_ho", ra_soat), ("E15 Sự kiện", "e15_su_kien", su_kien), ("E16 Cảnh báo", "e16_canh_bao", e16),
        ("E17 Nguồn", "e17_nguon", nguon), ("E17 Lần đồng bộ", "e17_lan_dong_bo", lan), ("E17 Bản ghi nguồn", "e17_ban_ghi_nguon", bgn),
        ("E20 Chế độ", "e20_che_do", cd), ("E21 Văn bản", "e21_van_ban_phap_ly", vb), ("E22 Tham số", "e22_tham_so_chinh_sach", ts),
        ("E23 Quy tắc", "e23_quy_tac", qt), ("E31 Đáng hưởng", "e31_dang_huong", e31_rows), ("E32 Lần tính", "e32_lan_tinh", lt),
        ("E33 BHXH BHYT", "e33_huong_bhxh_bhyt", bhxh), ("E34 Hỗ trợ ngoài NS", "e34_ho_tro_ngoai_ngan_sach", ngoai_ns),
        ("E35 Hoàn cảnh hộ", "e35_hoan_canh_ho", hoan_canh), ("E36 Kịch bản dự báo", "e36_kich_ban_du_bao", kb),
    ]


# ---------------------------------------------------------------- kiểm tra


def kiem_tra(e31, e16, bgn, e31_rows):
    loi = []
    theo_tc = defaultdict(list)
    for cb in e16:
        theo_tc[cb["ma_tc_mockup"]].append(cb)
    so_mong_doi = defaultdict(int)
    for c in ca_kiem_thu:
        so_mong_doi[c["ma_tc"]] += 1
    for c in ca_kiem_thu:
        if c["ma_tc"] in ("TC-M15", "TC-M16"):
            continue
        khop = [cb for cb in theo_tc.get(c["ma_tc"], []) if cb["loai"] == c["loai_mong_doi"] and cb["ma_quy_tac"] == c["quy_tac_mong_doi"]
                and cb["ma_doi_tuong"] == c["ma_doi_tuong"] and cb["ky_tu"] == c["ky_tu"] and cb["ky_den"] == c["ky_den"]
                and cb["so_tien_anh_huong"] == c["so_tien_mong_doi"]]
        c["ma_canh_bao_thuc_te"] = "; ".join(cb["ma_canh_bao"] for cb in khop) or \
            "; ".join(f"{cb['ma_canh_bao']} {cb['loai']} {cb['ma_quy_tac']} {cb['ky_tu']}-{cb['ky_den']} {cb['so_tien_anh_huong']}" for cb in theo_tc.get(c["ma_tc"], []))
        c["ket_qua"] = "Đạt" if len(khop) == 1 and len(theo_tc[c["ma_tc"]]) == so_mong_doi[c["ma_tc"]] else "Không đạt"
    tc16 = next(c for c in ca_kiem_thu if c["ma_tc"] == "TC-M16")
    me = tc16["ma_doi_tuong"]
    pv = next(p["ma"] for p in nguoi.values() if p["phuc_vu_cho"] == me)
    can = {(me, "CD04"): 9_036_000, (me, "CD05"): 2_524_000, (pv, "CD06"): 3_012_000}
    dung = all(e31.get(("Người", m, cd, ky), {}).get("muc_dang_huong") == v for (m, cd), v in can.items() for ky in KY)
    tc16["ma_canh_bao_thuc_te"] = "; ".join(cb["ma_canh_bao"] for cb in theo_tc.get("TC-M16", []))
    tc16["ket_qua"] = "Đạt" if dung and not theo_tc.get("TC-M16") else "Không đạt"
    tc15 = next(c for c in ca_kiem_thu if c["ma_tc"] == "TC-M15")
    tt = sorted(b["trang_thai_ghep"] for b in bgn if b["ma_tc_mockup"] == "TC-M15")
    tc15["ma_canh_bao_thuc_te"] = ""
    tc15["ket_qua"] = "Đạt" if tt == ["Ghép mờ chờ duyệt", "Không ghép được"] else "Không đạt"
    la = [cb["ma_canh_bao"] + " " + cb["loai"] for cb in e16 if cb["ma_tc_mockup"] is None]
    if la:
        loi.append(f"Cảnh báo ngoài ca gieo sẵn: {la}")
    loi += [f"{c['ma_tc']} không đạt" for c in ca_kiem_thu if c["ket_qua"] != "Đạt"]
    khoa = [(r["loai_doi_tuong"], r["ma_doi_tuong"], r["ma_che_do"], r["ky"]) for r in e31_rows]
    if len(khoa) != len(set(khoa)):
        loi.append("Trùng khóa E31")
    for ten, rows, cot in [("E03", thanh_vien, "ma_nguoi"), ("E05", huong, "ma_nguoi_nhan"), ("E06", quan_he, "ma_nguoi_1"),
                           ("E06", quan_he, "ma_nguoi_2"), ("E11", giam_dinh, "ma_nguoi"), ("E33", bhxh, "ma_nguoi")]:
        sai = [r[cot] for r in rows if r[cot] not in nguoi]
        if sai:
            loi.append(f"{ten}.{cot} tham chiếu người không có: {sai[:3]}")
    ma_h = {h["ma_huong"] for h in huong}
    if any(c["ma_huong"] not in ma_h for c in chi_tra) or any(q["ma_huong"] not in ma_h for q in quyet_dinh):
        loi.append("E07 hoặc E09 tham chiếu E05 không có")
    return loi


# ---------------------------------------------------------------- ghi file

TIEU_DE = Font(bold=True, color="FFFFFF")
NEN_TD = PatternFill("solid", fgColor="1F4E78")
NEN_GIA = PatternFill("solid", fgColor="FCE4D6")
COT_TIEN = ("muc", "so_tien", "kinh_phi", "so_thuc_chi", "chenh", "so_phai_chi", "thu_nhap")


def dinh_dang(k, v):
    if isinstance(v, bool) or v is None:
        return None
    if isinstance(v, datetime):
        return "dd/mm/yyyy hh:mm"
    if isinstance(v, date):
        return "dd/mm/yyyy"
    if isinstance(v, int) and k.startswith(COT_TIEN + ("gia_tri",)) and abs(v) >= 1000:
        return "#,##0"
    return None


def ghi_sheet(ws, rows):
    if not rows:
        ws.append(["(không có dòng)"])
        return
    cot = list(dict.fromkeys(k for r in rows for k in r))
    ws.append(cot)
    for c in ws[1]:
        c.font, c.fill = TIEU_DE, NEN_TD
    for r in rows:
        ws.append([r.get(k) for k in cot])
        for j, k in enumerate(cot, 1):
            f = dinh_dang(k, r.get(k))
            if f:
                ws.cell(ws.max_row, j).number_format = f
    for j, k in enumerate(cot, 1):
        rong = max([len(str(k))] + [len(str(r.get(k) or "")) for r in rows[:200]])
        ws.column_dimensions[get_column_letter(j)].width = min(max(10, rong + 2), 60)
    ws.freeze_panes = "B2"
    ws.auto_filter.ref = ws.dimensions


def ghi_csv(path, rows):
    cot = list(dict.fromkeys(k for r in rows for k in r))
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=cot)
        w.writeheader()
        for r in rows:
            w.writerow({k: (v.isoformat() if isinstance(v, (date, datetime)) else v) for k, v in r.items()})


def doc_truoc(sheets, ket_qua):
    dat = sum(1 for c in ca_kiem_thu if c["ket_qua"] == "Đạt")
    return [
        ("BỘ DỮ LIỆU GIẢ (MOCKUP) THEO MÔ HÌNH DỮ LIỆU LÕI project019", True),
        ("Toàn bộ là DỮ LIỆU GIẢ: tên, số định danh, mã số BHXH, tài khoản, địa bàn, số quyết định đều bịa. Số định danh giả bắt đầu bằng 099. Không dùng làm số liệu thật.", True),
        (f"Sinh ngày 03/11/2026 bằng work/project019_019_sinh_du_lieu_mockup.py (hạt giống 19, chạy lại ra cùng kết quả). Ngày chốt dữ liệu {NGAY_CHOT:%d/%m/%Y}; kỳ hưởng 07 đến 10/2026.", False),
        ("Căn cứ: sheet Mô hình dữ liệu, Mô hình hóa thực thể, Quy tắc BR, Tham số BR, Tham số NCC, Kịch bản dự báo, Task & Usecase của file 013.", False),
        ("", False),
        ("Cách dùng", True),
        ("• Mỗi sheet Exx là một thực thể; dòng 1 là tên cột dạng mã (dùng làm tên cột khi nạp thử vào Oracle). Bản CSV (UTF-8) cùng nội dung ở thư mục output/project019_019_du_lieu_mockup_csv.", False),
        ("• Lớp 1 (ETL/API) và lớp 2 (cấu hình) là đầu vào. Lớp 3 (E04 phần suy ra, E15, E16, E31, E32, E36) do engine thu nhỏ trong script tính từ đầu vào; dùng làm kết quả mong đợi khi kiểm thử engine thật.", False),
        ("• Dân số nền khớp quy tắc nên không sinh cảnh báo. 16 ca gieo sẵn (sheet Kịch bản kiểm thử; cột ma_tc_mockup ở E01, E02, E10, E16, E17) lệch có chủ đích để kiểm UC06 đến UC11, UC16, UC01, UC04.", False),
        (f"• Kết quả tự kiểm: {dat}/{len(ca_kiem_thu)} ca đạt; {ket_qua}.", False),
        ("", False),
        ("Giả định riêng của bộ mockup (chưa phải quyết định nghiệp vụ)", True),
        ("• Một tỉnh giả T99 sau sắp xếp 2025, 3 xã mới gộp từ 5 xã cũ. Tên 7 nguồn ở E17 là giả định BA.", False),
        ("• TGXH dựng trẻ em mồ côi cả cha mẹ (Điều 5 khoản 1 điểm b, khoản 2 giả định học liên tục đến dưới 22 tuổi), đơn thân hộ nghèo, cận nghèo nuôi con (khoản 4, cộng thêm theo BR-03), NCT hộ nghèo không người phụng dưỡng (khoản 5a), NKT nặng, đặc biệt nặng (khoản 6), hỗ trợ hộ chăm sóc NKT đặc biệt nặng. Chưa có HIV, các trường hợp khác của khoản 1, hỗ trợ người nhận chăm sóc trẻ mồ côi. Không có mức chuẩn riêng của tỉnh.", False),
        ("• Truy lĩnh: NĐ 335 hiệu lực 05/10/2026 nhưng chuyển mức từ 01/07/2026, nên mockup giả định kỳ 07 đến 09 chi theo mức chuẩn cũ (cùng hệ số) và kỳ 10 truy lĩnh từng kỳ gốc (một dòng E07 cho mỗi kỳ gốc, cột ky_huong). Ca gieo sẵn TC-M02 là xã chưa chuyển mức.", False),
        ("• Mai táng TGXH 20 × mức chuẩn tính theo mức NĐ 335 cho cả ca chết từ 07/2026; áp cả cho người hưởng hưu trí xã hội (theo Điều 33 khoản 2). Mai táng NCC dùng mức GIẢ ĐỊNH 23.400.000 (10 × lương cơ sở 2.340.000), vì sheet chưa có mức (VL-23). Người có lương hưu thì chỉ hưởng mai táng BHXH.", False),
        ("• Tuất thân nhân liệt sĩ: tuất hằng tháng (PL Điều 16 khoản 3), tuất nuôi dưỡng khi sống cô đơn, rút gọn là sống một mình và không có người phụng dưỡng (khoản 4), trợ cấp một lần 3 tháng khi chết (khoản 11), mai táng (khoản 12). Chưa áp giới hạn 2 suất của BR-26, chưa có tuất của thân nhân NCC khác (vợ người nhiễm chất độc hóa học đã mất), chưa có con liệt sĩ mồ côi hưởng tuất nuôi dưỡng.", False),
        ("• Hưu trí xã hội rút gọn: từ 75 tuổi, không lương hưu, không hưởng trợ cấp NCC hằng tháng (quy tắc KT-HTXH, chưa trích điều NĐ 176/2025).", False),
        ("• NCC chỉ dựng BMVNAH, người phục vụ, thân nhân 1 và 2 liệt sĩ, con liệt sĩ dưới 18, nhiễm chất độc hóa học; áp NĐ 321/2026 từ 07/2026 cho mọi mục, chưa tách hai mốc của BR-21. Chưa tính tuất, thờ cúng, điều dưỡng (VL-39) và nhóm C E24 đến E30 (VL-30).", False),
        ("• Con liệt sĩ đủ 18 tuổi được giả định đang đi học nên chuyển sang mục thân nhân 01 liệt sĩ (TC-M10).", False),
        ("• Ba quy tắc KT-HTXH, KT-TK, KT-BHYT chỉ có trong mockup, chưa có trong sheet Quy tắc BR. Không có truy lĩnh, truy thu (T13).", False),
        ("• Chi trả ghi ngày 10 hằng tháng. Số tài khoản chỉ lưu dạng đã che.", False),
        ("", False),
        ("Danh sách sheet", True),
    ] + [(f"• {t}: {len(r)} dòng", False) for t, _, r in sheets]


def ghi_file(sheets, ket_qua):
    wb = Workbook()
    ws = wb.active
    ws.title = "Đọc trước"
    for text, dam in doc_truoc(sheets, ket_qua):
        ws.append([text])
        if dam:
            ws.cell(ws.max_row, 1).font = Font(bold=True)
    ws.column_dimensions["A"].width = 150
    for c in ws["A"]:
        c.alignment = Alignment(wrap_text=True, vertical="top")
    ws["A2"].fill = NEN_GIA
    ghi_sheet(wb.create_sheet("Kịch bản kiểm thử"), ca_kiem_thu)
    OUT_CSV.mkdir(parents=True, exist_ok=True)
    ghi_csv(OUT_CSV / "kich_ban_kiem_thu.csv", ca_kiem_thu)
    for ten, file, rows in sheets:
        ghi_sheet(wb.create_sheet(ten), rows)
        ghi_csv(OUT_CSV / f"{file}.csv", rows)
    wb.save(OUT_XLSX)


# ---------------------------------------------------------------- chạy


def main():
    if any(OUT_XLSX.parent.glob("~$*")):
        sys.exit("Có file Excel đang mở trong output/ (~$*), dừng.")
    sinh_dan_so_nen()
    gieo_ca()
    e31, dien = tinh_dang_huong()
    suy_huong_nen(e31)
    hau_xu_ly_ca()
    su_kien = sinh_su_kien(e31)
    sinh_bhxh(e31)
    e16 = lap_canh_bao(phat_hien(e31, su_kien), su_kien)
    ra_soat = ra_soat_ho()
    bgn, lan = ban_ghi_nguon(ra_soat)
    e31_rows = dong_e31(e31)
    loi = kiem_tra(e31, e16, bgn, e31_rows)
    ket_qua = "không có lỗi tham chiếu, không có cảnh báo ngoài ca gieo sẵn" if not loi else "; ".join(loi)
    sheets = danh_sach_sheet(dong_e04(dien), dong_e12(), e31_rows, e16, ra_soat, hoan_canh_ho(), bgn, lan, kich_ban_du_bao(e31), su_kien)
    ghi_file(sheets, ket_qua)
    for c in ca_kiem_thu:
        print(f"{c['ma_tc']}: {c['ket_qua']}  {c['ma_canh_bao_thuc_te']}")
    print("Lỗi:", loi or "không")
    print("Số dòng:", {f: len(r) for _, f, r in sheets})
    return 1 if loi else 0


if __name__ == "__main__":
    sys.exit(main())
