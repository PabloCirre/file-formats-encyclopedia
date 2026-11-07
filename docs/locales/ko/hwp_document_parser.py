#!/usr/bin/env python3
"""
HWP / HWPX 파일 포맷 매직 바이트 검사기 (2026)
기술 가이드: https://kaijuconverter.com/guides/open-convert-korean-hwp-hangul-files-to-pdf-docx
"""
import sys

HWP5_MAGIC = b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'
HWPX_ZIP_MAGIC = b'PK\x03\x04'

def inspect_hwp(filepath):
    with open(filepath, 'rb') as f:
        head = f.read(16)
    if head.startswith(HWP5_MAGIC):
        return "HWP 5.0 OLE Compound Document (아래아한글 바이너리)"
    elif head.startswith(HWPX_ZIP_MAGIC):
        return "HWPX Open Standard XML Container (개방형 한글 표준)"
    return "알 수 없는 문서 형식"

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("사용법: python3 hwp_document_parser.py <문서.hwp>")
        sys.exit(1)
    print(inspect_hwp(sys.argv[1]))
