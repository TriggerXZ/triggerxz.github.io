#!/usr/bin/env python3
"""Generate OG social image (1200x630) for the AI agents service landing."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG = (13, 17, 23)       # #0d1117
CARD = (22, 27, 34)     # #161b22
BORDER = (48, 54, 61)   # #30363d
GREEN = (126, 231, 135) # #7ee787
MUTED = (139, 148, 158) # #8b949e
FG = (230, 237, 243)    # #e6edf3

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# subtle radial-ish glow at top
for i in range(60):
    alpha = 6 - i // 12
    if alpha <= 0:
        break
    d.ellipse([W//2 - 520 + i*4, -120 + i*2, W//2 + 520 - i*4, 220 - i*2], fill=(40, 90, 50, 0))

f_big = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 72)
f_mid = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 30)
f_small = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 26)

# badge
badge = "INDEPENDENT AI AGENT BUILDER"
d.rounded_rectangle([60, 56, 60 + 320, 56 + 44], radius=22, fill=CARD, outline=BORDER)
d.text((82, 66), badge, font=f_small, fill=GREEN)

# headline
d.text((60, 150), "Custom AI agents that run", font=f_big, fill=FG)
d.text((60, 238), "your dev workflow on autopilot.", font=f_big, fill=GREEN)

# sub
sub = "Changelogs · Code review · CI safety · Weekly reporting — tested, documented, from $300"
d.text((60, 360), sub, font=f_mid, fill=MUTED)

# proof line
proof = "51/51 tests passing   ·   7 open-source tools   ·   github.com/TriggerXZ"
d.text((60, 440), proof, font=f_small, fill=(88, 166, 255))

# url pill bottom
d.rounded_rectangle([60, 512, 60 + 560, 512 + 52], radius=26, fill=GREEN)
d.text((96, 524), "triggerxz.github.io/ai-agents-service/", font=f_mid, fill=(13, 17, 23))

img.save("og-image.png")
print("og-image.png written")
