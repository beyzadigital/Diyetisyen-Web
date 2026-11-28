"""Post6 (influencer / yüzsüz sayfa) yazıları: Gönderi 4 ile aynı düzen.
Her panelin altında altın etiket (INFLUENCER: / YÜZÜNÜ GÖSTERMEYEN:) + krem renkli büyük harfli tırnaklı cümle.
Karartma YOK: okunurluk koyu kontur + gölge ile sağlanır.
Girdi: post6/yazisiz/sayfaN.jpg   Çıktı: post6/yazili/sayfaN.jpg   (sayfa 4 iptal; sayfa 6 CTA metni bekleniyor)
"""
import os, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
FONT="/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
SRC="/home/user/Diyetisyen-Web/dark-money/images/post6/yazisiz"
OUT="/home/user/Diyetisyen-Web/dark-money/images/post6/yazili"
CREAM=(255,247,232); GOLD=(240,196,104)
TOP="Influencer"; BOT="Yüzünü göstermeyen"
def up(s): return s.replace("i","İ").replace("ı","I").upper()
T={1:("“Para için yüzünü göstermen şart mı?”","“Hayır, yüzümü göstermeden sayfamı kuruyorum.”"),
   2:("“Kameraya çıkacağım, önce saçım!”","“Ben görünmeyeceğim, önce fikrim.”"),
   3:("“Yüzüm yorgun çıktı, baştan!”","“Karakterimi yapay zekâyla çizdiriyorum.”"),
   5:("“Dışarı çıkıyorum, herkes bana bakıyor.”","“Kimse beni tanımıyor, rahatça dolaşıyorum.”")}
def divider(im):
    a=np.asarray(im.convert("L"),dtype=float); H=a.shape[0]
    lo,hi=int(H*.45),int(H*.55)
    return lo+int(a[lo:hi].std(axis=1).argmin())
def wrap(d,t,f,mw):
    ls,c=[],""
    for w in t.split():
        s=(c+" "+w).strip()
        if d.textlength(s,font=f)<=mw: c=s
        else: ls.append(c); c=w
    if c: ls.append(c)
    return ls
def text_block(im,lines,cy):
    W=im.size[0]; base=im.convert("RGBA"); d=ImageDraw.Draw(base)
    total=sum(int(s*1.18) for _,_,s in lines); y=cy-total/2
    sh=Image.new("RGBA",im.size,(0,0,0,0)); sd=ImageDraw.Draw(sh); pos=[]
    for t,fill,s in lines:
        f=ImageFont.truetype(FONT,s); w=d.textlength(t,font=f); x=(W-w)/2
        pos.append((x,y,t,fill,f))
        sd.text((x,y),t,font=f,fill=(0,0,0,255),stroke_width=max(5,s//9),stroke_fill=(0,0,0,255)); y+=int(s*1.18)
    sh=sh.filter(ImageFilter.GaussianBlur(4)); base=Image.alpha_composite(base,sh)
    # keskin koyu kontur (okunurluk)
    ol=Image.new("RGBA",im.size,(0,0,0,0)); od=ImageDraw.Draw(ol)
    for x,y,t,fill,f in pos: od.text((x,y),t,font=f,fill=(0,0,0,235),stroke_width=max(3,f.size//16),stroke_fill=(0,0,0,235))
    base=Image.alpha_composite(base,ol); d=ImageDraw.Draw(base)
    for x,y,t,fill,f in pos: d.text((x,y),t,font=f,fill=fill)
    return base.convert("RGB")
def panel_caption(im,label,quote,bottom,H):
    size=int(H*0.030); W=im.size[0]
    d=ImageDraw.Draw(im); f=ImageFont.truetype(FONT,size)
    ql=wrap(d,up(quote),f,W*0.86)
    while len(ql)>3: size-=2; f=ImageFont.truetype(FONT,size); ql=wrap(d,up(quote),f,W*0.86)
    lines=[(up(label)+":",GOLD,int(size*0.8))]+[(l,CREAM,size) for l in ql]
    h=sum(int(s*1.18) for _,_,s in lines)
    return text_block(im,lines,bottom-h/2-H*0.02)
os.makedirs(OUT,exist_ok=True)
for n,((q1),(q2)) in [(k,(v[0],v[1])) for k,v in T.items()]:
    im=Image.open(f"{SRC}/sayfa{n}.jpg").convert("RGB"); W,H=im.size; dv=divider(im)
    im=panel_caption(im,TOP,q1,dv-4,H); im=panel_caption(im,BOT,q2,H,H)
    im.save(f"{OUT}/sayfa{n}.jpg",quality=92)
    print("ok sayfa",n,"ayırıcı y=",dv)
