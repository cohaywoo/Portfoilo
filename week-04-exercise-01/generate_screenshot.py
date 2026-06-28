from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

width, height = 1400, 900
img = Image.new('RGB', (width, height), '#8ed1ff')
draw = ImageDraw.Draw(img)

# sky and ground
for y in range(height):
    if y < 320:
        draw.line([(0, y), (width, y)], fill='#8ed1ff')
    elif y < 480:
        draw.line([(0, y), (width, y)], fill='#7bbf3f')
    else:
        draw.line([(0, y), (width, y)], fill='#a96b3f')

# blocky landscape
for x in range(0, width, 80):
    for y in range(500, 760, 80):
        draw.rectangle((x, y, x + 70, y + 70), fill='#5f3d1d')

for x in range(40, width, 120):
    draw.rectangle((x, 420, x + 90, 510), fill='#7bbf3f')
    draw.rectangle((x + 20, 360, x + 110, 450), fill='#5cc04a')

# browser window
for x0, y0, x1, y1 in [(40, 40, width - 40, height - 40)]:
    draw.rounded_rectangle((x0, y0, x1, y1), radius=26, fill='#fdf9ff', outline='#d0d8e8', width=3)

# address bar
draw.rounded_rectangle((70, 70, width - 70, 110), radius=18, fill='#f2f4ff', outline='#c4d0ea', width=2)
for x, y in [(95, 95), (120, 95), (145, 95)]:
    draw.ellipse((x, y, x + 10, y + 10), fill='#ff5f57')

# title and headline
try:
    font_title = ImageFont.truetype('/Library/Fonts/Arial.ttf', 54)
    font_body = ImageFont.truetype('/Library/Fonts/Arial.ttf', 30)
    font_small = ImageFont.truetype('/Library/Fonts/Arial.ttf', 22)
except Exception:
    font_title = ImageFont.load_default()
    font_body = ImageFont.load_default()
    font_small = ImageFont.load_default()

headline = 'The Creeper is now a friendly cat'
sub = 'A wildly unnecessary redesign, but somehow very on brand.'

draw.text((90, 230), 'minecraft.net', font=font_small, fill='#3d6f31')
draw.text((90, 260), headline, font=font_title, fill='#1b2f1a')
draw.text((90, 340), sub, font=font_body, fill='#35552d')

# buttons
for x0, y0, x1, y1, color, text in [
    (90, 430, 280, 480, '#7bbf3f', 'Play Now'),
    (310, 430, 510, 480, '#3d6f31', 'Explore Blocks'),
]:
    draw.rounded_rectangle((x0, y0, x1, y1), radius=16, fill=color)
    draw.text((x0 + 28, y0 + 12), text, font=font_body, fill='white')

# cards
for x0, y0, x1, y1, title, blurb in [
    (90, 560, 360, 740, 'Blocky', 'Totally local edits'),
    (420, 560, 690, 740, 'Pixel', 'Crystals and chaos'),
    (750, 560, 1020, 740, 'Crafty', 'Refresh to reset'),
]:
    draw.rounded_rectangle((x0, y0, x1, y1), radius=24, fill='white', outline='#d8e7d2', width=3)
    draw.text((x0 + 24, y0 + 24), title, font=font_body, fill='#1b2f1a')
    draw.text((x0 + 24, y0 + 70), blurb, font=font_small, fill='#56784d')

footer = 'Dev Tools Edition • browser-only edits • refresh to lose them all'
draw.text((90, 790), footer, font=font_small, fill='#3d6f31')

out_path = Path('devtools-vandalism-screenshot.png')
img.save(out_path)
print(out_path)
