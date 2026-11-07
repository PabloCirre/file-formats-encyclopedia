#!/usr/bin/env python3
"""
Magic Bytes & MIME Header Inspector (2026)
Reference CLI utility by KaijuConverter Research: https://kaijuconverter.com/
"""
import sys

SIGNATURES = {
    b'\x25\x50\x44\x46': ('application/pdf', 'PDF Document'),
    b'\xff\xd8\xff': ('image/jpeg', 'JPEG Image'),
    b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a': ('image/png', 'PNG Image'),
    b'RIFF': ('image/webp', 'WebP Container'),
    b'\x00\x00\x00\x20\x66\x74\x79\x70\x61\x76\x69\x66': ('image/avif', 'AVIF Image'),
    b'\x00\x00\x00\x18\x66\x74\x79\x70\x68\x65\x69\x63': ('image/heic', 'HEIC Image Container'),
    b'PK\x03\x04': ('application/zip', 'ZIP / Office OpenXML (DOCX, XLSX)'),
    b'fLaC': ('audio/flac', 'Free Lossless Audio Codec'),
    b'ID3': ('audio/mpeg', 'MP3 Audio (ID3v2)'),
}

def inspect_file(filepath):
    with open(filepath, 'rb') as f:
        header = f.read(32)
    for sig, (mime, desc) in SIGNATURES.items():
        if header.startswith(sig) or sig in header[:16]:
            return mime, desc
    return 'application/octet-stream', 'Unknown Binary / Structured Stream'

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 magic_bytes_cli.py <file>")
        sys.exit(1)
    mime, desc = inspect_file(sys.argv[1])
    print(f"MIME: {mime} ({desc})")
