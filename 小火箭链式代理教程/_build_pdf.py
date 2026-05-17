#!/usr/bin/env python3
"""Shadowrocket 链式代理完整配置教程 → PDF (精美版)"""
from pathlib import Path
import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

BASE = Path(__file__).parent
SRC_MD = BASE / "Shadowrocket链式代理完整配置教程.md"
OUT_PDF = BASE / "Shadowrocket链式代理完整配置教程.pdf"

md_text = SRC_MD.read_text(encoding="utf-8")

html_body = markdown.markdown(
    md_text,
    extensions=["extra", "codehilite", "toc", "tables", "fenced_code", "sane_lists"],
)

cover = """
<div class="cover">
  <div class="cover-inner">
    <div class="cover-top">网络工具实战手册</div>
    <div class="cover-icon">🚀</div>
    <h1 class="cover-title">Shadowrocket</h1>
    <h1 class="cover-title">链式代理</h1>
    <h2 class="cover-subtitle">完整配置教程 · 中转 · 住宅 · 多跳 · 分流</h2>
    <div class="cover-meta">
      <div>10 章实战 · 5 种典型拓扑 · 1 份速查卡</div>
      <div>逐字步骤 · 排错清单 · 调优技巧</div>
      <div>从入门到上手 · 30 分钟读完即可落地</div>
    </div>
    <div class="cover-bottom">出品 · 由 Kiro 协助整理</div>
  </div>
</div>
<div class="page-break"></div>
"""

html_full = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="utf-8"/><title>Shadowrocket 链式代理完整配置教程</title></head>
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
    content: "Shadowrocket 链式代理完整配置教程";
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
  background: linear-gradient(135deg, #0ea5e9 0%, #2563eb 35%, #1e40af 70%, #1e1b4b 100%);
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
  opacity: 0.9;
  margin-bottom: 20pt;
  color: #bae6fd;
}
.cover-icon {
  font-size: 90pt;
  margin: 10pt 0 20pt 0;
}
.cover-title {
  font-size: 60pt;
  font-weight: 900;
  margin: 0;
  letter-spacing: 4pt;
  text-shadow: 0 4px 24px rgba(14, 165, 233, 0.5);
  line-height: 1.15;
  background: linear-gradient(90deg, #fff 0%, #bae6fd 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.cover-subtitle {
  font-size: 20pt;
  font-weight: 400;
  margin-top: 24pt;
  opacity: 0.95;
  letter-spacing: 1pt;
  color: #e0f2fe;
}
.cover-meta {
  margin-top: 60pt;
  font-size: 14pt;
  line-height: 2.2;
  opacity: 0.95;
  color: #dbeafe;
}
.cover-bottom {
  margin-top: 70pt;
  font-size: 11pt;
  opacity: 0.7;
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
  color: #1e40af;
  line-height: 1.4;
  page-break-after: avoid;
  font-weight: 800;
}
h1 {
  font-size: 28pt;
  border-bottom: 4px solid #2563eb;
  padding-bottom: 10pt;
  margin-top: 30pt;
  margin-bottom: 22pt;
  page-break-before: always;
}
.content h1:first-child { page-break-before: auto; }
h2 {
  font-size: 21pt;
  border-left: 6px solid #2563eb;
  padding-left: 14pt;
  margin-top: 28pt;
  margin-bottom: 14pt;
  color: #1e3a8a;
}
h3 {
  font-size: 17pt;
  margin-top: 22pt;
  margin-bottom: 10pt;
  color: #1e40af;
}
h4 {
  font-size: 14.5pt;
  color: #333;
  margin-top: 18pt;
}
h5 {
  font-size: 13.5pt;
  color: #555;
}

p {
  margin: 8pt 0;
  text-align: justify;
}

blockquote {
  background: #dbeafe;
  border-left: 5px solid #2563eb;
  padding: 12pt 18pt;
  margin: 14pt 0;
  color: #1f2937;
  font-size: 12.5pt;
  border-radius: 4pt;
}

code {
  font-family: "Noto Sans Mono CJK SC", "Courier New", monospace;
  font-size: 11.5pt;
  background: #e0f2fe;
  color: #1e40af;
  padding: 2pt 6pt;
  border-radius: 4pt;
}
pre {
  background: #0f172a;
  color: #e2e8f0;
  padding: 14pt 16pt;
  border-radius: 6pt;
  overflow-x: auto;
  font-size: 10.5pt;
  line-height: 1.65;
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
  font-size: 12pt;
  page-break-inside: avoid;
}
th {
  background: #2563eb;
  color: #fff;
  padding: 9pt 10pt;
  text-align: left;
  border: 1px solid #2563eb;
  font-size: 12.5pt;
  font-weight: 700;
}
td {
  padding: 8pt 10pt;
  border: 1px solid #c7d2fe;
  vertical-align: top;
}
tr:nth-child(even) td { background: #eff6ff; }

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
  border-top: 1.5px dashed #93c5fd;
  margin: 22pt 0;
}

a {
  color: #2563eb;
  text-decoration: none;
  word-break: break-all;
}

strong {
  color: #b91c1c;
  font-weight: 700;
}
em {
  color: #475569;
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
