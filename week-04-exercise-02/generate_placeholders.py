from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

Path('.').mkdir(parents=True, exist_ok=True)

colors = [('#6fbf37','Creeper'),('#42a1ff','Diamond Sword'),('#7b4b2a','Nether Portal'),('#c24b2b','Redstone'),('#a17a3a','Loot Chest'),('#4dbb74','Oak Sapling')]
for i,(color,label) in enumerate(colors, start=1):
    img = Image.new('RGB',(800,500),color)
    d = ImageDraw.Draw(img)
    # add a blocky checker overlay
    block = 40
    for by in range(0,500,block):
        for bx in range(0,800,block):
            if ((bx//block) + (by//block)) % 2 == 0:
                d.rectangle([bx,by,bx+block-1,by+block-1], fill=(0,0,0,0), outline=None)
    try:
        f = ImageFont.truetype('/Library/Fonts/Arial Bold.ttf',48)
    except:
        f = ImageFont.load_default()
    text = label
    try:
        bbox = d.textbbox((0,0), text, font=f)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
    except AttributeError:
        w, h = d.textsize(text, font=f)
    # draw a wood-like banner for text
    banner_h = h + 30
    d.rectangle([(0,380),(800,380+banner_h)], fill='#5b3d28')
    d.text(((800-w)/2,400),text,fill='white',font=f)
    img.save(f'item-0{i}.png')
    print('created',f'item-0{i}.png')
