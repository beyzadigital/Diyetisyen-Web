"""Post6 sayfa 3: laptop ekranında yarı çizilmiş portre sola kayar, sağına karakter haritasından
paltolu kadının önden / çapraz / yandan / arkadan boy görünümleri eklenir (mimikler ve büyük portre YOK).
Girdi : post6/yazisiz/kaynak/sayfa3_ilk.jpg + karakter haritası PNG   Çıktı: post6/yazisiz/sayfa3.jpg
"""
import numpy as np
from PIL import Image, ImageDraw, ImageChops, ImageFilter, ImageFont
R="/home/user/Diyetisyen-Web/dark-money/images/post6/yazisiz/"
BASE=R+"kaynak/sayfa3_ilk.jpg"; OUT=R+"sayfa3.jpg"
SHEET=R+"kaynak/karakter_haritasi.png"
QUAD=[(1063.9,1496.3),(1586.0,1508.1),(1517.1,1943.9),(988.8,1885.8)]   # ekranın kağıt alanı (sol-üst, sağ-üst, sağ-alt, sol-alt)
FW,FH=1040,860                                              # düz ekran tuvali
SHEET_BOX=(325,490,1034,972)                                # paltolu kadın: 5 boy görünüm

def coeffs(out_pts,in_pts):
    A=[];b=[]
    for (x,y),(u,v) in zip(out_pts,in_pts):
        A.append([x,y,1,0,0,0,-u*x,-u*y]); b.append(u)
        A.append([0,0,0,x,y,1,-v*x,-v*y]); b.append(v)
    return np.linalg.solve(np.array(A,float),np.array(b,float)).tolist()
def expand(q,px):
    cx=sum(p[0] for p in q)/4; cy=sum(p[1] for p in q)/4; o=[]
    for x,y in q:
        dx,dy=x-cx,y-cy; n=(dx*dx+dy*dy)**.5; o.append((x+dx/n*px,y+dy/n*px))
    return o

base=Image.open(BASE).convert("RGB")
rect=[(0,0),(FW,0),(FW,FH),(0,FH)]
# 1) mevcut ekranı düzleştir (portre)
flat=base.transform((FW,FH),Image.PERSPECTIVE,coeffs(rect,QUAD),Image.BICUBIC)
paper=tuple(int(v) for v in np.median(np.asarray(flat)[90:150,900:1000].reshape(-1,3),axis=0))
print("kağıt rengi",paper)
# portrenin sınırlayıcı kutusu (kağıt renginden farklı alan)
a=np.asarray(flat).astype(int); diff=np.abs(a-np.array(paper)).max(axis=2)>28
ys,xs=np.where(diff); bx=(max(0,xs.min()-6),max(0,ys.min()-6),min(FW,xs.max()+6),min(FH,ys.max()+6)); print("portre kutusu",bx)
portrait=flat.crop(bx)

# 2) yeni düz ekran: sol portre kartı, sağ karakter haritası kartı
BG=(255,255,255); CARD=(252,250,247); EDGE=(206,198,190)
canvas=Image.new("RGB",(FW,FH),BG); d=ImageDraw.Draw(canvas)
GAP=22; CW=(FW-3*GAP)//2
# portre kartı
pw,ph=portrait.size; s=CW/pw
p2=portrait.resize((CW,int(ph*s)),Image.LANCZOS)
py=(FH-p2.size[1])//2
canvas.paste(p2,(GAP,py)); d.rectangle([GAP,py,GAP+CW,py+p2.size[1]],outline=EDGE,width=3)
# karakter haritası kartı (paltolu kadın, 5 boy görünüm)
sh=Image.open(SHEET).convert("RGB").crop(SHEET_BOX)
sw,sh_=sh.size; s2=(CW-24)/sw
t=sh.resize((CW-24,int(sh_*s2)),Image.LANCZOS)
t=ImageChops.multiply(t,Image.new("RGB",t.size,CARD))
ch=t.size[1]+30; cy0=(FH-ch)//2; cx0=2*GAP+CW
d.rounded_rectangle([cx0,cy0,cx0+CW,cy0+ch],10,fill=CARD,outline=EDGE,width=3)
canvas.paste(t,(cx0+12,cy0+15))

