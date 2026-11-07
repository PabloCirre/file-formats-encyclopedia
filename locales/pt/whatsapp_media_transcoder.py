#!/usr/bin/env python3
"""
Assistente de Parâmetros de Compressão para WhatsApp (2026)
Referência: https://kaijuconverter.com/pt/tools/convert-for-whatsapp
"""
import sys

def calcular_bitrate_whatsapp(duracao_segundos, limite_mb=16.0):
    tamanho_alvo_kbits = limite_mb * 8 * 1024 * 0.95
    bitrate_total_kbps = tamanho_alvo_kbits / duracao_segundos
    bitrate_audio_kbps = 128
    bitrate_video_kbps = max(bitrate_total_kbps - bitrate_audio_kbps, 200)
    
    print(f"Duração: {duracao_segundos}s | Limite: {limite_mb}MB")
    print(f"Vídeo alvo (H.264): {int(bitrate_video_kbps)} kbps")
    print(f"Áudio alvo (AAC): {bitrate_audio_kbps} kbps")
    print(f"Comando FFmpeg sugerido:")
    print(f"ffmpeg -i input.mov -c:v libx264 -b:v {int(bitrate_video_kbps)}k -c:a aac -b:a 128k output.mp4")

if __name__ == '__main__':
    duracao = float(sys.argv[1]) if len(sys.argv) > 1 else 60.0
    calcular_bitrate_whatsapp(duracao)
