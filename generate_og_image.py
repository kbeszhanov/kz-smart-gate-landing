"""Generate og-image.png for smartgate.kz (1200x630)."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
output = os.path.join(os.path.dirname(__file__), 'og-image.png')

img = Image.new('RGB', (W, H), '#0b0f1a')
draw = ImageDraw.Draw(img)

# Grid pattern (subtle)
for x in range(0, W, 40):
    draw.line([(x, 0), (x, H)], fill='#131b33', width=1)
for y in range(0, H, 40):
    draw.line([(0, y), (W, y)], fill='#131b33', width=1)

# Gradient-like cyan glow (top-right corner)
for i in range(200):
    alpha = max(0, 30 - i // 7)
    r, g, b = 14, 165, 233
    color = (r * alpha // 30, g * alpha // 30, b * alpha // 30)
    draw.ellipse([W - 400 + i//2, -200 + i//2, W + 200 - i//2, 200 - i//2], fill=color)

# Bottom-left glow
for i in range(200):
    alpha = max(0, 20 - i // 10)
    color = (14 * alpha // 20, 165 * alpha // 20, 233 * alpha // 20)
    draw.ellipse([-200 + i//2, H - 200 + i//2, 300 - i//2, H + 200 - i//2], fill=color)

# Try to load fonts
try:
    font_title = ImageFont.truetype('C:/Windows/Fonts/calibrib.ttf', 72)
    font_sub = ImageFont.truetype('C:/Windows/Fonts/calibri.ttf', 30)
    font_badge = ImageFont.truetype('C:/Windows/Fonts/calibrib.ttf', 18)
    font_logo = ImageFont.truetype('C:/Windows/Fonts/calibrib.ttf', 48)
except:
    font_title = ImageFont.load_default()
    font_sub = ImageFont.load_default()
    font_badge = ImageFont.load_default()
    font_logo = ImageFont.load_default()

# Logo "SG" box (top-left)
logo_x, logo_y = 60, 50
draw.rounded_rectangle([logo_x, logo_y, logo_x + 64, logo_y + 64], radius=14, fill='#0f1629', outline='#0ea5e9', width=2)
bbox = draw.textbbox((0, 0), 'SG', font=font_logo)
tw = bbox[2] - bbox[0]
th = bbox[3] - bbox[1]
draw.text((logo_x + 32 - tw // 2, logo_y + 32 - th // 2 - 4), 'SG', fill='#0ea5e9', font=font_logo)

# Brand name next to logo
draw.text((logo_x + 80, logo_y + 10), 'KZ Smart Gate', fill='#e2e8f0', font=font_sub)

# Cyan line separator
draw.line([(60, 140), (W - 60, 140)], fill='#0ea5e9', width=2)

# Main title
title_lines = ['Умный контроль', 'доступа транспорта']
y = 180
for line in title_lines:
    draw.text((60, y), line, fill='#e2e8f0', font=font_title)
    y += 85

# Subtitle
draw.text((60, y + 20), 'ANPR камеры  •  Оплата Kaspi  •  Автоматические шлагбаумы', fill='#94a3b8', font=font_sub)

# Badge bottom
badge_y = H - 70
draw.rounded_rectangle([60, badge_y, 280, badge_y + 36], radius=18, fill='#0ea5e9')
bbox = draw.textbbox((0, 0), 'smartgate.kz', font=font_badge)
tw = bbox[2] - bbox[0]
draw.text((170 - tw // 2, badge_y + 8), 'smartgate.kz', fill='#ffffff', font=font_badge)

# "Казахстан" text
draw.text((300, badge_y + 8), 'Казахстан', fill='#64748b', font=font_badge)

img.save(output, 'PNG', optimize=True)
print(f'Created: {output} ({os.path.getsize(output)} bytes)')
