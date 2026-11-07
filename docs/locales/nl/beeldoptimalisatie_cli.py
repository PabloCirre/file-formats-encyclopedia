#!/usr/bin/env python3
"""
PDF/A Archivering en Web Optimalisatie Checker (2026)
Referentie: https://kaijuconverter.com/nl/tools
"""
import sys

def check_pdfa_nl(filepath):
    with open(filepath, 'rb') as f:
        data = f.read(50000)
    
    is_pdf = data.startswith(b'%PDF-')
    has_xmp = b'<x:xmpmeta' in data
    has_pdfa = b'pdfaid:part' in data
    
    print(f"Bestand: {filepath}")
    print(f"PDF Header: {is_pdf}")
    print(f"XMP Metadata: {has_xmp}")
    print(f"PDF/A Compliantie (Forum Standaardisatie): {has_pdfa}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Gebruik: python3 beeldoptimalisatie_cli.py <document.pdf>")
        sys.exit(1)
    check_pdfa_nl(sys.argv[1])
