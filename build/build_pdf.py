"""README + projects/*.md → build/out/portfolio.html → portfolio.pdf (Chrome headless)."""
import glob, os, subprocess, markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "build", "out")
os.makedirs(OUT, exist_ok=True)
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

files = [os.path.join(ROOT, "README.md")] + sorted(glob.glob(os.path.join(ROOT, "projects", "*.md")))
sections = []
for f in files:
    md = open(f, encoding="utf-8").read()
    md = md.replace("](../figures/", "](file://" + os.path.join(ROOT, "figures") + "/")
    md = md.replace("](projects/", "](file://" + os.path.join(ROOT, "projects") + "/")
    html = markdown.markdown(md, extensions=["tables"])
    sections.append(f"<section>{html}</section>")
# 꼬리말은 마지막 section 안에 넣어야 별도 쪽으로 밀리지 않는다
sections[-1] = sections[-1].replace("</section>", '<p class="foot">김영민 포트폴리오 · 2026.09</p></section>')

css = open(os.path.join(ROOT, "build", "style.css"), encoding="utf-8").read()
doc = f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>김영민 포트폴리오</title><style>{css}</style></head><body>{"".join(sections)}</body></html>'
html_path = os.path.join(OUT, "portfolio.html")
open(html_path, "w", encoding="utf-8").write(doc)

pdf_path = os.path.join(OUT, "portfolio.pdf")
subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=8000",
                f"--print-to-pdf={pdf_path}", f"file://{html_path}"], check=True, capture_output=True)
import pdfplumber
with pdfplumber.open(pdf_path) as d:
    print(f"PDF {os.path.getsize(pdf_path)/1024:.0f}KB, {len(d.pages)}쪽 → {pdf_path}")
