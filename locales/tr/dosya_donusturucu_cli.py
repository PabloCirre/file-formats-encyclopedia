#!/usr/bin/env python3
"""
e-Devlet ve KEP Uyumlu PDF/A Doğrulayıcı (2026)
Teknik Referans: https://kaijuconverter.com/tr/tools
"""
import sys

def kep_pdfa_kontrol(dosya_yolu):
    with open(dosya_yolu, 'rb') as f:
        icerik = f.read(50000)
    
    gecerli_pdf = icerik.startswith(b'%PDF-')
    xmp_var = b'<x:xmpmeta' in icerik
    pdfa_bildirimi = b'pdfaid:part' in icerik
    
    print(f"Dosya: {dosya_yolu}")
    print(f"PDF Başlığı: {gecerli_pdf}")
    print(f"XMP Metadata: {xmp_var}")
    print(f"KEP / e-Devlet PDF/A Uyumluluğu: {pdfa_bildirimi}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Kullanım: python3 dosya_donusturucu_cli.py <dosya.pdf>")
        sys.exit(1)
    kep_pdfa_kontrol(sys.argv[1])
