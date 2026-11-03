#!/usr/bin/env python3
"""POC project019: chạy các bước xử lý của module trên bộ DỮ LIỆU GIẢ 019.

Đầu vào: output/project019_019_du_lieu_mockup_csv/ (30 bảng, coi như dữ liệu đã nạp từ 7 nguồn).
Đầu ra:
- output/project019_020_poc_ket_qua.json: số liệu của 7 màn hình.
- output/project019_020_poc.html: giao diện tĩnh, nhúng sẵn JSON, mở trực tiếp bằng trình duyệt.

Các bước (mã theo checklist 013):
  1. Nguồn và đồng bộ (T02), ghép định danh (T06), chất lượng dữ liệu (UC01, DB05)
  2. Tổng quan theo ngày chốt (UC02, DB01; BR-50, BR-51, BR-53)
  3. Hồ sơ 360° (UC04)
  4. Đối soát đáng hưởng với thực chi (UC06, UC07, UC09, UC11; BR-41, BR-07, BR-52), tính lại độc lập
     từ E31, E05, E07 rồi đối chiếu với E16 của bộ mockup
  5. Danh sách đối soát và thu hồi (đầu ra 2), đề xuất chính sách (đầu ra 1)
  6. Chỉ tiêu theo xã và dự báo chi 1 đến 5 năm theo già hóa (đầu ra 3; UC12, UC14, UC18)

Mọi giả định của POC ghi trong khóa "gia_dinh" của JSON và hiện trên giao diện.
Chạy: python3 -I work/project019_020_poc_pipeline.py
"""
import csv
import json
import sys
from collections import Counter, defaultdict
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "output" / "project019_019_du_lieu_mockup_csv"
OUT_JSON = ROOT / "output" / "project019_020_poc_ket_qua.json"
OUT_HTML = ROOT / "output" / "project019_020_poc.html"
TEMPLATE = ROOT / "work" / "project019_020_poc_giao_dien.html"

NGAY_CHOT = date(2026, 10, 31)
CAC_NGAY_CHOT = [date(2026, 7, 31), date(2026, 8, 31), date(2026, 9, 30), NGAY_CHOT]
KY = ["2026-07", "2026-08", "2026-09", "2026-10"]
KY_CHUYEN = "2026-10"
NGUONG_TK_NGUOI = 3
CD_NCC = {"CD04", "CD05", "CD06", "CD07", "CD08", "CD10", "CD11"}
MOT_LAN = {"CD09", "CD10", "CD11"}
NHOM = {"NCC": "Người có công và thân nhân", "TGXH": "Trợ giúp xã hội hằng tháng", "HTXH": "Trợ cấp hưu trí xã hội"}
UC_THEO_LOAI = {"Trùng chế độ": "UC06", "Bỏ sót phần cộng thêm": "UC06", "Tài khoản nhận bất thường": "UC08",
                "Bỏ sót": "UC09", "Chuyển đổi chế độ": "UC11", "Chưa có thẻ BHYT": "UC16"}

GIA_DINH = [
    "Người đã mất trước ngày chốt không được đếm ở DB01 dù diện chưa ghi ngày kết thúc.",
    "Người có trạng thái sống \"chưa xác định\" vẫn được đếm ở DB01, tách riêng một số đếm (BR-52).",
    "Một người có nhiều nơi cư trú hiệu lực thì lấy bản ghi bắt đầu muộn nhất; mã xã cũ được đổi qua bảng ánh xạ E13.",
    "Quan hệ \"chăm sóc\" chỉ tính loại quan hệ có chữ \"chăm sóc\"; \"phụng dưỡng\" không thay thế được (Q46).",
    "Dự báo: mức hiện hành giữ nguyên; người tròn 75 tuổi, chưa hưởng TGXH, hưu trí XH hay lương hưu thì vào hưu trí XH; "
    "người hưởng TGXH tuổi 60–75 khi tròn 75 lên hệ số 2,0; giảm do tử vong theo tỷ lệ chết thô quan sát kỳ 07–10/2026.",
    "Khoảng dao động của dự báo: tỷ lệ tử vong ±50%.",
]


# ---------------------------------------------------------------- đọc dữ liệu và tiện ích


def doc(ten):
    with open(SRC / f"{ten}.csv", encoding="utf-8-sig", newline="") as f:
        return [{k: (v if v != "" else None) for k, v in r.items()} for r in csv.DictReader(f)]


def ngay(s):
    return date.fromisoformat(s[:10]) if s else None


def ky_dau(ky):
    y, m = map(int, ky.split("-"))
    return date(y, m, 1)