# ekran başlığı
TITLE="AI ile kendi karakterini oluştur"
tf=ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-Bold.otf",62)
while d.textlength(TITLE,font=tf)>FW*0.9: tf=ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-Bold.otf",tf.size-2)
top_card=min(py,cy0)
d.text((FW/2,top_card/2),TITLE,font=tf,fill=(44,36,32),anchor="mm")

canvas=ImageChops.offset(canvas,0,46)   # başlık + kartlar bloğunu dikeyde ortala

# ---- uygulama penceresi çubuğu: sekme + yeni sekme + küçült / büyüt / kapat
canvas=canvas.copy(); w=ImageDraw.Draw(canvas)
HB=76; BARC=(246,166,35); AMB_D=(196,112,8); INK2=(52,44,40)
w.rectangle([0,0,FW,HB],fill=BARC)
w.line([(0,HB),(FW,HB)],fill=AMB_D,width=2)
# açık sekme (üstü yuvarlak, içeriğe bitişik)
w.rounded_rectangle([26,16,372,HB+14],16,fill=(255,255,255),outline=AMB_D,width=2)
w.rectangle([28,HB-2,370,HB+10],fill=(255,255,255))
# sekme ikonu: dört köşeli parıltı
cx_,cy_=64,46
for dx,dy in ((0,-13),(13,0),(0,13),(-13,0)): w.line([(cx_,cy_),(cx_+dx,cy_+dy)],fill=INK2,width=4)
w.polygon([(cx_,cy_-14),(cx_+4,cy_-4),(cx_+14,cy_),(cx_+4,cy_+4),(cx_,cy_+14),(cx_-4,cy_+4),(cx_-14,cy_),(cx_-4,cy_-4)],fill=INK2)
tf2=ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-SemiBold.otf",25)
w.text((98,46),"Karakter Oluştur",font=tf2,fill=INK2,anchor="lm")
# sekme kapat (küçük x)
for o in ((-7,-7,7,7),(-7,7,7,-7)): w.line([(346+o[0],46+o[1]),(346+o[2],46+o[3])],fill=(120,108,100),width=3)
# yeni sekme +
w.line([(412,46),(432,46)],fill=INK2,width=4); w.line([(422,36),(422,56)],fill=INK2,width=4)
# pencere denetimleri (sağ üst)
w.line([(FW-182,46),(FW-158,46)],fill=INK2,width=4)                                 # küçült
w.rectangle([FW-122,34,FW-98,58],outline=INK2,width=4)                              # büyüt
w.ellipse([FW-78,22,FW-22,70],fill=(214,64,58))                                     # kapat
for o in ((-8,-8,8,8),(-8,8,8,-8)): w.line([(FW-50+o[0],46+o[1]),(FW-50+o[2],46+o[3])],fill=(255,255,255),width=5)

# 3) tekrar eğimle ekrana yerleştir
dq=expand(QUAD,2.5)
layer=canvas.transform(base.size,Image.PERSPECTIVE,coeffs(dq,rect),Image.BICUBIC)
mask=Image.new("L",(base.size[0]*3,base.size[1]*3),0)
ImageDraw.Draw(mask).polygon([(x*3,y*3) for x,y in dq],fill=255)
mask=mask.resize(base.size,Image.LANCZOS)
Image.composite(layer,base,mask).save(OUT,quality=95)
canvas.save("/tmp/claude-0/-home-user-Diyetisyen-Web/e41dd7e6-c0f5-56e1-b80a-11bb233e9350/scratchpad/p5/crops/s3_flat.png")
print("ok",OUT)
