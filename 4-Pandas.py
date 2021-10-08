# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 15:56:09 2021

@author: Mehmethan
"""

#--------------------PANDAS KÜTÜPHANESİ--------------------#

import numpy as np
import pandas as pd

# Pandas kütüphanesi verileri excel'deki gibi tablolar haline getirmemizi sağlıyor.

#--------------------Series--------------------#

sozluk={"mehmet":22,"ahmet":18,"can":33}
pd.Series(sozluk)                          # Sözlüklerde default halde key'ler index, value'lar ise data olarak seri haline gelmektedir.
pd.Series(data=sozluk.keys(),index=(sozluk.values())) # Ancak Serilerin bir özelliiği olan data ve index ile istediğimizi 
                                                      # belirleyebiliriz.
                                                      # Data ve indexler int veya str gibi tip fark etmez.
meyve=np.array(["elma","armut","muz"])
kalori=np.array([100,150,200])        # Farkli dizileri de bu şekilde seri haline getirebiliriz.
pd.Series(data=kalori,index=meyve)  

pd.Series(meyve,kalori)             
pd.Series(index=meyve,data=kalori) # Burdaki gibi index ve datayı belirtmezsek öntanımlı olarak "önce data sonra index" olarak    
                                   # kabul edilmektedir.
                                   
sayidizi=np.arange(0,5)
pd.Series(sayidizi)              # Index değeri olarak her hangi bir şey verilmezse (0,1,..) şekline sayılar otomatik atanır.

sericik=pd.Series([1,2,3],["a","b","c"]) # Şeklindebir yerden değer almadan da direkt tanımlama yapılabilir.


puanDurumu1=pd.Series([23,12,45,31],["fb","gs","bjk","ibb"])
puanDurumu2=pd.Series([43,12,25,11],["fb","gs","bjk","ibb"])
print(puanDurumu1+puanDurumu2)   # Bu şekilde seriler arası aritmetik işlemler yapılabilmektedir. İşlemler tamamen index değerleri 
                                 # ile yapılmaktadır.
                                 
puanDurumu3=pd.Series([23,12,45,31],["fb","manu","bjk","bar"])
puanDurumu4=pd.Series([43,12,25,11],["fb","city","bjk","real"])
print(puanDurumu3+puanDurumu4)   # index ilişkisi bulamadığı değerlerde işlem yapmayıp NaN değeri verdi, indexleri uyanlarda işlemleri
                                 # gerçekleştirdi.

#--------------------Data Frames--------------------#

# Data frame'ler aslında sütünlarla birleştirilmiş serilerdir denebilir.

veri=np.random.randn(4,3)    # 4x3'lük random bir matris.

ilkDataF=pd.DataFrame(veri)  # DataFrame'in oluşturulması.
ilkDataF[0]       # DataFrame'in 0 indexli kolonunu verir.
type(ilkDataF[0]) # Görüldüğü üzere bu kolon bir seridir.


# Kolon ve indexlere farklı str ve int isimleri de verilebilir.

dataFrame2=pd.DataFrame(veri,index=["bir","iki","üç","dört"],columns=["sen","ben","şu"])


isim=["metan","kafkas","ares","badem"]
veriSozluk={"kilo":[95,50,5,3],"yas":[23,1,1,1],"cins":[1,2,3,3]}
bizFrame=pd.DataFrame(columns=isim,index=veriSozluk.keys(),data=veriSozluk.values())

# Veriler bu şekilde bir yerden alınabilir.
# Kolonlar aslında farklı serileri ifade etmektedir. DataFrame'lerin seri olduğunu da bu şekilde anlayabiliriz.
# Örneğin kilo serisinin indexler mehmet,kafkas,badem,ares'tir ve değerleri mevcuttur.

bizFrame["kafkas"]  # Bu şekilde kolonlara(mesela burda kafkas kolonu(serisi)) erişim sağlanabilir.
bizFrame[["kafkas","ares"]] # Çoklu erişimde [[]] yapısı.. 


bizFrame.loc["yas"] # xx.loc (locate) metodu ile indexler üzerinden veri çağırılması yapılabiliyor.
bizFrame["yas"] # şeklinde çağırmaya kalkarsak hata verir. Çünkü bu çağırma yapısında sadece kolonları çağırmaktadır.

bizFrame.iloc[1] # Bu ifade de indexle veri çağırır. loc'tan farkı indexe verilen label ismi yerine index numarası kullanılmaktadır.
beg=[65,17,0]
bizFrame["beg"]=beg                                    # Gibi ifadelerle yeni kolonlar eklenebilmektedir. 
bizFrame["metan"]["kilo"]= bizFrame["metan"]["kilo"] + 5   # Burda aynı zamanda aritmetik işlemlerin yapılabildiğini de görmekteyiz.
print(bizFrame)


# xx.drop() metodu ile istenen kısımlar dataframe'den atılabilir. Bir kolon atmak için "axis=1" kullanılmalıdır.
# index sırası atmak için "axis=0" kullanılabilir ama defauld değerde zaten axis=0'dır.
bizFrame.drop("metan",axis=1) # metan kolonu çıkarıldı.
bizFrame.drop("cins",axis=0)  # cins indexli sıra çıkarıldı.

# Burda önemli nokta yapılan çıkarma işleri DataFrame'in ana halini etkilememektedir. 
# Çıkarma yapılmış hali bir değişkene atanarak yeni bir dataframe alınabilir.
metaneksikFrame=bizFrame.drop("metan",axis=1)
 
# Ana dataframe'de bir değişiklik yapılmak isteniyorsa da "inplace=True" özelliği eklenmelidir. Defauld olarak false'dur. 
bizFrame.drop("metan",axis=1,inplace=True)

bizFrame.loc["kilo"]["kafkas"]  # Bu şekilde spesifik değerlere de ulaşılabilir. (matrislerde bir değere erişmekle benzer mantık)


kucukDeger= bizFrame < 5
bizFrame[kucukDeger]      # Büyük/küçük değerler bu şekilde özel olarak alınabilir.

bizFrame[bizFrame<5]      # Ama değişkene atanmayı gerektiren özel bir durum yoksa bu yöntem daha kısa.


bizFrame[bizFrame["kafkas"] > 2] # İfadesi NaN değer çeviren kısımlar filtre yapılabilir. Kolon ve satırlar silinebilmektedir.
                                 # Yapılan bu değişiklik ana dataframe'de bir değişikliğe sebep olmamaktadır.

# Index'lerde resetleme ve değiştirme işlemleri xx.reset_index() metodu ile yapılabilmektedir.

bizFrame.reset_index() # index için yapılan isimlendirmeler kaydırıldı ve sayısal değerler yerini aldı. Ana frame'e bir etkisi yoktur.

yeniIndexList=["k","y","c"]
bizFrame["yeni index"]=yeniIndexList  # Önce bir kolon olarak ekleyip sonra set_index ile index haline getirilmeli.
bizFrame.set_index("yeni index",inplace=True)      # Bu şekilde yapılan değişiklik "inplace=True" ana frame'e etki edecektir.
bizFrame.loc["k"]                                  # inplace=True demeseydik yine etki etmeyecekti.


# Multi index'ler bazı durumlarda gerekli olabilmektedir.

ilkIndex=["TES","TES","TES","Fallout","Fallout","Fallout"]
icIndex=["Morrowind","Oblivion","Skyrim","Fallout 3","New Vegas","Fallout 4"] 
birlesikIndex=list(zip(ilkIndex,icIndex))
birlesikIndex=pd.MultiIndex.from_tuples(birlesikIndex)

oyunListesi=[[2002,"RPG"],[2006,"RPG"],[2011,"RPG"],[2008,"RPG"],[2010,"RPG"],[2015,"RPG"]]
oyunDizisi=np.array(oyunListesi)

bethesdaFrame=pd.DataFrame(oyunDizisi,index=birlesikIndex,columns=["Yıl","Tur"])
bethesdaFrame.index.names=["Franchise","Oyun Adı"]
print(bethesdaFrame)
print(bethesdaFrame.loc["TES"])
print(bethesdaFrame.loc["Fallout"].loc["New Vegas"])


# DataFrame'de eksik verilerin olduğu yerlerde işlemlere daha rahat devam edebilmek adına eksik verilere birtakım işlemler 
# uygulanabilmektedir.
# Eksik verileri örneklerimizde tanımlamak için "np.nan" metodunu kullanacağız.
ornekSozluk={"elma":[1,2,np.nan],"armut":[4,np.nan,6],"kavun":[7,np.nan,np.nan]}
oyleFrame=pd.DataFrame(ornekSozluk)
oyleFrame.dropna()       # Boş değerlerin atılmasını sağlar. Öntanımlı olarak axis=0(satır) değerine sahiptir. (axis=1 kolonlardır)
oyleFrame.dropna(axis=1) # Yapılan değişiklikler ana frame'e etki etmez. Yeni değişkene atanırsa değişmiş frame alınabilir.

oyleFrame.dropna(axis=1,thresh=2) # Thresh metodu ile sadece istenen sayı ve fazlasında NaN değerlerinin atılmasını sağlar.

oyleFrame.fillna(333)  # NaN değerlerin yerine istenen değerlerin doldurulmasını sağlar.


# Gruplama tekniği çok sayıda veri ile uğraşmamız gerektiğinde verilerin incelenmesini çok daha kolaylaştırmaktadır.
# Pandas kütüphanesinde bulunan groupby fonksiyonu ve ona ait alt metodlarla gruplama işlemleri yapılabilmektedir.

yemekSozlugu = { 
                "yemek siparis":["çorba","kebap","çorba","döner","döner","salata","salata"],
                "masa num.":["masa1","masa1","masa3","masa3","masa2","masa5","masa5"],
                "fiyat":[10,20,10,15,15,10,10]
              }

restoranDataFrame = pd.DataFrame(yemekSozlugu)
grupObjesi = restoranDataFrame.groupby("masa num.")  # masa numarasına göre gruplandırıldı.

print(grupObjesi.count())
print(grupObjesi.mean())
print(grupObjesi.min())
print(grupObjesi.max())
print(grupObjesi.describe()) # Her türlü istasistiksel bilgiyi vermektedir.


# Birden fazla dataframe'e sahip olup bunları birleştirmemiz gerekirse .concat(dataframeadı,...) metodunu kullanmamız gerekmektedir.
# axis=0 öntanımlı olup alt alta birleştirme yapmaktadır.(axis=1'de ise yan yana)
# Index numaralarını tanımlamazsak her birinin kendi içinde sahip olduğu index numarasını veriyor ve saçma bir şey oluyor.
veri1=np.random.randn(1,9).reshape(3,3)
birData=pd.DataFrame(veri1,index=[1,2,3],columns=["bir","iki","üc"])

veri2=np.random.randn(1,9).reshape(3,3)
ikiData=pd.DataFrame(veri2,index=[4,5,6],columns=["bir","iki","üc"])

veri3=np.random.randn(1,9).reshape(3,3)
ucData=pd.DataFrame(veri3,index=[7,8,9],columns=["bir","iki","üc"])

birlesik= pd.concat([birData,ikiData,ucData],axis=0)


# Merge metodu da bir birleştirme işlemidir fakar concat'dan farkı ortak kolonlar üzerinden birden fazla dataframe'i eşleyerek
# birleştirme işlemini yapmasıdır.
# Hangi ortak kolon üzerinden birleştirileceğini ise "on=xxx" parametresi ile sağlamaktayız.

sozlukk1={"isim":["ahmet","mehmet","mustafa","han"],"spor":["futbol","basketbol","koşu","yüzme"]}
spordata=pd.DataFrame(sozlukk1)

sozlukk2={"isim":["ahmet","mehmet","mustafa","han"],"kalori":[100,200,400,400]}
kaloridata=pd.DataFrame(sozlukk2)

mergedaData=pd.merge(spordata,kaloridata,on=("isim"))


# Bu kısımda ise dataframe'lerde kullanılabilecek bazı faydalı metodlar mevcuttur.

yemekSozlugu = { 
                "yemek siparis":["çorba","kebap","çorba","döner","döner","salata","salata"],
                "masa num.":["masa1","masa1","masa3","masa3","masa2","masa5","masa5"],
                "fiyat":[10,20,10,15,15,10,10]
               }

restoranDataFrame = pd.DataFrame(yemekSozlugu)
restoranDataFrame["yemek siparis"].unique()        # Seçilen kolondaki çoklu değerleri tekil olarak ele alır.
restoranDataFrame["yemek siparis"].nunique()       # Seçilen kolondaki çoklu değerlerin tekil sayısını verir.
restoranDataFrame["yemek siparis"].value_counts()  # Değerlerden kaçar tane olduğunu verir.

def vergiFiyat(fiyat):
    return fiyat*0.18
restoranDataFrame["fiyat"].apply(vergiFiyat)  # apply() metodu map metoduna benzer şekilde seçili bir fonksiyonun istenen kolonla 
                                              # çalıştırılmasını sağlar.

restoranDataFrame.isnull()  # NaN değerlerin olup olmadığını sorgular.



# pivot_table metodu multi index'le aynı görüntüde bir tablo oluşturmaktadır.
# Farkı ise tabloda işlemlerin yapılabilmesidir.

yemekSozlugu = { 
                "yemek siparis":["çorba","kebap","çorba","döner","döner","salata","salata"],
                "masa num.":["masa1","masa1","masa3","masa3","masa3","masa5","masa5"],
                "fiyat":[10,20,10,15,15,10,10]
               }

restoranDataFrame = pd.DataFrame(yemekSozlugu)
print(restoranDataFrame.pivot_table(values = "fiyat", index = ["yemek siparis", "masa num."],aggfunc=np.sum))
# aggfunc= ifadesi yapılmak istenen bir aritmetik işlemi belirtebildiğimiz bir metoddur.
# Burda np.sum yani toplama işlemini kullandık.
# Görüldüğü üzere masa3 ve döner siparişi aynı olduğu için ikisinin fiyatını topladı ve tek seferde yazdı.

# Veri bilimi işlerinde verileri Exel dosyalarından otomatik olarak çekmemiz gerekecektir.
# Bunun için pandas metodları kullanılacaktır.

okuVeri=pd.read_excel("exeladi.xlsx")  # .read_exel metodu ile exel dosyaları okunmaktadır.
okuVeri2=pd.read_csv("dosyaadi.csv")   # .read_csv metodu ile csv dosyaları okunmaktadır.


yazVeri=pd.to_excel("exeladi.xlsx")  # .to_exel metodu ile exel dosyalarına yazıp kaydetme yapılmaktadır.
yazVeri2=pd.to_csv("dosyaadi.csv")   # .to_csv metodu ile csv dosyalarına yazıp kaydetme yapılmaktadır.


# Okunan dosyalarda eksik veri olma ihtimaline karşı .dropna() metodu ile NaN veriler çıkarılıp tam verili belge bir değişkene verilir.
# Tam verili dosya to_exel/csv metodu ile kaydedilip işlemlere geçilebilir. Ana dosyada bir değişiklik olmaz.


bisikletVeri=pd.read_excel("bisiklet_fiyatlari.xlsx")
bisikletSlacing=bisikletVeri[2:10]  # dataframe'lerde de slicing yapılabilmektedir.

bisikletVeri.info()              # dataframe hakkındaki bilgileri verir.
bisikletVeri.sample(5)           # dataframeden istenen sayıda rastgele örnek veri seçip getirir.
bisikletVeri.sample(frac=0.005)  # frac parametresi ile istenen oranda (mesela burda binde beş) rastgele veri seçip getirir.

bisikletVeri[["Fiyat","BisikletOzellik2"]].head(7)  # istenen sütunlardan istenen sayıdaki ilk değerleri getirir.(burda ilk 7 değer.)
bisikletVeri["BisikletOzellik1"].tail(5)            # istenen sütunlardan istenen sayıdaki son değerleri getirir.(burda son 5 değer.)

bisikletVeri[bisikletVeri.Fiyat>1100].head(10)      # fiyat değeri 1100'den yüksek ilk 10 değeri listeler.
bisikletVeri[(bisikletVeri.Fiyat>1100)&(bisikletVeri.Fiyat<1150)].head(5) # 1100-1150 fiyat aralığındaki ilk 5 değeri listeler.

bisikletAnaliz=bisikletVeri.corr()  # corr metodu veri işlemede çok önemli olan korelasyon analizini gerçekleştirmektedir.

import seaborn as sns  # seaborn bir grafik kütüphanesidir.
# heatmap fonksiyonu korelasyon matrisini oluşturmaktadır.
# annot metodunun True olması ile sayısal değerler grafikte yazdırılmaktadır. False olsa görünmezdi.
# cmap color map'in kısaltmasıdır ve kullanılacak renklendirme çeşidini belirtir.
# linewidths ise grafikte veriler arasındaki çizgilerin kalınlığını ayarlamaktadır.
sns.heatmap(bisikletVeri.corr(), annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.01)





