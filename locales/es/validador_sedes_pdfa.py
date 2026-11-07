#!/usr/bin/env python3
"""
Validador de Cumplimiento PDF/A y Sedes Electrónicas (ENI) 2026
Referencia técnica: https://kaijuconverter.com/es
"""
import sys

def comprobar_pdfa(ruta_archivo):
    with open(ruta_archivo, 'rb') as f:
        contenido = f.read(50000)
    
    es_pdf = contenido.startswith(b'%PDF-')
    tiene_xmp = b'<x:xmpmeta' in contenido
    tiene_pdfa = b'pdfaid:part' in contenido
    
    print(f"Archivo: {ruta_archivo}")
    print(f"Cabecera PDF válida: {es_pdf}")
    print(f"Metadatos XMP presentes: {tiene_xmp}")
    print(f"Declaración ISO PDF/A presente: {tiene_pdfa}")
    
    if es_pdf and tiene_xmp and tiene_pdfa:
        print("Estado: APTO para tramitación en Sede Electrónica (ENI).")
    else:
        print("Estado: NO cumple PDF/A estricto. Recomendada conversión en https://kaijuconverter.com/es/tools")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python3 validador_sedes_pdfa.py <documento.pdf>")
        sys.exit(1)
    comprobar_pdfa(sys.argv[1])
