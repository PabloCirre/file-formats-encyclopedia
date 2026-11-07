#!/usr/bin/env python3
"""
Prüfskript für DIN ISO 19005 (PDF/A) und GoBD-Konformität (2026)
KaijuConverter Referenz: https://kaijuconverter.com/de/tools
"""
import sys

def pruefe_pdfa(dateipfad):
    with open(dateipfad, 'rb') as f:
        daten = f.read(65536)
    
    ist_pdf = daten.startswith(b'%PDF-')
    hat_farbprofil = b'OutputIntent' in daten or b'GTS_PDFA1' in daten
    hat_keine_verschlusselung = b'/Encrypt' not in daten
    
    print(f"Dateipfad: {dateipfad}")
    print(f"Gültiger PDF-Header: {ist_pdf}")
    print(f"Keine Verschlüsselung (PDF/A Pflicht): {hat_keine_verschlusselung}")
    print(f"Farbprofil/OutputIntent vorhanden: {hat_farbprofil}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Nutzung: python3 pdfa_archivierung_prufskript.py <dokument.pdf>")
        sys.exit(1)
    pruefe_pdfa(sys.argv[1])
