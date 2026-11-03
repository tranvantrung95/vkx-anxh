#!/usr/bin/env python3
"""Kiểm thử POC project019 (dữ liệu giả 019). Chạy: python3 -I work/project019_020_poc_test.py

Mỗi kiểm tra đếm lại bằng cách khác với pipeline, hoặc so với kết quả kỳ vọng có sẵn trong bộ 019
(E16 cảnh báo, kich_ban_kiem_thu TC-Mxx, E36 kịch bản VD2).
"""
import importlib.util
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("poc", ROOT / "work" / "project019_020_poc_pipeline.py")
P = importlib.util.module_from_spec(spec)
spec.loader.exec_module(P)
D, KQ = P.chay()
KQ_LOI = []


def kiem(ten, dung, chi_tiet=""):
    print(("ĐẠT     " if dung else "KHÔNG ĐẠT ") + ten + (f" — {chi_tiet}" if chi_tiet and not dung else ""))
    if not dung:
        KQ_LOI.append(ten)


# 1. Đối soát tính lại khớp từng cảnh báo E16
e16 = {(c["loai"], c["loai_doi_tuong"], c["ma_doi_tuong"], c["ma_che_do"] or "", c["ky_tu"], c["ky_den"], int(c["so_tien_anh_huong"]), c["ma_quy_tac"])
       for c in D.bang["e16_canh_bao"]}
poc = {(c["loai"], c["loai_doi_tuong"], c["ma_doi_tuong"], c["che_do"], c["ky_tu"], c["ky_den"], c["so_tien"], c["quy_tac"]) for c in KQ["canh_bao"]}
kiem(f"Đối soát: {len(poc)} cảnh báo POC trùng khớp {len(e16)} cảnh báo E16", poc == e16, f"thừa {poc - e16}; thiếu {e16 - poc}")

# 2. Từng ca TC-M (trừ M15 ghép định danh, M16 không sinh cảnh báo)
for c in D.bang["kich_ban_kiem_thu"]:
    if c["ma_tc"] in ("TC-M15", "TC-M16"):
        continue
    khop = [x for x in KQ["canh_bao"] if x["loai"] == c["loai_mong_doi"] and x["quy_tac"] == c["quy_tac_mong_doi"] and x["ma_doi_tuong"] == c["ma_doi_tuong"]
            and x["ky_tu"] == c["ky_tu"] and x["ky_den"] == c["ky_den"] and x["so_tien"] == int(c["so_tien_mong_doi"])]
    kiem(f"{c['ma_tc']} {c['ten']}", len(khop) == 1)
tt = sorted(b["trang_thai_ghep"] for b in D.bang["e17_ban_ghi_nguon"] if b["ma_tc_mockup"] == "TC-M15")
kiem("TC-M15 Ghép định danh: một ghép mờ, một không ghép được", tt == ["Ghép mờ chờ duyệt", "Không ghép được"])
m16 = next(c for c in D.bang["kich_ban_kiem_thu"] if c["ma_tc"] == "TC-M16")
kiem("TC-M16 Mẹ VNAH hưởng đủ, không sinh cảnh báo", not any(x["ma_doi_tuong"] == m16["ma_doi_tuong"] for x in KQ["canh_bao"]))

# 3. DB01: BR-50, BR-51, BR-53, đếm lại theo cách khác
for ngay_chot, d in KQ["db01"].items():
    nd = P.ngay(ngay_chot)
    nguoi = set()
    for r in D.bang["e04_dien_doi_tuong"]:
        p = D.nguoi[r["ma_nguoi"]]
        if (P.ngay(r["hieu_luc_tu"]) <= nd and (not r["hieu_luc_den"] or P.ngay(r["hieu_luc_den"]) >= nd)
                and not (p["ngay_mat"] and P.ngay(p["ngay_mat"]) <= nd)):
            nguoi.add(r["ma_nguoi"])
    kiem(f"BR-50 {ngay_chot}: số người duy nhất {d['tong_duy_nhat']} = đếm lại {len(nguoi)}", d["tong_duy_nhat"] == len(nguoi))
    kiem(f"BR-50 {ngay_chot}: tổng nhóm ≥ số người duy nhất", sum(g["tong"] for g in d["nhom"].values()) >= d["tong_duy_nhat"])
    kiem(f"BR-53 {ngay_chot}: tổng theo xã kể cả chưa rõ địa bàn = số người", sum(d["duy_nhat"].values()) == d["tong_duy_nhat"])
