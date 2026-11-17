#!/usr/bin/env python3
"""Generate 1200x630 OG image for Aria (aria-tv/aria) using the site's exact dark-mode palette."""
from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1200, 630
BG = (9, 9, 11)          # --bg-color dark #09090b
TEXT = (250, 250, 250)   # --text-color dark #fafafa
MUTED = (161, 161, 170)  # --muted-text-color #a1a1aa
ACCENT = (129, 140, 248) # --accent-color dark #818cf8
BORDER = (39, 39, 42)    # --border-color dark #27272a

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# subtle radial glow behind the mark
for i in range(120, 0, -1):
    alpha = i / 120
    r = int(ACCENT[0] * alpha * 0.16 + BG[0])
    g = int(ACCENT[1] * alpha * 0.16 + BG[1])
    b = int(ACCENT[2] * alpha * 0.16 + BG[2])
    d.ellipse([600 - i * 2.6, 180 - i * 2.6, 600 + i * 2.6, 180 + i * 2.6], fill=(r, g, b))

def font(path, size):
    return ImageFont.truetype(path, size)

F_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
F_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# TV / play mark at top-center
cx, cy = 600, 170
# rounded TV frame
frame = [cx - 70, cy - 48, cx + 70, cy + 48]
d.rounded_rectangle(frame, radius=16, outline=ACCENT, width=5)
# play triangle
d.polygon([(cx - 24, cy - 26), (cx - 24, cy + 26), (cx + 38, cy)], fill=ACCENT)
# antenna
d.line([(cx - 40, cy - 48), (cx - 70, cy - 95)], fill=MUTED, width=5)
d.line([(cx + 40, cy - 48), (cx + 70, cy - 95)], fill=MUTED, width=5)
d.ellipse([cx - 70 - 7, cy - 95 - 7, cx - 70 + 7, cy - 95 + 7], outline=MUTED, width=4)
d.ellipse([cx + 70 - 7, cy - 95 - 7, cx + 70 + 7, cy - 95 + 7], outline=MUTED, width=4)

# wordmark
f_word = font(F_BOLD, 96)
d.text((600, 300), "Aria", font=f_word, fill=TEXT, anchor="mm")

# tagline
f_tag = font(F_REG, 34)
tag = "A curated, high-quality collection of IPTV channels"
d.text((600, 392), tag, font=f_tag, fill=MUTED, anchor="mm")
tag2 = "from around the world."
d.text((600, 436), tag2, font=f_tag, fill=MUTED, anchor="mm")

# domain pill
pill_w = 300
pill_h = 52
pill_x0 = 600 - pill_w // 2
pill_y0 = 500
d.rounded_rectangle([pill_x0, pill_y0, pill_x0 + pill_w, pill_y0 + pill_h], radius=26, outline=BORDER, width=3)
f_dom = font(F_BOLD, 28)
d.text((600, pill_y0 + pill_h // 2), "aria.5x0.org", font=f_dom, fill=TEXT, anchor="mm")

img.save("og-image.png")
print("saved og-image.png", img.size)