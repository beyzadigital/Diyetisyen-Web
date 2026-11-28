"""Post6 sayfa 1: laptop ekranını @moneyymadam'ın kendi Instagram profil sayfası olarak çizer.
Üst çubukta Instagram ikonu; profil resmi, kullanıcı adı, 'Profili düzenle' / 'Arşivi görüntüle' (kendi sayfası olduğunu belli eder),
profil adı, biyografi ve şapkalı kadının 3 gönderisi. Takipçi / takip / gönderi / beğeni SAYISI YOK.
Girdi : post6/yazisiz/kaynak/sayfa1_bos_ekran.jpg + kaynak/profil_resmi_kare.png   Çıktı: post6/yazisiz/sayfa1.jpg
"""
import math, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
R="/home/user/Diyetisyen-Web/dark-money/images/"
BASE=R+"post6/yazisiz/kaynak/sayfa1_bos_ekran.jpg"; AVATAR=R+"post6/yazisiz/kaynak/profil_resmi_kare.png"
OUT=R+"post6/yazisiz/sayfa1.jpg"
FD="/usr/share/fonts/opentype/inter/Inter-"; EMOJI="/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"
# ekranın beyaz alanının köşeleri (sol-üst, sağ-üst, sağ-alt, sol-alt)
SCREEN=[(1250,1515),(1696,1521),(1594,1996),(1165,1912)]
# ızgara sırası (soldan sağa): yağmurlu sokak, ofis, butik
SRC=[(R+"post3/yazisiz/sayfa1.jpg",(1322,168,1792,638)),
     (R+"post4/yazisiz/sayfa4.jpg",(851,1131,1523,1803)),
     (R+"post1/yazisiz/sayfa1.jpg",(1121,607,1744,1230))]
NAME="Money Madam | AI ile Kazan"; USER="moneyymadam"
BIO=[("🎭","Yüz göstermeden AI ile sayfanızı oluşturun ve kazanmayı öğrenin"),
     ("💸","Para dünyasının arkasındaki küçük sırları keşfedin"),
     ("👑","Kendi kazancının Madam’ı ol")]
W,H=1000,1000; K=2
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
def emoji(ch,x,y,size):
    f=ImageFont.truetype(EMOJI,109); g=Image.new("RGBA",(160,140),(0,0,0,0))
    ImageDraw.Draw(g).text((0,0),ch,font=f,embedded_color=True)
    g=g.crop(g.getbbox()); s=r(size); g=g.resize((s,int(s*g.size[1]/g.size[0])),Image.LANCZOS)
    cv.paste(g,(r(x),r(y)),g)

def insta_glyph(x,y,s):
    S=int(s*K*3); yy,xx=np.mgrid[0:S,0:S]
    t=1-((xx/S)*0.55+(1-yy/S)*0.9)/1.45
    stops=[(0,(254,218,117)),(0.3,(250,126,30)),(0.55,(214,41,118)),(0.8,(150,47,191)),(1,(79,91,213))]
    px=np.zeros((S,S,3))
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

def avatar_circle(d_px):
    av=Image.open(AVATAR).convert("RGB").resize((r(d_px),r(d_px)),Image.LANCZOS)
    m=Image.new("L",av.size,0); ImageDraw.Draw(m).ellipse([0,0,av.size[0]-1,av.size[1]-1],fill=255)
    return av,m

# ---- üst çubuk
d.rectangle([0,0,W*K,r(86)],fill=(255,255,255)); line([(0,86),(W,86)],2,LINE)
insta_glyph(34,17,52)
rrect((300,21,610,65),22,fill=(238,233,228))
circ(334,43,9,outline=GRAY,w=3); line([(341,50),(349,58)],3,GRAY)
d.text((r(362),r(43)),"Ara",font=font("Medium",20),fill=GRAY,anchor="lm")
line([(690,46),(708,30),(726,46)],3.2); line([(695,44),(695,62),(721,62),(721,44)],3.2)
rrect((764,31,796,63),9,outline=INK,w=3.2); line([(780,38),(780,56)],3.2); line([(771,47),(789,47)],3.2)
pts=[]
for a in np.linspace(0,2*math.pi,80):
    hx=16*math.sin(a)**3; hy=13*math.cos(a)-5*math.cos(2*a)-2*math.cos(3*a)-math.cos(4*a)
    pts.append((846+hx,46-hy))
