# 2026 File Formats, IANA MIME Types & Magic Bytes Open Encyclopedia (CC-BY 4.0)

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Formats Covered](https://img.shields.io/badge/Formats-201%2B-ef4444)](https://kaijuconverter.com/formats)
[![Conversion Pairs](https://img.shields.io/badge/Conversion_Pairs-3%2C208-38bdf8)](https://kaijuconverter.com/convert)
[![MCP Server](https://glama.ai/mcp/servers/PabloCirre/kaijuconverter-mcp/badges/score.svg)](https://glama.ai/mcp/servers/PabloCirre/kaijuconverter-mcp)

An open engineering reference and machine-readable dataset covering **201+ file formats**, **IANA MIME types**, **hexadecimal Magic Bytes signatures**, compression algorithms, and lossless/lossy transcoding paths across **3,208 verified conversion pairs**.

Maintained by the engineering team at **[KaijuConverter](https://kaijuconverter.com)** — the hybrid WebAssembly + ISO-27001 cloud file conversion workbench with **[54 specialized Studio tools](https://kaijuconverter.com/tools)**, **[REST API v1](https://kaijuconverter.com/api-docs)**, and **[Model Context Protocol (MCP) server](https://kaijuconverter.com/integrations)**.

---

## 🔗 Quick Links & Live Benchmarks

- **Interactive Encyclopedia (201+ Formats):** [https://kaijuconverter.com/formats](https://kaijuconverter.com/formats)
- **Open CSV Dataset Download (`CC-BY 4.0`):** [https://kaijuconverter.com/downloads/kaijuconverter-2026-file-formats-dataset.csv](https://kaijuconverter.com/downloads/kaijuconverter-2026-file-formats-dataset.csv)
- **54 Precision Studio Workspaces:** [https://kaijuconverter.com/tools](https://kaijuconverter.com/tools)
- **Side-by-Side Format Comparisons:** [https://kaijuconverter.com/compare](https://kaijuconverter.com/compare)
- **Engineering & Format Guides:** [https://kaijuconverter.com/guides](https://kaijuconverter.com/guides)
- **Remote Streamable HTTP MCP Endpoint:** `https://kaijuconverter.com/api/mcp` ([MCP & AI Hub](https://kaijuconverter.com/integrations))
- **GitHub Pages Documentation Portal:** [https://pablocirre.github.io/file-formats-encyclopedia/](https://pablocirre.github.io/file-formats-encyclopedia/)

---

## 📊 Most Consulted Format Specifications & Converters

| Extension | Format Name | Primary MIME Type | Magic Bytes (Hex) | Specification | Top Conversion Pairs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `.heic` | Apple High Efficiency Image | `image/heic` | `66 74 79 70 68 65 69 63` | [HEIC Spec](https://kaijuconverter.com/formats/heic) | [HEIC to JPG](https://kaijuconverter.com/convert/heic-to-jpg) · [HEIC to PNG](https://kaijuconverter.com/convert/heic-to-png) |
| `.avif` | AV1 Image File Format | `image/avif` | `66 74 79 70 61 76 69 66` | [AVIF Spec](https://kaijuconverter.com/formats/avif) | [AVIF to PNG](https://kaijuconverter.com/convert/avif-to-png) · [AVIF to JPG](https://kaijuconverter.com/convert/avif-to-jpg) |
| `.webp` | WebP Raster Image | `image/webp` | `52 49 46 46 .. 57 45 42 50` | [WebP Spec](https://kaijuconverter.com/formats/webp) | [WebP to PNG](https://kaijuconverter.com/convert/webp-to-png) · [WebP to JPG](https://kaijuconverter.com/convert/webp-to-jpg) |
| `.pdf` | Portable Document Format (ISO 32000) | `application/pdf` | `25 50 44 46 2D` (`%PDF-`) | [PDF Spec](https://kaijuconverter.com/formats/pdf) | [PDF to DOCX](https://kaijuconverter.com/convert/pdf-to-docx) · [PDF to PPTX](https://kaijuconverter.com/convert/pdf-to-pptx) · [PDF to PDF/A](https://kaijuconverter.com/tools/pdf-to-pdfa) |
| `.svg` | Scalable Vector Graphics | `image/svg+xml` | `3C 73 76 67` (`<svg`) | [SVG Spec](https://kaijuconverter.com/formats/svg) | [SVG to AI](https://kaijuconverter.com/convert/svg-to-ai) · [SVG to EPS](https://kaijuconverter.com/convert/svg-to-eps) · [SVG to PNG](https://kaijuconverter.com/convert/svg-to-png) |
| `.bmp` | Windows Device Independent Bitmap | `image/bmp` | `42 4D` (`BM`) | [BMP Spec](https://kaijuconverter.com/formats/bmp) | [BMP to PNG](https://kaijuconverter.com/convert/bmp-to-png) · [BMP to JPG](https://kaijuconverter.com/convert/bmp-to-jpg) |
| `.tiff` | Tagged Image File Format | `image/tiff` | `49 49 2A 00` / `4D 4D 00 2A` | [TIFF Spec](https://kaijuconverter.com/formats/tiff) | [TIFF to PDF](https://kaijuconverter.com/convert/tiff-to-pdf) · [TIFF to JPG](https://kaijuconverter.com/convert/tiff-to-jpg) |
| `.epub` | EPUB 3 Open E-Book Container | `application/epub+zip` | `50 4B 03 04` (ZIP/OCF) | [EPUB Spec](https://kaijuconverter.com/formats/epub) | [MOBI to EPUB](https://kaijuconverter.com/convert/mobi-to-epub) · [EPUB to PDF](https://kaijuconverter.com/convert/epub-to-pdf) |
| `.flac` | Free Lossless Audio Codec | `audio/flac` | `66 4C 61 43` (`fLaC`) | [FLAC Spec](https://kaijuconverter.com/formats/flac) | [FLAC to MP3](https://kaijuconverter.com/convert/flac-to-mp3) · [WAV to FLAC](https://kaijuconverter.com/convert/wav-to-flac) |
| `.mp4` | ISO Base Media Video Container | `video/mp4` | `66 74 79 70 69 73 6F 6D` | [MP4 Spec](https://kaijuconverter.com/formats/mp4) | [WEBM to MP4](https://kaijuconverter.com/convert/webm-to-mp4) · [MOV to MP4](https://kaijuconverter.com/convert/mov-to-mp4) · [Video to GIF](https://kaijuconverter.com/tools/video-to-gif) |

---

## 🛠️ Featured Engineering Guides & Format Comparisons

- [JPG vs JXL (JPEG XL) Technical Benchmark](https://kaijuconverter.com/compare/jpg-vs-jxl)
- [AAC vs MP3 Audio Codec Comparison](https://kaijuconverter.com/compare/aac-vs-mp3)
- [FLAC vs MP3 Lossless vs Lossy Audio Guide](https://kaijuconverter.com/compare/flac-vs-mp3)
- [DOCX vs PDF Document Architecture](https://kaijuconverter.com/compare/docx-vs-pdf)
- [JSON vs TXT Structured Data Comparison](https://kaijuconverter.com/compare/json-vs-txt)
- [WebP Animation Complete Engineering Guide](https://kaijuconverter.com/guides/webp-animation-guide)
- [H.264 / AVC Video Codec Complete Guide](https://kaijuconverter.com/guides/h264-avc-video-codec-complete-guide)
- [HEVC / H.265 Video Codec Complete Guide](https://kaijuconverter.com/guides/hevc-h265-video-codec-complete-guide)
- [Audio Sample Rates (44.1 kHz vs 48 kHz vs 96 kHz)](https://kaijuconverter.com/guides/audio-sample-rates-44100-48000-96000)
- [How to Compress Image to Exact 20KB / 50KB / 100KB](https://kaijuconverter.com/tools/compress-image-to-20kb)

---

## 🌍 Multilingual Format Encyclopedias (12 Languages)

- [English](https://kaijuconverter.com/) · [Español](https://kaijuconverter.com/es) · [Português](https://kaijuconverter.com/pt) · [Deutsch](https://kaijuconverter.com/de) · [Français](https://kaijuconverter.com/fr) · [日本語](https://kaijuconverter.com/ja) · [Italiano](https://kaijuconverter.com/it) · [Bahasa Indonesia](https://kaijuconverter.com/id) · [Türkçe](https://kaijuconverter.com/tr) · [한국어](https://kaijuconverter.com/ko) · [Polski](https://kaijuconverter.com/pl) · [Nederlands](https://kaijuconverter.com/nl)
