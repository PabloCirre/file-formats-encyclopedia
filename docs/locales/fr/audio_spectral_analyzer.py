#!/usr/bin/env python3
"""
Calculateur de Qualité et Débits Audio (2026)
Référence KaijuConverter: https://kaijuconverter.com/fr/compare
"""
import sys

AUDIO_PRESETS = {
    'flac': {'lossless': True, 'kbps': 920, 'cutoff_khz': 22.05},
    'm4a_aac': {'lossless': False, 'kbps': 256, 'cutoff_khz': 20.0},
    'mp3_320': {'lossless': False, 'kbps': 320, 'cutoff_khz': 20.5},
    'mp3_128': {'lossless': False, 'kbps': 128, 'cutoff_khz': 16.0},
}

def afficher_comparaison():
    print(f"{'Format':<10} | {'Type':<10} | {'Débit Typique':<15} | {'Coupure Aigus'}")
    print("-" * 55)
    for fmt, data in AUDIO_PRESETS.items():
        type_str = "Sans perte" if data['lossless'] else "Destructif"
        print(f"{fmt:<10} | {type_str:<10} | {data['kbps']} kbps{'':<8} | {data['cutoff_khz']} kHz")

if __name__ == '__main__':
    afficher_comparaison()
