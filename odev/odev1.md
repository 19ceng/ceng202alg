# Ödev1: Sıralama ve Mükemmel Çırpı Tasarımı

CENG202 HESAPLAMA TEKNİKLERİ (BİL202) - ÖDEV 1

Ödevde ihtiyacınız olacak csv dosyası: [ogrenci10.csv](ogrenci10.csv) ve ödevin
pdf versiyonu: [odev1.pdf](odev1.pdf). Ödevin teslimi için son tarih:
**05.Mart.2011**. Ödevi kendi `@bil` adresinden,
<mailto:ceng202hestek@bil.omu.edu.tr/> adresine göndermelisiniz.

## Bölüm 1: Mükemmel Çırpma - 75 puan

Ödevin bu bölümünde sizden, 75 öğrencinin TC kimlik numarası ve isim
bilgilerinin yer aldığı bir veri kümesi için hatasız bir çırpma fonksiyonu
gerçeklemeniz beklenmektedir. Buna göre:

- Programınızı yazacağınız modülün (betik dosyasının) ismini, **p[öğrenci numaranız]**
şeklinde belirleyiniz. Örneğin, numarası 09876543 olan bir öğrencinin
hazırlayacağı betik dosyası, **“p09876543.py”** isminde olmalıdır. Numaranızın ilk
hanesi “0” olsa da bu “0” ı kullanınız.

- Modülünüzün içerisinde *sadece bir tane* fonksiyon bulunmalı ve bu fonksiyonun adı
*kesinlikle* “hash” olmalıdır. Aksi halde ödeviniz değerlendirilmeyecektir.

- `hash` fonksiyonunuz, argüman olarak TC kimlik numarası almalı ve sonuç olarak
`[1, 75]` kapalı aralığında bir çırpı değeri döndürmelidir.

- Sizden istenen, 75 farklı TC kimlik numarasının her biri için farklı bir çırpı
değeri üretebilen bir `hash` fonksiyonu yazmanızdır. Bu durumda, ödevinizin 1.
bölümüne tam (75) puan verilecektir. Eğer yazmış olduğunuz `hash` fonksiyonu, 75
farklı TC kimlik numarası içerisinden 2 veya daha fazlası için aynı çırpı
değerini üretiyorsa ya da herhangi bir TC kimlik numarası için [1, 75] kapalı
aralığı dışında bir değer üretiyorsa fonksiyonunuz bu TC kimlik numaraları için
başarısız olmuş demektir. Bu durumda ise bu bölümden, başarılı olunan (kendileri
için eşsiz çırpı değerleri üretilen) TC kimlik numarası adedince puan
verilecektir.

## Bölüm 2: Arama Algoritmaları - 25 puan

Bu bölümde ise sizden, derste öğrendiğiniz arama algoritmalarını (ardışıl sıralı
arama, ardışıl sırasız arama, ikil arama) performans kriteri bakımından
karşılaştırarak hızlıdan yavaşa doğru sıralayacak bir Python programı yazmanız
beklenmektedir. Bu işlemler için de bir önceki bölümde bahsedilen veri kümesini
kullanmanız gerekmektedir. Daha sağlıklı sonuç elde etmek adına tek bir öğeyi
aratmak yerine belirli sayıda öğeyi aratarak ortalama performans değerleri
üzerinden hareket ediniz.

