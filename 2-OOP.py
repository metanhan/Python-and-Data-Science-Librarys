# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 15:58:19 2021

@author: Mehmethan
"""

#----------Sınıf Tanımlama----------#

# Sınıf tanımlarken sınıfın ismini büyük harfle yazmak genel jargona daha uygundur. Büyük harf sınıf adı küçük harf o sınıfın  
# attribute'u olarak kalıplaşmıştır.
# __init__ metodu sınıftan bir nesne oluşturulup nesne çağırıldığında direkt olarak çalıştırılacak fonksiyonların tanımlanmasını sağlar.
# Bunlar ve daha fazla metodun kullanımlarını daha ayrıntılı olarak bak.
# Bu metodları bulmak için "Magic Methods" ya da "Dunder Methods" yazarak araştırma yapabilirsin.
# Bir sınıf tanımlarken nesne içerisindeki tüm değerlere "self" parametresi ile ulaşılır. "self" yerine 
# başka kelimeler de kullanılabilir ancak programlama camiası geneli bir jargon haline geldiği için "self" ifadesi daha 
# kullanışlı olacaktır.
# Tanımlanacak nesnenin ilk parametresi self olmalıdır.


class Oyun():
    def __init__(self,isim,tur,yil):
        self.isim=isim       # eşittirden önceki "isim" attribute'u temsil eder, sonraki "isim" ise sınıfın aldığı argümanı temsil eder.
        self.tur=tur         # self.xxx şeklindeki kısım fonksiyona ait özelliklere(attributes) erişmek için belirlenen isimlerdir.
        self.yil=yil         # bu tıpkı daha önce kullandığımız metodların alt özelliklerine erişmek için "." koymamızla aynı şey.
                             # aslında self ifadesi ile alt özellikleri tanımlıyoruz. alt isimlere karşılık gelen değerleri ise
                             # sınıf parametrelerinden seçiyoruz.
    def genelBilgi(self):
        print(f"oyunun genel bilgileri: {self.isim}, {self.tur}, {self.yil}")

                             
tesSkyrim=Oyun("Skyrim", "RPG",2011)
print(tesSkyrim.isim)
tesSkyrim.isim="elder scrools v"  # şeklinde mevcut değerler değiştirilebilir.
print(tesSkyrim.isim)

print(tesSkyrim.genelBilgi()) # diğer bir fonksiyon ile farklı işlemler yapılabilir. sınıf içindeki iletişim self ifadesi ile sağlanır.

# Sınıf içindeki fonksiyonlardaki argümanlare (mesela isim,tur,yil) ön değerler verilebilir. Bu sayede kullanıcı tarafınfan hiçbir bilgi
# gelmese bile programın çökmesinin önüne geçilebilir. Farklı bir değer atamsı yapıldığı anda ise yine değer değişecektir.
# Ön tanımlı değer kalıcı değildir.


# Farklı sınıflar birbirine bağlandığı takdirde birbirlerinin özelliklerini kullanabilir. Buna kalıtım almak (inheritance) denmektedir.

class Deniyoruz():
    def __init__(self):
        print("Deniyoruz sınıfı çalıştı")
        
    def metod1(self):
        print("deniyoruz metod1")
        
    def metod2(self):
        print("deniyoruz metod2")
        
class Deney(Deniyoruz):
    def __init__(self):
        Deniyoruz.__init__(self)        # Deniyoruz sınıfına ait init fonksiyonunu bile çağırabiliyoruz.
        print("deney sınıf çalıştı") 
        
    def metod2(self):
        print("deney metod2")           # Deniyoruz sınıfına ait metodları kullanabilmemizin yanında bu sınıf içinde de aynı isimde 
                                        # fakat farklı işleve ait fonksiyonlar yazıp kullanabiliriz.
deney1=Deniyoruz()
deney1.metod2()

deney2=Deney()
deney2.metod2()                         # Aynı isimli olmasına rağmen Deney sınıfındaki nesne ile çağırdığımız için onu çalıştırdı.



# Aynı isimdeki fonksiyonlar/methodların farklı amaca hizmet edebilmesine Polymorphism(çok boyutluluk) denmektedir.

class TesV():
    def __init__(self,isim):
        self.isim=isim
    def oyunAdi(self):
        return self.isim+" oyunun adıdır."

class Fallout():
    def __init__(self,isim):
        self.isim=isim
    def oyunAdi(self):
        return self.isim+" oyunun adıdır."

skyrim=TesV("skyrim")
skyrim.oyunAdi()
                                    
newVegas=Fallout("new vegas")
newVegas.oyunAdi()


oyunListesi=[skyrim,newVegas]
for oyun in oyunListesi:            # oyunAdi fonksiyonu farklı sınıflarda olmasına rağmen oluşturulan nesnelerin sınıfı ayrı olduğu 
    print(oyun.oyunAdi())           # için ait olduğu sınıftaki fonksiyonlar çalışmaktadır. Bu çok boyutluluktur.



def isimOgren(oyun):
    print(oyun.oyunAdi())
                                    # Bu da farklı bir uygulamasıdır. Bu şekilde çeşitlendirilebilir.
isimOgren(skyrim)
isimOgren(newVegas)    


# __str__ metodu sınıftan geri döndürülen değerlerin print gibi ifadelerde yazılabilmesini sağlar. Bu metod olmadan print ile
# bir çıktı alınamaz.
# __len__ metodu sınıfta karşılık gelen değerlerin çağırılmasını sağlar.

class Meyve():
    
    def __init__(self,isim,kalori):
        self.isim = isim
        self.kalori = kalori
        
    def __str__(self):
        return f"{self.isim} şu kadar kaloriye sahiptir: {self.kalori}"
    
    def __len__(self):
        return self.kalori

muz = Meyve("Muz",150)
muz.kalori
print(muz)
len(muz)




#--------------------try&except&else&finally--------------------#

# İstenmeyen girdiler karşısında programın çökmesini önlemek için try-except yapısı kullanılmaktadır.
# Else yapısı altındaki ifadelerin hemen çağırılması istenmiyorsa bu yapı kullanılabilir. Mesela break ile döngü bitirilsin isteniyorsa.
# Finally ise her durumda en son çağırılacak yapılar için kullanılabilir.

while True:
    try:
        sayiDeger=int(input("sayı giriniz: "))
    except:
        print("sadece sayı giriniz!")
        continue
    else: 
        print("işlem sonlandı!")
        break
    finally:
        print("bizi kullandığınız için teşekkürler :) ")




