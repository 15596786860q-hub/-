#!/usr/bin/env python3
"""Android 应用安全分析报告 Markdown -> PDF"""
from pathlib import Path
import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

BASE = Path(__file__).parent
SRC_MD = BASE / "Android应用安全分析报告.md"
OUT_PDF = BASE / "Android应用安全分析报告.pdf"

md_text = SRC_MD.read_text(encoding="utf-8")

html_body = markdown.markdown(
    md_text,
    extensions=["extra", "codehilite", "toc", "tables", "fenced_code", "sane_lists"],
)

cover = """
<div class="cover">
  <div class="cover-inner">
    <div class="cover-top">SECURITY RESEARCH · CONFIDENTIAL</div>
    <div class="cover-icon">&#128274;</div>
    <h1 class="cover-title">Android 应用<br/>安全分析报告</h1>
    <h2 class="cover-subtitle">RealPersonAuthActivity 模块</h2>
    <div class="cover-meta">
      <div>报告编号：SEC-2026-0515-001</div>
      <div>风险评级：严重 (Critical)</div>
      <div>报告日期：2026-05-15</div>
    </div>
    <div class="cover-bottom">
      仅用于安全研究与教学，禁止用于任何非法用途<br/>
      由 Kiro 协助整理
    </div>
  </div>
</div>
<div class="page-break"></div>
"""

html_full = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="utf-8"/><title>Android 应用安全分析报告</title></head>
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
    content: "Android 安全分析报告 · SEC-2026-0515-001";
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
  background: linear-gradient(135deg, #0f1c3f 0%, #b8002a 100%);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}
.cover-inner { padding: 40px; }
.cover-top {
  font-size: 11pt;
  letter-spacing: 4pt;
  opacity: 0.85;
  margin-bottom: 30pt;
  font-weight: 600;
}
.cover-icon {
  font-size: 70pt;
  margin: 10pt 0 24pt 0;
}
.cover-title {
  font-size: 48pt;
  font-weight: 900;
  margin: 0;
  letter-spacing: 3pt;
  line-height: 1.25;
  text-shadow: 0 4px 20px rgba(0,0,0,0.4);
}
.cover-subtitle {
  font-size: 20pt;
  font-weight: 400;
  margin-top: 18pt;
  opacity: 0.95;
  letter-spacing: 2pt;
}
.cover-meta {
  margin-top: 70pt;
  font-size: 12pt;
  line-height: 2.2;
  opacity: 0.92;
}
.cover-bottom {
  margin-top: 70pt;
  font-size: 9pt;
  opacity: 0.7;
  line-height: 1.7;
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
  color: #0f1c3f;
  line-height: 1.4;
  page-break-after: avoid;
}
h1 {
  font-size: 22pt;
  border-bottom: 3px solid #b8002a;
  padding-bottom: 8pt;
  margin-top: 30pt;
  margin-bottom: 18pt;
  page-break-before: always;
}
.content h1:first-child { page-break-before: auto; }
h2 {
  font-size: 16pt;
  border-left: 5px solid #b8002a;
  padding-left: 10pt;
  margin-top: 24pt;
  margin-bottom: 12pt;
  color: #0f1c3f;
}
h3 {
  font-size: 13pt;
  margin-top: 18pt;
  color: #b8002a;
}
h4 { font-size: 11.5pt; color: #444; }
h5 { font-size: 10.8pt; color: #555; }

p { margin: 6pt 0; text-align: justify; }

blockquote {
  background: #fff5f5;
  border-left: 4px solid #b8002a;
  padding: 10pt 14pt;
  margin: 10pt 0;
  color: #333;
}

code {
  font-family: "Noto Sans Mono CJK SC", "Courier New", monospace;
  font-size: 9.5pt;
  background: #f4f5f7;
  color: #b8002a;
  padding: 1pt 5pt;
  border-radius: 3pt;
}
pre {
  background: #1e2235;
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
  background: #0f1c3f;
  color: #fff;
  padding: 6pt 8pt;
  text-align: left;
  border: 1px solid #0f1c3f;
}
td {
  padding: 5pt 8pt;
  border: 1px solid #ddd;
  vertical-align: top;
}
tr:nth-child(even) td { background: #f7f8fc; }

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
  color: #b8002a;
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
print(f"PDF 已生成: {OUT_PDF}")
print(f"文件大小: {OUT_PDF.stat().st_size / 1024:.1f} KB")