d.polygon([(r(x),r(y)) for x,y in pts],outline=INK,width=r(3.2))
av,m=avatar_circle(44); cv.paste(av,(r(900),r(21)),m); circ(922,43,23,outline=INK,w=2)

# ---- profil başlığı: avatar (halka + artı rozeti), kullanıcı adı, butonlar
AV=186; AX,AY=76,118
circ(AX+AV/2+5,AY+AV/2+5,AV/2+9,outline=(221,225,230),w=4)
av,m=avatar_circle(AV); cv.paste(av,(r(AX+5),r(AY+5)),m)
circ(AX+AV-12,AY+AV-8,25,fill=(255,255,255)); circ(AX+AV-12,AY+AV-8,20,fill=(28,28,32))
line([(AX+AV-12,AY+AV-18),(AX+AV-12,AY+AV+2)],3.6,(255,255,255)); line([(AX+AV-22,AY+AV-8),(AX+AV-2,AY+AV-8)],3.6,(255,255,255))
d.text((r(340),r(150)),USER,font=font("Bold",60),fill=INK,anchor="lm")
cx,cy=915,150
for i in range(8):
    a=i*math.pi/4
    line([(cx+math.cos(a)*15,cy+math.sin(a)*15),(cx+math.cos(a)*23,cy+math.sin(a)*23)],7,INK)
circ(cx,cy,18,fill=INK); circ(cx,cy,8,fill=BG)
rrect((340,214,600,274),15,fill=(236,231,226))
d.text((r(470),r(244)),"Profili düzenle",font=font("SemiBold",27),fill=INK,anchor="mm")
rrect((616,214,876,274),15,fill=(236,231,226))
d.text((r(746),r(244)),"Arşivi görüntüle",font=font("SemiBold",27),fill=INK,anchor="mm")

# ---- profil adı + biyografi (ekran görüntüsündeki gerçek metin)
d.text((r(76),r(352)),NAME,font=font("Bold",40),fill=INK,anchor="lm")
BF=font("Medium",31); maxw=(W-76-48-50)*K
y=406
for em,txt in BIO:
    # uzun satırı kelimelere bölerek sar
    lines=[];cur=""
    for w in txt.split():
        s=(cur+" "+w).strip()
        if d.textlength(s,font=BF)<=maxw: cur=s
        else: lines.append(cur); cur=w
    lines.append(cur)
    emoji(em,76,y-17,33)
    for i,l in enumerate(lines):
        d.text((r(124),r(y)),l,font=BF,fill=INK,anchor="lm"); y+=45
    y+=3

# ---- sekmeler
ty=y+10
line([(40,ty),(960,ty)],2,LINE)
gx,gy=367,ty+20
for i in range(3):
    for j in range(3): rrect((gx+i*12,gy+j*12,gx+i*12+9,gy+j*12+9),1.5,fill=INK)
line([(330,ty),(440,ty)],3.5,INK)
rrect((484,ty+18,516,ty+50),9,outline=GRAY,w=3); d.polygon([(r(496),r(ty+26)),(r(496),r(ty+42)),(r(509),r(ty+34))],fill=GRAY)
rrect((564,ty+18,596,ty+50),9,outline=GRAY,w=3); circ(580,ty+29,5,outline=GRAY,w=2.6); d.arc([r(569),r(ty+36),r(591),r(ty+60)],200,340,fill=GRAY,width=r(2.6))

# ---- gönderi ızgarası (3 gönderi, tek sıra)
PAD=46; SZ=(W-2*PAD-2*8)//3; gy0=ty+68
for i in range(3):
    t=crop(i); s=min(t.size); t=t.crop(((t.size[0]-s)//2,(t.size[1]-s)//2,(t.size[0]+s)//2,(t.size[1]+s)//2)).resize((r(SZ),r(SZ)),Image.LANCZOS)
    cv.paste(t,(r(PAD+i*(SZ+8)),r(gy0)))
print("grid bitiş y:",gy0+SZ,"/",H)

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
