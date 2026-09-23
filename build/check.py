"""포트폴리오 검사: 상세 페이지 글자수, 금지 표현, PDF 크기·쪽수."""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANNED = ["7,200만", "llama2", "llama3", "Llama", "자체 개발", "25%", "40%", "멀티모달", "배포 서버", "plc-edge"]
ok = True

def body_chars(md: str) -> int:
    lines = []
    for line in md.splitlines():
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("|") or s.startswith("![") or s.startswith("*그림"):
            continue
        s = re.sub(r"\(https?://[^)]+\)", "", s)  # 링크 URL 제외
        s = s.replace("**", "")
        lines.append(s)
    return len("".join(lines))

mds = sorted(glob.glob(os.path.join(ROOT, "projects", "*.md")))
if not mds:
    print("FAIL: projects/*.md 없음"); ok = False
for p in mds:
    n = body_chars(open(p, encoding="utf-8").read())
    flag = "OK " if 400 <= n <= 600 else "FAIL"
    if flag == "FAIL": ok = False
    print(f"{flag} {os.path.relpath(p, ROOT)} 본문 {n}자 (400~600)")

for p in [os.path.join(ROOT, "README.md")] + mds:
    if not os.path.exists(p):
        continue
    t = open(p, encoding="utf-8").read()
    hits = [b for b in BANNED if b in t]
    if hits:
        print(f"FAIL {os.path.relpath(p, ROOT)} 금지 표현 {hits}"); ok = False

pdf = os.path.join(ROOT, "build", "out", "portfolio.pdf")
if os.path.exists(pdf):
    import pdfplumber
    size = os.path.getsize(pdf)
    with pdfplumber.open(pdf) as d:
        pages = len(d.pages)
    flag = "OK " if size <= 1_000_000 and 4 <= pages <= 7 else "FAIL"
    if flag == "FAIL": ok = False
    print(f"{flag} PDF {size/1024:.0f}KB, {pages}쪽 (1MB 이하, 4~7쪽)")

print("PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
