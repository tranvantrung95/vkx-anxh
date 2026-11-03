#!/usr/bin/env python3
"""Profiling một file dữ liệu nguồn (CSV/XLSX) cho BA project019.

Chỉ xuất thống kê và mẫu định dạng đã che. Không in giá trị thô vì dữ liệu chứa thông tin cá nhân.
"""
import argparse
import re
import sys
from pathlib import Path

import pandas as pd

CCCD_RE = re.compile(r"^\d{12}$")
DATE_FORMATS = ("%d/%m/%Y", "%Y-%m-%d")
TOP_PATTERNS = 3


def mask_pattern(value: str) -> str:
    """Đổi chữ số thành 9, chữ cái thành A, rút gọn chuỗi dài: '0791...' -> '<12 chữ số>'."""
    if value.isdigit():
        return f"<{len(value)} chữ số>"
    p = re.sub(r"[A-Za-zÀ-ỹ]", "A", re.sub(r"\d", "9", value))
    return p if len(p) <= 12 else p[:12] + "…"


def load(path: Path, sheet: str | None) -> pd.DataFrame:
    if path.suffix.lower() in (".xlsx", ".xlsm", ".xls"):
        return pd.read_excel(path, sheet_name=sheet or 0, dtype=str)
    return pd.read_csv(path, dtype=str, encoding="utf-8-sig")


def date_ok_rate(s: pd.Series) -> float:
    vals = s.dropna().str.strip()
    if vals.empty:
        return 0.0
    ok = pd.Series(False, index=vals.index)
    for fmt in DATE_FORMATS:
        ok |= pd.to_datetime(vals, format=fmt, errors="coerce").notna()
    return ok.mean()


def column_rows(df: pd.DataFrame) -> list[str]:
    rows = []
    for col in df.columns:
        s = df[col].astype("string").str.strip().replace("", pd.NA)
        patterns = s.dropna().map(mask_pattern).value_counts().head(TOP_PATTERNS)
        top = "; ".join(f"{p} ({n})" for p, n in patterns.items()) or "—"
        rows.append(f"| {col} | {s.isna().mean():.1%} | {s.nunique()} | {top} |")
    return rows


def checks(df: pd.DataFrame, a: argparse.Namespace) -> list[str]:
    out = []
    for name in [c for c in (a.key, a.cccd, a.ma_dia_ban) if c] + a.date:
        if name not in df.columns:
            sys.exit(f"LỖI: không có cột '{name}'. Các cột: {list(df.columns)}")
    if a.key:
        dup = df[a.key].dropna().duplicated(keep=False).sum()
        out.append(f"- Trùng theo khóa `{a.key}`: {dup} dòng thuộc nhóm trùng")
    if a.cccd:
        s = df[a.cccd].dropna().astype(str).str.strip()
        valid = s.str.match(CCCD_RE).mean() if len(s) else 0.0
        out.append(f"- Số định danh `{a.cccd}`: có giá trị {len(s)}/{len(df)} dòng; đúng 12 chữ số {valid:.1%}")
    for col in a.date:
        out.append(f"- Ngày `{col}`: đọc được theo dd/mm/yyyy hoặc yyyy-mm-dd {date_ok_rate(df[col]):.1%}")
    if a.ma_dia_ban:
        s = df[a.ma_dia_ban].dropna().astype(str).str.strip()
        lens = s.str.len().value_counts().to_dict()
        out.append(f"- Mã địa bàn `{a.ma_dia_ban}`: {s.nunique()} mã khác nhau; độ dài mã {lens}")
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--ten-nguon", default="")
    ap.add_argument("--sheet")
    ap.add_argument("--key")
    ap.add_argument("--cccd")
    ap.add_argument("--date", default="", help="các cột ngày, phân cách bằng dấu phẩy")
    ap.add_argument("--ma-dia-ban")
    ap.add_argument("--out")
    a = ap.parse_args()
    a.date = [c for c in a.date.split(",") if c]

    path = Path(a.file)
    df = load(path, a.sheet)
    lines = [
        f"# Profiling nguồn: {a.ten_nguon or path.stem}",
        "",
        f"- File: `{path.name}` · Số dòng: {len(df)} · Số cột: {len(df.columns)}",
        "- Mẫu định dạng: 9 = chữ số, A = chữ cái; không hiển thị giá trị thật.",
        "",
        "## Kiểm tra trọng điểm",
        *(checks(df, a) or ["- (không chỉ định cột khóa/CCCD/ngày/địa bàn)"]),
        "",
        "## Thống kê theo cột",
        "",
        "| Cột | Tỷ lệ trống | Số giá trị khác nhau | Mẫu định dạng phổ biến |",
        "|---|---|---|---|",
        *column_rows(df),
    ]
    text = "\n".join(lines) + "\n"
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
        print("Đã ghi:", a.out)
    else:
        print(text)


if __name__ == "__main__":
    main()
