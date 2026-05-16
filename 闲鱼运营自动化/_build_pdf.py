#!/usr/bin/env python3
"""闲鱼店铺运营自动化架构 → PDF"""
from pathlib import Path
import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

BASE = Path(__file__).parent
SRC_MD = BASE / "闲鱼店铺运营自动化架构.md"
OUT_PDF = BASE / "闲鱼店铺运营自动化架构.pdf"

md_text = SRC_MD.read_text(encoding="utf-8")

html_body = markdown.markdown(
    md_text,
    extensions=["extra", "codehilite", "toc", "tables", "fenced_code", "sane_lists"],
)

cover = """
<div class="cover">
  <div class="cover-inner">
    <div class="cover-top">技术服务卖家 · 半自动化体系</div>
    <div class="cover-icon">🐟</div>
    <h1 class="cover-title">闲鱼店铺运营</h1>
    <h2 class="cover-subtitle">自动化架构</h2>
    <div class="cover-meta">
      <div>内容侧全自动 · 客服侧人机协同</div>
      <div>7 大模块 · 4 周落地 · 月成本 &lt; ¥50</div>
    </div>
    <div class="cover-bottom">出品:由 Kiro 协助整理</div>
  </div>
</div>
<div class="page-break"></div>
"""

html_full = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="utf-8"/><title>闲鱼店铺运营自动化架构</title></head>
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
  margin: 2cm 1.8cm 2.2cm 1.8cm;
  @bottom-center {
    content: counter(page) " / " counter(pages);
    font-family: "Noto Sans CJK SC", sans-serif;
    font-size: 9pt;
    color: #888;
  }
  @top-right {
    content: "闲鱼店铺运营自动化架构";
    font-family: "Noto Sans CJK SC", sans-serif;
    font-size: 9pt;
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
  background: linear-gradient(135deg, #ff5722 0%, #ffc107 100%);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}
.cover-inner { padding: 40px; }
.cover-top {
  font-size: 14pt;
  letter-spacing: 4pt;
  opacity: 0.95;
  margin-bottom: 20pt;
}
.cover-icon {
  font-size: 76pt;
  margin: 10pt 0 20pt 0;
}
.cover-title {
  font-size: 56pt;
  font-weight: 900;
  margin: 0;
  letter-spacing: 4pt;
  text-shadow: 0 4px 20px rgba(0,0,0,0.3);
}
.cover-subtitle {
  font-size: 32pt;
  font-weight: 400;
  margin-top: 14pt;
  opacity: 0.95;
  letter-spacing: 8pt;
}
.cover-meta {
  margin-top: 70pt;
  font-size: 12pt;
  line-height: 2;
  opacity: 0.95;
}
.cover-bottom {
  margin-top: 80pt;
  font-size: 10pt;
  opacity: 0.75;
}

html, body {
  font-family: "Noto Sans CJK SC", "Noto Sans", sans-serif;
  font-size: 10.5pt;
  line-height: 1.75;
  color: #222;
  margin: 0;
  padding: 0;
}
.page-break { page-break-before: always; }
.content { max-width: 100%; }

h1, h2, h3, h4, h5 {
  font-family: "Noto Sans CJK SC", sans-serif;
  color: #d84315;
  line-height: 1.4;
  page-break-after: avoid;
}
h1 {
  font-size: 22pt;
  border-bottom: 3px solid #ff5722;
  padding-bottom: 8pt;
  margin-top: 30pt;
  margin-bottom: 18pt;
  page-break-before: always;
}
.content h1:first-child { page-break-before: auto; }
h2 {
  font-size: 16pt;
  border-left: 5px solid #ff5722;
  padding-left: 10pt;
  margin-top: 24pt;
  margin-bottom: 12pt;
  color: #d84315;
}
h3 {
  font-size: 13pt;
  margin-top: 18pt;
  color: #bf360c;
}
h4 { font-size: 11.5pt; color: #444; }
h5 { font-size: 10.8pt; color: #555; }

p { margin: 6pt 0; text-align: justify; }

blockquote {
  background: #fff3e0;
  border-left: 4px solid #ff5722;
  padding: 10pt 14pt;
  margin: 10pt 0;
  color: #333;
}

code {
  font-family: "Noto Sans Mono CJK SC", "Courier New", monospace;
  font-size: 9.5pt;
  background: #f4f5f7;
  color: #d84315;
  padding: 1pt 5pt;
  border-radius: 3pt;
}
pre {
  background: #2d2d2d;
  color: #f8f8f2;
  padding: 12pt;
  border-radius: 5pt;
  overflow-x: auto;
  font-size: 9pt;
  line-height: 1.55;
  page-break-inside: avoid;
  white-space: pre-wrap;
  word-wrap: break-word;
}
pre code {
  background: none;
  color: inherit;
  padding: 0;
}

table {
  border-collapse: collapse;
  width: 100%;
  margin: 10pt 0;
  font-size: 9.5pt;
  page-break-inside: avoid;
}
th {
  background: #ff5722;
  color: #fff;
  padding: 6pt 8pt;
  text-align: left;
  border: 1px solid #ff5722;
}
td {
  padding: 5pt 8pt;
  border: 1px solid #ddd;
  vertical-align: top;
}
tr:nth-child(even) td { background: #fff8f3; }

ul, ol {
  margin: 6pt 0;
  padding-left: 22pt;
}
li {
  margin: 3pt 0;
  line-height: 1.7;
}

hr {
  border: none;
  border-top: 1.5px dashed #bbb;
  margin: 18pt 0;
}

a {
  color: #ff5722;
  text-decoration: none;
}

strong { color: #b8002a; font-weight: 700; }
em { color: #444; }
"""

font_config = FontConfiguration()
HTML(string=html_full, base_url=str(BASE)).write_pdf(
    str(OUT_PDF),
    stylesheets=[CSS(string=CSS_TEXT, font_config=font_config)],
    font_config=font_config,
)
print(f"PDF 已生成:{OUT_PDF}")
print(f"文件大小:{OUT_PDF.stat().st_size / 1024:.1f} KB")
