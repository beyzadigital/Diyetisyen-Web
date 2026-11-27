from PIL import Image, ImageDraw, ImageFont
FONT="/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"; K=1.17; INK=(28,18,10)
SRC="/home/user/Diyetisyen-Web/dark-money/images/post1/yazisiz/sayfa7.jpg"
OUT="/home/user/Diyetisyen-Web/dark-money/images/post1/yazili/sayfa7.jpg"
im=Image.open(SRC).convert("RGB"); d=ImageDraw.Draw(im)
def inner(b):
    x0,y0,x1,y1=b; w=x1-x0; h=y1-y0
    return [int(v*K) for v in (x0+w*.13,y0+h*.17,x1-w*.13,y1-h*.20)]
def wrap(t,f,mw):
    ls,c=[],""
    for w in t.split():
        s=(c+" "+w).strip()
        if d.textlength(s,font=f)<=mw: c=s
        else: ls.append(c); c=w
    if c: ls.append(c)
    return ls
def draw_block(parts,box,mx=96,gap_lines=0,colors=None):
    # parts: list of text; between parts a blank gap of gap_lines lines
    x0,y0,x1,y1=box
    for s in range(mx,22,-2):
        f=ImageFont.truetype(FONT,s); lh=int(s*1.12)
        blocks=[wrap(p,f,x1-x0) for p in parts]
        n=sum(len(b) for b in blocks)+gap_lines*(len(parts)-1)
        if n*lh<=y1-y0: break
    y=y0+((y1-y0)-n*lh)/2
    for i,b in enumerate(blocks):
        for l in b:
            wl=d.textlength(l,font=f); d.text((x0+((x1-x0)-wl)/2,y),l,font=f,fill=(colors[i] if colors else INK)); y+=lh
        if i<len(blocks)-1: y+=gap_lines*lh
draw_block(["Ben tasarruf ettiğimi sanmıştım."],inner((15,60,650,415)))
draw_block(["Ne kadar harcadığına da bak.","@moneyymadam","hesabını takip et, şirketlerin seni nasıl daha çok almaya ittiğini öğren."],inner((655,30,1480,475)),gap_lines=0,colors=[INK,(176,104,12),INK])
im.save(OUT,quality=92)
