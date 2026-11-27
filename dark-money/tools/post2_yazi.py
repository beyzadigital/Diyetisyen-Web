import os
from PIL import Image, ImageDraw, ImageFont
FONT="/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
K=1.17; INK=(28,18,10)
SRC="/home/user/Diyetisyen-Web/dark-money/images/post2/yazisiz"
OUT="/home/user/Diyetisyen-Web/dark-money/images/post2/yazili"
# balon dis kutulari (gorunen koordinat 1493x2000): (x0,y0,x1,y1)
B={1:[(30,50,660,390),(670,30,1480,470)],
   2:[(30,50,665,395),(670,25,1480,470)],
   3:[(38,62,722,440),(738,55,1478,450)],
   4:[(85,12,720,390),(732,5,1475,415)],
   5:[(50,48,695,430),(710,38,1478,460)]}
T={1:["Patlamış mısır neden bu kadar pahalı?","Film stüdyoları bilet gelirinden pay alır. Sinema, patlamış mısır gibi ürünlerin satışından daha fazla kazanır."],
   2:["Ağda rolonu ucuzdu. Neden sürekli yeni bant alıyorum?","Rolonu bir kez alırsın. Yeni bant aldıkça onlar para kazanmaya devam eder."],
   3:["Ücretsiz bir oyun nasıl para kazanır?","Oyuncular kıyafet, oyun parası ve başka ekstralar satın alabilir."],
   4:["Bu uygulamayı kullanmak için para ödemiyorum.","Şirketler sana reklam göstermek için ödeme yapar. Satın aldıkları şey senin dikkatin."],
   5:["Demek ürün, hikâyenin sadece bir parçası.","hesabını takip et. İşletmelerin parayı nasıl kazandığını anlatıyoruz."]}
def inner(b,top_reserve=0.0):
    x0,y0,x1,y1=b; w=x1-x0; h=y1-y0
    ix0=x0+w*0.13; ix1=x1-w*0.13; iy0=y0+h*0.17; iy1=y1-h*0.20
    iy0+= (iy1-iy0)*top_reserve
    return [int(v*K) for v in (ix0,iy0,ix1,iy1)]
def wrap(d,t,f,mw):
    ls,c=[],""
    for w in t.split():
        s=(c+" "+w).strip()
        if d.textlength(s,font=f)<=mw: c=s
        else: ls.append(c); c=w
    if c: ls.append(c)
    return ls
def fit(d,t,box,mx=96):
    x0,y0,x1,y1=box
    for s in range(mx,22,-2):
        f=ImageFont.truetype(FONT,s); ls=wrap(d,t,f,x1-x0)
        lh=int(s*1.12)
        if lh*len(ls)<=y1-y0 and all(d.textlength(l,font=f)<=x1-x0 for l in ls): return f,ls,lh
    f=ImageFont.truetype(FONT,22); return f,wrap(d,t,f,x1-x0),25
os.makedirs(OUT,exist_ok=True)
for n in range(1,6):
    im=Image.open(f"{SRC}/sayfa{n}.jpg").convert("RGB"); d=ImageDraw.Draw(im)
    sizes=[]
    for i,(b,t) in enumerate(zip(B[n],T[n])):
        box=inner(b, 0.30 if (n==5 and i==1) else 0.0)
        f,ls,lh=fit(d,t,box)
        if n==5 and i==1: y=box[1]
        else: y=box[1]+((box[3]-box[1])-lh*len(ls))/2
        for l in ls:
            wl=d.textlength(l,font=f); d.text((box[0]+((box[2]-box[0])-wl)/2,y),l,font=f,fill=INK); y+=lh
        if n==5 and i==1:
            ob=inner(b,0.0); nm="@moneyymadam"; nf=ImageFont.truetype(FONT,int(f.size*1.25))
            wn=d.textlength(nm,font=nf); ty=ob[1]+((box[1]-ob[1])-nf.size)/2
            d.text((ob[0]+((ob[2]-ob[0])-wn)/2,ty),nm,font=nf,fill=(176,104,12))
    im.save(f"{OUT}/sayfa{n}.jpg",quality=92)
sheet=Image.new("RGB",(436*5,584))
for n in range(1,6): sheet.paste(Image.open(f"{OUT}/sayfa{n}.jpg").resize((436,584)),((n-1)*436,0))
sheet.save("ozet_post2.png")
