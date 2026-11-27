# Moneyy Madam — Proje Devam Notu

Bu dosya, yeni bir Claude Code sohbetinde kaldığımız yerden devam etmek için yazıldı.
Son güncelleme: 2026-11-27 (kullanıcı düzeltmeleri işlendi). Güvenilir olmayan ya da teyit edilmemiş bilgiler **[BELİRSİZ]** ile işaretlidir.

---

## 0. Hızlı Özet

- Proje: Instagram için **kaydırmalı (carousel) gönderiler**. Para/işletme/kariyer konularında "gizli düzenleri" anlatan, çizgi film (2D illüstrasyon) tarzında görsel serisi.
- Hesap adı: **@moneyymadam** (sayfa adı "Moneyy Madam"). Karar verildi, görsellere eklendi.
- Referans (esinlendiğimiz) hesap: **@darkmoneyfilesai**. Aynı format, **kadın karakterlerle**, **Türkçe** metinle, **kendi amber renk paletimizle**.
- Şimdiye kadar **4 gönderi** üretildi (toplam 24 görsel). Hepsi yazılı ve yazısız hâlleriyle depoda duruyor. **Oran kuralı: her zaman 4:5** (Gönderi 1–2 yanlışlıkla 3:4 kaldı, düzeltme bekliyor).
- Görsel üretim aracı: **Higgsfield** (model `gpt_image_2_6`). Yazılar yapay zekâyla değil, **Python/Pillow ile koda** eklenir (Türkçe harfler hatasız olsun diye).
- Her görselin sırası: **önce sahne (yazısız, boş balonlu/boş alt kısımlı) üretilir → onaylanır → yazı en son eklenir.**

> Not: Kullanıcı "animasyon" diyor, ama şu ana kadar üretilen şey **hareketsiz görsellerden oluşan kaydırmalı gönderilerdir**. Video/animasyon üretildiğine dair bir karar yok. **[BELİRSİZ: ileride video/animasyon isteniyor mu]**

---

## 1. Projenin Amacı ve Konsepti

- Referans hesabın kaydırmalı gönderilerini inceleyip aynı formatta **özgün, Türkçe** içerik üretmek. Birebir kopya değil: karakterler, diyalog ve konular değiştirilir.
- Format: her gönderi 5–7 sayfa. Her sayfada tek sahne ya da iki panel (üst/alt). Karakterler: **ön planda duran endişeli/merak eden ana kadın** + **arkada yüzü görünmeyen şapkalı kadın** (bilge yönlendirici/kılavuz figür).
- Dil: **Türkçe**. İngilizce metinler çevrilip biraz değiştirilerek kullanılır.
- Para birimi: **dolar simgesi rakamdan SONRA**: `100$`, `60$`, `2$`, `+2$`. "dolar" kelimesi yazılmaz, `$` simgesi kullanılır.
- Hesap adı gerektiren çağrı cümlelerinde **@moneyymadam** altın/gold renkle vurgulanır.

---

## 2. Hikâye ve Senaryo (Gönderi Gönderi)

### Gönderi 1 — Tüketici psikolojisi / şirketler seni nasıl daha çok harcatır (7 sayfa)
Konu: İndirim, kıtlık, ücretsiz kargo, paket fiyat, "üst satış", sosyal kanıt, sonunda harcama farkındalığı + takip çağrısı.
1. Mağazada elbise: 100$ üstü çizili, 60$.
2. Evde laptop başında: "son 2 ürün" (kıtlık), laptop ekranında çanta 139.99$ ve kırmızı "Sepete Ekle" butonu.
3. Masada laptop: ücretsiz kargo için 15$ daha ekle (kargo 5$).
4. Market rafı: 3 tanesi 24$ / 1 tanesi 10$ (mor lavanta ürünler).
5. Kafe: büyük boy +2$ (tabela).
6. Kafede laptop: "çok satan" (laptop ekranında mor "En Çok Satanlar" butonu, alt orta).
7. Yağmurlu sokak: elinde poşet ve fiş, takip çağrısı.

