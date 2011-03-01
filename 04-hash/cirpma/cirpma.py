def cirpma_fonk(csv_dosyasi):
    import csv
    csv_dosyasi = 'ogrenci_Listesi.csv' # Sonradan silinecek.

    alfabe = 'abcdefghijklmnopqrstuvwxyz'
    cirpma_sonuclari = dict()
    cirpma_degeri = 0
    i = 0
    for row in csv.reader(open(csv_dosyasi)):
        j = 1
        for col in row:
            cirpma_degeri +=  alfabe.find(col[0])*(j**5 ) + alfabe.find(col[len(col)-1])*(j**3) 
            j = j + 7 # j=j*10 gibi j' yi dongu icerisinde degistiren yapilar...
        cirpma_sonuclari[i] = cirpma_degeri % 50
        i = i + 1
    print cirpma_sonuclari
    return cirpma_sonuclari



def farkLi_sonucLar(cirpma_sonuclari):
    uzunluk = len(cirpma_sonuclari)

    for i in range(0, uzunluk):
        for j in range(0, uzunluk):
            if not(i==j):
                if (cirpma_sonuclari[i] == cirpma_sonuclari[j]):
                    cirpma_sonuclari[j] = -1
    farkLiLarin_sayisi = 0
    for i in range(0, uzunluk):
        if (cirpma_sonuclari[i] != -1):
            farkLiLarin_sayisi = farkLiLarin_sayisi + 1
    print 'Basari : ', ((farkLiLarin_sayisi * 1.0)/uzunluk)

    return farkLiLarin_sayisi

#F5 e basinca komut satirina alttaki komutu yaz:
# farkLi_sonucLar(cirpma_fonk(''))
