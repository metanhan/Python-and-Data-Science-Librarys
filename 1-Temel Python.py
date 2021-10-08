# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 15:58:19 2021

@author: Mehmethan
"""


#----------Python Notları----------#

#   STR ve BAZI METODLAR - SLICING - INDEX   #

#   x bir değişken adı(str)/liste/tuple/set/sözlük olmak üzere:
#   x[başlangıç indeksi:son index:atlama miktarı] ile istenilen değerlere ulaşılabilir. 
#   Başlangıç değeri= -değerden itibaren; son index= -bu indekse kadar; atlama miktarı= -bu kadar adımla.
#   Bu tip işlemlere slicing denir.

deneme="deneme metnidir"
print(deneme[1:12:2])

liste=[1,2,3,4,5,6,7,8,9]
print(liste[1:6:3])

#   indexlerle işlem yapılabilir

islem=liste[0]*liste[5]
print(islem)
 
#   Slicing işleminde sadece atlama değerine - verilirse son indexten yazma işlemi yapılabilir.
ters=deneme[::-1]  # Bu özel kullanımda listw/vb. tamamen tersten yazar.
print(ters)


ilkBuyuk=deneme.capitalize()    # x.capitalize() metodu str tipte ilk harfi büyük yapar.
print(ilkBuyuk)

hepBuyuk=deneme.upper()         # x.upper() metodu bütün harfleri büyük yapar.
print(hepBuyuk)

ayri=deneme.split()             # x.split() metodu ifadenin aralarındaki boşluklardan ayırır ve bir liste oluşturur.
print(ayri)
print(ayri[0].capitalize()+" "+ayri[1].capitalize()) # Her iki kelimenin de baş harfi büyük yapıldı.

                                # str ile alakalı diğer metodları da öğren.

#----------DİZİLER/LİSTELER----------#

# Listeler "mutable" yani içindeki elemanlar değiştirilebilir yapılardır.

liste2=[1,2,3,4,5,6,7,8,9]   # şeklinde liste tanımlanabilir.
print(liste2)

bosListe=[]                 # Bu şekilde boş bir liste tanımlanıp sonradan atama veya 
bosListe2=list()            # append metodu ile içine elemanlar konulabilir.

liste2[0]=123                # ile listenin istenen indeksine istenen yeni değer verilebilir.
print(liste2)

liste2.append(532)           # x.append metodu ile listenin sonuna yeni elemanlar eklenebilir.
print(liste2)

liste2.pop()                 # x.pop metodu ile listeden parantez içinde istenen "indisteki eleman" silinebilir. 
print(liste2)                # Parantez içinde index değeri yoksa en son elemanı siler. 

liste2.remove(8)             # x.remove() metodu ile parantez içinde "belirtilen eleman" liste içerisinden silinebilir.
print(liste2) 

kacAdet=liste2.count(3)      # x.count() metodu ile parantez içinde belirtilen elemanın liste içerisinde kaç tane olduğu
print(kacAdet)              # kontrol edilebilir.


degisken1=23                            # Farklı değişkenler ile yeni listeler tanımlanabilir.
degisken2=21
degiskenListesi=[degisken1,degisken2]    # Virgül yerine matematik işlemleri de konulabilir. 
print(degiskenListesi)                   # Bu sayede yeni liste elemanları işlemlerle de belirlenebilir.


bilgi=["ben","mehmethan","yüksel"]      # listelerde/Listelerde STR işlemleri de yapılabilir.
cevap=["memnun","oldum"]
iletisim=[bilgi+cevap]
print(iletisim)

print(iletisim*5)                       # listeyi 5 kere yazdırıp bir liste oluşturur.


# Liste içerisinde farklı tipte elemanlar, hatta başka listeler bile tanımlanabilir.
karisikListe=[1,"kelime",["liste içinde liste",12.3,[1,2]]]
print(karisikListe[2][2][1])  # Şeklinde ifadelerle ile liste içerisindeki listelerin elemanlarına erişim sağlanabilir.



#----------SÖZLÜKLER----------#

# Sözlüklerin listelerden farkı key-value pairing (anahtar kelime - değer eşleşmesi) denilen özelliğidir.
# Adından da anlaşıldığı üzere sözlük içerisindeki bir elemanı çağırabilmek için bir anahtar kelime tanımlanır.

sozluk1={"ad":"mehmethan"}   # Sözlük içerisinden "ad" anahtar kelimesi çağrılınca ona karşılık gelen "mehmethan" 
print(sozluk1["ad"])         # değeri çağırılıp yazdırılacaktır.

sozluk1["ad"]="mustafa"      # Sözlük içerisindeki değerler yeni atamalarla değiştirilebilir(mutable).
print(sozluk1["ad"])

sozluk2={1:"ilk",-1:"önce",0.5:2134314}  #Anahtar kelimeler ve değerler istenen tipte olabilir.
print(sozluk2[0.5])

# Sözlük içinde liste hatta farklı sözlükler bile tanımlanabilir.
sozluk3={-12:[1,2,3],"liste":["as",7,0.54],"icSozluk":{"ad":[1,2,3],2:34}} 
# Listelerdekine benzer bir yöntemle, içerdeki liste ve sözlüklerden değer çağırılabilir.
print(sozluk3[-12][2])                  # Sözlük içinden liste elemanı çağırmak.
print(sozluk3["icSozluk"]["ad"][0])     # Sözlük içindeki sözlüğün içindeki listenin elemanının çağırılması.

print(sozluk3.keys())                   # Bu metot sayesinde sözlüğün key'leri çağırılabilir.  
print(sozluk3.values())                 # Bu metot sayesinde sözlüğün değerleri çağırılabilir.
                                        # Sözlüğe ait diğer metotlardan da öğren.

bosSozluk={}                            # Bu şekilde boş bir sözlük tanımlanıp sonradan içine elemanlar konulabilir.
bosSozluk2=dict()
bosSozluk["key"]="value"



#----------SET'LER----------#

# Setler listeler ile çok çok benzerdir. Aradaki fark ise bir Set'te her elemandan yalnızda bir tane bulunabilir.
# Listelerde kendini tekrar eden elemanlar bulunurken, set'lerde her elemandan bir tane bulunmaktadır.

birListe=[1,1,2,2,3,3]
print(birListe)
birSet=set(birListe)       # Yukardaki tanımın somut hali bu kodlarda görünmektedir.
print(birSet)

ornekSet={1,2,3,4,5}       # Set tanımlama şekli.
type(ornekSet)

bosSet=set()               # Bu şekilde boş bir set tanımlanıp sonradan x.add metodu ile içine elemanlar konulabilir.

bosSet.add(1)
bosSet.add(1)
bosSet.add(2)
bosSet.add(3)
print(bosSet)              # Görüleceği üzere her elemandan 1 tane bulunmakta. 



#----------TUPLE'LAR----------#

# Listelerle benzerlik gösterir ancak farkı immutable(değeri değiştirilemez) olmasıdır.
# Yani tuple bir kere tanımlandıktan sonra her hangi bir indexteki elemanı değiştiremeyiz.

ilkTuple=(1,2,3,4,5,"a","b")
ilkTuple[0]    

ilkTuple.count(1)    # Metodu ile istenen elemanın tuple içinde kaç kez geçtiğini öğrenebiliriz.

ilkTuple.index("a")  # Metodu ile istenen elemanın tuple'ın kaçıncı indeksinde olduğu öğrenilebilir.




#----------BOOLEAN----------#

# Adından da anlaşılacağı üzere boolean ifadeler True veya False'dur.
# True ve False değerleri bir değişkende tanımlı olabileceği gibi ">,<,>=,<=,!=,and,or,not" gibi 
# ifade karşılaştırmaları sonucunda da elde edilebilir.

a=1
b=2
a>b
a<b              # Sonuç değer False'dur, tipi ise Bool.

c=True           # Ön tanımlı True olan bir Bool ifadesi.

a!=b
a<b and a>b     
a<b or a>b
not a<b          # And, Or, Not kullanımı



#---------- if-elif-else Yapıları ----------#

# If ifadesi içinde tek değer kıyası haricinde and/or ile çoklu ifadeler de karşılaştırılabilir.
# == eşitse, != eşit değilse
d1=1
d2=2

if d1<d2 or d1>d2:
    print("vuhuğ")

# Değişkene True bir ifade ön tanımlanmışsa if içerisinde true yazmaya gerek yoktur.

dogru=True

if dogru:
    print("doğru")
   
# in ifadesi ile bir str,liste vb. şeylerin içinde istenen değerin varlığı kontrol edilebilir.

isim="mehmethan"
if "tha" in isim:
    print("istediğin kısım bulundu")

sayilar=[1,2,3,4,5]
if 3 in sayilar:
    print("burda")

sozlukA={"isim":"mehmethan","yaş":23}
if "isim" in sozlukA.keys():                # sozluk.keys metodu ile istenen key'in sözlükte varlığı kontrol edilir.
    print(sozlukA["isim"])

if 23 in sozlukA.values():
    print("genç")                           # sozluk.keys metodu ile istenen değerin sözlükte varlığı kontrol edilir.



#----------For Döngüsü----------#

# For döngüsünde bir string,liste,sözlük,tuple,set gibi ifadeler içindeki değerlerin indis değerleri 
# bir değişkene atanarak döngü altında istenen işlemler yapılabilir.

numList=[1,2,3,4,54,56,7,7,8]
for numara in numList:
    print(numara*2)

sayiTuple=(1,2,3,4,5,6,67,7)
for eleman in sayiTuple:
    print(eleman)
    
karisikliste=[(34,665,674),(1,2,3),(34,5,5)]
for (eleman,deger,degis) in karisikliste:     # Değişken sırası ile tuple indisini eşleyip ayrı ayrı değer alabiliyoruz.
    print(deger)                             # Aynı işlem dict'ler için de yapılabiir.
                                             
benimSozluk = {"muz": 150, "portakal" : 250, "elma" : 400}   # Sözlüklerde sozluk.items() metodu ile erişim sağlanır.
for (anahtar,deger) in benimSozluk.items():
    print(deger)



#----------Break-Continue-Pass----------#

# Break ifadesinin yazıldığı noktada program sonlandırılır. Döngü veya koşul içindeyse işlem o  noktada kesilir.
# Continue ifadesinin yazıldığı noktada program o kısmı atlar. Döngü veya koşul içindeyse o noktadan bir sonrakine geçilir.
# Pass ifadesi daha çok içine henüz bir şey yazılmamış döngü ve koşul ifadelerinde bir hata almamak amacıyla programın o kısmının
# görmezden gelinmesi için kullanılır.

benimListem = [5,10,15,20,25,30]

for numara in benimListem:
    if numara == 15:
        break
    print(numara)

for numara in benimListem:
    if numara == 15:
        continue
    print(numara)

for numara in benimListem:
    pass



#----------While Döngüsü----------#

# While döngüsü de yazım olarak if ile çok benzerdir. Aradaki fark ise yazılan "koşul sağlandığı sürece döngünün çalışmasıdır".
# İf koşul sağlanınca bir şey yaptırır, for belirli sınırlar içinde çalışır, While ise koşul sağlandığı sürece sürekli çalışır.

listeO=[1,2,3,4,5,67,8,8,7]
while 3 in listeO:
    print("çalışıyor")
    listeO.pop()

i=0    
while i<10:
    print(f"yeniDegisken'in güncel değeri: {i}")  # Çift tırnaktan önce konulan 'f' süslü panrantez({}) içindeki ifadenin 
    i=i+1                                         # kod bloğu olarak algılanıp çalıştırılmasını sağlar.



#----------Faydalı Metodlar----------#

# range(a,b,c) başlangıcı a, bitişi b, atlama miktarı c olacak şekilde değerler oluşturur.
# Oluşturulan değerler bir değişkene, listeye vb. atanabilir.

numara=list(range(0,10,2))
print(numara)


# enumerate liste, değişken vb. şeylerin elemanlarının indexleri ile birlikte yazılmasını sağlar. 
# Hem index hem de değer farklı olarak alınarak çeşitli işlemler yapılabilir.

for eleman in enumerate(list(range(0,9))):
    print(eleman)

for (index,eleman) in enumerate(list(range(0,9))):
    print(eleman)


# random(a,b) verilen aralıklarda rastgele değerlerin oluşturulmasını sağlar. 
# Kullanmadan önce kütüphanesinin dahil edilmesi gerekir.

from random import randint
randint(0, 100)

# shuffle(liste) metodu ile listenin içindeki elemaların yerleri random şekilde karıştırılır.

from random import shuffle
liste1=[1,2,3,4,5]
shuffle(liste1)
print(liste1)

# birlesikListe=zip(liste1,liste,...) metodu ile listeler birleştirilip yeni bir liste oluşturulur.
# Yeni liste tipi bir tuple'dır.
liste1=["bir","iki","üç"]
liste2=[1,2,3]
liste3=["sa","naber","yo"]
birlesikListe=list(zip(liste1,liste2,liste3))
print(birlesikListe)

# Çok kullanışlı özel bir liste ve döngü tekniği bulunmaktadır.

ad="mehmethan"
listeAd=[eleman for eleman in ad]  # Bir değişken içindeki eğeri önce bir değişkene atayıp döngü ile çevirip daha sonra ister yine
print(listeAd)                     # bir değişkene atıp kullanılabilir ya da istenen farklı işlemler yapılabilir.
                                   # Bu tekniğin farklı kullanım şekillerini araştır.



#----------Fonksiyon Tanımlama----------#

def fonksiyonAdi(alabilecekDeger):                 # Fonksiyonun adı verildikten sonra parantez içinde işleme tabii tutulacak 
    print("fonksiyon çalışıyor!")                  # bir değişken verilebilir. İstenirse bu değişkene bir ön değer de tanımlanabilir.
    alabilecekYeniDeger=alabilecekDeger+" metni"   # Bu sayede fonksiyon içinde bir değer verilmezse ön tanımlı değer ile işlem yapılır.
    return alabilecekYeniDeger                     # return ise işlemler yapıldıktan sonra çıktıyı fonksiyon dışına geri çevirir.
                                                   # Bu sayede işlenmiş yeni değer değişkene atanıp farklı şeyler için kullanılabilir.
fonksiyonAdi("deneme")                             # Fonksiyonun çağırılması da bu şekilde yapılır.

# Fonksiyonda birden fazla değerle işlem yapılması gerekiyorsa bir sınırlama olmaması için "*args" ifadesi parantez içine yazılır.
# Aslında bu ifadede önemli olan "*" işaretidir, "args" yerine başka bir şey de yazılabilir ama evrensel bir kullanım olduğu için
# "*args" tercih edilmesi daha iyi olacaktır.

def topla(*args):
    return sum(args)
sonuc=topla(1,2,3,4,5,6,7,7,8,9)
print(sonuc)


# "**kwargs" ile de bir anahtar değer ve onun değeri alınabilir. Oluşan çıktı bir sözlük olacaktır.
# Yine bunda da "kwargs" zorunlu bir ifade olmamasına rağmen kullanımı tercih edilmelidir.

def degerler(**kwargs):
    return kwargs
degerler(ad="mehmethan",yas=22)




#----------Faydalı Fonksiyonlar----------#

# Map fonksiyonu iki adet değer alır. İlki çalıştırılmak istenen fonksiyon, ikincisi ise fonksiyon içinde çalıştırılmak istenen şey.

def bolmeIslemi(numara):
    return numara / 2

benimListem = [1,2,3,4,5,6,7,8,9,10]
print(list(map(bolmeIslemi,benimListem)))


def kontrolFonksiyonu(string):
    return "a" in string
stringListesi = ["metan","begonya","ares","badem","mehmet","ahmet"]
sonucListesi = list(map(kontrolFonksiyonu,stringListesi))
print(sonucListesi)


# Filter fonksiyonu map ile benzerdir. Aradaki fark str işlemlerde bool ifade yerine değerleri geri döndürür.
def kontrolFonksiyonu(string):
    return "a" in string
stringListesi = ["metan","begonya","ares","badem","mehmet","ahmet"]
print(list(filter(kontrolFonksiyonu,stringListesi)))


# Lambda ayrıca bir fonksiyon tanımlamaya gerek kalmadan aritmetik işlemlerin yapılabilmesini sağlar.
# Tek satırda halledilmesi gereken küçük şeylerde kullanılabilir.
ornekListesi = [10,20,30]
print(list(map(lambda numara : numara * 4,ornekListesi)))