### Gönderi 2 — "Para nasıl kazanılır?" (şirketler gelirini nereden elde eder) (5 sayfa)
1. Sinema (patlamış mısır pahalı) 2. Ağda bantları (set ucuz, yedek bant pahalı — referansta jilet vardı, bizde ağda rolonu ve bantlar) 3. Ücretsiz oyun (kıyafet/oyun parası satışı, laptopta kadın avatarlı moda oyunu) 4. Telefon ve reklam (sponsorlu pembe topuklu reklamı) 5. Son sahne / takip çağrısı (yağmurlu sokak, kitaplı şapkalı kadın).

### Gönderi 3 — "X yaşında …, Y yaşında başlar" zaman çizgisi (referansta 7 sayfa; bizde 6 sayfa üretildi)
Her sayfa iki panel: üst panel = geleceğin sonucu, alt panel = başlangıç. Sayfa 1 yoksulluk, 2 pişmanlık, 3 liderlik, 4 servet, 5 obezite, 7 "takip ettiğin içerikler hayatına dönüşür". **6. sayfa kullanıcı tarafından bilerek atlandı, üretilmeyecek.**

### Gönderi 4 — Kötü patron / lider karşılaştırması (6 sayfa)
Her sayfa iki panel: üst = patron (sert patron kadın), alt = lider (şapkalı kadın). Konular (cümlelerden çıkarılan, kullanıcı açıkça belirtmedi): hasta/izin, zam, hafta sonu iş, iş yığını, işten ayrılma **[BELİRSİZ: kullanıcının koyduğu resmî konu başlıkları]**. Son sayfa tek görsel + takip çağrısı.

---

## 3. Karakter Tasarımları (SON ONAYLANAN)

**Karakter sayfası görseli (güncel):** Higgsfield medya ID `4fdbe9fa-14f0-48cb-88d3-0ca1dd0117f0` (kullanıcının 2. gönderide verdiği güncellenmiş karakter görseli). **[BELİRSİZ: Higgsfield bu medyayı ne kadar saklar; süresi dolarsa kullanıcıdan yeniden istenmeli]**

### Ana kadın (ön plandaki, kırmızılı)
- Kahverengi dağınık/kıvırcık topuz, **sarı (blond) röfleli** saç.
- **Yuvarlak siyah gözlük**, yanağında **ben (beauty mark)**.
- **Bordo (burgundy) düğmeli gömlek**, **krem pantolon**.
- Gönderi 2'den itibaren bu hâli kullanılır.
- Kıyafet değişiklikleri (yalnızca belirtilen yerlerde):
  - Gönderi 3, sayfa 3 ve 4 üst panel: **beyaz gömlek + lacivert kadın blazer ceketi**. Alt paneller bordo gömlek.
  - Gönderi 3, sayfa 5 üst panel: aynı yüzle **obez** (kıyafet aynı bordo gömlek/krem pantolon). Alt panel: **yeşil eşofman takımı** (koyu yeşil, beyaz yan şeritli), beyaz çorap.
  - Gönderi 3, sayfa 2 üst panel: siyah garson önlüğü.
  - Gönderi 1 (eski): bordo gömlek, krem pantolon (aşağıdaki not).

### Şapkalı kadın (arkadaki, yüzü görünmeyen)
- **Siyah geniş kenarlı şapka gözlerini örter**, **kırmızı dudaklar** görünür.
- Uzun dalgalı koyu kahverengi saç.
- Uzun siyah palto, altında siyah balıkçı/boğazlı üst.
- Referanstaki paltolu adamın pozlarını yapar (başparmak yukarı, kitap tutma, kollar kavuşturulmuş vb.). Kapalı **deri kitap** (küre amblemli) taşıyabilir.

### Patron kadın (yalnızca Gönderi 4)
- **Mor/erik rengi blazer ve pantolon**, beyaz fiyonklu bluz, altın küpe, topuz saç, kırmızı dudak, sert/kibirli bakış.

### ESKİ karakter versiyonu (artık kullanılmıyor)
- İlk karakter sayfası (medya ID `b881ec80-e00e-44ee-95a5-c0f7b1b8a840`): çillerli, **gözlüksüz**, benli olmayan ana kadın.
- **Gönderi 1'in 1–7. sayfaları bu eski karakterle üretildi.** Kullanıcı kararı: **Gönderi 1 yeni karakterle YENİDEN ÜRETİLMEYECEK.** Aktif karakter, gözlüklü ve benli olan güncel karakter sayfasıdır (yukarıdaki ID). Bundan sonraki her üretimde bu karakter kullanılır.

