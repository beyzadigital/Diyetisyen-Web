import os, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
FONT="/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
SRC="/home/user/Diyetisyen-Web/dark-money/images/post4/yazisiz"
OUT="/home/user/Diyetisyen-Web/dark-money/images/post4/yazili"
CREAM=(255,247,232); GOLD=(240,196,104)
def up(s): return s.replace("i","İ").replace("ı","I").upper()
T={1:(("Patron","“Raporunu getir, sonra konuşalım.”"),("Lider","“Sen sağlığına bak, biz hallederiz.”")),
   2:(("Patron","“Şu an zam konuşmanın sırası değil.”"),("Lider","“Emeğinin karşılığını birlikte değerlendirelim.”")),
   3:(("Patron","“Beş dakikalık iş, hemen halledersin.”"),("Lider","“İyi hafta sonları, pazartesi görüşürüz.”")),
   4:(("Patron","“Bunların hepsini bugün tamamlamanı istiyorum.”"),("Lider","“İlk günün, acele etme. Takıldığın yerde bana sor.”")),
   5:(("Patron","“Senin yerini doldurmak zor olmayacaktır.”"),("Lider","“Yolun açık olsun. Seninle çalışmak güzeldi.”"))}
def divider(im):
    a=np.asarray(im.convert("L"),dtype=float); H=a.shape[0]
    rows=a[int(H*.47):int(H*.53)].mean(axis=1)
    return int(H*.47)+int(rows.argmin())
def gradient(im,y0,y1,s):
    a=np.asarray(im).astype(float)
    for y in range(y0,y1):
        a[y]*=1-s*((y-y0)/max(1,y1-y0))
    return Image.fromarray(a.clip(0,255).astype("uint8"))
def wrap(d,t,f,mw):
    ls,c=[],""
    for w in t.split():
        s=(c+" "+w).strip()
        if d.textlength(s,font=f)<=mw: c=s
        else: ls.append(c); c=w
    if c: ls.append(c)
    return ls
def text_block(im,lines,cy,size,fills):
    # lines: list of (text, fill, size)
    W=im.size[0]; base=im.convert("RGBA")
    d=ImageDraw.Draw(base)
    total=sum(int(s*1.18) for _,_,s in lines); y=cy-total/2
    sh=Image.new("RGBA",im.size,(0,0,0,0)); sd=ImageDraw.Draw(sh)
    pos=[]
    for t,fill,s in lines:
        f=ImageFont.truetype(FONT,s); w=d.textlength(t,font=f); x=(W-w)/2
        pos.append((x,y,t,fill,f,s)); 
        sd.text((x,y),t,font=f,fill=(0,0,0,235),stroke_width=max(3,s//14),stroke_fill=(0,0,0,235)); y+=int(s*1.18)
    sh=sh.filter(ImageFilter.GaussianBlur(3)); base=Image.alpha_composite(base,sh)
    d=ImageDraw.Draw(base)
    for x,y,t,fill,f,s in pos: d.text((x,y),t,font=f,fill=fill)
    return base.convert("RGB")
def panel_caption(im,label,quote,bottom,H):
    size=int(H*0.030); W=im.size[0]
    d=ImageDraw.Draw(im); f=ImageFont.truetype(FONT,size)
    ql=wrap(d,up(quote),f,W*0.86)
    while len(ql)>3: size-=2; f=ImageFont.truetype(FONT,size); ql=wrap(d,up(quote),f,W*0.86)
    lines=[(up(label)+":",GOLD,int(size*0.8))]+[(l,CREAM,size) for l in ql]
    h=sum(int(s*1.18) for _,_,s in lines)
    return text_block(im,lines,bottom-h/2-H*0.02,size,None)
os.makedirs(OUT,exist_ok=True)
for n in range(1,6):
    im=Image.open(f"{SRC}/sayfa{n}.jpg").convert("RGB"); W,H=im.size; dv=divider(im)
    im=gradient(im,int(dv-H*0.17),dv-4,0.62); im=gradient(im,int(H-H*0.17),H,0.65)
    (l1,q1),(l2,q2)=T[n]
    im=panel_caption(im,l1,q1,dv-4,H); im=panel_caption(im,l2,q2,H,H)
    im.save(f"{OUT}/sayfa{n}.jpg",quality=92)
# slide 6
im=Image.open(f"{SRC}/sayfa6.jpg").convert("RGB"); W,H=im.size
im=gradient(im,int(H*0.60),H,0.78)
S=int(H*0.032); S2=int(H*0.0235)
d=ImageDraw.Draw(im)
f=ImageFont.truetype(FONT,S)
l1=wrap(d,"Kötü patronun önüne geçemezsin sanma;",f,W*0.9)
l2=wrap(d,up("kendi yolunu çizerek hayatının patronu olabilirsin."),f,W*0.9)
lines=[(l,CREAM,S) for l in l1]+[(l,CREAM,S) for l in l2]
im=text_block(im,lines,H*0.800,S,None)
lines=[("Nasıl yapacağını öğrenmek için",CREAM,S2),("@moneyymadam",GOLD,int(S2*1.25)),("hesabını takip et.",CREAM,S2)]
im=text_block(im,lines,H*0.915,S2,None)
im.save(f"{OUT}/sayfa6.jpg",quality=92)
sh=Image.new("RGB",(360*6,450))
for n in range(1,7): sh.paste(Image.open(f"{OUT}/sayfa{n}.jpg").resize((360,450)),((n-1)*360,0))
sh.save("ozet_post4.png")
