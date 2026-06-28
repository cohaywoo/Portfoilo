from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

width, height = 1400, 900
img = Image.new('RGB', (width, height), '#0f1024')
draw = ImageDraw.Draw(img)

for y in range(0, height, 80):
    fill = (20, 25, 60) if y % 160 == 0 else (12, 16, 40)
    draw.rectangle([0, y, width, y + 40], fill=fill)

# browser window
for x0, y0, x1, y1 in [(40, 40, width - 40, height - 40)]:
    draw.rounded_rectangle((x0, y0, x1, y1), radius=26, fill='#fdf9ff', outline='#d3d5eb', width=3)

# address bar
for x0, y0, x1, y1 in [(70, 70, width - 70, 110)]:
    draw.rounded_rectangle((x0, y0, x1, y1), radius=18, fill='#f2f4ff', outline='#bfc6e8', width=2)

for x, y in [(95, 95), (120, 95), (145, 95)]:
    draw.ellipse((x, y, x + 10, y + 10), fill='#ff5f57')
for x, y in [(120, 95), (145, 95)]:
    pass

# giant blobs
for x0, y0, x1, y1, color in [
    (780, 140, 1320, 500, '#ff5bd1'),
    (620, 220, 1180, 620, '#62f7ff'),
    (220, 560, 760, 760, '#ffe36b'),
]:
    draw.ellipse((x0, y0, x1, y1), fill=color)

# nav pills
for i, label in enumerate(['Store', 'Mac', 'iPhone', 'Watch']):
    x = 90 + i * 140
    draw.rounded_rectangle((x, 165, x + 100, 205), radius=14, fill=['#111839', '#ff5bd1', '#62f7ff', '#111839'][i % 4])
    draw.text((x + 20, 172), label, fill='white')

try:
    font_title = ImageFont.truetype('/Library/Fonts/Arial.ttf', 54)
    font_body = ImageFont.truetype('/Library/Fonts/Arial.ttf', 30)
    font_small = ImageFont.truetype('/Library/Fonts/Arial.ttf', 22)
except Exception:
    font_title = ImageFont.load_default()
    font_body = ImageFont.load_default()
    font_small = ImageFont.load_default()

headline = 'The iPhone is now a toaster'
sub = 'A completely unnecessary redesign, but somehow still iconic.'

text_color = '#111839'
draw.text((90, 280), 'apple.com', font=font_small, fill='#4d5ab6')
draw.text((90, 310), headline, font=font_title, fill=text_color)
draw.text((90, 390), sub, font=font_body, fill='#27315d')

button = (90, 470, 330, 520)
draw.rounded_rectangle(button, radius=16, fill='#111839')
draw.text((130, 476), 'Buy a toaster', font=font_body, fill='white')

for rect in [
    (90, 590, 360, 740),
    (420, 590, 690, 740),
    (750, 590, 1020, 740),
]:
    draw.rounded_rectangle(rect, radius=24, fill='white', outline='#d7dcf5', width=3)

for x, y, label in [(120, 625, 'Neon'), (450, 625, 'Glowing'), (780, 625, 'Chaotic')]:
    draw.text((x, y), label, font=font_body, fill='#111839')
    draw.text((x, y + 40), 'completely local', font=font_small, fill='#6b75ad')

footer = 'Dev Tools Edition • browser-only edits • refresh to lose them all'
draw.text((90, 790), footer, font=font_small, fill='#4d5ab6')

out_path = Path('devtools-vandalism-screenshot.png')
img.save(out_path)
print(out_path)
