"""Post6 sayfa 1: laptop ekranını @moneyymadam'ın kendi Instagram profil sayfası olarak çizer.
Üst çubukta Instagram ikonu, profil fotoğrafı, kullanıcı adı, 'Profili düzenle' / 'Arşivi görüntüle' (kendi sayfası olduğunu belli eder),
sekme ikonları ve şapkalı kadının 3 gönderisi. Takipçi / gönderi sayısı YOK.
Girdi : post6/yazisiz/kaynak/sayfa1_bos_ekran.jpg   Çıktı: post6/yazisiz/sayfa1.jpg
"""
import math, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
R="/home/user/Diyetisyen-Web/dark-money/images/"
BASE=R+"post6/yazisiz/kaynak/sayfa1_bos_ekran.jpg"; OUT=R+"post6/yazisiz/sayfa1.jpg"
FD="/usr/share/fonts/opentype/inter/Inter-"
# ekranın beyaz alanının köşeleri (sol-üst, sağ-üst, sağ-alt, sol-alt)
SCREEN=[(1250,1515),(1696,1521),(1594,1996),(1165,1912)]
SRC=[(R+"post4/yazisiz/sayfa4.jpg",(851,1131,1523,1803)),
     (R+"post3/yazisiz/sayfa1.jpg",(1322,168,1792,638)),
     (R+"post1/yazisiz/sayfa1.jpg",(1121,607,1744,1230))]
W,H=1000,880; K=2                       # tuval ve çizim ölçeği (2x çizip küçültüyoruz)
BG=(252,246,240); INK=(38,38,38); GRAY=(142,142,142); LINE=(225,219,213)

def font(w,sz): return ImageFont.truetype(FD+w+".otf",int(sz*K))
def clean_tail(im):
    a=np.asarray(im).astype(float)
    for y in range(0,42): a[y,419:486]=a[y,486:502].mean(axis=0)
    out=Image.fromarray(a.astype("uint8"))
    m=Image.new("L",im.size,0); ImageDraw.Draw(m).rectangle((417,0,488,43),fill=255)
    return Image.composite(out.filter(ImageFilter.GaussianBlur(1.2)),im,m.filter(ImageFilter.GaussianBlur(1.0)))
def crop(i):
    p,b=SRC[i]; im=Image.open(p).convert("RGB").crop(b)
    return clean_tail(im) if "post1" in p else im

cv=Image.new("RGB",(W*K,H*K),BG); d=ImageDraw.Draw(cv)
def r(x): return int(x*K)
def line(p,w=3,fill=INK): d.line([(r(x),r(y)) for x,y in p],fill=fill,width=max(1,r(w)),joint="curve")
def rrect(b,rad,fill=None,outline=None,w=3): d.rounded_rectangle([r(b[0]),r(b[1]),r(b[2]),r(b[3])],r(rad),fill=fill,outline=outline,width=r(w))
def circ(cx,cy,rad,fill=None,outline=None,w=3): d.ellipse([r(cx-rad),r(cy-rad),r(cx+rad),r(cy+rad)],fill=fill,outline=outline,width=r(w))

def insta_glyph(x,y,s):
    S=int(s*K*3); g=Image.new("RGB",(S,S))
    px=np.zeros((S,S,3)); yy,xx=np.mgrid[0:S,0:S]
    t=((xx/S)*0.55+(1-yy/S)*0.9)/1.45          # sol-alt -> sağ-üst
    stops=[(0,(254,218,117)),(0.3,(250,126,30)),(0.55,(214,41,118)),(0.8,(150,47,191)),(1,(79,91,213))]
    t=1-t
    for i in range(len(stops)-1):
        t0,c0=stops[i]; t1,c1=stops[i+1]
        m=(t>=t0)&(t<=t1); f=((t-t0)/(t1-t0))[m][:,None]
        px[m]=np.array(c0)*(1-f)+np.array(c1)*f
    g=Image.fromarray(px.astype("uint8"))
    mk=Image.new("L",(S,S),0); ImageDraw.Draw(mk).rounded_rectangle([0,0,S-1,S-1],int(S*.26),fill=255)
    gd=ImageDraw.Draw(g); wd=int(S*.07)
    gd.rounded_rectangle([int(S*.17),int(S*.17),int(S*.83),int(S*.83)],int(S*.2),outline=(255,255,255),width=wd)
    gd.ellipse([int(S*.34),int(S*.34),int(S*.66),int(S*.66)],outline=(255,255,255),width=wd)
    gd.ellipse([int(S*.66),int(S*.2),int(S*.76),int(S*.3)],fill=(255,255,255))
    tgt=int(s*K); g=g.resize((tgt,tgt),Image.LANCZOS); mk=mk.resize((tgt,tgt),Image.LANCZOS)
    cv.paste(g,(r(x),r(y)),mk)

# ---- üst çubuk
d.rectangle([0,0,W*K,r(86)],fill=(255,255,255)); line([(0,86),(W,86)],2,LINE)
insta_glyph(34,17,52)
rrect((300,21,610,65),22,fill=(238,233,228))
circ(334,43,9,outline=GRAY,w=3); line([(341,50),(349,58)],3,GRAY)
d.text((r(362),r(43)),"Ara",font=font("Medium",20),fill=GRAY,anchor="lm")
# home
line([(690,46),(708,30),(726,46)],3.2); line([(695,44),(695,62),(721,62),(721,44)],3.2)
# plus kare
rrect((764,31,796,63),9,outline=INK,w=3.2); line([(780,38),(780,56)],3.2); line([(771,47),(789,47)],3.2)
# kalp
pts=[]
for a in np.linspace(0,2*math.pi,80):
    hx=16*math.sin(a)**3; hy=13*math.cos(a)-5*math.cos(2*a)-2*math.cos(3*a)-math.cos(4*a)
    pts.append((846+hx*1.0,46-hy*1.0))
