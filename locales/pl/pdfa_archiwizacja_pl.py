#!/usr/bin/env python3
"""
Weryfikator PDF/A dla Systemów EZD i ePUAP (2026)
Referencja: https://kaijuconverter.com/pl/tools
"""
import sys

def sprawdz_epuap_pdfa(sciezka):
    with open(sciezka, 'rb') as f:
        dane = f.read(50000)
    
    jest_pdf = dane.startswith(b'%PDF-')
    ma_xmp = b'<x:xmpmeta' in dane
    ma_pdfa = b'pdfaid:part' in dane
    
    print(f"Plik: {sciezka}")
    print(f"Nagłówek PDF: {jest_pdf}")
    print(f"Metadane XMP: {ma_xmp}")
    print(f"Standard PDF/A (EZD / ePUAP): {ma_pdfa}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Użycie: python3 pdfa_archiwizacja_pl.py <dokument.pdf>")
        sys.exit(1)
    sprawdz_epuap_pdfa(sys.argv[1])
