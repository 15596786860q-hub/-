#!/usr/bin/env python3
"""SukiSU Ultra + SUSFS + KPM 反检测环境完整配置手册 → PDF (大字版)"""
from pathlib import Path
import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

BASE = Path(__file__).parent
SRC_MD = BASE / "SukiSU_Ultra反检测环境完整配置手册.md"
OUT_PDF = BASE / "SukiSU_Ultra反检测环境完整配置手册.pdf"

md_text = SRC_MD.read_text(encoding="utf-8")

html_body = markdown.markdown(
    md_text,
    extensions=["extra", "codehilite", "toc", "tables", "fenced_code", "sane_lists"],
)

cover = """
<div class="cover">
  <div class="cover-inner">
    <div class="cover-top">虚拟服务自动化系列 · 第 4 部</div>
    <div class="cover-icon">⚙️</div>
    <h1 class="cover-title">SukiSU Ultra</h1>
    <h1 class="cover-title">反检测环境</h1>
    <h2 class="cover-subtitle">GKI · SUSFS · KPM · 内核级隐藏完整配置</h2>
    <div class="cover-meta">
      <div>2026 年安卓侧最强反检测组合</div>
      <div>刷机 · 模块 · keybox · KPM · 体检 · 调优</div>
      <div>过 Play Integrity 强完整性 · 风控通过率 90%+</div>
    </div>
    <div class="cover-bottom">出品 · 由 Kiro 协助整理</div>
  </div>
</div>
<div class="page-break"></div>
"""

html_full = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="utf-8"/><title>SukiSU Ultra 反检测环境完整配置手册</title></head>
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
    content: "SukiSU Ultra 反检测环境配置手册";
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
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 30%, #312e81 70%, #4c1d95 100%);
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
  color: #c4b5fd;
}
.cover-icon {
  font-size: 90pt;
  margin: 10pt 0 20pt 0;
}
.cover-title {
  font-size: 56pt;
  font-weight: 900;
  margin: 0;
  letter-spacing: 4pt;
  text-shadow: 0 4px 24px rgba(139, 92, 246, 0.5);
  line-height: 1.15;
  background: linear-gradient(90deg, #fff 0%, #c4b5fd 100%);
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
  color: #ddd6fe;
}
.cover-meta {
  margin-top: 60pt;
  font-size: 14pt;
  line-height: 2.2;
  opacity: 0.95;
  color: #e9d5ff;
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
  color: #5b21b6;
  line-height: 1.4;
  page-break-after: avoid;
  font-weight: 800;
}
h1 {
  font-size: 28pt;
  border-bottom: 4px solid #7c3aed;
  padding-bottom: 10pt;
  margin-top: 30pt;
  margin-bottom: 22pt;
  page-break-before: always;
}
.content h1:first-child { page-break-before: auto; }
h2 {
  font-size: 21pt;
  border-left: 6px solid #7c3aed;
  padding-left: 14pt;
  margin-top: 28pt;
  margin-bottom: 14pt;
  color: #4c1d95;
}
h3 {
  font-size: 17pt;
  margin-top: 22pt;
  margin-bottom: 10pt;
  color: #5b21b6;
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
  background: #f3e8ff;
  border-left: 5px solid #7c3aed;
  padding: 12pt 18pt;
  margin: 14pt 0;
  color: #1f2937;
  font-size: 12.5pt;
}

code {
  font-family: "Noto Sans Mono CJK SC", "Courier New", monospace;
  font-size: 11.5pt;
  background: #ede9fe;
  color: #5b21b6;
  padding: 2pt 6pt;
  border-radius: 4pt;
}
pre {
  background: #0f172a;
  color: #e2e8f0;
  padding: 14pt 16pt;
  border-radius: 6pt;
  overflow-x: auto;
  font-size: 11pt;
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
  font-size: 11pt;
}

table {
  border-collapse: collapse;
  width: 100%;
  margin: 14pt 0;
  font-size: 12pt;
  page-break-inside: avoid;
}
th {
  background: #7c3aed;
  color: #fff;
  padding: 9pt 10pt;
  text-align: left;
  border: 1px solid #7c3aed;
  font-size: 12.5pt;
  font-weight: 700;
}
td {
  padding: 8pt 10pt;
  border: 1px solid #e9d5ff;
  vertical-align: top;
}
tr:nth-child(even) td { background: #faf5ff; }

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
  border-top: 1.5px dashed #c4b5fd;
  margin: 22pt 0;
}

a {
  color: #7c3aed;
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
