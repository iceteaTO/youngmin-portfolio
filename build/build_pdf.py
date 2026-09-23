"""README + projects/*.md → build/out/portfolio.html → portfolio.pdf (Chrome headless)."""
import glob, os, subprocess, markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "build", "out")
os.makedirs(OUT, exist_ok=True)
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

files = [os.path.join(ROOT, "README.md")] + sorted(glob.glob(os.path.join(ROOT, "projects", "*.md")))
sections = []
n_proj = len(files) - 1
for i, f in enumerate(files):
    md = open(f, encoding="utf-8").read()
    md = md.replace("](../figures/", "](file://" + os.path.join(ROOT, "figures") + "/")
    md = md.replace("](projects/", "](file://" + os.path.join(ROOT, "projects") + "/")
    html = markdown.markdown(md, extensions=["tables"])
    # 한 section = 한 쪽. 프로젝트 쪽은 머리에 번호, 모든 쪽 아래에 쪽번호
    kicker = f'<p class="kicker">프로젝트 {i} / {n_proj}</p>' if i else ""
    foot = f'<p class="foot"><span>김영민 포트폴리오 · 2026.09</span><span>{i + 1} / {len(files)}</span></p>'
    cls = "project" if i else "cover"
    sections.append(f'<section class="{cls}">{kicker}{html}{foot}</section>')

FONTS = {"NotoSansCJKkr-Regular.otf": "Sans/OTF/Korean/NotoSansCJKkr-Regular.otf",
         "NotoSansCJKkr-Bold.otf": "Sans/OTF/Korean/NotoSansCJKkr-Bold.otf",
         "NotoSerifCJKkr-Bold.otf": "Serif/OTF/Korean/NotoSerifCJKkr-Bold.otf"}
font_dir = os.path.join(ROOT, "build", "fonts")
os.makedirs(font_dir, exist_ok=True)
for name, path in FONTS.items():
    if not os.path.exists(os.path.join(font_dir, name)):
        subprocess.run(["curl", "-sL", "-o", os.path.join(font_dir, name),
                        f"https://github.com/notofonts/noto-cjk/raw/main/{path}"], check=True)
css = open(os.path.join(ROOT, "build", "style.css"), encoding="utf-8").read().replace("FONTDIR", "file://" + font_dir)
doc = f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>김영민 포트폴리오</title><style>{css}</style></head><body>{"".join(sections)}</body></html>'
html_path = os.path.join(OUT, "portfolio.html")
open(html_path, "w", encoding="utf-8").write(doc)

pdf_path = os.path.join(OUT, "portfolio.pdf")
subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=15000",
                f"--print-to-pdf={pdf_path}", f"file://{html_path}"], check=True, capture_output=True)
import pdfplumber
with pdfplumber.open(pdf_path) as d:
    print(f"PDF {os.path.getsize(pdf_path)/1024:.0f}KB, {len(d.pages)}쪽 → {pdf_path}")
