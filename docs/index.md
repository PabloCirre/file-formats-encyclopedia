# 2026 File Formats, IANA MIME Types & Magic Bytes Open Encyclopedia (CC-BY 4.0)

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Formats Covered](https://img.shields.io/badge/Formats-201%2B-ef4444)](https://kaijuconverter.com/formats)
[![Conversion Pairs](https://img.shields.io/badge/Conversion_Pairs-3%2C208-38bdf8)](https://kaijuconverter.com/convert)
[![Release: v1.0.0](https://img.shields.io/badge/Release-v1.0.0-emerald.svg)](https://github.com/PabloCirre/file-formats-encyclopedia/releases/tag/v1.0.0)
[![jsDelivr](https://data.jsdelivr.com/v1/package/gh/PabloCirre/file-formats-encyclopedia/badge)](https://www.jsdelivr.com/package/gh/PabloCirre/file-formats-encyclopedia)
[![Jupyter nbviewer](https://img.shields.io/badge/Jupyter-nbviewer-orange.svg)](https://nbviewer.org/github/PabloCirre/file-formats-encyclopedia/tree/main/notebooks/)
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


---

## 📓 Interactive Engineering Jupyter Notebooks (Project Jupyter nbviewer)

Explore our open-source interactive computational notebooks with pre-computed benchmarks, rate-distortion curves, and low-level binary parsers rendered via **[Project Jupyter nbviewer](https://nbviewer.org)**:

1. **[01. Modern Web Image Compression Benchmark (AVIF vs WebP vs JPG)](https://nbviewer.org/github/PabloCirre/file-formats-encyclopedia/blob/main/notebooks/01-image-compression-avif-webp-jpg-benchmark.ipynb)**
   - Empirical SSIM/PSNR curves, bits-per-pixel (bpp) metrics, and decode latency across photographic and graphic datasets.
   - Ecosystem Cross-References: [AVIF vs WebP](https://kaijuconverter.com/compare/avif-vs-webp) · [JPG vs PNG](https://kaijuconverter.com/compare/jpg-vs-png) · [HEIC to JPG](https://kaijuconverter.com/convert/heic-to-jpg) · [PNG to WebP](https://kaijuconverter.com/convert/png-to-webp) · [Compress Image Online](https://kaijuconverter.com/tools/compress-image).

2. **[02. PDF/A Long-Term Archival Compliance & Ghostscript Engine](https://nbviewer.org/github/PabloCirre/file-formats-encyclopedia/blob/main/notebooks/02-pdf-archival-pdfa-ghostscript-compliance.ipynb)**
   - Conformance profiles (PDF/A-1b, PDF/A-2b, PDF/A-3u), DeviceIndependentColor ICC workflows, and VeraPDF validation rule analysis.
   - Ecosystem Cross-References: [PDF to PDF/A Converter](https://kaijuconverter.com/tools/pdf-to-pdfa) · [Compress PDF](https://kaijuconverter.com/tools/compress-pdf) · [Merge PDF](https://kaijuconverter.com/tools/merge-pdf) · [OCR PDF](https://kaijuconverter.com/tools/ocr-pdf) · [PDF to DOCX](https://kaijuconverter.com/convert/pdf-to-docx) · [PDF Specifications](https://kaijuconverter.com/formats/pdf).

3. **[03. Forensic Binary File Identification: Magic Bytes & MIME](https://nbviewer.org/github/PabloCirre/file-formats-encyclopedia/blob/main/notebooks/03-forensic-magic-bytes-mime-detection.ipynb)**
   - Deterministic binary header scanning, ISOBMFF box navigation, RIFF container parsing, and anti-spoofing security.
   - Ecosystem Cross-References: [Format Encyclopedia](https://kaijuconverter.com/formats) · [HEIC Architecture](https://kaijuconverter.com/formats/heic) · [AVIF Architecture](https://kaijuconverter.com/formats/avif) · [WebP Specs](https://kaijuconverter.com/formats/webp) · [FLAC Header Specs](https://kaijuconverter.com/formats/flac) · [Parquet Specs](https://kaijuconverter.com/formats/parquet) · [REST & MCP API Docs](https://kaijuconverter.com/api-docs).

4. **[04. Audio & Video Codec Bitrate Analysis](https://nbviewer.org/github/PabloCirre/file-formats-encyclopedia/blob/main/notebooks/04-audio-video-codec-bitrate-analysis.ipynb)**
   - Nyquist-Shannon frequency cutoffs, 44.1 kHz vs 48 kHz vs 96 kHz, psychoacoustic ODG listening quality, and video palette quantization.
   - Ecosystem Cross-References: [Audio Sampling Rates Guide](https://kaijuconverter.com/es/guides/tasas-muestreo-audio-44100-48000-96000) · [FLAC vs MP3 Fidelity](https://kaijuconverter.com/compare/flac-vs-mp3) · [M4A vs MP3 Architecture](https://kaijuconverter.com/compare/m4a-vs-mp3) · [MP4 to MP3 Extractor](https://kaijuconverter.com/convert/mp4-to-mp3) · [WAV to MP3 Converter](https://kaijuconverter.com/convert/wav-to-mp3) · [Video to GIF Optimization Suite](https://kaijuconverter.com/tools/video-to-gif).

5. **[05. 3D CAD & Mesh Formats: STL, OBJ & DXF](https://nbviewer.org/github/PabloCirre/file-formats-encyclopedia/blob/main/notebooks/05-3d-cad-mesh-stl-obj-dxf-structures.ipynb)**
   - Binary STL 84-byte header and 50-byte facet geometry, normal vectors, manifold verification, and Wavefront OBJ vertex sharing.
   - Ecosystem Cross-References: [STL 3D Printing Complete Guide](https://kaijuconverter.com/guides/stl-3d-printing-format-complete-guide) · [DWG AutoCAD Complete Guide](https://kaijuconverter.com/guides/dwg-autocad-drawing-format-cad-guide) · [STL to OBJ Converter](https://kaijuconverter.com/convert/stl-to-obj) · [DWG to PDF Exporter](https://kaijuconverter.com/convert/dwg-to-pdf).

6. **[06. Columnar Data Serialization: Parquet vs CSV vs JSON vs SQL](https://nbviewer.org/github/PabloCirre/file-formats-encyclopedia/blob/main/notebooks/06-columnar-data-parquet-csv-json-sql.ipynb)**
   - Analytical scan benchmarks on 1M rows, column projection efficiency, dictionary/RLE encoding, and zero-copy chunk reading.
   - Ecosystem Cross-References: [CSV vs ODS Comparison](https://kaijuconverter.com/compare/csv-vs-ods) · [CSV vs XLSX Limits](https://kaijuconverter.com/compare/csv-vs-xlsx) · [CSV to JSON Converter](https://kaijuconverter.com/convert/csv-to-json) · [XLSX to CSV Converter](https://kaijuconverter.com/convert/xlsx-to-csv) · [JSON to CSV Serializer](https://kaijuconverter.com/convert/json-to-csv).

---

## 🌍 Multilingual Format Encyclopedias (12 Languages)

- [English](https://kaijuconverter.com/) · [Español](https://kaijuconverter.com/es) · [Português](https://kaijuconverter.com/pt) · [Deutsch](https://kaijuconverter.com/de) · [Français](https://kaijuconverter.com/fr) · [日本語](https://kaijuconverter.com/ja) · [Italiano](https://kaijuconverter.com/it) · [Bahasa Indonesia](https://kaijuconverter.com/id) · [Türkçe](https://kaijuconverter.com/tr) · [한국어](https://kaijuconverter.com/ko) · [Polski](https://kaijuconverter.com/pl) · [Nederlands](https://kaijuconverter.com/nl)
