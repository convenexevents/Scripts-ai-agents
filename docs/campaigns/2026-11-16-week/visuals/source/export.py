"""Rebuild every visual for the 16-22 Nov 2026 week from gen.py.

Usage (from anywhere):
    python3 export.py

Steps: gen.py writes the HTML into a temp folder; headless Chrome prints the
2 carousels to PDF and screenshots the 2 cards at 1080 x 1350; the PDF page
box is trimmed to exactly 810 x 1012.5 pt (1080 x 1350 px), because Chrome
rounds the page up to 14.07in and leaves an unpainted white hairline at the
foot of every slide; then contact-sheet.png is rebuilt from the outputs.

Needs: google-chrome, pdftoppm (poppler), Python with pypdf and Pillow.
Added by Felix (brand review, 10 Nov 2026). Copy still comes only from gen.py.
"""
import pathlib, subprocess, sys, tempfile

from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject
from PIL import Image, ImageDraw, ImageFont

SRC = pathlib.Path(__file__).resolve().parent
VIS = SRC.parent
CHROME = "google-chrome"
FLAGS = ["--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
         "--no-pdf-header-footer", "--virtual-time-budget=15000"]

PDFS = {"mon": "2026-11-16-mon-carousel-7-slides.pdf", "thu": "2026-11-19-thu-carousel-8-slides.pdf"}
PNGS = {"wed": "2026-11-18-wed-stat-card.png", "sat": "2026-11-21-sat-checklist-card.png"}
PAGE_H_PT = 1012.5  # 1350 px at 0.75 pt/px


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def trim(pdf: pathlib.Path):
    r, w = PdfReader(str(pdf)), PdfWriter()
    for p in r.pages:
        x0, _, x1, y1 = [float(v) for v in p.mediabox]
        box = RectangleObject([x0, y1 - PAGE_H_PT, x1, y1])
        p.mediabox = box
        p.cropbox = box
        w.add_page(p)
    with open(pdf, "wb") as f:
        w.write(f)


def contact_sheet(tmp: pathlib.Path):
    rows = []
    for key, n in (("mon", 7), ("thu", 8)):
        run(["pdftoppm", "-r", "96", "-png", str(VIS / PDFS[key]), str(tmp / key)])
        files = sorted(tmp.glob(f"{key}-*.png"), key=lambda f: int(f.stem.split("-")[-1]))
        assert len(files) == n, (key, len(files))
        rows.append((f"{key.capitalize()} carousel ({n} slides)", files))
    rows.append(("Wed stat card / Sat checklist card", [VIS / PNGS["wed"], VIS / PNGS["sat"]]))
    tw, th, gap, pad, lab = 238, 298, 11, 11, 34
    W = pad * 2 + 8 * tw + 7 * gap
    H = sum(lab + th + gap for _ in rows) + pad
    sheet = Image.new("RGB", (W, H), "#141414")
    d = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 14)
    except OSError:
        font = ImageFont.load_default()
    y = pad
    for label, files in rows:
        d.text((pad, y + 8), label, fill="#FCD500", font=font)
        y += lab
        for i, f in enumerate(files):
            im = Image.open(f).convert("RGB").resize((tw, th), Image.LANCZOS)
            x = pad + i * (tw + gap)
            sheet.paste(im, (x, y))
            d.rectangle([x - 1, y - 1, x + tw, y + th], outline="#3A3A3A")
        y += th + gap
    sheet.save(VIS / "contact-sheet.png")


def main():
    with tempfile.TemporaryDirectory() as t:
        tmp = pathlib.Path(t)
        run([sys.executable, str(SRC / "gen.py"), str(tmp), str(SRC / "logo-footer.svg")])
        for key, name in PDFS.items():
            out = VIS / name
            run([CHROME, *FLAGS, f"--print-to-pdf={out}", (tmp / f"{key}.html").as_uri()])
            trim(out)
        for key, name in PNGS.items():
            run([CHROME, *FLAGS, "--window-size=1080,1350", f"--screenshot={VIS / name}",
                 (tmp / f"{key}.html").as_uri()])
        contact_sheet(tmp)
    print("ok")


if __name__ == "__main__":
    main()
