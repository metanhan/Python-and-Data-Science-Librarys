# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 15:57:41 2021

@author: Mehmethan
"""

#--------------------NUMPY KÜTÜPHANESİ--------------------#

# Matrix işlemleri yapılmasına olanak sağlar.
# Çok çeşitli metodları bulunmaktadır.

import numpy as np # as np ifadesi ile kütüphane adını uzunca yazmaktansa np olarak çağırmak istedğimizi belirtiyoruz.

#  numpy.array metodu ile hazırda var olan bir liste ile veya kendi tanımımız ile bir numpy dizisi taznımlarız.
liste=[1,2,3,4,5,6,7,8,9]
theMatrix=np.array(liste)
print(type(theMatrix))
print(theMatrix)

matrixList=[[1,2,3],[4,5,6],[7,8,9]]
matrix2=np.array(matrixList)
print(matrix2)                        # 3x3 boyutunda bir matrise dönüştü dizi içinde dizi olan yapımız.

# arange metodu range metodu ile aynı işi yapmaktadır.

mesafe=np.arange(0,20,3)
print(mesafe)

# zeros metodu ile istenen boyutta sıfır matrisler oluşturulabilir.
sifir=np.zeros((3,3))
print(sifir)

# ones metodu ile istenen boyutta birim matrisler oluşturulabilir.
bir=np.ones((3,3))

# full metodu ile istenen boyutta ve istenen değerleri içeren bir matris oluşturulabilir.
dolu=np.full((3,3), "metan")

# linspace verilen aralıkra istenen sayıda değer oluşturur. Değerlerin özellikleri ise aralarında eşit miktarda fark olmasıdır.
# Kısaca istenen değer aralığını istenen sayıda eşit parçaya böler.
esitParca=np.linspace(0,10,20)
print(esitParca)

# eye metodu verilen boyutta köşegenleri 1, geri kalan elemanları 0 olan bir matris oluşturur.
kosegen=np.eye(5)
print(kosegen)

# random metodu da bildiğimiz random gibi çalışır. İstenen kadar değer veya istenen boyutta rastgele matris oluşturur.  
# Çağırılma şekli biraz farklı sadece. Alt özellikleri bulunmakta.

randomSayi=np.random.randn(4,5) # Random şekilde sayılar ve matrisler oluşturur. Genellikle float değerler.
print(randomSayi)

randomSayi2=np.random.randint(1,10,3) # Bunun farkı ise oluşan sayılar tam sayıdır.
print(randomSayi2)                    # İstenen aralıkta istenen sayıda değer döndürmekte.

# reshape metodu adından da anlaşılacağı üzere diziyi istenen boyutta bir matrise çevirir.

yenidenBoyut=np.arange(0,10).reshape(5,2) # Burdaki gibi birleştirilmiş tanımlamalar da yapılabilir.
print(yenidenBoyut)
print(yenidenBoyut.dtype)  # dtype metodu ile veri tipi öğrenilebilir.
diziMatris=np.array([1,2,3,4,5,6,7,8]).reshape(2,4)
print(diziMatris)

# Diziler ve matrisler içerisindeki en küçük ve en büyük değeri veren metodlar da vardır.Hatta bunların indexlerini de alabiliriz.

print(diziMatris.max())    # Bu
print(diziMatris.min())    # ve bu en büyük ve en küçük değerleri verir.
print(diziMatris.argmax()) # Bu
print(diziMatris.argmin()) # ve bu en büyük ve en küçük değerlerin indexini verir.

print(diziMatris.shape)    # Bu metod ise matrisin boyutunu verir.
print(diziMatris.ravel())  # reshape metodunun tam aksini yapar. Çok boyutlu bir diziyi tek boyuta çevirir.


#----------Numpy Dizilerinde Slicing İşlemleri----------#

# Bildiğimiz slicing işlemlerini numpy dizileri ile de yapabilmekteyiz.

diziDizisi=np.arange(1,10)
print(diziDizisi[4])         # İstenen indisi yazdırmak.
print(diziDizisi[1:9:2])     # Belli aralıklarda istenen miktar kadar boşlukla yazdırma.
yeniHal=diziDizisi[1:3]      # Dizinin belli bir kısmı başka bir değişkene atanda
yeniHal[:]=9                 # Yeni dizinin tüm elemanları yeni bir değerle değiştirildi. 
print(yeniHal)
print(diziDizisi)            # Yapılan değişiklik ana diziyi de etkiliyor bu şekilde.

yeniDizi=np.arange(1,20)
yeniDiziKopya=yeniDizi.copy()              # copy metodu ile dizinin bir kopyası oluşturuldu ve kopya dizi üzerinden işlemler yapıldı.
yeniDiziKopyaSlicing=yeniDiziKopya[2:10]   # Bu sayede ana dizide değişiklik olmasının önüne geçildi.
yeniDiziKopyaSlicing[1:7]=200
print(yeniDiziKopyaSlicing)
print(yeniDiziKopya)
print(yeniDizi)



#----------Matrislerde İşlemler----------#

# Matrislerde listelerdekine benzer şekilde indisle elemanlara erişim sağlanabilir.

matris1=np.matrix([[1,2,3],[4,5,6],[7,8,9]])
print(matris1[0])       # 1. satırı çağırdı.
print(matris1[2,1])     # 3. satır, 2. sütun elemanını çağırdı. 
                        # İndis numarası satır/sütun numarasının bir eksiği yine 0'dan başladığı için.
print(matris1[1:,:2])   # 2. satırdan sonrasını ve 3. sütuna kadar olan kısmı yazdırır.
                        # Bu şekilde matrisler içinde de slicing işlemleri yapılabilir.
print(matris1[(1,2),1:3]) # 2 ve 3. satırla, 2 ve 3. sütun arası elemanları listeler. 

randomDizi=np.random.randint(1,100,15)  # Random şekilde bir dizi oluşturduk.
buyuklerDizisi=randomDizi>15            # Dizi içindeki değeri 15'ten büyük elamanları yeni bir değişkene atayarak belirledik.
print(buyuklerDizisi)                   # Yeni dizide büyük olanlar belirtilirken ana dizide bir değişiklik olmadı.

print(randomDizi[buyuklerDizisi])       # İfadesi ile de bool değer yerine doğrudan sayısal değerleri aldık.
print(randomDizi)                       # Ana dizide bir değişiklik söz konusu değil.
                                        # Çünkü kodun manası "randomDizi içindeki 15 sayısından büyük değerleri ayıkla ve yazdır."dır.
print(randomDizi[randomDizi>15])        # İfadesi ile başka değişkene atamaya gerek kalmadan tek satırda kolayca yapılabilir.


print(randomDizi+randomDizi)
print(randomDizi-1)
print(randomDizi*3)
print(randomDizi/4)                     
print(np.sqrt(randomDizi))             # Şeklinde matrislerde matematik işlemleri de yapılabilir.



dolu1=np.full((2,3),1)
dolu2=np.full((2,3),2)
dolu3=np.full((2,3),3)

birlesik=np.concatenate((dolu1,dolu2,dolu3), axis=0)  # concatanate metodu ile diziler birleştirilebilmektedir.
birlesik2=np.concatenate((dolu1,dolu2,dolu3), axis=1) # axis=0 y ekseninde, axis=1 ise x ekseninde birleştirir.
                                                      # satır ve sütun sayıları uyumlu olmak zorundadır, yoksa hata verir.





