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

# ---- SON SLAYT (6): CTA — ilk cümle normal harf, ikinci cümle büyük harf, hesap adı altın
def draw_rich(im,lines,cy,gap=1.2):
    # lines: [[(metin,renk,boyut), ...], ...]  her satır ortalanır, parçalar yan yana
    W=im.size[0]; base=im.convert("RGBA"); m=ImageDraw.Draw(base)
    hs=[max(s for _,_,s in ln) for ln in lines]; total=sum(int(h*gap) for h in hs); y=cy-total/2; items=[]
    for ln,h in zip(lines,hs):
        ws=[m.textlength(t,font=ImageFont.truetype(FONT,s)) for t,_,s in ln]; x=(W-sum(ws))/2
        for (t,c,s),w in zip(ln,ws): items.append((x,y+(h-s)*0.6,t,c,ImageFont.truetype(FONT,s))); x+=w
        y+=int(h*gap)
    sh=Image.new("RGBA",im.size,(0,0,0,0)); sd=ImageDraw.Draw(sh)
    for x,yy,t,c,f in items: sd.text((x,yy),t,font=f,fill=(0,0,0,255),stroke_width=max(5,f.size//9),stroke_fill=(0,0,0,255))
    base=Image.alpha_composite(base,sh.filter(ImageFilter.GaussianBlur(4)))
    ol=Image.new("RGBA",im.size,(0,0,0,0)); od=ImageDraw.Draw(ol)
    for x,yy,t,c,f in items: od.text((x,yy),t,font=f,fill=(0,0,0,235),stroke_width=max(3,f.size//16),stroke_fill=(0,0,0,235))
    base=Image.alpha_composite(base,ol); d=ImageDraw.Draw(base)
    for x,yy,t,c,f in items: d.text((x,yy),t,font=f,fill=c)
    return base.convert("RGB")
def rich_wrap(words,mw,m):
    # words: [[(metin,renk,boyut),...], ...] (her kelime birden çok parça olabilir); satırlara böler
    lines=[];cur=[];cw=0
    sp=m.textlength(" ",font=ImageFont.truetype(FONT,words[0][0][2]))
    for w in words:
        ww=sum(m.textlength(t,font=ImageFont.truetype(FONT,s)) for t,_,s in w)
        add=ww+(sp if cur else 0)
        if cur and cw+add>mw: lines.append(cur); cur=[];cw=0;add=ww
        if cur: cur.append((" ",CREAM,w[0][2]))
        cur.extend(w); cw+=add
    if cur: lines.append(cur)
    return lines
im=Image.open(f"{SRC}/sayfa6.jpg").convert("RGB"); W,H=im.size; S=int(H*0.0265); m=ImageDraw.Draw(im)
P1="Çoğu insan, yüzünü göstermeden de içerik üretebileceğini geç fark ediyor.".split()
S2=int(S*1.2)
P2_pre=up("Yüzünü göstermeden kendi karakterini oluşturmak için").split()
w1=[[(w,CREAM,S)] for w in P1]
L1=rich_wrap(w1,W*0.88,m)
L2=rich_wrap([[(w,CREAM,S2)] for w in P2_pre],W*0.90,m)
# son satır: tek satırda  @moneyymadam’ı TAKİP ET VE YORUMA KARAKTER(altın) YAZ.
S3=int(S*1.15)
while True:
    last=[("@moneyymadam",GOLD,S3),("’ı",CREAM,S3),(" "+up("takip et ve yoruma")+" ",CREAM,S3),("KARAKTER",GOLD,S3),(" YAZ.",CREAM,S3)]
    if sum(m.textlength(t,font=ImageFont.truetype(FONT,sz)) for t,_,sz in last)<=W*0.95: break
    S3-=1
print("son satır puntosu:",S3,"/",S)
lines=L1+[[("",CREAM,int(S*0.55))]]+L2+[[("",CREAM,int(S*0.35))]]+[last]
im=draw_rich(im,lines,H*0.815)
im.save(f"{OUT}/sayfa6.jpg",quality=92); print("ok sayfa 6, satır:",len(lines))