---

## 4. Onaylanan Görsel Stil ve Standartlar

- **Stil:** 2D çizgi film/anime illüstrasyon (kalın kontur, sıcak boyama). Referans hesaptakiyle aynı mantık.
- **Renk paleti:** Sıcak **amber / altın-turuncu gün batımı** tonları (kullanıcının "sayfa rengimiz"). Referanslardaki koyu lacivert/gri gece görünümü **kullanılmaz**.
  - Gönderi 1, 2, 4: **karartma yok**, mekânlar aydınlık amber.
  - Gönderi 3: kullanıcı özellikle **mekânı ve diğer insanları karartıp**, kırmızılı kadını ve şapkalı kadını parlak bırakmamızı istedi (referanstaki gibi). Bu karartma **yalnızca Gönderi 3 için** geçerli. Gönderi 4 için kullanıcı açıkça "karartmayı unut" dedi.
- **Boyut KURALI (kullanıcı kararı): her gönderi, Dark Money referans sayfasının gönderi oranında yapılır.** Referans ekran görüntüleri yaklaşık 1290×1600 px, yani **4:5**. Yeni her görsel **4:5 (1792×2240 px)** üretilir.
  - Gönderi 3 ve 4: 4:5 (doğru).
  - **Gönderi 1 ve 2: 3:4 (1744×2336 px) üretildi. Bu YANLIŞ oran.** Başta referans oranını kontrol etmeden 3:4 seçtim, sonradan düzeltmedim. Kullanıcı bunun 4:5 olması gerektiğini söyledi. **Bu iki gönderiyi 4:5'e çevirme işi henüz yapılmadı** (bkz. Bölüm 10, 13).
- **Her görselde:** Her kadının tam **iki eli** olacak (fazla el/yanlış anatomi sorun çıkardı, düzeltildi).
- **Görselin içinde yazılar:** Referanstaki İngilizce yazılar silinir. Gerekli sahne yazıları (etiket, ekran düğmesi, tabela) Türkçe ve kısa tutulur; sorun çıkarsa boş bırakılıp koda eklenir.
- **Yazı kuralları (koddan eklenen):**
  - Yazı tipi: **Inter ExtraBold** (`/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf`).
  - Gönderi 1 ve 2: **konuşma balonları** içinde, koyu mürekkep rengi (28,18,10), balona sığacak şekilde otomatik boyut.
  - Gönderi 3: panel altlarında **büyük harfli**, krem renkli (255,247,232) alt yazı, koyu gölge + panel altı karartma. Büyük harf Türkçe kurala göre: `i→İ`, `ı→I`.
  - Gönderi 4: panel altlarında altın renkli etiket (`PATRON:` / `LİDER:`) + krem renkli büyük harfli tırnak içi cümle. Son sayfa: ilk satır normal harf, ikinci kısım büyük harf, `@moneyymadam` altın renkte biraz büyük.
  - Hesap adı rengi: altın (240,196,104); balon içinde krem zeminde okunsun diye koyu altın (176,104,12).

---

## 5. Sahne Sahne Üretim Planı ve Son Metinler

### Gönderi 1 (şu an 3:4, olması gereken 4:5; balonlu) — eski karakterle
| Sayfa | Sol balon | Sağ balon |
|---|---|---|
| 1 | 1 hafta önce 100$'dı, şimdi sadece 60$! | Önce yüksek fiyatı gösterirler. Böylece 60$ sana daha uygun gelir. |
| 2 | Son 2 ürün kalmış! Hemen almalıyım. | Bu mesaj kaçırma korkusu yaratır. Başka fiyatlara bakamadan aceleyle almana neden olur. |
| 3 | Ücretsiz kargo için 15$ daha eklemem lazım. | 5$ kargo ödememek için 15$'lık fazladan ürün alıyorsun. Tasarruf ettiğini sanırken daha çok harcıyorsun. |
| 4 | 3 tanesi 24$. Bu çok iyi bir fırsat! | Tanesi ucuz ama daha çok alıyorsun. Tek ürün yeterliyken 14$ fazladan ödüyorsun. |
| 5 | Büyük boy sadece 2$ fazla. | Buna “üst satış” denir. Biraz daha fazla öde, daha büyüğünü al der. Sen de alırsın. (Tabela: BÜYÜK BOY AL, SADECE +2$ FARKLA) |
| 6 | Herkes bunu alıyor, iyidir herhalde. | Mağazalar, seni ikna etmek için yorumları ve satış sayılarını gösterir. Başkalarının aldığını görmek, senin de almanı kolaylaştırır. |
| 7 | Ben tasarruf ettiğimi sanmıştım. | Ne kadar harcadığına da bak. **@moneyymadam** hesabını takip et, şirketlerin seni nasıl daha çok almaya ittiğini öğren. |