het = [r for r in D.bang["e04_dien_doi_tuong"] if r["hieu_luc_den"] and "2026-07-31" < r["hieu_luc_den"] < "2026-10-31"]
if het:
    r = het[0]
    co_dien_khac = any(P.hieu_luc(x, P.NGAY_CHOT) for x in D.dien[r["ma_nguoi"]])
    kiem(f"BR-51: diện {r['ma_dien_dt']} hết hiệu lực {r['hieu_luc_den']} không còn được tính ở ngày chốt 31/10",
         co_dien_khac or r["ma_nguoi"] not in {m for m, ds in D.dien.items() if any(P.hieu_luc(x, P.NGAY_CHOT) for x in ds)})

# 4. DB05: nguồn chi trả chưa đánh giá, không ra 0%
ct = next(n for n in KQ["nguon"] if n["ma"] == "NGUON-CT")
kiem("BR-53 DB05: nguồn chi trả hiện \"chưa đánh giá\" thay vì 0%", ct["ghep_tu"] is None and ct["ghi_chu"])
kiem("DB05: mọi tỷ lệ phép đo trong khoảng 0–100%", all(m["ty_le"] is None or 0 <= m["ty_le"] <= 100 for m in KQ["phep_do"]),
     [m["ten"] for m in KQ["phep_do"] if m["ty_le"] and m["ty_le"] > 100])

# 5. Thu hồi: tổng = các cảnh báo chi thừa trừ BR-41 và cảnh báo tài khoản
mong = sum(c["so_tien"] for c in KQ["canh_bao"] if c["chieu"] == "Thừa" and c["quy_tac"] != "BR-41" and c["loai_doi_tuong"] != "Tài khoản")
kiem(f"Thu hồi: tổng {KQ['thu_hoi']['tong']:,} = cảnh báo chi thừa đủ điều kiện {mong:,}", KQ["thu_hoi"]["tong"] == mong)
kiem("Thu hồi: tổng theo xã bằng tổng danh sách", sum(x["tien"] for x in KQ["thu_hoi"]["theo_xa"].values()) == KQ["thu_hoi"]["tong"])
kiem("Thu hồi: chỉ cảnh báo \"Xác nhận đúng\" mới là đề nghị thu hồi",
     all((c["buoc"] == "Đề nghị thu hồi") == (c["trang_thai"] == "Xác nhận đúng") for c in KQ["thu_hoi"]["danh_sach"]))

# 6. VD2 theo xã: chi CD01–CD03 kỳ 10/2026 của POC so với cơ sở E36
co_so = defaultdict(int)
for (lt, mdt, cd, ky), r in P.doi_soat(D)[1].items():
    if ky == "2026-10" and cd in ("CD01", "CD02", "CD03") and r["muc_dang_huong"]:
        co_so[D.xa_doi_tuong(lt, mdt)] += int(r["muc_dang_huong"])
for v in KQ["vi_mo"]["vd2_xa"]:
    kiem(f"VD2 {v['xa']}: cơ sở E36 {v['co_so']:,} = POC tính lại {co_so[v['xa']]:,}", v["co_so"] == co_so[v["xa"]])

# 7. Hồ sơ 360: quan hệ hai chiều
q = D.bang["e06_quan_he"][0]
kiem("UC04: quan hệ E06 hiện ở hồ sơ cả hai người",
     any(r["ma"] == q["ma_nguoi_2"] for r in KQ["ho_so"][q["ma_nguoi_1"]]["quan_he"]) and any(r["ma"] == q["ma_nguoi_1"] for r in KQ["ho_so"][q["ma_nguoi_2"]]["quan_he"]))
kiem("UC04: số định danh hiển thị đã che, chỉ còn 4 số cuối", all(h["so_dd_che"].startswith("••") for h in KQ["ho_so"].values() if h["so_dd_che"]))

# 8. Trang HTML đã nhúng dữ liệu
html = P.OUT_HTML.read_text(encoding="utf-8") if P.OUT_HTML.exists() else ""
kiem("HTML: đã nhúng dữ liệu (chạy pipeline trước)", "/*__POC_DATA__*/" not in html and '"canh_bao"' in html)

print(f"\n{'Tất cả đạt' if not KQ_LOI else str(len(KQ_LOI)) + ' kiểm tra không đạt'}")
sys.exit(1 if KQ_LOI else 0)
