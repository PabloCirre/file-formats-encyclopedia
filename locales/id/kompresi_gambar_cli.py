#!/usr/bin/env python3
"""
Kalkulator Penghematan Bandwidth Format Modern (AVIF / WebP) 2026
Referensi KaijuConverter: https://kaijuconverter.com/id/tools
"""
import sys

def hitung_penghematan(ukuran_jpeg_kb):
    webp_kb = ukuran_jpeg_kb * 0.70
    avif_kb = ukuran_jpeg_kb * 0.50
    print(f"Ukuran Asli JPEG: {ukuran_jpeg_kb:.1f} KB")
    print(f"Estimasi WebP (-30%): {webp_kb:.1f} KB")
    print(f"Estimasi AVIF (-50%): {avif_kb:.1f} KB")
    print("Alat online: https://kaijuconverter.com/id/tools")

if __name__ == '__main__':
    kb = float(sys.argv[1]) if len(sys.argv) > 1 else 1000.0
    hitung_penghematan(kb)