d.polygon([(r(x),r(y)) for x,y in pts],outline=INK,width=r(3.2))
# kendi küçük profil fotoğrafı
av=crop(2).crop((60,0,560,500)).resize((r(44),r(44)),Image.LANCZOS)
m=Image.new("L",av.size,0); ImageDraw.Draw(m).ellipse([0,0,av.size[0]-1,av.size[1]-1],fill=255)
cv.paste(av,(r(900),r(21)),m); circ(922,43,23,outline=INK,w=2)

# ---- profil başlığı
AV=190
av=crop(2).crop((60,0,560,500)).resize((r(AV),r(AV)),Image.LANCZOS)
m=Image.new("L",av.size,0); ImageDraw.Draw(m).ellipse([0,0,av.size[0]-1,av.size[1]-1],fill=255)
cv.paste(av,(r(86),r(130)),m); circ(86+AV/2,130+AV/2,AV/2,outline=LINE,w=3)
d.text((r(340),r(160)),"moneyymadam",font=font("Bold",40),fill=INK,anchor="lm")
# dişli ikonu (kendi profili)
cx,cy=900,160
for i in range(8):
    a=i*math.pi/4; x1,y1=cx+math.cos(a)*15,cy+math.sin(a)*15; x2,y2=cx+math.cos(a)*23,cy+math.sin(a)*23
    line([(x1,y1),(x2,y2)],7,INK)
circ(cx,cy,18,fill=INK); circ(cx,cy,8,fill=BG)
rrect((340,214,590,268),14,fill=(236,231,226))
d.text((r(465),r(241)),"Profili düzenle",font=font("SemiBold",22),fill=INK,anchor="mm")
rrect((606,214,856,268),14,fill=(236,231,226))
d.text((r(731),r(241)),"Arşivi görüntüle",font=font("SemiBold",22),fill=INK,anchor="mm")
d.text((r(340),r(312)),"Moneyy Madam",font=font("Bold",24),fill=INK,anchor="lm")

# ---- sekmeler
line([(40,372),(960,372)],2,LINE)
# ızgara (aktif)
gx,gy=367,392
for i in range(3):
    for j in range(3): rrect((gx+i*12,gy+j*12,gx+i*12+9,gy+j*12+9),1.5,fill=INK)
line([(330,372),(440,372)],3.5,INK)
# reels
rrect((484,390,516,422),9,outline=GRAY,w=3); d.polygon([(r(496),r(398)),(r(496),r(414)),(r(509),r(406))],fill=GRAY)
# etiketli
rrect((564,390,596,422),9,outline=GRAY,w=3); circ(580,401,5,outline=GRAY,w=2.6); d.arc([r(569),r(408),r(591),r(432)],200,340,fill=GRAY,width=r(2.6))

# ---- gönderi ızgarası (3 gönderi, tek sıra)
SZ=(W-2*30-2*8)//3
for i in range(3):
    t=crop(i); s=min(t.size); t=t.crop(((t.size[0]-s)//2,(t.size[1]-s)//2,(t.size[0]+s)//2,(t.size[1]+s)//2)).resize((r(SZ),r(SZ)),Image.LANCZOS)
    cv.paste(t,(r(30+i*(SZ+8)),r(446)))

flat=cv.resize((W,H),Image.LANCZOS)

# ---- ekrana perspektifle yerleştir
def coeffs(dst,sw,sh):
    src=[(0,0),(sw,0),(sw,sh),(0,sh)]; A=[];b=[]
    for (x,y),(u,v) in zip(dst,src):
        A.append([x,y,1,0,0,0,-u*x,-u*y]); b.append(u)
        A.append([0,0,0,x,y,1,-v*x,-v*y]); b.append(v)
    return np.linalg.solve(np.array(A,float),np.array(b,float)).tolist()
def expand(q,px):
    cx=sum(p[0] for p in q)/4; cy=sum(p[1] for p in q)/4; o=[]
    for x,y in q:
        dx,dy=x-cx,y-cy; n=(dx*dx+dy*dy)**.5; o.append((x+dx/n*px,y+dy/n*px))
    return o
base=Image.open(BASE).convert("RGB")
dq=expand(SCREEN,1.5)
layer=flat.transform(base.size,Image.PERSPECTIVE,coeffs(dq,W,H),Image.BICUBIC)
mask=Image.new("L",(base.size[0]*3,base.size[1]*3),0)
ImageDraw.Draw(mask).polygon([(x*3,y*3) for x,y in dq],fill=255)
mask=mask.resize(base.size,Image.LANCZOS)
Image.composite(layer,base,mask).save(OUT,quality=95)
flat.save("/tmp/claude-0/-home-user-Diyetisyen-Web/e41dd7e6-c0f5-56e1-b80a-11bb233e9350/scratchpad/p5/crops/flat_ui.png")
print("ok",OUT)
