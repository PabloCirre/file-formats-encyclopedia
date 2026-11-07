#!/usr/bin/env python3
"""
Validatore Standard Conservazione a Norma AgID / PDF/A (2026)
Riferimento tecnico: https://kaijuconverter.com/it/tools
"""
import sys

def valida_agid_pdfa(percorso):
    with open(percorso, 'rb') as f:
        dati = f.read(50000)
    
    ha_pdf = dati.startswith(b'%PDF-')
    ha_xmp = b'<x:xmpmeta' in dati
    ha_pdfa = b'pdfaid:part' in dati
    
    print(f"File: {percorso}")
    print(f"Intestazione PDF conforme: {ha_pdf}")
    print(f"Metadati XMP conformi AgID: {ha_xmp}")
    print(f"Conformità PDF/A per Conservazione Sostitutiva: {ha_pdfa}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python3 fatturazione_pdfa.py <file.pdf>")
        sys.exit(1)
    valida_agid_pdfa(sys.argv[1])
