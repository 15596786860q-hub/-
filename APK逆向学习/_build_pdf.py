#!/usr/bin/env python3
"""合并 9 份 Markdown → HTML → PDF(中文)"""
import os
import re
from pathlib import Path

import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

BASE = Path(__file__).parent
OUT_HTML = BASE / "APK逆向学习_完整版.html"
OUT_PDF = BASE / "APK逆向学习_完整版.pdf"

# 按顺序合并
FILES = [
    "README.md",
    "00_从零开始_看这里.md",
    "01_知识架构_一张图看懂全貌.md",
    "02_名词大辞典_小白版.md",
    "03_工具手册_每个工具干什么用.md",
    "04_AI辅助学习法_怎么跟AI提问.md",
    "05_12周学习路线_每日任务.md",
    "06_实战案例集_从简单到难.md",
    "07_避坑指南_法律与常见问题.md",
]

# 合并 Markdown
merged_md = []
for fname in FILES:
    fpath = BASE / fname
    if not fpath.exists():
        print(f"跳过:{fname}(不存在)")
        continue
    content = fpath.read_text(encoding="utf-8")
    # 每个文件之间加分页符
    if merged_md:
        merged_md.append('\n\n<div class="page-break"></div>\n\n')
    merged_md.append(content)

md_text = "\n\n".join(merged_md)

# Markdown → HTML
html_body = markdown.markdown(
    md_text,
    extensions=["extra", "codehilite", "toc", "tables", "fenced_code", "sane_lists"],
)

# 封面 + 样式
cover = """
<div class="cover">
  <div class="cover-inner">
    <div class="cover-top">零基础 · AI 辅助</div>
    <h1 class="cover-title">APK 逆向学习</h1>
    <h2 class="cover-subtitle">完整小白文档</h2>
    <div class="cover-meta">
      <div>12 周学习路线 · 10 个实战案例</div>
      <div>80+ 术语辞典 · 23 个工具手册</div>
    </div>
    <div class="cover-bottom">出品:由 Kiro 协助整理</div>
  </div>
</div>
<div class="page-break"></div>
"""

html_full = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"/>
<title>APK 逆向学习 · 完整小白文档</title>
</head>
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
    content: "APK 逆向学习 · 小白完整文档";
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
  background: linear-gradient(135deg, #1a2980 0%, #26d0ce 100%);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}
.cover-inner { padding: 40px; }
.cover-top {
  font-size: 14pt;
  letter-spacing: 6pt;
  opacity: 0.85;
  margin-bottom: 30pt;
}
.cover-title {
  font-size: 58pt;
  font-weight: 900;
  margin: 0;
  letter-spacing: 4pt;
  text-shadow: 0 4px 20px rgba(0,0,0,0.3);
}
.cover-subtitle {
  font-size: 26pt;
  font-weight: 400;
  margin-top: 16pt;
  opacity: 0.95;
}
.cover-meta {
  margin-top: 80pt;
  font-size: 12pt;
  line-height: 2;
  opacity: 0.9;
}
.cover-bottom {
  margin-top: 100pt;
  font-size: 10pt;
  opacity: 0.7;
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
  color: #1a2980;
  line-height: 1.4;
  page-break-after: avoid;
}
h1 {
  font-size: 22pt;
  border-bottom: 3px solid #1a2980;
  padding-bottom: 8pt;
  margin-top: 30pt;
  margin-bottom: 18pt;
  page-break-before: always;
}
.content h1:first-child { page-break-before: auto; }
h2 {
  font-size: 16pt;
  border-left: 5px solid #26d0ce;
  padding-left: 10pt;
  margin-top: 24pt;
  margin-bottom: 12pt;
  color: #1a2980;
}
h3 {
  font-size: 13pt;
  margin-top: 18pt;
  color: #2a4fa8;
}
h4 {
  font-size: 11.5pt;
  color: #444;
}
h5 { font-size: 10.8pt; color: #555; }

p { margin: 6pt 0; text-align: justify; }

blockquote {
  background: #f0f7fa;
  border-left: 4px solid #26d0ce;
  padding: 10pt 14pt;
  margin: 10pt 0;
  color: #333;
  font-style: normal;
}

code {
  font-family: "Noto Sans Mono CJK SC", "Courier New", monospace;
  font-size: 9.5pt;
  background: #f4f5f7;
  color: #c7254e;
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
  background: #1a2980;
  color: #fff;
  padding: 6pt 8pt;
  text-align: left;
  border: 1px solid #1a2980;
}
td {
  padding: 5pt 8pt;
  border: 1px solid #ddd;
  vertical-align: top;
}
tr:nth-child(even) td { background: #f7f9fc; }

ul, ol {
  margin: 6pt 0;
  padding-left: 22pt;
}
li {
  margin: 3pt 0;
  line-height: 1.7;
}
li > ul, li > ol { margin: 2pt 0; }

hr {
  border: none;
  border-top: 1.5px dashed #bbb;
  margin: 18pt 0;
}

a {
  color: #1a6fd0;
  text-decoration: none;
}

strong { color: #b8002a; font-weight: 700; }
em { color: #444; }

/* 任务清单样式(GitHub 风格) */
ul li input[type="checkbox"] {
  margin-right: 5pt;
}
"""

# 处理图标字符,避免某些 emoji 缺字体导致渲染异常
# weasyprint 对 emoji 支持有限,这里保留原样即可

OUT_HTML.write_text(html_full, encoding="utf-8")
print(f"HTML 已生成:{OUT_HTML}")

font_config = FontConfiguration()
HTML(string=html_full, base_url=str(BASE)).write_pdf(
    str(OUT_PDF),
    stylesheets=[CSS(string=CSS_TEXT, font_config=font_config)],
    font_config=font_config,
)
print(f"PDF 已生成:{OUT_PDF}")
print(f"文件大小:{OUT_PDF.stat().st_size / 1024:.1f} KB")
