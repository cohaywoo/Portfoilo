from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

Path('.').mkdir(parents=True, exist_ok=True)

colors = ['#7bbf3f','#5ca6ff','#ffb86b','#d87bff','#ff6b6b','#4bd6c3']
for i,color in enumerate(colors, start=1):
    img = Image.new('RGB',(800,500),color)
    d = ImageDraw.Draw(img)
    try:
        f = ImageFont.truetype('/Library/Fonts/Arial.ttf',48)
    except:
        f = ImageFont.load_default()
    text = f'Item {i}'
    # compute text bbox for centering
    try:
        bbox = d.textbbox((0,0), text, font=f)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
    except AttributeError:
        # fallback for older Pillow
        w, h = d.textsize(text, font=f)
    d.text(((800-w)/2,(500-h)/2),text,fill='white',font=f)
    img.save(f'item-0{i}.png')
    print('created',f'item-0{i}.png')
