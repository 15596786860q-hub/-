#!/usr/bin/env python3
"""协议发包对抗易盾完整方案 → PDF (大字版)"""
from pathlib import Path
import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

BASE = Path(__file__).parent
SRC_MD = BASE / "协议发包对抗易盾完整方案.md"
OUT_PDF = BASE / "协议发包对抗易盾完整方案.pdf"

md_text = SRC_MD.read_text(encoding="utf-8")

html_body = markdown.markdown(
    md_text,
    extensions=["extra", "codehilite", "toc", "tables", "fenced_code", "sane_lists"],
)

cover = """
<div class="cover">
  <div class="cover-inner">
    <div class="cover-top">闲鱼自动化系列 · 第 4 部</div>
    <div class="cover-icon">⚔️</div>
    <h1 class="cover-title">协议发包</h1>
    <h1 class="cover-title">对抗易盾</h1>
    <h2 class="cover-subtitle">完整方案 · 架构 · 代码 · 实战纪律</h2>
    <div class="cover-meta">
      <div>4 大方案对比 · 12 章实战手册</div>
      <div>Sekiro · 设备画像 · 混合架构</div>
      <div>从零到 500 账号矩阵的工业级方案</div>
    </div>
    <div class="cover-bottom">出品 · 由 Kiro 协助整理</div>
  </div>
</div>
<div class="page-break"></div>
"""

html_full = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="utf-8"/><title>协议发包对抗易盾完整方案</title></head>
<body>
{cover}
<div class="content">
{html_body}
</div>
</body>
</html>
"""

CSS_TEXT = """
@page {
  size: A4;
  margin: 2.2cm 2cm 2.4cm 2cm;
  @bottom-center {
    content: counter(page) " / " counter(pages);
    font-family: "Noto Sans CJK SC", sans-serif;
    font-size: 10pt;
    color: #888;
  }
  @top-right {
    content: "协议发包对抗易盾完整方案";
    font-family: "Noto Sans CJK SC", sans-serif;
    font-size: 10pt;
    color: #aaa;
  }
}
@page cover {
  margin: 0;
  @bottom-center { content: none; }
  @top-right { content: none; }
}
.cover {
  page: cover;
  page-break-after: always;
  width: 100%;
  height: 100vh;
  background: linear-gradient(135deg, #1a237e 0%, #4527a0 50%, #d81b60 100%);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}
.cover-inner { padding: 40px; }
.cover-top {
  font-size: 16pt;
  letter-spacing: 4pt;
  opacity: 0.95;
  margin-bottom: 20pt;
}
.cover-icon {
  font-size: 90pt;
  margin: 10pt 0 20pt 0;
}
.cover-title {
  font-size: 64pt;
  font-weight: 900;
  margin: 0;
  letter-spacing: 6pt;
  text-shadow: 0 4px 24px rgba(0,0,0,0.35);
  line-height: 1.1;
}
.cover-subtitle {
  font-size: 20pt;
  font-weight: 400;
  margin-top: 24pt;
  opacity: 0.95;
  letter-spacing: 2pt;
}
.cover-meta {
  margin-top: 60pt;
  font-size: 14pt;
  line-height: 2.2;
  opacity: 0.95;
}
.cover-bottom {
  margin-top: 70pt;
  font-size: 11pt;
  opacity: 0.8;
}

html, body {
  font-family: "Noto Sans CJK SC", "Noto Sans", sans-serif;
  font-size: 13pt;
  line-height: 1.85;
  color: #1f2937;
  margin: 0;
  padding: 0;
}
.page-break { page-break-before: always; }
.content { max-width: 100%; }

h1, h2, h3, h4, h5 {
  font-family: "Noto Sans CJK SC", sans-serif;
  color: #4527a0;
  line-height: 1.4;
  page-break-after: avoid;
  font-weight: 800;
}
h1 {
  font-size: 26pt;
  border-bottom: 4px solid #4527a0;
  padding-bottom: 10pt;
  margin-top: 30pt;
  margin-bottom: 22pt;
  page-break-before: always;
}
.content h1:first-child { page-break-before: auto; }
h2 {
  font-size: 20pt;
  border-left: 6px solid #4527a0;
  padding-left: 14pt;
  margin-top: 28pt;
  margin-bottom: 14pt;
  color: #311b92;
}
h3 {
  font-size: 16pt;
  margin-top: 22pt;
  margin-bottom: 10pt;
  color: #4527a0;
}
h4 {
  font-size: 14pt;
  color: #333;
  margin-top: 18pt;
}
h5 {
  font-size: 13pt;
  color: #555;
}

p {
  margin: 8pt 0;
  text-align: justify;
}

blockquote {
  background: #ede7f6;
  border-left: 5px solid #4527a0;
  padding: 12pt 18pt;
  margin: 14pt 0;
  color: #1f2937;
  font-size: 12.5pt;
}

code {
  font-family: "Noto Sans Mono CJK SC", "Courier New", monospace;
  font-size: 11pt;
  background: #f3e5f5;
  color: #4527a0;
  padding: 2pt 6pt;
  border-radius: 4pt;
}
pre {
  background: #1e293b;
  color: #f1f5f9;
  padding: 14pt 16pt;
  border-radius: 6pt;
  overflow-x: auto;
  font-size: 10.5pt;
  line-height: 1.6;
  page-break-inside: avoid;
  white-space: pre-wrap;
  word-wrap: break-word;
  margin: 12pt 0;
}
pre code {
  background: none;
  color: inherit;
  padding: 0;
  font-size: 10.5pt;
}

table {
  border-collapse: collapse;
  width: 100%;
  margin: 14pt 0;
  font-size: 11.5pt;
  page-break-inside: avoid;
}
th {
  background: #4527a0;
  color: #fff;
  padding: 9pt 10pt;
  text-align: left;
  border: 1px solid #4527a0;
  font-size: 12pt;
  font-weight: 700;
}
td {
  padding: 8pt 10pt;
  border: 1px solid #d1c4e9;
  vertical-align: top;
}
tr:nth-child(even) td { background: #f8f5fc; }

ul, ol {
  margin: 8pt 0;
  padding-left: 26pt;
}
li {
  margin: 5pt 0;
  line-height: 1.85;
}

hr {
  border: none;
  border-top: 1.5px dashed #b39ddb;
  margin: 22pt 0;
}

a {
  color: #4527a0;
  text-decoration: none;
}

strong {
  color: #b8002a;
  font-weight: 700;
}
em {
  color: #455a64;
  font-style: normal;
  font-weight: 600;
}
"""

font_config = FontConfiguration()
HTML(string=html_full, base_url=str(BASE)).write_pdf(
    str(OUT_PDF),
    stylesheets=[CSS(string=CSS_TEXT, font_config=font_config)],
    font_config=font_config,
)
print(f"PDF 已生成:{OUT_PDF}")
print(f"文件大小:{OUT_PDF.stat().st_size / 1024:.1f} KB")
