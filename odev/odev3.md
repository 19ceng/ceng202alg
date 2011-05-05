# Ödev3: Sınırlandırılmış Öncelik Kuyruğu

CENG202 HESAPLAMA TEKNİKLERİ (BİL202) - ÖDEV 3

Ödevin teslimi için son tarih:
**10.Mayıs.2011**. Ödevi kendi `@bil` adresinizden,
<mailto:ceng202hestek@bil.omu.edu.tr/> adresine göndermelisiniz. Bunun haricinde
bir yöntemle/adrese gönderilen mailler dikkate alınmayacak ve ödevden sıfır
alacaktır.

## Açıklama

İkil Yığın ile ilgili yapılacaklar,

- min yerine max temelinde gerçeklenmelidir

- yığın boyutu `N` ile sınırlanmalıdır. Yığın dolduğunda aşağıda verilen strateji izlenmelidir

- `buildHeap` işlevi sıralama temelinde gerçeklenecektir.

- tasarımınızı yük (iş) bilgisi tutacak biçimde tasarlanmanız gerekecek. Bu
  amaçla paralel iki liste (`heapList` yerine `priorityList` ve `loadList`)
  kullanabilir veya tek listede elemanları tuple'da tutabilirsiniz (`heapList =
  [(priority, load)]`)

Yığın doluyken yeni eleman geldiğinde,

- yığın içindekilerden daha düşük öncelikle geleni reddet

- yığın içindekilerden en düşük öncelikliyle eşitse de reddet

- yığın içindekilerden daha yüksek öncelikli geldiyse en düşük öncelikliyi
  yığından çıkart ve onun yerine yeni geleni koy ve doğru yerine süzülerek
  hareket ettir. `insert` yöntemi dikkatli tasarlanmalıdır

Yukarıda verilen İkil Yığın'dan miraslanan Öncelik Kuyruğu Soyut Veri Türünü
gerçekleyiniz. Gerçekleyeceğiniz Öncelik Kuyruğu aşağıdaki doctestten
geçebilmelidir.

	>>> pq = PriorityQueue(N=4)
	>>> pq.enqueue(priority=1, load='A')
	>>> pq.enqueue(priority=2, load='B')
	>>> pq.enqueue(priority=3, load='C')
	>>> pq.enqueue(priority=2, load='D')
	>>> pq.enqueue(priority=1, load='E')
	>>> pq.dequeu()
	'C'
	>>> pq.dequeu()
	'B'
	>>> pq.dequeu()
	'D'
	>>> pq.dequeu()
	'A'
	>>> pq.dequeu()
	'Kuyruk Bos'