def ky_cuoi(ky):
    d = ky_dau(ky)
    return date(d.year + d.month // 12, d.month % 12 + 1, 1) - timedelta(days=1)


def thang(d):
    return d.strftime("%Y-%m") if d else None


def hieu_luc(r, d, tu="hieu_luc_tu", den="hieu_luc_den"):
    return (ngay(r[tu]) or date.min) <= d and (r[den] is None or ngay(r[den]) >= d)


def tuoi(dob, d):
    return d.year - dob.year - ((d.month, d.day) < (dob.month, dob.day))


def so(x):
    return int(float(x)) if x is not None else None


def che_so(s):
    return "•••••••• " + s[-4:] if s else None


class DuLieu:
    def __init__(self):
        t = self.bang = {p.stem: doc(p.stem) for p in sorted(SRC.glob("*.csv"))}
        self.nguoi = {p["ma_nguoi"]: p for p in t["e01_nguoi"]}
        self.ho = {h["ma_ho"]: h for h in t["e02_ho"]}
        self.xa = {x["ma_dia_ban"]: x["ten"] for x in t["e13_dia_ban"] if x["cap"] == "Xã"}
        self.anh_xa = {a["ma_cu"]: a["ma_moi"] for a in t["e13_anh_xa_dia_ban"]}
        self.che_do = {c["ma_che_do"]: c for c in t["e20_che_do"]}
        self.huong = t["e05_huong_che_do"]
        self.huong_ma = {h["ma_huong"]: h for h in self.huong}
        self.chi = t["e07_chi_tra"]
        self.su_kien = t["e15_su_kien"]
        self.tv_theo_nguoi = defaultdict(list)
        self.tv_theo_ho = defaultdict(list)
        for m in t["e03_thanh_vien_ho"]:
            self.tv_theo_nguoi[m["ma_nguoi"]].append(m)
            self.tv_theo_ho[m["ma_ho"]].append(m)
        self.cu_tru = defaultdict(list)
        for c in t["e12_cu_tru"]:
            self.cu_tru[c["ma_nguoi"]].append(c)
        self.dien = defaultdict(list)
        for d in t["e04_dien_doi_tuong"]:
            self.dien[d["ma_nguoi"]].append(d)

    def tham_so(self, ma, d):
        ds = [p for p in self.bang["e22_tham_so_chinh_sach"] if p["ma_tham_so"] == ma and hieu_luc(p, d, "ap_dung_tu", "ap_dung_den")]
        return float(max(ds, key=lambda p: p["ap_dung_tu"] or "")["gia_tri"]) if ds else None

    def con_song(self, ma, d):
        """True/False; None nếu trạng thái sống chưa xác định (BR-52)."""
        p = self.nguoi[ma]
        if p["trang_thai_song"] == "Chưa xác định":
            return None
        return p["ngay_mat"] is None or ngay(p["ngay_mat"]) > d

    def song_trong_ky(self, ma, ky):
        p = self.nguoi[ma]
        if p["trang_thai_song"] == "Chưa xác định":
            return None
        return p["ngay_mat"] is None or ngay(p["ngay_mat"]) >= ky_dau(ky)

    def ho_luc(self, ma, d):
        ds = [m for m in self.tv_theo_nguoi.get(ma, []) if hieu_luc(m, d, "tu_ngay", "den_ngay")]
        return ds[0]["ma_ho"] if ds else None

    def xa_nguoi(self, ma, d):
        ds = [c for c in self.cu_tru.get(ma, []) if hieu_luc(c, d, "tu_ngay", "den_ngay")]
        if not ds:
            return None
        m = max(ds, key=lambda c: c["tu_ngay"] or "")["ma_dia_ban"]
        m = self.anh_xa.get(m, m)
        return m if m in self.xa else None

    def xa_doi_tuong(self, loai, ma):
        """Xã của đối tượng cảnh báo: hộ tại ngày chốt, nếu không có thì hộ gần nhất, rồi nơi cư trú gần nhất."""
        if loai == "Hộ":
            return self.ho[ma]["ma_dia_ban"]
        if loai != "Người":
            return None
        h = self.ho_luc(ma, NGAY_CHOT)
        if not h and self.tv_theo_nguoi.get(ma):
            h = max(self.tv_theo_nguoi[ma], key=lambda m: m["tu_ngay"] or "")["ma_ho"]
        if h:
            return self.ho[h]["ma_dia_ban"]
        ds = self.cu_tru.get(ma)
        return self.anh_xa.get(ds[-1]["ma_dia_ban"], ds[-1]["ma_dia_ban"]) if ds else None


# ---------------------------------------------------------------- 1. nguồn, ghép định danh, chất lượng


def nguon_va_chat_luong(D):
    bgn = D.bang["e17_ban_ghi_nguon"]
    lan = {l["ma_nguon"]: l for l in D.bang["e17_lan_dong_bo"]}
    theo_nguon = defaultdict(list)
    for b in bgn:
        theo_nguon[b["ma_nguon"]].append(b)
    nguon = []
    for n in D.bang["e17_nguon"]:
        rows = theo_nguon.get(n["ma_nguon"], [])
        l = lan.get(n["ma_nguon"])
        tt = Counter(b["trang_thai_ghep"] for b in rows)
        khoa = Counter(b["khoa_nguon"] for b in rows)
        nguon.append(dict(
            ma=n["ma_nguon"], ten=n["ten"], co_quan=n["co_quan"],
            kieu=l["kieu"] if l else None, thoi_diem=l["thoi_diem"] if l else None,
            so_ban_ghi=so(l["so_ban_ghi"]) if l else None, so_loi=so(l["so_loi"]) if l else None,
            ghep_tu=tt["Đã ghép"] if rows else None, ghep_mau=len(rows) if rows else None,
            ghep_mo=tt["Ghép mờ chờ duyệt"], khong_ghep=tt["Không ghép được"],
            trung_khoa=sum(v - 1 for v in khoa.values() if v > 1) if rows else None,
            ghi_chu=None if rows else "Chưa có bản ghi nguồn đã qua bước ghép (T06 chưa chạy cho nguồn này)"))
    loi_ghep = [dict(nguon=b["ma_nguon"], khoa=b["khoa_nguon"][:4] + "••" + b["khoa_nguon"][-2:], trang_thai=b["trang_thai_ghep"],
                     phuong_phap=b["phuong_phap_ghep"], tin_cay=float(b["do_tin_cay"])) for b in bgn if b["trang_thai_ghep"] != "Đã ghép"]

    ng = list(D.nguoi.values())
    def do(nhom, ten, tu, mau, thuc_the, ghi_chu=None):
        return dict(nhom=nhom, ten=ten, tu=tu, mau=mau, ty_le=round(100 * tu / mau, 1) if mau else None, thuc_the=thuc_the, ghi_chu=ghi_chu)
    e12 = D.bang["e12_cu_tru"]
    dbn = {d["ma_nguoi"] for d in D.bang["e04_dien_doi_tuong"] if "DBN" in d["ma_dien"]}
    cham_soc = set()
    for q in D.bang["e06_quan_he"]:
        if "chăm sóc" in q["loai"].lower():
            cham_soc |= {q["ma_nguoi_1"], q["ma_nguoi_2"]}
    da_mat = {p["ma_nguoi"] for p in ng if p["trang_thai_song"] == "Đã mất"}
    van_huong = {h["ma_nguoi_doi_tuong"] for h in D.huong if h["trang_thai"] == "Đang hưởng" and h["ma_nguoi_doi_tuong"] in da_mat}
    phep_do = [
        do("Đủ", "Người có ngày sinh", sum(1 for p in ng if p["ngay_sinh"]), len(ng), "E01"),
        do("Đủ", "Hưởng chế độ có người nhận tiền", sum(1 for h in D.huong if h["ma_nguoi_nhan"]), len(D.huong), "E05"),
        do("Đúng", "Số định danh đủ 12 chữ số", sum(1 for p in ng if (p["so_dinh_danh_gia"] or "").isdigit() and len(p["so_dinh_danh_gia"]) == 12), len(ng), "E01"),
        do("Đúng", "Mã địa bàn cư trú ánh xạ được", sum(1 for c in e12 if D.anh_xa.get(c["ma_dia_ban"], c["ma_dia_ban"]) in D.xa), len(e12), "E12, E13"),
        do("Đúng", "Mã chế độ có trong danh mục", sum(1 for h in D.huong if h["ma_che_do"] in D.che_do), len(D.huong), "E05, E20"),
        do("Sạch", "Bản ghi nguồn ghép được vào NGƯỜI hoặc HỘ", sum(1 for b in bgn if b["trang_thai_ghep"] == "Đã ghép"), len(bgn), "E17", "Không gồm nguồn chi trả (chưa đánh giá)"),
        do("Sống", "Người đã mất nhưng còn hưởng \"Đang hưởng\"", len(van_huong), len(da_mat), "E01, E05", "Đếm người; càng thấp càng tốt"),
        do("Sống", "Người có trạng thái sống chưa xác định", sum(1 for p in ng if p["trang_thai_song"] == "Chưa xác định"), len(ng), "E01", "BR-52"),
        do("Sống", "Người đã mất vẫn là thành viên hộ", sum(1 for m in da_mat if D.ho_luc(m, NGAY_CHOT)), len(da_mat), "E01, E03",
           "Càng thấp càng tốt; nguồn dân cư chưa cắt khẩu"),
        do("Quan hệ", "Người thuộc một hộ tại ngày chốt",
           sum(1 for p in ng if D.con_song(p["ma_nguoi"], NGAY_CHOT) is not False and D.ho_luc(p["ma_nguoi"], NGAY_CHOT)),
           sum(1 for p in ng if D.con_song(p["ma_nguoi"], NGAY_CHOT) is not False), "E03", "Mẫu số: người chưa mất"),
        do("Quan hệ", "NKT đặc biệt nặng có quan hệ chăm sóc", len(dbn & cham_soc), len(dbn), "E04, E06", "Q46"),
    ]
    return nguon, loi_ghep, phep_do, sum(1 for b in bgn if b["trang_thai_ghep"] != "Đã ghép" and b["loai_don_vi"] == "Cá nhân")


# ---------------------------------------------------------------- 2. DB01 theo ngày chốt


def tong_quan(D, ho_so_chua_xd):
    out = {}
    for d in CAC_NGAY_CHOT:
        nhom_xa = defaultdict(Counter)
        duy_nhat = Counter()
        chua_xd_song = 0
        tuoi_nhom = Counter()
        for ma, ds in D.dien.items():
            if D.con_song(ma, d) is False:
                continue
            hl = [x for x in ds if hieu_luc(x, d)]
            if not hl:
                continue
            xa = D.xa_nguoi(ma, d) or "CHUA_RO"
            for nh in {x["ma_dien"].split("-")[0] for x in hl}:
                nhom_xa[nh][xa] += 1
            duy_nhat[xa] += 1
            if D.con_song(ma, d) is None:
                chua_xd_song += 1
            a = tuoi(ngay(D.nguoi[ma]["ngay_sinh"]), d)
            tuoi_nhom["Dưới 16" if a < 16 else "16–59" if a < 60 else "60–74" if a < 75 else "Từ 75"] += 1
        ho_ds = [h for h in D.ho.values() if any(hieu_luc(m, d, "tu_ngay", "den_ngay") for m in D.tv_theo_ho.get(h["ma_ho"], []))]
        pl = Counter(r["phan_loai"] for r in D.bang["e14_ket_qua_ra_soat_ho"])
        out[d.isoformat()] = dict(
            nhom={nh: dict(ten=NHOM[nh], theo_xa=dict(c), tong=sum(c.values())) for nh, c in sorted(nhom_xa.items())},
            duy_nhat=dict(duy_nhat), tong_duy_nhat=sum(duy_nhat.values()), chua_xd_song=chua_xd_song,
            tuoi=dict(tuoi_nhom), so_ho=len(ho_ds), phan_loai_ho=dict(pl), ho_so_chua_xd_nguoi=ho_so_chua_xd)
    return out


# ---------------------------------------------------------------- 4. đối soát (tính lại độc lập)


def doi_soat(D):
    e31 = {}
    for r in D.bang["e31_dang_huong"]:
        e31[(r["loai_doi_tuong"], r["ma_doi_tuong"], r["ma_che_do"], r["ky"])] = r
    theo_khoa = defaultdict(list)
    for h in D.huong:
        theo_khoa[(h["loai_doi_tuong_huong"], h["ma_doi_tuong_huong"], h["ma_che_do"])].append(h)
    chi_idx = defaultdict(list)  # BR-41: gộp theo kỳ hưởng gốc
    for c in D.chi:
        chi_idx[(c["ma_huong"], c["ky_huong"])].append(c)

    def dang_huong_ky(h, ky):
        return thang(ngay(h["hieu_luc_tu"])) <= ky and (h["hieu_luc_den"] is None or thang(ngay(h["hieu_luc_den"])) >= ky)

    gom = {}

    def ghi(loai, nhom, qt, lt, mdt, cd, ky, tien, mh, chieu=""):
        g = gom.setdefault((loai, lt, mdt, cd), dict(loai=loai, nhom=nhom, qt=qt, lt=lt, mdt=mdt, cd=cd, ky=[], tien=0, huong=set(), chieu=chieu))
        g["ky"].append(ky)
        g["tien"] += tien
        g["huong"] |= set(mh)

    def phan_loai(k, ky, act, dang, dung, chi, dh):
        lt, mdt, cd = k
        if not act:
            return "Bỏ sót", "BỎ SÓT", dh["ma_quy_tac"].split(";")[0], dung
        doi = lt == "Người" and any(s["ma_nguoi"] == mdt and s["loai"].startswith("Đủ") and ngay(s["ngay_xay_ra"]) <= ky_cuoi(ky) for s in D.su_kien)
        qt_doi = "BR-22" if cd == "CD07" else "BR-05"
        if dung == 0:
            if lt == "Hộ":
                return "Chi khi người được chăm sóc đã mất", "CHI SAI", "BR-09", chi
            if D.song_trong_ky(mdt, ky) is False:
                return "Chi sau ngày mất", "CHI SAI", "BR-28" if cd in CD_NCC else "BR-05; BR-08", chi
            if doi:
                return "Chuyển đổi chế độ", "CHUYỂN ĐỔI", qt_doi, chi
            return "Chi khi không đủ điều kiện", "CHI SAI", {"CD03": "KT-HTXH", "CD09": "BR-10", "CD10": "BR-27"}.get(cd, "BR-08"), chi
        if len(act) > 1:
            if len({h["ma_dia_ban_chi_tra"] for h in act}) > 1:
                return "Trùng nơi chi", "CHI SAI", "BR-06", chi - dung
            return "Trùng chế độ", "CHI SAI", "BR-02", chi - dung
        if dang < dung and "BR-03" in (dh["ma_quy_tac"] or "") and not any("K4" in (h["ma_dien_theo_nguon"] or "") for h in act):
            return "Bỏ sót phần cộng thêm", "BỎ SÓT", "BR-03", dung - dang
        if doi:
            return "Chuyển đổi chế độ", "CHUYỂN ĐỔI", qt_doi, abs(dang - dung)
        return "Sai mức", "CHI SAI", "BR-20" if cd in CD_NCC else "BR-13", abs(dang - dung)

    for k in sorted({x[:3] for x in e31} | set(theo_khoa)):
        for ky in KY:
            dh = e31.get(k + (ky,))
            act = [h for h in theo_khoa.get(k, []) if dang_huong_ky(h, ky)]
            chi = sum(so(c["so_thuc_chi"]) for h in act for c in chi_idx[(h["ma_huong"], ky)])
            mh = [h["ma_huong"] for h in act]
            if dh and dh["muc_dang_huong"] is None:
                if act:
                    ghi("Chưa đủ dữ liệu", "KHÁC", "BR-52", *k, ky, chi, mh)
                continue
            dang, dung = sum(so(h["muc_theo_qd"]) for h in act), so(dh["muc_dang_huong"]) if dh else 0
            if dang == dung:
                continue
            loai, nhom, qt, tien = phan_loai(k, ky, act, dang, dung, chi, dh)
            ghi(loai, nhom, qt, *k, ky, tien, mh, "Thừa" if dang > dung else "Thiếu")
    for h in D.huong:  # BR-41
        if h["hinh_thuc"] != "Tiền hằng tháng":
            continue
        for ky in KY:
            dong = chi_idx[(h["ma_huong"], ky)]
            if not dong or any(c["ket_qua"] != "Đã chi" for c in dong):
                continue
            da_chi, qd = sum(so(c["so_thuc_chi"]) for c in dong), so(h["muc_theo_qd"])
            if da_chi == qd:
                continue
            co_tl = any(c["loai_khoan"] == "Truy lĩnh" for c in dong)
            loai = ("Truy lĩnh thiếu" if ky < KY_CHUYEN else "Chi lệch quyết định") if da_chi < qd else ("Truy lĩnh thừa" if co_tl else "Chi lệch quyết định")
            ghi(loai, "CHI SAI", "BR-41", h["loai_doi_tuong_huong"], h["ma_doi_tuong_huong"], h["ma_che_do"], ky, abs(da_chi - qd), [h["ma_huong"]],
                "Thiếu" if da_chi < qd else "Thừa")
    nguong = D.tham_so("P-TAM-DUNG-THANG", NGAY_CHOT)
    for h in D.huong:  # BR-07
        khong = sorted({c["ky_huong"] for c in D.chi if c["ma_huong"] == h["ma_huong"] and c["ket_qua"] == "Không nhận"})
        if len(khong) >= nguong and h["trang_thai"] == "Đang hưởng":
            for ky in khong:
                ghi("Cần tạm dừng", "CHI SAI", "BR-07", h["loai_doi_tuong_huong"], h["ma_doi_tuong_huong"], h["ma_che_do"], ky, so(h["muc_theo_qd"]), [h["ma_huong"]])
    vao_tk = defaultdict(list)  # KT-TK
    for c in D.chi:
        if c["ma_tai_khoan"]:
            vao_tk[c["ma_tai_khoan"]].append(c)
    for tk, ds in vao_tk.items():
        dt = {D.huong_ma[c["ma_huong"]]["ma_doi_tuong_huong"] for c in ds}
        so_ho = {D.ho_luc(d, NGAY_CHOT) if d in D.nguoi else d for d in dt}
        if len(dt) >= NGUONG_TK_NGUOI and len(so_ho) >= 2:
            for c in ds:
                ghi("Tài khoản nhận bất thường", "CHI SAI", "KT-TK", "Tài khoản", tk, "", c["ky_chi"], so(c["so_thuc_chi"]), [c["ma_huong"]])
    co_the = {b["ma_nguoi"] for b in D.bang["e33_huong_bhxh_bhyt"] if b["loai"] == "Thẻ BHYT" and (b["den_ngay"] is None or ngay(b["den_ngay"]) >= NGAY_CHOT)}
    for (lt, mdt, cd, ky), r in e31.items():  # KT-BHYT
        if ky == KY[-1] and lt == "Người" and cd in ("CD01", "CD03", "CD04", "CD07") and so(r["muc_dang_huong"]) and mdt not in co_the:
            ghi("Chưa có thẻ BHYT", "KHÁC", "KT-BHYT", lt, mdt, cd, ky, 0, [])

    e16 = {(c["loai"], c["loai_doi_tuong"], c["ma_doi_tuong"], c["ma_che_do"] or ""): c for c in D.bang["e16_canh_bao"]}
    quy_tac = {q["ma_quy_tac"]: q["ten"] for q in D.bang["e23_quy_tac"]}
    out = []
    for i, g in enumerate(sorted(gom.values(), key=lambda g: (g["nhom"], g["loai"], g["mdt"])), 1):
        ky = sorted(set(g["ky"]))
        loai = g["loai"]
        uc = ("UC23" if g["cd"] in ("CD07", "CD08", "CD11") else "UC11" if g["cd"] in ("CD09", "CD10") else "UC10" if g["cd"] == "CD02" else "UC09") \
            if loai == "Bỏ sót" else UC_THEO_LOAI.get(loai, "UC07")
        goc = e16.get((loai, g["lt"], g["mdt"], g["cd"]))
        sk = [s for s in D.su_kien if s["ma_nguoi"] == g["mdt"]]
        out.append(dict(
            ma=f"POC-{i:03d}", ma_e16=goc["ma_canh_bao"] if goc else None, ma_tc=goc["ma_tc_mockup"] if goc else None,
            nhom=g["nhom"], loai=loai, chieu=g["chieu"] or "Chưa xác định", quy_tac=g["qt"],
            ten_quy_tac="; ".join(quy_tac.get(q.strip(), "") for q in g["qt"].split(";")),
            loai_doi_tuong=g["lt"], ma_doi_tuong=g["mdt"], che_do=g["cd"], ten_che_do=D.che_do[g["cd"]]["ten"] if g["cd"] else "Nhiều chế độ",
            ky_tu=ky[0], ky_den=ky[-1], so_ky=len(ky), so_tien=g["tien"], huong=sorted(g["huong"]),
            su_kien=[f"{s['ma_su_kien']} · {s['loai']}, {ngay(s['ngay_xay_ra']).strftime('%d/%m/%Y')}" for s in sk],
            xa=D.xa_doi_tuong(g["lt"], g["mdt"]), uc=uc, vai_tro="VT06" if uc in ("UC06", "UC07", "UC08") else "VT05",
            trang_thai=goc["trang_thai"] if goc else "Mới", ket_qua_xu_ly=goc["ket_qua_xu_ly"] if goc else None))
    return out, e31


# ---------------------------------------------------------------- 3. hồ sơ 360°


def ho_so(D, canh_bao):
    ho_ten = {m: p["ho_ten_gia"] for m, p in D.nguoi.items()}
    gd = defaultdict(list)
    for g in D.bang["e11_ket_qua_giam_dinh"]:
        gd[g["ma_nguoi"]].append(f"{g['loai_chi_so']}: {g['gia_tri']} ({g['ngay_giam_dinh']})")
    qh = defaultdict(list)
    for q in D.bang["e06_quan_he"]:
        qh[q["ma_nguoi_1"]].append(dict(ma=q["ma_nguoi_2"], ten=ho_ten.get(q["ma_nguoi_2"]), loai=q["loai"], chieu="Người này là", nguon=q["nguon"]))
        qh[q["ma_nguoi_2"]].append(dict(ma=q["ma_nguoi_1"], ten=ho_ten.get(q["ma_nguoi_1"]), loai=q["loai"], chieu="Quan hệ với", nguon=q["nguon"]))
    chi_cuoi = {}
    for c in D.chi:
        if c["ket_qua"] == "Đã chi" and (c["ma_huong"] not in chi_cuoi or c["ky_chi"] > chi_cuoi[c["ma_huong"]][0]):
            chi_cuoi[c["ma_huong"]] = (c["ky_chi"], so(c["so_thuc_chi"]))
    rs = {r["ma_ho"]: r for r in D.bang["e14_ket_qua_ra_soat_ho"]}
    hc = {r["ma_ho"]: r for r in D.bang["e35_hoan_canh_ho"]}
    bgn = defaultdict(list)
    for b in D.bang["e17_ban_ghi_nguon"]:
        if b["ma_nguoi"]:
            bgn[b["ma_nguoi"]].append(dict(nguon=b["ma_nguon"], phuong_phap=b["phuong_phap_ghep"], tin_cay=float(b["do_tin_cay"]), trang_thai=b["trang_thai_ghep"]))
    bhyt = {b["ma_nguoi"] for b in D.bang["e33_huong_bhxh_bhyt"] if b["loai"] == "Thẻ BHYT" and (b["den_ngay"] is None or ngay(b["den_ngay"]) >= NGAY_CHOT)}
    cb_theo = defaultdict(list)
    for c in canh_bao:
        cb_theo[c["ma_doi_tuong"]].append(c["ma"])
    out = {}
    for ma, p in D.nguoi.items():
        h_ma = D.ho_luc(ma, NGAY_CHOT)
        tv = [m for m in D.tv_theo_ho.get(h_ma, []) if hieu_luc(m, NGAY_CHOT, "tu_ngay", "den_ngay")] if h_ma else []
        vai = next((m["quan_he_chu_ho"] for m in tv if m["ma_nguoi"] == ma), None)
        huong = []
        for h in D.huong:
            vt = []
            if h["ma_nguoi_doi_tuong"] == ma:
                vt.append("đối tượng")
            if h["ma_nguoi_nhan"] == ma:
                vt.append("người nhận tiền")
            if h["loai_doi_tuong_huong"] == "Hộ" and h["ma_doi_tuong_huong"] == h_ma and not vt:
                vt.append("thành viên hộ được hưởng")
            if vt:
                cc = chi_cuoi.get(h["ma_huong"])
                huong.append(dict(che_do=D.che_do[h["ma_che_do"]]["ten"], vai_tro=", ".join(vt), muc=so(h["muc_theo_qd"]), he_so=h["he_so"],
                                  trang_thai=h["trang_thai"], doi_tuong=h["ma_nguoi_doi_tuong"], nhan=h["ma_nguoi_nhan"],
                                  ky_chi=cc[0] if cc else None, da_chi=cc[1] if cc else None))
        dob = ngay(p["ngay_sinh"])
        xa = D.xa_nguoi(ma, NGAY_CHOT) or (D.ho[h_ma]["ma_dia_ban"] if h_ma else None)
        out[ma] = dict(
            ma=ma, ten=p["ho_ten_gia"], so_dd=p["so_dinh_danh_gia"], so_dd_che=che_so(p["so_dinh_danh_gia"]),
            gioi=p["gioi_tinh"], nam_sinh=dob.year, tuoi=tuoi(dob, NGAY_CHOT if not p["ngay_mat"] else ngay(p["ngay_mat"])),
            song=p["trang_thai_song"], ngay_mat=p["ngay_mat"], xa=D.xa.get(xa, "Chưa rõ địa bàn"),
            dien=[dict(ten=d["ten_dien"], ma=d["ma_dien"], tu=d["hieu_luc_tu"], den=d["hieu_luc_den"], hieu_luc=hieu_luc(d, NGAY_CHOT), nguon=d["nguon"]) for d in D.dien.get(ma, [])],
            giam_dinh=gd.get(ma, []), huong=huong, quan_he=qh.get(ma, []),
            ho=dict(ma=h_ma, vai_tro=vai, so_tv=len(tv), phan_loai=rs.get(h_ma, {}).get("phan_loai"), nha_o=hc.get(h_ma, {}).get("nha_o")) if h_ma else None,
            canh_bao=cb_theo.get(ma, []) + (cb_theo.get(h_ma, []) if h_ma else []), nguon=bgn.get(ma, []), bhyt=ma in bhyt)
    return out


# ---------------------------------------------------------------- 5. đầu ra 1 và 2


def thu_hoi(D, canh_bao):
    ds, rieng, trung = [], [], []
    for c in canh_bao:
        if c["loai"] in ("Trùng nơi chi", "Trùng chế độ"):
            trung.append(dict(ma=c["ma"], noi_dung=c["loai"], quy_tac=c["quy_tac"], so_tien=c["so_tien"], xa=c["xa"]))
        if c["chieu"] != "Thừa" and c["loai_doi_tuong"] != "Tài khoản":
            continue
        if c["quy_tac"] == "BR-41" or c["loai_doi_tuong"] == "Tài khoản":
            rieng.append(dict(ma=c["ma"], loai=c["loai"], so_tien=c["so_tien"],
                              ly_do="Có thể do cách ghi truy lĩnh, chờ Q39" if c["quy_tac"] == "BR-41" else "Cần xác minh chủ tài khoản, chưa rõ địa bàn"))
            continue
        buoc = "Đề nghị thu hồi" if c["trang_thai"] == "Xác nhận đúng" else "Đang xác minh" if c["trang_thai"] == "Đang xác minh" else "Gửi xã xác minh"
        ds.append(dict(c, buoc=buoc))
    for b in D.bang["e17_ban_ghi_nguon"]:
        if b["trang_thai_ghep"] == "Ghép mờ chờ duyệt":
            trung.append(dict(ma=b["ma_bgn"], noi_dung=f"Bản ghi {b['ma_nguon']} có thể trùng một người đã có ({b['phuong_phap_ghep']})",
                              quy_tac="T06", so_tien=0, xa=None, tin_cay=float(b["do_tin_cay"])))
    theo_xa = {}
    for c in ds:
        x = theo_xa.setdefault(c["xa"] or "CHUA_RO", dict(so=0, tien=0))
        x["so"] += 1
        x["tien"] += c["so_tien"]
    return dict(danh_sach=ds, theo_xa=theo_xa, tong=sum(c["so_tien"] for c in ds),
                de_nghi_ngay=sum(c["so_tien"] for c in ds if c["buoc"] == "Đề nghị thu hồi"), de_rieng=rieng, trung_lap=trung)


def de_xuat(D, canh_bao, e31):
    def dong_nguoi(ma, d):
        p = D.nguoi[ma]
        h = D.ho_luc(ma, d)
        tv = [m for m in D.tv_theo_ho.get(h, []) if hieu_luc(m, d, "tu_ngay", "den_ngay")] if h else []
        return dict(ma=ma, ten=p["ho_ten_gia"], tuoi=tuoi(ngay(p["ngay_sinh"]), d), xa=D.xa.get(D.xa_nguoi(ma, d) or "", "Chưa rõ"),
                    so_tv_ho=len(tv), ma_ho=h)
    qh = defaultdict(set)
    for q in D.bang["e06_quan_he"]:
        qh[q["ma_nguoi_1"]].add(q["loai"])
        qh[q["ma_nguoi_2"]].add(q["loai"])
    ty_le = {g["ma_nguoi"]: so(g["gia_tri"]) for g in D.bang["e11_ket_qua_giam_dinh"] if "Tỷ lệ" in g["loai_chi_so"]}
    muc_pv = D.tham_so("NCC-PL1-54", NGAY_CHOT)
    me, tbb = [], []
    for ma, ds in D.dien.items():
        if D.con_song(ma, NGAY_CHOT) is False:
            continue
        hl = [x for x in ds if hieu_luc(x, NGAY_CHOT)]
        ma_dien = {x["ma_dien"] for x in hl}
        if "NCC-BMVNAH" in ma_dien:
            r = dong_nguoi(ma, NGAY_CHOT)
            r["co_phung_duong"] = any("Phụng dưỡng" in l or "phục vụ" in l for l in qh.get(ma, ()))
            me.append(r)
        if ma_dien & {"NCC-CDHH", "NCC-TB", "NCC-BB"}:
            r = dong_nguoi(ma, NGAY_CHOT)
            r["dien"] = next(x["ten_dien"] for x in hl if x["ma_dien"] in ("NCC-CDHH", "NCC-TB", "NCC-BB"))
            r["ty_le"] = ty_le.get(ma)
            r["co_nguoi_phuc_vu"] = "Người phục vụ NCC" in qh.get(ma, ())
            r["de_xuat"] = "Trợ cấp người phục vụ" if (r["ty_le"] or 0) >= 81 and not r["co_nguoi_phuc_vu"] else "Điều dưỡng, thăm hỏi"
            r["muc_thang"] = int(muc_pv) if r["de_xuat"] == "Trợ cấp người phục vụ" else 0
            tbb.append(r)
    bo_sot = []
    for c in canh_bao:
        if c["nhom"] != "BỎ SÓT":
            continue
        r10 = e31.get((c["loai_doi_tuong"], c["ma_doi_tuong"], c["che_do"], KY[-1]))
        bo_sot.append(dict(ma=c["ma"], ma_doi_tuong=c["ma_doi_tuong"], loai_doi_tuong=c["loai_doi_tuong"], loai=c["loai"], quy_tac=c["quy_tac"],
                           che_do=c["ten_che_do"], xa=D.xa.get(c["xa"] or "", "Chưa rõ"), truy_linh=c["so_tien"],
                           hang_thang=so(r10["muc_dang_huong"]) if r10 and c["che_do"] not in MOT_LAN else 0,
                           mot_lan=c["che_do"] in MOT_LAN))
    nha = []
    for r in D.bang["e35_hoan_canh_ho"]:
        if r["nha_o"] not in ("Nhà tạm", "Bán kiên cố, xuống cấp"):
            continue
        tv = [m["ma_nguoi"] for m in D.tv_theo_ho.get(r["ma_ho"], []) if hieu_luc(m, NGAY_CHOT, "tu_ngay", "den_ngay")]
        ncc = [m for m in tv if any(x["ma_dien"].startswith("NCC") and hieu_luc(x, NGAY_CHOT) for x in D.dien.get(m, []))]
        nha.append(dict(ma_ho=r["ma_ho"], xa=D.xa.get(D.ho[r["ma_ho"]]["ma_dia_ban"], "Chưa rõ"), nha_o=r["nha_o"], phu_thuoc=so(r["so_nguoi_phu_thuoc"]),
                        so_tv=len(tv), co_ncc=bool(ncc), nguon_thu_nhap=r["nguon_thu_nhap_chinh"]))
    return dict(me=me, tbb=tbb, bo_sot=bo_sot, nha=nha, muc_phuc_vu=int(muc_pv))


# ---------------------------------------------------------------- 6. chỉ tiêu theo xã và dự báo


def vi_mo(D, e31, db01):
    nam_ky = KY[-1]
    chi_xa = Counter()
    nguoi_huong = defaultdict(set)
    chi_cd = Counter()
    for (lt, mdt, cd, ky), r in e31.items():
        if ky != nam_ky or cd in MOT_LAN or not so(r["muc_dang_huong"]):
            continue
        xa = D.xa_doi_tuong(lt, mdt)
        chi_xa[xa] += so(r["muc_dang_huong"])
        chi_cd[cd] += so(r["muc_dang_huong"])
        nguoi_huong[xa].add(mdt)
    xa_ct = []
    dan = Counter()
    tu75 = Counter()
    for ma in D.nguoi:
        if D.con_song(ma, NGAY_CHOT) is False:
            continue
        x = D.xa_nguoi(ma, NGAY_CHOT)
        if not x:
            continue
        dan[x] += 1
        if tuoi(ngay(D.nguoi[ma]["ngay_sinh"]), NGAY_CHOT) >= 75:
            tu75[x] += 1
    dn = db01[NGAY_CHOT.isoformat()]["duy_nhat"]
    for x, ten in D.xa.items():
        xa_ct.append(dict(ma=x, ten=ten, dan_so=dan[x], co_dien=dn.get(x, 0), mat_do=round(1000 * dn.get(x, 0) / dan[x], 1) if dan[x] else None,
                          ty_le_75=round(100 * tu75[x] / dan[x], 1) if dan[x] else None, chi_thang=chi_xa[x],
                          chi_bq=round(chi_xa[x] / len(nguoi_huong[x])) if nguoi_huong[x] else None))

    # dự báo theo già hóa (giả định ghi trong GIA_DINH)
    muc_ht = D.tham_so("P-HUU-TRI-XH", NGAY_CHOT)
    muc_chuan = D.tham_so("P-MUC-CHUAN-TGXH", NGAY_CHOT)
    co_huong = {h["ma_nguoi_doi_tuong"] for h in D.huong if h["trang_thai"] == "Đang hưởng"} | {k[1] for k, r in e31.items() if k[0] == "Người" and so(r["muc_dang_huong"])}
    luong_huu = {b["ma_nguoi"] for b in D.bang["e33_huong_bhxh_bhyt"] if b["loai"] == "Lương hưu"}
    nct_60_75 = {d["ma_nguoi"] for d in D.bang["e04_dien_doi_tuong"] if d["ma_dien"] == "TGXH-K5A-60DEN75" and hieu_luc(d, NGAY_CHOT)}
    song = [m for m in D.nguoi if D.con_song(m, NGAY_CHOT) is not False]
    chet = sum(1 for s in D.su_kien if s["loai"] == "Chết")
    ty_le_chet = chet / len(song) * 3  # 4 tháng quan sát → năm
    goc = sum(chi_cd.values()) * 12
    tgxh_goc = sum(v for cd, v in chi_cd.items() if cd in ("CD01", "CD02", "CD03")) * 12
    nam, co_so, cao, thap, vd2, moi_75, len_he_so = [], [], [], [], [], [], []
    for n in range(1, 6):
        y = NGAY_CHOT.year + n
        moc = date(y, 12, 31)
        them = [m for m in song if m not in co_huong and m not in luong_huu and tuoi(ngay(D.nguoi[m]["ngay_sinh"]), moc) >= 75]
        len_hs = [m for m in nct_60_75 if tuoi(ngay(D.nguoi[m]["ngay_sinh"]), moc) >= 75]
        tang = len(them) * muc_ht * 12 + len(len_hs) * 0.5 * muc_chuan * 12

        def tinh(tl):
            return round((goc + tang) * (1 - tl) ** n)
        nam.append(y)
        moi_75.append(len(them))
        len_he_so.append(len(len_hs))
        co_so.append(tinh(ty_le_chet))
        cao.append(tinh(ty_le_chet * 0.5))
        thap.append(tinh(ty_le_chet * 1.5))
        vd2.append(round((goc + tang + (tgxh_goc + len(them) * muc_ht * 12 + len(len_hs) * 0.5 * muc_chuan * 12) * (600000 / muc_chuan - 1)) * (1 - ty_le_chet) ** n))
    vd2_xa = []
    for r in D.bang["e36_kich_ban_du_bao"]:
        if r["ma_vd"] == "VD2":
            vd2_xa.append(dict(xa=r["ma_dia_ban"], so_nguoi=so(r["so_nguoi"]), co_so=so(r["kinh_phi_co_so"]), kich_ban=so(r["kinh_phi_kich_ban"]), chenh=so(r["chenh_lech"])))
    return dict(xa=xa_ct, du_bao=dict(nam_goc=NGAY_CHOT.year, goc=goc, nam=nam, co_so=co_so, cao=cao, thap=thap, vd2=vd2,
                                      moi_75=moi_75, len_he_so=len_he_so, ty_le_chet=round(ty_le_chet * 100, 2),
                                      muc_ht=int(muc_ht), muc_chuan=int(muc_chuan)),
                vd2_xa=vd2_xa, chi_che_do={D.che_do[k]["ten"]: v for k, v in chi_cd.items()})


# ---------------------------------------------------------------- chạy


def chay():
    D = DuLieu()
    nguon, loi_ghep, phep_do, chua_xd = nguon_va_chat_luong(D)
    db01 = tong_quan(D, chua_xd)
    canh_bao, e31 = doi_soat(D)
    lan = D.bang["e32_lan_tinh"][0]
    kq = dict(
        tao_luc=NGAY_CHOT.isoformat(), nguon_du_lieu=str(SRC.relative_to(ROOT)), gia_dinh=GIA_DINH,
        xa=D.xa, lan_tinh=dict(ma=lan["ma_lan_tinh"], thoi_diem=lan["thoi_diem"], cau_hinh=lan["phien_ban_cau_hinh"], so_dang_huong=len(D.bang["e31_dang_huong"])),
        nguon=nguon, loi_ghep=loi_ghep, phep_do=phep_do, db01=db01, canh_bao=canh_bao,
        ho_so=ho_so(D, canh_bao), thu_hoi=thu_hoi(D, canh_bao), de_xuat=de_xuat(D, canh_bao, e31), vi_mo=vi_mo(D, e31, db01))
    return D, kq


def main():
    _, kq = chay()
    OUT_JSON.write_text(json.dumps(kq, ensure_ascii=False, indent=1, default=str), encoding="utf-8")
    tpl = TEMPLATE.read_text(encoding="utf-8")
    if "/*__POC_DATA__*/null" not in tpl:
        sys.exit("Mẫu giao diện thiếu chỗ nhúng dữ liệu /*__POC_DATA__*/null")
    du_lieu = json.dumps(kq, ensure_ascii=False, separators=(",", ":"), default=str).replace("</", "<\\/")
    OUT_HTML.write_text(tpl.replace("/*__POC_DATA__*/null", du_lieu), encoding="utf-8")
    khop = sum(1 for c in kq["canh_bao"] if c["ma_e16"])
    print(f"Cảnh báo POC: {len(kq['canh_bao'])} (khớp E16: {khop}/{len(kq['canh_bao'])}); "
          f"DB01 {NGAY_CHOT}: {kq['db01'][NGAY_CHOT.isoformat()]['tong_duy_nhat']} người; thu hồi {kq['thu_hoi']['tong']:,} đ")
    print(f"Ghi: {OUT_JSON.relative_to(ROOT)}, {OUT_HTML.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
