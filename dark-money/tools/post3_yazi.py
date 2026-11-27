import os, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
FONT="/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
SRC="/home/user/Diyetisyen-Web/dark-money/images/post3/yazisiz"
OUT="/home/user/Diyetisyen-Web/dark-money/images/post3/yazili"
CREAM=(255,247,232); GOLD=(236,190,96)
def tr_upper(s): return s.replace("i","İ").replace("ı","I").upper()
CAP={1:("48 yaşında yoksulluk,","23 yaşında başlar."),
     2:("44 yaşında pişmanlık,","20 yaşında başlar."),
     3:("45 yaşında liderlik,","22 yaşında başlar."),
     4:("40 yaşında servet,","19 yaşında başlar."),
     5:("52 yaşında obezite,","21 yaşında başlar.")}
def divider(im):
    a=np.asarray(im.convert("L"),dtype=float); H=a.shape[0]
    rows=a[int(H*.47):int(H*.53)].mean(axis=1)
    return int(H*.47)+int(rows.argmin())
def gradient(im,y0,y1,strength):
    a=np.asarray(im).astype(float); H,W,_=a.shape
    for y in range(y0,y1):
        t=(y-y0)/max(1,(y1-y0)); f=1-strength*t
        a[y]*=f
    return Image.fromarray(a.clip(0,255).astype("uint8"))
def draw_line(im,text,cy,size,fill=CREAM,gap=None):
    d=ImageDraw.Draw(im); W=im.size[0]
    f=ImageFont.truetype(FONT,size)
    w=d.textlength(text,font=f)
    while w>W*0.9:
        size-=2; f=ImageFont.truetype(FONT,size); w=d.textlength(text,font=f)
    x=(W-w)/2; y=cy-size/2
    sh=Image.new("RGBA",im.size,(0,0,0,0)); sd=ImageDraw.Draw(sh)
    sd.text((x,y+size*0.05),text,font=f,fill=(0,0,0,235),stroke_width=max(3,size//14),stroke_fill=(0,0,0,235))
    sh=sh.filter(ImageFilter.GaussianBlur(size*0.04))
    base=im.convert("RGBA"); base=Image.alpha_composite(base,sh)
    d2=ImageDraw.Draw(base); d2.text((x,y),text,font=f,fill=fill)
    return base.convert("RGB")
os.makedirs(OUT,exist_ok=True)
for n in (1,2,3,4,5,7):
    im=Image.open(f"{SRC}/sayfa{n}.jpg").convert("RGB"); W,H=im.size; dv=divider(im)
    if n!=7:
        im=gradient(im,int(dv-H*0.13),dv-4,0.55)
        im=gradient(im,int(H-H*0.14),H,0.6)
        top,bot=CAP[n]
        im=draw_line(im,tr_upper(top),dv-H*0.045,int(H*0.034))
        im=draw_line(im,tr_upper(bot),H-H*0.045,int(H*0.034))
    else:
        im=gradient(im,int(dv-H*0.13),dv-4,0.55)
        im=gradient(im,int(H*0.68),H,0.72)
        im=draw_line(im,tr_upper("25 yaşında takip ettiğin içerikler..."),dv-H*0.045,int(H*0.034))
        im=draw_line(im,tr_upper("45 yaşında hayatına dönüşür."),H*0.800,int(H*0.034))
        im=draw_line(im,tr_upper("Takip ettiklerinle başla."),H*0.848,int(H*0.022))
        im=draw_line(im,tr_upper("Okulda sana öğretilmeyen para dersleri için"),H*0.890,int(H*0.022))
        im=draw_line(im,"@moneyymadam",H*0.935,int(H*0.028),fill=GOLD)
        im=draw_line(im,tr_upper("hesabını takip et."),H*0.978,int(H*0.022))
    im.save(f"{OUT}/sayfa{n}.jpg",quality=92)
sheet=Image.new("RGB",(360*6,450))
for i,n in enumerate((1,2,3,4,5,7)): sheet.paste(Image.open(f"{OUT}/sayfa{n}.jpg").resize((360,450)),(i*360,0))
sheet.save("ozet_post3.png")
