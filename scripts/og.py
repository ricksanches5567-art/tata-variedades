# Imagem de compartilhamento (1200x630): preto, branco e rosa
from PIL import Image, ImageDraw, ImageFont
import numpy as np
D = '/usr/share/fonts/truetype/sand-box/google/'
W, H = 1200, 630
im = Image.new('RGB', (W, H), (11, 9, 11)); d = ImageDraw.Draw(im)
# brilho rosa
g = Image.new('RGB', (W, H), (0, 0, 0)); gd = ImageDraw.Draw(g); gd.ellipse((-300, -200, 700, 600), fill=(120, 20, 70))
from PIL import ImageFilter
g = g.filter(ImageFilter.GaussianBlur(120)); im = Image.blend(im, Image.eval(Image.composite(g, im, Image.new('L', (W, H), 255)), lambda v: v), .5)
d = ImageDraw.Draw(im)
f = ImageFont.truetype(D + 'Playfair Display/PlayfairDisplay-Italic-VariableFont_wght.ttf', 250); f.set_variation_by_axes([700])
txt = Image.new('L', (W, H), 0); ImageDraw.Draw(txt).text((60, 60), 'Tata', font=f, fill=255)
grad = np.zeros((H, W, 3), np.uint8); xs = np.linspace(0, 1, W)[None, :, None]; ys = np.linspace(0, 1, H)[:, None, None]; t = (xs * .6 + ys * .8).clip(0, 1)
c0 = np.array([255, 179, 217]); c1 = np.array([255, 61, 154]); c2 = np.array([194, 24, 91])
grad = np.where(t < .5, c0 + (c1 - c0) * (t / .5), c1 + (c2 - c1) * ((t - .5) / .5)).astype(np.uint8)
im.paste(Image.fromarray(grad), (0, 0), txt); d = ImageDraw.Draw(im)
fs = ImageFont.truetype(D + 'Poppins/Poppins-SemiBold.ttf', 30); fr = ImageFont.truetype(D + 'Poppins/Poppins-Regular.ttf', 25)
d.text((72, 372), 'V A R I E D A D E S', font=fs, fill=(255, 255, 255))
d.line([(72, 428), (172, 428)], fill=(255, 61, 154), width=3)
for i, s in enumerate(['Vidros · Maçaricos · Isqueiros · Sex Shop', 'Curitiba – PR | envio discreto p/ todo o Brasil', 'Venda proibida para menores de 18 anos']):
    d.text((72, 448 + i * 40), s, font=fr, fill=(255, 235, 245) if i < 2 else (255, 140, 198))
def tile(path, x, y, w, h):
    t = Image.open(path).convert('RGB'); s = max(w / t.width, h / t.height); t = t.resize((int(t.width * s) + 1, int(t.height * s) + 1))
    t = t.crop(((t.width - w) // 2, (t.height - h) // 2, (t.width - w) // 2 + w, (t.height - h) // 2 + h))
    m = Image.new('L', (w, h), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, w - 1, h - 1), 22, fill=255); im.paste(t, (x, y), m)
tile('img/p/T4-05.webp', 690, 60, 230, 510); tile('img/p/T-SEX-12.webp', 940, 60, 230, 245); tile('img/p/T-SEX-09.webp', 940, 325, 230, 245)
im.save('img/og.jpg', quality=88)
