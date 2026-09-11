"""Render this fictional AURORA kit; no API calls or generation charges."""

from pathlib import Path
import os
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

ROOT = Path(__file__).resolve().parent
FONT_DIR = Path(os.environ.get("AURORA_FONT_DIR", "/System/Library/Fonts/Supplemental"))
NAVY, BLUE, ICE = "#101D38", "#2057BD", "#EAF2FA"
catalog = Image.open(ROOT / "catalog.png").convert("RGB")


def text(draw, xy, value, size, color=NAVY, bold=False):
    font = ImageFont.truetype(str(FONT_DIR / ("Arial Bold.ttf" if bold else "Arial.ttf")), size)
    draw.text(xy, value, font=font, fill=color)


card = Image.new("RGB", (1440, 1080), "white")
d = ImageDraw.Draw(card)
text(d, (76, 64), "A U R O R A", 34, bold=True)
text(d, (76, 260), "A study", 100, bold=True)
text(d, (76, 368), "in blue.", 100, bold=True)
d.rectangle((76, 516, 148, 524), fill=BLUE)
text(d, (76, 572), "Cobalt glass.", 31)
text(d, (76, 620), "A clean silhouette.", 31)
text(d, (76, 958), "FICTIONAL PRODUCT / VISUAL CONCEPT", 18)
product = catalog.resize((1000, 1000), Image.Resampling.LANCZOS)
card.paste(product.crop((270, 0, 760, 1000)), (878, 40))
card.save(ROOT / "brand-card.png")

detail = Image.new("RGB", (1080, 1080), ICE)
d = ImageDraw.Draw(detail)
text(d, (64, 58), "A U R O R A  /  DETAIL", 27, bold=True)
text(d, (64, 132), "Color. Form. Light.", 66, bold=True)
crop = catalog.crop((530, 585, 1510, 1565)).resize((850, 850), Image.Resampling.LANCZOS)
detail.paste(crop, (115, 280))
detail.save(ROOT / "detail.png")

# Original geometry, not a traced raster; wordmark remains editable SVG text.
(ROOT / "wordmark.svg").write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 130">
  <title>AURORA fictional concept wordmark</title>
  <path d="M24 102 69 24 114 102M44 70H94" fill="none" stroke="{BLUE}" stroke-width="7"/>
  <text x="146" y="91" font-family="Arial, sans-serif" font-size="60" letter-spacing="7" fill="{NAVY}">AURORA</text>
</svg>''')

c = canvas.Canvas(str(ROOT / "brand-guide.pdf"), pagesize=(960, 720))
c.setTitle("AURORA — fictional identity and listing kit")
c.setAuthor("Magic Hour")


def page(number, title):
    c.setFillColor(HexColor(NAVY))
    c.setFont("Helvetica-Bold", 14)
    c.drawString(54, 668, "A U R O R A")
    c.setFont("Helvetica", 10)
    c.drawRightString(906, 668, f"VISUAL IDENTITY / {number:02d}")
    c.setFont("Helvetica-Bold", 36)
    c.drawString(54, 588, title)


page(1, "A study in blue.")
c.drawImage(str(ROOT / "brand-card.png"), 36, 100, 888, 444, preserveAspectRatio=True, anchor="c")
c.setFont("Helvetica", 12)
c.drawString(54, 62, "Fictional concept. Original Magic Hour imagery with exact, editable layout and type.")
c.showPage()
page(2, "Identity that stays consistent.")
for i, (name, color) in enumerate((("MIDNIGHT", NAVY), ("COBALT", BLUE), ("ICE", ICE))):
    x = 54 + i * 294
    c.setFillColor(HexColor(color))
    c.rect(x, 370, 264, 150, fill=1, stroke=0)
    c.setFillColor(HexColor(NAVY))
    c.setFont("Helvetica-Bold", 13)
    c.drawString(x, 342, name)
    c.setFont("Helvetica", 13)
    c.drawString(x, 320, color)
c.setFont("Helvetica-Bold", 22)
c.drawString(54, 248, "Clear type. Precise copy. One product.")
c.setFont("Helvetica", 14)
for y, line in zip((210, 184, 158, 132, 106), (
    "Arial Bold for display; Arial for supporting copy. Keep text editable.",
    "Use navy text on white or ice. Cobalt is an accent, not a small-text default.",
    "Keep the supplied bottle and its printed AURORA label unchanged.",
    "The separate wordmark is a new concept; it does not replace the product label.",
    "No invented ingredients, size, performance, certifications or endorsements.",
)):
    c.drawString(54, y, line)
c.showPage()
page(3, "Build from accepted assets.")
c.drawImage(str(ROOT / "catalog.png"), 54, 210, 340, 340, preserveAspectRatio=True)
c.setFillColor(HexColor(NAVY))
c.setFont("Helvetica-Bold", 23)
c.drawString(442, 514, "One generated catalog edit.")
c.setFont("Helvetica", 14)
for y, line in zip((470, 440, 410, 350, 320, 290, 260), (
    "catalog.png   /   2048 x 2048 original MCP output",
    "detail.png   /   crop and editable render recipe",
    "brand-card.png   /   exact type and placement",
    "wordmark.svg   /   original paths + editable text",
    "render.py   /   local layout and PDF source",
    "README.md   /   prompts, cost and limitations",
    "No additional generation for a copy-only revision.",
)):
    c.drawString(442, y, line)
c.setFont("Helvetica", 12)
c.drawString(54, 110, "This demonstrates a fictional product page, not approval for a particular marketplace.")
c.drawString(54, 86, "The small original reference cannot verify unseen construction or exact material properties.")
c.save()
