"""Post6 sayfa 3: laptop ekranı bir uygulama penceresi olarak çizilir ve ekranın TÜM camına oturtulur.
İçerik: amber pencere çubuğu (sekme, yeni sekme, küçült/büyüt/kapat), başlık, sol portre kartı (yarı çizilmiş),
sağ karakter haritası kartı (paltolu kadının boy görünümleri; mimikler YOK), altta amber BAŞLA butonu.
Girdi : post6/yazisiz/kaynak/sayfa3_ilk.jpg + kaynak/karakter_haritasi.png   Çıktı: post6/yazisiz/sayfa3.jpg
"""
import numpy as np
from PIL import Image, ImageDraw, ImageChops, ImageFilter, ImageFont
R="/home/user/Diyetisyen-Web/dark-money/images/post6/yazisiz/"
BASE=R+"kaynak/sayfa3_ilk.jpg"; OUT=R+"sayfa3.jpg"; SHEET=R+"kaynak/karakter_haritasi.png"
FB="/usr/share/fonts/opentype/inter/Inter-"
PAPER_QUAD=[(1063.9,1496.3),(1586.0,1508.1),(1517.1,1943.9),(988.8,1885.8)]   # eski iç beyaz alan (portreyi çıkarmak için)
GLASS_QUAD=[(1044.0,1481.0),(1590.8,1493.3),(1518.5,1948.2),(967.4,1886.2)]  # ekran camının tamamı (bezelin iç kenarı)
SHEET_BOX=(325,490,1034,972)                                                  # paltolu kadın: 5 boy görünüm
FW,FH=1100,874
AMBER=(246,166,35); AMBER_D=(196,112,8); INK=(52,44,40); WHITE=(255,255,255); EDGE=(206,198,190)

def coeffs(out_pts,in_pts):
    A=[];b=[]
    for (x,y),(u,v) in zip(out_pts,in_pts):
        A.append([x,y,1,0,0,0,-u*x,-u*y]); b.append(u)
        A.append([0,0,0,x,y,1,-v*x,-v*y]); b.append(v)
    return np.linalg.solve(np.array(A,float),np.array(b,float)).tolist()
def grow(q,px):
    cx=sum(p[0] for p in q)/4; cy=sum(p[1] for p in q)/4; o=[]
    for x,y in q:
        dx,dy=x-cx,y-cy; n=(dx*dx+dy*dy)**.5; o.append((x+dx/n*px,y+dy/n*px))
    return o
def F(w,sz): return ImageFont.truetype(FB+w+".otf",sz)

base=Image.open(BASE).convert("RGB")
# 1) portre: eski ekrandan düzleştirip al
PW,PH=1040,860
portrait=base.transform((PW,PH),Image.PERSPECTIVE,coeffs([(0,0),(PW,0),(PW,PH),(0,PH)],PAPER_QUAD),Image.BICUBIC)

# 2) düz pencere tuvali
canvas=Image.new("RGB",(FW,FH),WHITE); d=ImageDraw.Draw(canvas)
HB=78
# ---- pencere çubuğu (en üstte, camın kenarına bitişik)
d.rectangle([0,0,FW,HB],fill=AMBER); d.line([(0,HB),(FW,HB)],fill=AMBER_D,width=3)
d.rounded_rectangle([26,14,392,HB+16],18,fill=WHITE,outline=AMBER_D,width=2)
d.rectangle([28,HB-3,390,HB+12],fill=WHITE)
cx_,cy_=68,46
d.polygon([(cx_,cy_-15),(cx_+4,cy_-4),(cx_+15,cy_),(cx_+4,cy_+4),(cx_,cy_+15),(cx_-4,cy_+4),(cx_-15,cy_),(cx_-4,cy_-4)],fill=INK)
d.text((104,46),"Karakter Oluştur",font=F("SemiBold",26),fill=INK,anchor="lm")
for o in ((-7,-7,7,7),(-7,7,7,-7)): d.line([(364+o[0],46+o[1]),(364+o[2],46+o[3])],fill=(120,108,100),width=3)
d.line([(432,46),(454,46)],fill=INK,width=4); d.line([(443,35),(443,57)],fill=INK,width=4)
d.line([(FW-196,46),(FW-170,46)],fill=INK,width=4)
d.rectangle([FW-130,33,FW-104,59],outline=INK,width=4)
d.ellipse([FW-84,20,FW-26,72],fill=(214,64,58))
for o in ((-9,-9,9,9),(-9,9,9,-9)): d.line([(FW-55+o[0],46+o[1]),(FW-55+o[2],46+o[3])],fill=WHITE,width=5)

