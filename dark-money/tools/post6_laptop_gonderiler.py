"""Gönderi (post6) sayfa 1: laptop ekranındaki 3 boş kareye şapkalı kadının kendi gönderilerini yerleştirir.
Kaynak: yalnızca şapkalı kadın görünecek şekilde kırpılmış yazısız sahneler (Gönderi 4 s4, Gönderi 3 s1, Gönderi 1 s1).
Girdi : post6/yazisiz/kaynak/sayfa1_bos_ekran.jpg   Çıktı: post6/yazisiz/sayfa1.jpg
"""
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
R="/home/user/Diyetisyen-Web/dark-money/images/"
BASE=R+"post6/yazisiz/kaynak/sayfa1_bos_ekran.jpg"
OUT=R+"post6/yazisiz/sayfa1.jpg"
# ekrandaki 3 karenin köşeleri (sol-üst, sağ-üst, sağ-alt, sol-alt), soldan sağa
QUADS=[[(1220,1788),(1327,1800),(1300,1916),(1194,1896)],
       [(1346,1803),(1464,1816),(1435,1942),(1319,1920)],
       [(1485,1818),(1605,1832),(1575,1968),(1456,1945)]]
# şapkalı kadını gösteren kare kırpmalar (x0,y0,x1,y1)
SRC=[(R+"post4/yazisiz/sayfa4.jpg",(851,1131,1523,1803)),
     (R+"post3/yazisiz/sayfa1.jpg",(1322,168,1792,638)),
     (R+"post1/yazisiz/sayfa1.jpg",(1121,607,1744,1230))]

def coeffs(dst,S):
    src=[(0,0),(S,0),(S,S),(0,S)]
    A=[];b=[]
    for (x,y),(u,v) in zip(dst,src):
        A.append([x,y,1,0,0,0,-u*x,-u*y]); b.append(u)
        A.append([0,0,0,x,y,1,-v*x,-v*y]); b.append(v)
    return np.linalg.solve(np.array(A,float),np.array(b,float)).tolist()

def expand(q,px):
    cx=sum(p[0] for p in q)/4; cy=sum(p[1] for p in q)/4; out=[]
    for x,y in q:
        dx,dy=x-cx,y-cy; n=(dx*dx+dy*dy)**.5
        out.append((x+dx/n*px,y+dy/n*px))
    return out

def clean_tail(im):
    # 3. kırpmadaki baloncuk kuyruğu ucunu arka plandan örnekle boyayarak temizle
    a=np.asarray(im).astype(float)
    for y in range(0,42):
        a[y,419:486]=a[y,486:502].mean(axis=0)
    out=Image.fromarray(a.astype("uint8"))
    m=Image.new("L",im.size,0); ImageDraw.Draw(m).rectangle((417,0,488,43),fill=255)
    blur=out.filter(ImageFilter.GaussianBlur(1.2))
    return Image.composite(blur,im,m.filter(ImageFilter.GaussianBlur(1.0)))

base=Image.open(BASE).convert("RGB")
# hesap adının altındaki istenmeyen küçük noktayı sil (yandaki beyaz ekran satırlarından örnekle)
_a=np.asarray(base).astype(float)
for y in range(1779,1790):
    _a[y,1408:1423]=_a[y,1426:1441].mean(axis=0)
base=Image.fromarray(_a.astype("uint8"))
for q,(path,box) in zip(QUADS,SRC):
    crop=Image.open(path).convert("RGB").crop(box)
    if "post1" in path: crop=clean_tail(crop)
    S=260
    crop=crop.resize((S,S),Image.LANCZOS)
    dq=expand(q,3.5)
    layer=crop.transform(base.size,Image.PERSPECTIVE,coeffs(dq,S),Image.BICUBIC)
    mask=Image.new("L",(base.size[0]*3,base.size[1]*3),0)
    ImageDraw.Draw(mask).polygon([(x*3,y*3) for x,y in dq],fill=255)
    mask=mask.resize(base.size,Image.LANCZOS)
    base=Image.composite(layer,base,mask)
base.save(OUT,quality=95)
print("ok",OUT)