Sahne içi yazılar (görselde, yapay zekâdan gelen): fiyat etiketleri `100$ → 60$`, laptop `139.99$`, "Sepete Ekle" (2. sayfa), 3. sayfa ekranı "Ücretsiz kargo için 15$ ekle" / kargo 5$, 4. sayfa tabelalar "3 ADET 24$" / "1 ADET 10$", 6. sayfa mor düğme "En Çok Satanlar". Bunlar görselde rakamdan sonra `$` olacak şekilde düzeltildi.

### Gönderi 2 (şu an 3:4, olması gereken 4:5; balonlu) — yeni karakterle, referans 2. gönderi görselleri
| Sayfa | Sol balon | Sağ balon |
|---|---|---|
| 1 (sinema) | Patlamış mısır neden bu kadar pahalı? | Film stüdyoları bilet gelirinden pay alır. Sinema, patlamış mısır gibi ürünlerin satışından daha fazla kazanır. |
| 2 (ağda) | Ağda rolonu ucuzdu. Neden sürekli yeni bant alıyorum? | Rolonu bir kez alırsın. Yeni bant aldıkça onlar para kazanmaya devam eder. |
| 3 (oyun) | Ücretsiz bir oyun nasıl para kazanır? | Oyuncular kıyafet, oyun parası ve başka ekstralar satın alabilir. |
| 4 (telefon/reklam) | Bu uygulamayı kullanmak için para ödemiyorum. | Şirketler sana reklam göstermek için ödeme yapar. Satın aldıkları şey senin dikkatin. |
| 5 (son) | Demek ürün, hikâyenin sadece bir parçası. | **@moneyymadam** (altın) / hesabını takip et. İşletmelerin parayı nasıl kazandığını anlatıyoruz. |

Sahne notları: 2. sayfada **jilet yok**, yerine ağda kutusu, rolon ve pembe bantlar. 3. sayfada **oyun kumandası ve fazla el kaldırıldı**, laptopta kadın avatarlı mor kıyafet oyunu ekranı. 4. sayfada pembe topuklu ayakkabı reklamı, telefon yandan görünür, ekranda **"Sponsorlu"** yazısı büyük (ekranda küçük bir saat "19:24" çıkmış, kaldırılmadı).

### Gönderi 3 (4:5, iki panel, alt yazılı, **mekan karartmalı**) — sayfalar 1,2,3,4,5,7 (6. sayfa bilerek yok)
| Sayfa | Üst yazı | Alt yazı | Sahne notu |
|---|---|---|---|
| 1 | 48 YAŞINDA YOKSULLUK, | 23 YAŞINDA BAŞLAR. | Yağmurlu sokak, mor omuz çantası (sırt çantası değil). Alt: barda gülen kadın |
| 2 | 44 YAŞINDA PİŞMANLIK, | 20 YAŞINDA BAŞLAR. | Üst: garson önlüklü kadın, akşam yemeği salonu. Alt: koltukta TV'ye kapılmış, elinde **kumanda**, dağınık cips/çikolata masası, kahve |
| 3 | 45 YAŞINDA LİDERLİK, | 22 YAŞINDA BAŞLAR. | Üst: beyaz gömlek + lacivert blazer, toplantı masası. Alt: bordo gömlek, flipchart sunumu |
| 4 | 40 YAŞINDA SERVET, | 19 YAŞINDA BAŞLAR. | Üst: beyaz gömlek + lacivert blazer, ofis, laptop. Alt: bordo gömlek, dağınık odada laptop |
| 5 | 52 YAŞINDA OBEZİTE, | 21 YAŞINDA BAŞLAR. | Üst: obez kadın muayene yatağında, doktor akciğer filmi. Alt: yeşil eşofmanla kanepede hamburger |
| 6 | — **bilerek atlandı** | — | Üretilmeyecek |
| 7 | 25 YAŞINDA TAKİP ETTİĞİN İÇERİKLER... | 45 YAŞINDA HAYATINA DÖNÜŞÜR. / TAKİP ETTİKLERİNLE BAŞLA. / OKULDA SANA ÖĞRETİLMEYEN PARA DERSLERİ İÇİN / **@moneyymadam** / HESABINI TAKİP ET. | Balkon + oturma odası, telefon |