# ---- başlık
TITLE="AI ile kendi karakterini oluştur"
tf=F("Bold",64)
while d.textlength(TITLE,font=tf)>FW*0.9: tf=F("Bold",tf.size-2)
d.text((FW/2,HB+84),TITLE,font=tf,fill=(44,36,32),anchor="mm")

# ---- kartlar
GAP=24; CW=(FW-3*GAP)//2; ROW0=HB+156
pw,ph=portrait.size; p2=portrait.resize((CW,int(ph*CW/pw)),Image.LANCZOS); rowh=p2.size[1]
canvas.paste(p2,(GAP,ROW0)); d.rectangle([GAP,ROW0,GAP+CW,ROW0+rowh],outline=EDGE,width=3)
sh=Image.open(SHEET).convert("RGB").crop(SHEET_BOX); sw,sh_=sh.size
t=sh.resize((CW-24,int(sh_*(CW-24)/sw)),Image.LANCZOS); t=ImageChops.multiply(t,Image.new("RGB",t.size,(252,250,247)))
ch=t.size[1]+30; cy0=ROW0+(rowh-ch)//2; cx0=2*GAP+CW
d.rounded_rectangle([cx0,cy0,cx0+CW,cy0+ch],10,fill=(252,250,247),outline=EDGE,width=3)
canvas.paste(t,(cx0+12,cy0+15))

# ---- amber BAŞLA butonu (kartların altında, ortalı)
BW,BH=400,92; bx=(FW-BW)//2; by=ROW0+rowh+38
d.rounded_rectangle([bx,by+8,bx+BW,by+BH+8],30,fill=AMBER_D)          # alt kalınlık
d.rounded_rectangle([bx,by,bx+BW,by+BH],30,fill=AMBER)
hl=Image.new("RGBA",(BW,BH//2),(255,255,255,0)); hd=ImageDraw.Draw(hl)
hd.rounded_rectangle([8,6,BW-8,BH//2],24,fill=(255,255,255,46))
canvas.paste(hl,(bx,by),hl)
d.text((bx+BW/2,by+BH/2+1),"BAŞLA",font=F("ExtraBold",50),fill=INK,anchor="mm")

# ---- cam hissi: kenarlara hafif iç gölge + çapraz yansıma
ov=Image.new("RGBA",(FW,FH),(0,0,0,0)); od=ImageDraw.Draw(ov)
for i in range(18):
    a=int(46*(1-i/18)**2)
    od.rectangle([i,i,FW-1-i,FH-1-i],outline=(0,0,0,a),width=1)
od.polygon([(FW*0.55,0),(FW*0.78,0),(FW*0.40,FH),(FW*0.17,FH)],fill=(255,255,255,16))
canvas=Image.alpha_composite(canvas.convert("RGBA"),ov).convert("RGB")

# 3) ekranın tüm camına perspektifle oturt (yuvarlak köşeli maske)
dq=grow(GLASS_QUAD,-1.5)
rect=[(0,0),(FW,0),(FW,FH),(0,FH)]
layer=canvas.transform(base.size,Image.PERSPECTIVE,coeffs(dq,rect),Image.BICUBIC)
rm=Image.new("L",(FW,FH),0); ImageDraw.Draw(rm).rounded_rectangle([0,0,FW-1,FH-1],26,fill=255)
mask=rm.transform(base.size,Image.PERSPECTIVE,coeffs(dq,rect),Image.BICUBIC).filter(ImageFilter.GaussianBlur(0.8))
Image.composite(layer,base,mask).save(OUT,quality=95)
canvas.save("/tmp/claude-0/-home-user-Diyetisyen-Web/e41dd7e6-c0f5-56e1-b80a-11bb233e9350/scratchpad/p5/crops/s3_flat.png")
print("ok",OUT)
