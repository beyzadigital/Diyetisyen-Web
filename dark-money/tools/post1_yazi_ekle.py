import sys, os
from PIL import Image, ImageDraw, ImageFont

SRC = sys.argv[1]
OUT = sys.argv[2]
FONT = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
K = 1.17  # display -> original
INK = (28, 18, 10)

# Her sayfa icin: balon yazi kutulari (gorunen koordinat: x0,y0,x1,y1), metin
SLIDES = {
    1: [((95, 150, 640, 430), "1 hafta önce 100$'dı, şimdi sadece 60$!"),
        ((775, 125, 1415, 440), "Önce yüksek fiyatı gösterirler. Böylece 60$ sana daha uygun gelir.")],
    2: [((90, 95, 640, 400), "Son 2 ürün kalmış! Hemen almalıyım."),
        ((775, 70, 1410, 425), "Bu mesaj kaçırma korkusu yaratır. Başka fiyatlara bakamadan aceleyle almana neden olur.")],
    3: [((85, 85, 625, 375), "Ücretsiz kargo için 15$ daha eklemem lazım."),
        ((770, 75, 1410, 390), "5$ kargo ödememek için 15$'lık fazladan ürün alıyorsun. Tasarruf ettiğini sanırken daha çok harcıyorsun.")],
    4: [((95, 130, 640, 450), "3 tanesi 24$. Bu çok iyi bir fırsat!"),
        ((800, 120, 1395, 465), "Tanesi ucuz ama daha çok alıyorsun. Tek ürün yeterliyken 14$ fazladan ödüyorsun.")],
    5: [((90, 110, 625, 370), "Büyük boy sadece 2$ fazla."),
        ((800, 95, 1380, 420), "Buna “avantajlı ürün” denir. Biraz daha fazla öde, daha büyüğünü al der. Sen de alırsın.")],
    6: [((90, 95, 640, 400), "Herkes bunu alıyor, iyidir herhalde."),
        ((775, 70, 1410, 425), "Mağazalar, seni ikna etmek için yorumları ve satış sayılarını gösterir. Başkalarının aldığını görmek, senin de almanı kolaylaştırır.")],
    7: [((75, 110, 590, 370), "Ben tasarruf ettiğimi sanmıştım.")],
}


def wrap(draw, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit(draw, text, box, maxsize=120, minsize=24, spacing=1.12):
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    for size in range(maxsize, minsize, -2):
        f = ImageFont.truetype(FONT, size)
        lines = wrap(draw, text, f, w)
        if any(draw.textlength(l, font=f) > w for l in lines):
            continue
        lh = int(size * spacing)
        if lh * len(lines) <= h:
            return f, lines, lh
    f = ImageFont.truetype(FONT, minsize)
    return f, wrap(draw, text, f, w), int(minsize * spacing)


def draw_centered(draw, text, box, color=INK, maxsize=120):
    x0, y0, x1, y1 = [int(v * K) for v in box]
    f, lines, lh = fit(draw, text, (x0, y0, x1, y1), maxsize=int(maxsize))
    total = lh * len(lines)
    y = y0 + ((y1 - y0) - total) / 2
    for l in lines:
        wl = draw.textlength(l, font=f)
        draw.text((x0 + ((x1 - x0) - wl) / 2, y), l, font=f, fill=color)
        y += lh


def main():
    n = int(sys.argv[3])
    im = Image.open(SRC).convert("RGB")
    d = ImageDraw.Draw(im)
    for box, text in SLIDES[n]:
        # her balon icin ayni boyutu kullanmak yerine her biri sigdigi kadar buyur
        draw_centered(d, text, box, maxsize=96)
    if n == 5:
        # tabela: tebesir yazisi (hafif egimli)
        sign = Image.new("RGBA", im.size, (0, 0, 0, 0))
        sd = ImageDraw.Draw(sign)
        box = [int(v * K) for v in (955, 1460, 1205, 1725)]
        f, lines, lh = fit(sd, "BÜYÜK BOY AL, SADECE +2$ FARKLA", tuple(box), maxsize=90)
        total = lh * len(lines)
        y = box[1] + ((box[3] - box[1]) - total) / 2
        for l in lines:
            wl = sd.textlength(l, font=f)
            sd.text((box[0] + ((box[2] - box[0]) - wl) / 2, y), l, font=f, fill=(245, 240, 225, 235))
            y += lh
        sign = sign.rotate(-2, resample=Image.BICUBIC, center=((box[0] + box[2]) // 2, (box[1] + box[3]) // 2))
        im = Image.alpha_composite(im.convert("RGBA"), sign).convert("RGB")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    im.save(OUT, quality=95)


main()
