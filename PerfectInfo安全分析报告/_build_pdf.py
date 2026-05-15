#!/usr/bin/env python3
"""PerfecttheinformationActivity 安全分析报告 Markdown -> PDF (大字号版)"""
from pathlib import Path
import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

BASE = Path(__file__).parent
SRC_MD = BASE / "PerfectInfo安全分析报告.md"
OUT_PDF = BASE / "PerfectInfo安全分析报告.pdf"

md_text = SRC_MD.read_text(encoding="utf-8")

html_body = markdown.markdown(
    md_text,
    extensions=["extra", "codehilite", "toc", "tables", "fenced_code", "sane_lists"],
)

cover = """
<div class="cover">
  <div class="cover-inner">
    <div class="cover-top">SECURITY RESEARCH &middot; CONFIDENTIAL</div>
    <div class="cover-icon">&#128274;</div>
    <h1 class="cover-title">PerfectInfo<br/>安全分析报告</h1>
    <h2 class="cover-subtitle">PerfecttheinformationActivity 模块</h2>
    <div class="cover-meta">
      <div>报告编号：SEC-2026-0515-002</div>
      <div>风险评级：高 (High)</div>
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
<head><meta charset="utf-8"/><title>PerfectInfo 安全分析报告</title></head>
<body>
{cover}
<div class="content">
{html_body}
</div>
</body>
</html>
"""

# ====== 大字号 CSS（正文 14pt，比上一版的 10.5pt 加大 ~33%） ======
CSS_TEXT = """
@page {
  size: A4;
  margin: 2cm 1.8cm 2.2cm 1.8cm;
  @bottom-center {
    content: counter(page) " / " counter(pages);
    font-family: "Noto Sans CJK SC", sans-serif;
    font-size: 11pt;
    color: #888;
  }
  @top-right {
    content: "PerfectInfo 安全分析报告 \\00B7 SEC-2026-0515-002";
    font-family: "Noto Sans CJK SC", sans-serif;
    font-size: 11pt;
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
  background: linear-gradient(135deg, #0f1c3f 0%, #007a4d 100%);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}
.cover-inner { padding: 40px; }
.cover-top {
  font-size: 13pt;
  letter-spacing: 4pt;
  opacity: 0.85;
  margin-bottom: 30pt;
  font-weight: 600;
}
.cover-icon {
  font-size: 80pt;
  margin: 10pt 0 24pt 0;
}
.cover-title {
  font-size: 54pt;
  font-weight: 900;
  margin: 0;
  letter-spacing: 3pt;
  line-height: 1.25;
  text-shadow: 0 4px 20px rgba(0,0,0,0.4);
}
.cover-subtitle {
  font-size: 22pt;
  font-weight: 400;
  margin-top: 18pt;
  opacity: 0.95;
  letter-spacing: 2pt;
}
.cover-meta {
  margin-top: 70pt;
  font-size: 14pt;
  line-height: 2.2;
  opacity: 0.92;
}
.cover-bottom {
  margin-top: 70pt;
  font-size: 11pt;
  opacity: 0.7;
  line-height: 1.7;
}

html, body {
  font-family: "Noto Sans CJK SC", "Noto Sans", sans-serif;
  font-size: 14pt;            /* 正文加大到 14pt */
  line-height: 1.85;
  color: #1a1a1a;             /* 颜色加深，更清晰 */
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
  font-size: 28pt;             /* 一级标题加大 */
  border-bottom: 3px solid #007a4d;
  padding-bottom: 10pt;
  margin-top: 32pt;
  margin-bottom: 22pt;
  page-break-before: always;
}
.content h1:first-child { page-break-before: auto; }
h2 {
  font-size: 20pt;
  border-left: 6px solid #007a4d;
  padding-left: 12pt;
  margin-top: 28pt;
  margin-bottom: 14pt;
  color: #0f1c3f;
}
h3 {
  font-size: 17pt;
  margin-top: 22pt;
  color: #007a4d;
}
h4 { font-size: 15pt; color: #333; margin-top: 16pt; }
h5 { font-size: 14pt; color: #555; }

p { margin: 8pt 0; text-align: justify; }

blockquote {
  background: #f0fdf4;
  border-left: 5px solid #007a4d;
  padding: 12pt 16pt;
  margin: 12pt 0;
  color: #1a1a1a;
  font-size: 13.5pt;
}

code {
  font-family: "Noto Sans Mono CJK SC", "Courier New", monospace;
  font-size: 12pt;
  background: #f4f5f7;
  color: #b8002a;
  padding: 2pt 6pt;
  border-radius: 3pt;
}
pre {
  background: #1e2235;
  color: #f8f8f2;
  padding: 14pt;
  border-radius: 5pt;
  overflow-x: auto;
  font-size: 11pt;            /* 代码区也比上一版大 */
  line-height: 1.65;
  page-break-inside: avoid;
  white-space: pre-wrap;
  word-wrap: break-word;
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
  margin: 12pt 0;
  font-size: 12.5pt;
  page-break-inside: avoid;
}
th {
  background: #0f1c3f;
  color: #fff;
  padding: 8pt 10pt;
  text-align: left;
  border: 1px solid #0f1c3f;
}
td {
  padding: 7pt 10pt;
  border: 1px solid #ddd;
  vertical-align: top;
}
tr:nth-child(even) td { background: #f7f8fc; }

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
  border-top: 1.5px dashed #bbb;
  margin: 22pt 0;
}

a {
  color: #007a4d;
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