Üst yazıların sonunda virgül, alt yazıların sonunda nokta var (referanstaki cümle iki panel boyunca devam eder). Kullanıcı nokta yazmıştı; ben virgül/nokta düzeni koydum. İtiraz gelmedi.

### Gönderi 4 (4:5, iki panel, diyalog alt yazılı, **karartma yok**) — 6 sayfa
| Sayfa | Üst panel (Patron) | Alt panel (Lider) |
|---|---|---|
| 1 | “Raporunu getir, sonra konuşalım.” | “Sen sağlığına bak, biz hallederiz.” |
| 2 | “Şu an zam konuşmanın sırası değil.” | “Emeğinin karşılığını birlikte değerlendirelim.” |
| 3 | “Beş dakikalık iş, hemen halledersin.” | “İyi hafta sonları, pazartesi görüşürüz.” |
| 4 | “Bunların hepsini bugün tamamlamanı istiyorum.” | “İlk günün, acele etme. Takıldığın yerde bana sor.” |
| 5 | “Senin yerini doldurmak zor olmayacaktır.” | “Yolun açık olsun. Seninle çalışmak güzeldi.” |

Sahneler: 1) hasta kadın yatakta telefonda, düşünce balonunda patron / diğerinde şapkalı kadın. 2) asansör önü (patron saatine bakıyor) / kafede şapkalı kadın finans raporu gösteriyor. 3) kanepede sandviç, patron "el sallama" düşüncesi / ofis önünde el sallayan iki kadın. 4) evrak yığını / ofiste kadın ve şapkalı kadın. 5) patronun odasında zarf bırakma / sarılma.
**Sayfa 6 (son, tek görsel):** Referanstaki adamın yerine **şapkalı kadın**, yağmurlu deniz kenarı terası, amber palet, alt beşte bir boş. Metin: “Kötü patronun önüne geçemezsin sanma; **KENDİ YOLUNU ÇİZEREK HAYATININ PATRONU OLABİLİRSİN.** Nasıl yapacağını öğrenmek için **@moneyymadam** hesabını takip et.” (Büyük/küçük harf ve altın renk referans son slayttaki gibi.)

---

## 6. Dosya Konumları

