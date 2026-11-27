import os, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
FONT="/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
SRC="/home/user/Diyetisyen-Web/dark-money/images/post5/yazisiz"
OUT="/home/user/Diyetisyen-Web/dark-money/images/post5/yazili"
CREAM=(255,247,232); GOLD=(240,196,104)
def up(s): return s.replace("i","İ").replace("ı","I").upper()

T={1:("Sen işine bütün emeğini koyarsın…","Ama kazancın büyük kısmı başkasının cebine girer."),
   2:("Yıllarca okudun, sonunda diplomanı aldın.","Ama kimse sana bunu nasıl gelire dönüştüreceğini öğretmedi."),
   3:("Kendi dükkânını açtın.","Ama kimse sana kira, vergi ve giderlerin ne kadar büyük olduğunu söylemedi."),
   4:("Ne kadar çok çalışırsan çalış, zamanın hep başkasının kontrolünde…","Maaş alır, faturaları öder ve yeniden çalışmaya dönersin."),
   5:("Seni yerinde tutmak için artık zincirlere ihtiyaçları yok…","Ekran başında geçirdiğin zaman, bunu senin yerine yapıyor."),
   6:("Paranın nereye gideceğini belirleyen bir planın olmalı.","İhtiyaçlarını, birikimini, yatırımını sen yönetmezsen paran senin yerine karar verir.")}

def divider(im):
    # ayırıcı çizgi: en düzgün (en düşük std) satır, görselin %30-60 bandında
    a=np.asarray(im.convert("L"),dtype=float); H=a.shape[0]
    lo,hi=int(H*.30),int(H*.60)
    return lo+int(a[lo:hi].std(axis=1).argmin())

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

def draw_crown(d,x,y,h,fill):
    # taç: x,y sol-üst, yükseklik h; uçlarda küçük toplar
    w=h*1.25
    pts=[(x,y+h),(x,y+h*0.3),(x+w*0.25,y+h*0.62),(x+w*0.5,y+h*0.12),(x+w*0.75,y+h*0.62),(x+w,y+h*0.3),(x+w,y+h)]
    d.polygon(pts,fill=fill)
    r=h*0.11
    for cx_,cy_ in ((x,y+h*0.26),(x+w*0.5,y+h*0.08),(x+w,y+h*0.26)):
        d.ellipse((cx_-r,cy_-r,cx_+r,cy_+r),fill=fill)
    return w

def text_block(im,lines,cy,cx=None):
    # lines: [[(text, fill, size) | ("crown", fill, size), ...], ...]  her satır cx etrafında ortalanır
    W=im.size[0]; base=im.convert("RGBA"); meas=ImageDraw.Draw(base)
    if cx is None: cx=W/2
    rows=[]; total=0
    for segs in lines:
        wsum=0; smax=0
        for t,fill,s in segs:
            smax=max(smax,s)
            wsum+= s*1.25+s*0.2 if t=="crown" else meas.textlength(t,font=ImageFont.truetype(FONT,s))
        rows.append((segs,wsum,smax)); total+=int(smax*1.2)
    y=cy-total/2
    sh=Image.new("RGBA",im.size,(0,0,0,0)); sd=ImageDraw.Draw(sh)
    layout=[]
    for segs,wsum,smax in rows:
        x=cx-wsum/2
        for t,fill,s in segs:
            if t=="crown":
                layout.append(("crown",x+s*0.2,y+smax*0.12,s*0.8,fill)); x+=s*1.25+s*0.2
            else:
                f=ImageFont.truetype(FONT,s); w=meas.textlength(t,font=f)
                sd.text((x,y+(smax-s)*0.6),t,font=f,fill=(0,0,0,235),stroke_width=max(3,s//14),stroke_fill=(0,0,0,235))
                layout.append(("text",x,y+(smax-s)*0.6,t,fill,f)); x+=w
        y+=int(smax*1.2)
    sh=sh.filter(ImageFilter.GaussianBlur(3)); base=Image.alpha_composite(base,sh)
    d=ImageDraw.Draw(base)
    for it in layout:
        if it[0]=="crown":
            _,x,yy,h,fill=it
            draw_crown(d,x-2,yy-2,h+4,(0,0,0)); draw_crown(d,x,yy,h,fill)
        else:
            _,x,yy,t,fill,f=it; d.text((x,yy),t,font=f,fill=fill)
    return base.convert("RGB")

def panel_caption(im,text,bottom,H,cx=None,wfrac=0.92,sizes=(0.031,0.029,0.027,0.025),maxlines=2):
    # önce en büyük punto ile en fazla 'maxlines' satıra sığdırmayı dener, olmazsa en küçük punto ile sığdırır
    W=im.size[0]; d=ImageDraw.Draw(im)
    for k,sz in enumerate(sizes):
        size=int(H*sz); f=ImageFont.truetype(FONT,size); ql=wrap(d,up(text),f,W*wfrac)
        if len(ql)<=maxlines: break
    h=len(ql)*int(size*1.2)
    return text_block(im,[[(l,CREAM,size)] for l in ql],bottom-h/2-H*0.022,cx)

os.makedirs(OUT,exist_ok=True)
for n in range(1,7):
    im=Image.open(f"{SRC}/sayfa{n}.jpg").convert("RGB"); W,H=im.size; dv=divider(im)
    im=gradient(im,int(dv-H*0.17),dv-4,0.62); im=gradient(im,int(H-H*0.17),H,0.65)
    top,bot=T[n]
    im=panel_caption(im,top,dv-4,H)
    if n==6:
        # defterdeki yazılar görünür kalsın: alt yazı defterin sağındaki boş masa alanına yazılır
        im=panel_caption(im,bot,H,H,cx=W*0.745,wfrac=0.44,sizes=(0.0275,0.026,0.0245),maxlines=6)
    else:
        im=panel_caption(im,bot,H,H)
    im.save(f"{OUT}/sayfa{n}.jpg",quality=92)

# SON slayt: CTA
im=Image.open(f"{SRC}/sayfa7.jpg").convert("RGB"); W,H=im.size
im=gradient(im,int(H*0.58),H,0.80)
S=int(H*0.027); d=ImageDraw.Draw(im); f=ImageFont.truetype(FONT,S); mw=W*0.88
lines=[]
for l in wrap(d,"Paranı nasıl yöneteceğini öğrenmek için yıllarını kaybetme.",f,mw): lines.append([(l,CREAM,S)])
lines.append([("",CREAM,int(S*0.5))])
l2=wrap(d,up("Kazancının kontrolünü eline al, geleceğini kendi kurallarına göre şekillendir."),f,mw-S*2)
for i,l in enumerate(l2):
    segs=[(l,CREAM,S)]
    if i==len(l2)-1: segs.append(("crown",GOLD,int(S*1.3)))
    lines.append(segs)
lines.append([("",CREAM,int(S*0.5))])
lines.append([("Para oyununu öğrenmek için",CREAM,int(S*0.9))])
lines.append([("@moneyymadam",GOLD,int(S*1.15)),("’ı takip et.",CREAM,int(S*0.9))])
im=text_block(im,lines,H*0.835)
im.save(f"{OUT}/sayfa7.jpg",quality=92)

sh=Image.new("RGB",(360*7,450))
for n in range(1,8): sh.paste(Image.open(f"{OUT}/sayfa{n}.jpg").resize((360,450)),((n-1)*360,0))
sh.save("/tmp/claude-0/-home-user-Diyetisyen-Web/e41dd7e6-c0f5-56e1-b80a-11bb233e9350/scratchpad/p5/ozet_post5.png")
