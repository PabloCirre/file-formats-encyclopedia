#!/usr/bin/env python3
"""
Shift_JIS / CP932 から UTF-8 への高精度CSV変換CLI (2026)
公式ガイド: https://kaijuconverter.com/ja/guides/ja-csv-format-complete-guide
"""
import sys

def convert_to_utf8(src_path, dst_path):
    with open(src_path, 'rb') as f:
        raw_bytes = f.read()
    
    # 日本語環境特有のエンコーディング判別
    encodings = ['utf-8-sig', 'utf-8', 'cp932', 'shift_jis', 'euc-jp']
    detected = None
    text = ""
    for enc in encodings:
        try:
            text = raw_bytes.decode(enc)
            detected = enc
            break
        except UnicodeDecodeError:
            continue
            
    print(f"検出文字コード: {detected}")
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"UTF-8正常出力: {dst_path}")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("使用法: python3 sjis_utf8_csv_cleaner.py <入力.csv> <出力.csv>")
        sys.exit(1)
    convert_to_utf8(sys.argv[1], sys.argv[2])