Depo: `beyzadigital/Diyetisyen-Web` (yerel: `/home/user/Diyetisyen-Web`). Çalışma dalı: **`claude/dark-money-dosya-dnd1vv`** (GitHub'a push edildi, **PR açılmadı**; kullanıcı istemedikçe açılmaz). `main` dalına dokunulmadı.

```
Diyetisyen-Web/
├── index.html, style.css, script.js, images/diyetisyen.jpg   ← ESKİ diyetisyen sitesi, DOKUNULMADI, Moneyy Madam ile ilgisi yok
├── Moneyy Madam.md                                           ← bu dosya
└── dark-money/
    ├── index.html, style.css, script.js, images/             ← ilk açılan BOŞ web sitesi iskeleti (koyu tema). Şu an kullanılmıyor [BELİRSİZ: web sitesi yapılacak mı]
    ├── tools/                                                ← yazı ekleme betikleri (aşağıya bak)
    └── images/
        ├── post1/yazili/ sayfa1..7.jpg   (3:4 — yanlış oran)   |  post1/yazisiz/ sayfa1..7.jpg
        ├── post2/yazili/ sayfa1..5.jpg   (3:4, yanlış oran)   |  post2/yazisiz/ sayfa1..5.jpg
        ├── post3/yazili/ sayfa1,2,3,4,5,7.jpg (4:5) | post3/yazisiz/ sayfa1,2,3,4,5,7.jpg
        └── post4/yazili/ sayfa1..6.jpg   (4:5)   |  post4/yazisiz/ sayfa1..6.jpg
```
GitHub: `https://github.com/beyzadigital/Diyetisyen-Web/tree/claude/dark-money-dosya-dnd1vv/dark-money/images/`

### Yazı ekleme betikleri (`dark-money/tools/`)
Hepsi Python 3 + Pillow, `python3 -I betik.py` ile çalışır. Yazısız görsellerden yazılıyı üretir.
- `post1_yazi_ekle.py` — kullanım: `python3 -I post1_yazi_ekle.py <kaynak.png> <çıktı.png> <sayfa_no>`. Balon koordinatları ve metinler içinde. (Ekran görüntüsü ölçeği için koordinatlar 1493×2000 ekranına göredir, çarpan 1.17.)
- `post1_sayfa7_yazi.py` — 1. gönderi 7. sayfa CTA balonu (hesap adı altın).
- `post2_yazi.py` — 2. gönderi 5 sayfa.
- `post3_yazi.py` — 3. gönderi (alt yazılar, 7. sayfa CTA).
- `post4_yazi.py` — 4. gönderi diyalogları + son sayfa.
**Dikkat:** Betiklerin içindeki kaynak/çıktı yolları `/home/user/Diyetisyen-Web/dark-money/images/...` biçimindedir (`post1_yazi_ekle.py` hariç, o yolları argüman olarak alır). Yeni sohbette yol değişirse düzeltilmeli. Betikler yazısız `sayfaN.jpg` dosyasını okuyup yazılıyı üretir. 1. gönderinin 7. sayfası için, hesap adı içeren sürüm `post1_sayfa7_yazi.py` ile üretilir; `post1_yazi_ekle.py` 7. sayfayı hesap adı olmadan yazar, bu yüzden 7. sayfa için **`post1_sayfa7_yazi.py` sonradan çalıştırılmalıdır.**

---

## 7. Teknik Bilgiler (Higgsfield ve Ortam)

- **Araç:** Higgsfield MCP (`mcp__Higgsfield__generate_image`, `generate_image_batch`, `jobs_wait`, `show_generation_by_ids`, `media_upload`, `media_confirm`). Model: `gpt_image_2_6`, kalite `high`, çözünürlük `2k`, oran **her zaman `4:5`** (post 1–2 eski üretimler yanlışlıkla `3:4` idi).
- **Maliyet:** Görsel başı yaklaşık 2 kredi. Başlangıçta bakiye 438.9 kredi idi; **güncel bakiye bilinmiyor** **[BELİRSİZ]**. Üretimden önce maliyet söylemeyi bazı sahnelerde atladım; kullanıcıya hatırlatmak iyi olur.
- **Aynı anda en fazla 4 iş** gönderilebiliyor (limit aşılırsa `submission_failed`).
- **Referans yükleme akışı:** `media_upload` → URL'ye `curl -X PUT -H "Content-Type: image/jpeg" -H "If-None-Match: *" --data-binary @dosya` → `media_confirm`. Referans görselleri üretim isteminde `image_references` ile verilir; önceki üretimin job ID'si de referans olabilir (stil/renk tutarlılığı için).
- **Ağ izni (bulut ortam):** Ortam `diyetisyen-web` (`env_011qfLxEN5QmV57tLGmDRV3j`) izinli hostlar: `upload.higgsfield.ai` (yükleme), `d8j0ntlcm91z4.cloudfront.net` (üretilen görselleri indirme). Yeni sohbet farklı ortamda açılırsa bu iki host yeniden eklenmeli.
- **GitHub:** Claude'un depoya yazması için GitHub bağlantısı kullanıcı tarafından yetkilendirildi. Push: `git push -u origin claude/dark-money-dosya-dnd1vv`. Commit mesajlarına şu satırlar eklenir: `Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>` ve `Claude-Session: https://claude.ai/code/session_01DJnELRHxzPfAmkumJCzBBp`.
- **Üretilen görselleri inceleme:** Görsel indirilip `Read` ile bakılır; küçük harfli sahne yazılarını (örn. "Sepete Ekle") yapay zekâ bazen hatalı yazar, bu yüzden kritik yazılar koda bırakılır.
- **Faydalı Higgsfield medya ID'leri (süreleri dolmuş olabilir) [BELİRSİZ]:** güncel karakter sayfası `4fdbe9fa-14f0-48cb-88d3-0ca1dd0117f0`; amber stil referansı olarak kullanılan üretimler `354e5a6a-293a-44d1-9050-72fcf81f279f` (G3 s3), `657a6d1f-c188-41f9-897a-85538997c2a9` (G2 s4).

---

## 8. Üretim İş Akışı (her yeni sayfa için)

1. Kullanıcı referans sayfa görselini gönderir. Ekran görüntüsüyse sahne kısmı kırpılır (arayüz, "1/7" etiketi, yazılar ve ikonlar çıkarılır).
2. Referans + güncel karakter sayfası + bir önceki amber üretim Higgsfield'a yüklenir.
3. İstem: referanstaki kompozisyonu kadın karakterlerle yeniden kur; amber palet; **yazı/rakam/etiket yok**; balonlar boş; her kadın için iki el; uygun oran.
4. Üretilen görsel indirilir, **kontrol edilir**, kullanıcıya gönderilir, depoya (`postN/yazisiz/sayfaM.jpg`) kaydedilir, commit + push yapılır.
5. Kullanıcı sahneleri onaylayınca Türkçe metin birlikte netleştirilir, sonra betikle yazılar eklenir (`postN/yazili/`), kullanıcıya gönderilir, push edilir.

---

## 9. Tamamlanan İşler

- Hesap adı kararı: @moneyymadam ve tüm CTA yerlerine eklendi.
- Gönderi 1: 7 sahne + Türkçe balon metinleri + görsel içi fiyatların `$` düzeltmesi. (Eski karakterle.)
- Gönderi 2: 5 sahne (yeni karakter) + Türkçe metinler + hesap adı.
- Gönderi 3: 6 sahne (1,2,3,4,5,7) + alt yazılar + hesap adı.
- Gönderi 4: 6 sahne + diyalog metinleri + son sayfa metni.
- Tüm yazılı ve yazısız görseller depoya push edildi.

## 10. Tamamlanmamış İşler / Mevcut Durum

- **Gönderi 3, 6. sayfa:** Kullanıcı **bilerek atladı**. Üretilmeyecek, eksik sayılmaz.
- **Gönderi 1 eski karakterle kalacak:** Kullanıcı kararı, yeniden üretilmeyecek.
- **Oran düzeltmesi bekliyor:** Gönderi 1 ve 2 görselleri 3:4, olması gereken 4:5. Nasıl çevrileceği (yeniden üretim mi, kırpma mı) **kullanıcıya sorulmadı/karara bağlanmadı**; kullanıcı henüz "çevir" demedi **[BELİRSİZ]**.
- Ufak bilinen kusurlar, kullanıcı şikâyet etmediği için **düzeltilmedi**: G2 s3 laptop ekranında "3,250" (virgül, referansta nokta); G2 s4 telefon ekranında küçük "19:24" saat; yeşil eşofman koyu yeşil çıktı (G3 s5); G3 s7 alt panelde yazılar vücut/paltonun üstüne biniyor (karartma ile okunur).
- İlk kurulan `dark-money/` web sitesi iskeleti boş, kullanılmıyor. Web sitesi yapılıp yapılmayacağı **belirsiz**.
- **Hashtag, paylaşım takvimi ve referans hesabın büyüme analizi (kaç günde bir paylaşım, hangi ayda açıldı, 11 bin takipçiye nasıl ulaştı):** Kullanıcı bunları **Claude Code'dan değil, elle kendisi yapıyor** (sohbet dolduğu için). Claude Code'da bu işler **yapılmayacak ve beklenmiyor**. Kullanıcı açıkça isterse tekrar konuşulur.
- Gönderi açıklaması (caption) konusu kullanıcıyla netleştirilmedi **[BELİRSİZ: caption'ı kim yazıyor]**.

## 11. Son Yapılan Revizeler (kronolojik, en yenisi sonda)

- Dolar simgesi **rakamdan sonra** (`100$`). Önceki `$100` yazımı **kaldırıldı**.
- 1. gönderi 7. sayfa CTA: hesap adı için boşluk, hesap adı bulununca @moneyymadam eklendi.
- 2. gönderi: karakter güncellendi (gözlük, röfle, ben). "Jilet" yerine ağda ürünleri. Kumanda ve fazla el silindi. Telefon ekranı yandan, "Sponsorlu", pembe topuklu.
- 3. gönderi: önce amber ton + mor omuz çantası (sırt çantası değil); sonra kullanıcı çevrenin karartılmasını istedi (referanstaki gibi). Sayfa 3–4 üst panel beyaz gömlek + lacivert blazer. Sayfa 5 üst obez, alt yeşil eşofman.
- 4. gönderi: karartma **yok**; boş yazı kutuları **silindi**; son sayfada adam yerine şapkalı kadın.
- Son: hesap adı tüm CTA'lara eklendi.

## 12. Geçersiz Kılınan / Artık Yapılmayacak Kararlar

- Eski karakter (çilli, gözlüksüz) → artık yeni karakter kullanılıyor. Gönderi 1 eski karakterle **kalır** (yeniden üretilmeyecek).
- 3:4 oran → artık **4:5** (Dark Money referans oranı). Gönderi 1–2 eski oranda kaldı, düzeltme bekliyor.
- "Gönderi 3'ün 6. sayfası eksik" düşüncesi → bilerek atlandı, eksik değil.
- "Referans hesap analizi / hashtag / takvim bu projede yapılacak" → kullanıcı elle yapıyor, Claude Code'da yapılmayacak.
- Metinde "dolar" kelimesi ve `$100` biçimi → artık `100$`.
- Hesap adı yer tutucuları ("[HESAP ADI]", boş balon) → artık **@moneyymadam**.
- Sepete Ekle düğmesi 6. sayfada → mor **"En Çok Satanlar"** düğmesi, alt ortada.
- 4. gönderide karartma → **uygulanmaz**.
- Oyun konsolu/oyun kolu: G2 s3'te elinden silindi. G3 s2 alt panelde istenen şey TV **kumandası** (oyun konsolu değil).

## 13. Bundan Sonraki Yapılacak İşler

1. **Yeni gönderi referansları** geldikçe (kullanıcı gönderecek) Bölüm 8 iş akışını uygula. **Her zaman 4:5 üret.**
2. **Gönderi 1 ve 2'yi 4:5'e çevirme:** Kullanıcı isterse yapılır. Önce yöntemi sor: yeniden üretim (kredi harcar, her sayfa ~2 kredi) ya da üst/alt kırpma (hızlı ama balon ve sahneyi kesebilir).
3. Kullanıcı isterse: PR açma (**açıkça istemedikçe açma**), caption yazımı.
4. Yapılmayacaklar: Gönderi 3'ün 6. sayfası, Gönderi 1'in yeni karakterle yeniden üretimi, hashtag/takvim/büyüme analizi (kullanıcı elle yapıyor).

## 14. Çalışma Kuralları (kullanıcı tercihleri)

- **Önce sahne, yazı en son.** Yazıyı kullanıcıyla birlikte çevirip değiştirdikten sonra ekle.
- **Oranı varsayma:** Her görsel Dark Money referans gönderisinin oranında (4:5) üretilir. Referansın oranını kontrol et.
- Üretim öncesi gerekli belirsizlik varsa kısa sor; kullanıcı "üret/başla" demeden pahalı toplu üretim yapma.
- Her görseli üretince **indirip kontrol et** ve ne gördüğünü dürüstçe söyle; doğrulayamadığını doğrulanmış gibi sunma.
- Kullanıcıya her görseli **buradan (sohbetten)** gönder; ayrıca depoya kaydet ve push et.
- Cevapları kısa, Türkçe ve net tut. Kullanıcı büyük harfle ve hızlı yazıyor; niyeti anla, gerekirse "şunu mu kastettin" diye işaretle.
- Aktif proje dosyalarını silme; yalnızca ekle/değiştir.
