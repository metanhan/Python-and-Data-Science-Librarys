# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 15:57:41 2021

@author: Mehmethan
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#---------------Plt ile Çizim---------------#

yilVeri=np.arange(2000,2022)
satisVeri=np.random.randint(1,100,22)

# xlabel, ylabel metodları ile eksenlerde yazılacak değerler belirlenir.
# title metodu ile grafiğin adı belirlenir.
# plot içindeki "ms-" ifadesi grafiğin çiziliş şeklini belirler. Mesela burda m(magenta) renginde, s(square) keşisim noktaları kare ile
# - ise değerler arası boşluğun çizgi ile birleştirileceğini ifade eder. 
# Bu çizdirme parametrelerinin pek çok çeşidi bulunmaktadır. ( https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html )

plt.plot(yilVeri,satisVeri,"ms-")   # İlk değer x ekseni, ikinci değer y eksenine verilir.
plt.xlabel("Yıl")
plt.ylabel("Satış Miktarı")
plt.title("Yıllara Göre Satış Değerleri")
plt.show()


#---------------Subplot---------------#

# Tek seferde birden çok grafik çizdirmek istediğimiz durumlarda subplot(alt çizim) metodunu kullanmaktayız.
yilVeri2=yilVeri
satisVeri2=np.random.randint(1,100,22)  # İki grafik farklı olsun diye ilkini biraz değiştirip kullanıyorum.

plt.subplot(1,2,1)  # Bu ifadedeki parametreler sırasıyla: ilki kaç sıra olacağını belirler(satırda veya sütunda gösterilmesi belirlenir.)
                    # İkincisi kaç tane grafik çizileceğini belirtir. Üçüncüsü ise kaç numaralının çizildiğini belirtir.
plt.plot(yilVeri, satisVeri,"ms-")

plt.subplot(1,2,2)
plt.plot(yilVeri2,satisVeri2,"r*-")
plt.show()


#---------------Figure Nesnesi ile Kendi Çizimimizi Oluşturmak---------------#

# Figure'ün plt'den farkı boş bir kanvas oluşturmasıdır. plt'de bir grafiğe değerleri atamaktayız. 
# Fifure'de ise boş bir kanvas üstüne istediğimiz grafiği inşaa etmekteyiz. Özelleştirilmesi çok daha iyidir.
# 0 axes yani ekseni bulunmayan boş bir kanvas oluşur.
ilkFigure=plt.figure()  # Bir figure nesnesi oluşturduk.
figurAxes=ilkFigure.add_axes([0.1,0.1,0.9,0.9]) # Buradaki sayıların son ikisi sırasıyla genişlik ve yüksekliktir. ([] ile değer ver.)
# İlk ikisi ise iç içe grafik oluşturulduğunda içteki grafiğin sol alt köşesinin konumunu belirleyecek değerlerdir.
figurAxes.plot(yilVeri,satisVeri,"g")
figurAxes.set_xlabel("Yıl")
figurAxes.set_ylabel("Satış Miktarı")
figurAxes.set_title("Satış Tablosu")


# İç içe birden çok grafik oluşturulacağı zaman birden fazla eksen tanımlanmalıdır.

ikiFigure=plt.figure()
eksen1=ikiFigure.add_axes([0.1,0.1,0.8,0.8])
eksen2=ikiFigure.add_axes([0.25,0.6,0.2,0.2])
# Burada 1 figürde 2 adet ayrı eksenin grafiği çizilmiştir. 
eksen1.plot(yilVeri,satisVeri,"g")
eksen1.set_xlabel("Ana Yıl Değerleri")
eksen1.set_ylabel("Ana Satış Miktarı")
eksen1.set_title("Ana Grafik Satış Tablosu")

eksen2.plot(yilVeri2,satisVeri2,"g")
eksen2.set_xlabel("Yıl Değerleri")
eksen2.set_ylabel("Satış Miktarı")
eksen2.set_title("Grafik Satış Tablosu")


#---------------Subplots---------------#

# subplots ile subplot birbirinden farklıdır. subplots ile figure'deki gibi çok eksenli grafikler oluşturulabilmektedir.
# subplots bir boş figür bir de eksen oluşturur tek seferde. yani figür ve eksenden oluşan bir tuple'dır. subplots(figür,eksen)

(subFigur,subEksen)=plt.subplots()
type(subEksen) # eksen
type(subFigur) # figür

subEksen.plot(yilVeri,satisVeri,"g")
subEksen.set_xlabel("Yıl Değerleri")
subEksen.set_ylabel("Satış Miktarı")
subEksen.set_title("Grafik Satış Tablosu")    



(subFigur2,subEksen2)=plt.subplots(nrows=1, ncols=2) # 2 kolon olduğu için eksenler artık bir dizi oluyor ve yukardaki gibi yapılamıyor.
type(subEksen2)
for eksen in subEksen2:
    eksen.plot(yilVeri,satisVeri,"g")
    eksen.set_xlabel("Yıl Değerleri")
    eksen.set_ylabel("Satış Miktarı")
    eksen.set_title("Grafik Satış Tablosu")    
plt.tight_layout() # İki grafik arasındaki boşluğu uygun şekilde ayarlar.


# Grafikler içine verileri açıklayan lejantlar ekleyebilmekteyiz.

veriFig=plt.figure() # figure fonksiyonunun değişik parametreleri bulunmaktadır. Bunlara internetten bakabilirsin.
veriEksen=veriFig.add_axes([0.1,0.1,0.9,0.9])
veriEksen.plot(yilVeri,satisVeri*4,label="satiş verisi**2")
veriEksen.plot(yilVeri,satisVeri*3,label="satış verisi**3")
veriEksen.legend(loc=2) # loc parametresi lejantın konumunu belirler. Farklı değerler deneyebilirsin.


veriFig.savefig("satış grafik.png",dpi=500) # dpi parametresi çözünürlüğü belirler.


# Bu kısımda grafik görsellikleri hakkında bazı parametrelere değinilecektir.

veriSeti=np.random.randint(0,100,20)
veriSeti2=veriSeti*2
(figur1,eksen1)=plt.subplots()
eksen1.plot(veriSeti,veriSeti2,veriSeti2,color="#3A95A8",alpha=0.5)
eksen1.plot(veriSeti2,veriSeti,color="#C96F23")



(yeniFigur, yeniEksen) = plt.subplots()
yeniEksen.plot(veriSeti,veriSeti + 10, color="blue", linewidth = 1.0)
yeniEksen.plot(veriSeti,veriSeti + 15, color ="yellow", linewidth = 1.0)

yeniEksen.plot(veriSeti,veriSeti + 20, color = "#C96F23", linestyle = "-.")
yeniEksen.plot(veriSeti,veriSeti + 25, color = "#C96F23", linestyle = ":")
yeniEksen.plot(veriSeti,veriSeti + 30, color = "#C96F23", linestyle = "--")

yeniEksen.plot(veriSeti,veriSeti + 35, color = "#000000", linestyle = "--", marker = "o",markersize = 8, markerfacecolor="red")
yeniEksen.plot(veriSeti,veriSeti + 40, color = "#000000", linestyle = "--", marker = "+",markersize = 4)

# scatter fonksiyonu ile veriler grafikte ayrı ve belirgin şekilde işaretlenir.
plt.scatter(veriSeti,veriSeti2)



plt.axis([2013,2025,55,130]) # Grafikte eksenlerde yerleşecek değer aralıkları bu metodla verilebilmektedir.(ilk ikisi x, diğerleri y) 
plt.title("Yıllara Göre Kilo Değişimi")
plt.xlabel("Yıllar",fontsize=16,fontname="Times New Roman",color="red")
plt.ylabel("Kilo",fontsize=16,fontname="Times New Roman",color="red")
plt.text(2016,75,"En Düşük",color="blue",style="italic",weight="bold",size=7)  # Yazıma özel bazı parametreler.
plt.text(2020,110,"En Yüksek",color="blue",style="italic",weight="bold",size=7) # Grafikte belli noktalara metinler yazılabilir.
plt.grid()
plt.plot([2016,2017,2018,2019,2020,2021],[75,78,85,80,110,95],"m*-")
esik=85
plt.axhline(esik,color="green",linestyle="--")  # axhline metodu bir eşik değer çizdirmek için kullanılır.
plt.show()



#---------------Fonksiyonların Grafiğinin Çizilmesi---------------#

x=np.linspace(1,3,1000000)
y = (np.sin(x**x))/(2**((x**x-np.pi/2)/np.pi))
# LaTeX versiyonu yazımı tamamen doğru fakat çalışmıyor. Sebebi belirsiz.
plt.text(1.25,0.4,'$y=\left|\frac{sinx^{x}}{2^{\frac{\frac{x^{x-\Pi}}{2}}{\Pi}}}\right|$',fontsize=12,bbox={'facecolor':'yellow','alpha':0.5})
plt.grid()
plt.plot(x,y)

# LaTeX formatı çalışan plot örneği.
a=np.arange(-2*np.pi,+2*np.pi,0.01)
b=3*np.tan(5*np.pi-a)
plt.text(1,-1500,'$b= 3tan(5\Pi -a)$',fontsize=12,bbox={'facecolor':'yellow','alpha':0.5})
plt.xticks([-2*np.pi,-1*np.pi,0,1*np.pi,2*np.pi],[r'$-2\pi$',r'$\pi$',0,r'$\pi$',r'$2\pi$']) # İlk dizi değerleri, ikincisi etiketleri içerir.
# Eksenlerde sayı harici matematiksel bir ifade yazdırılacağında LaTeX biçimini plt.xticks ve plt.yticks metodları ile kullanabilirsin.
plt.grid()
# Bir bölgeyi işaret ederek göstermek için plt.annotate metodu kullanılır. Parametreleri hakkında fikrim yok, işine yararsa araştır sonra.
plt.annotate('Önemli Nokta',xy=[-1,-1500],xycoords='data',xytext=[40,40],bbox=dict(boxstyle='round',color='k',fc='w',alpha=0.7),
             fontsize=10,textcoords='offset points',arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))
plt.plot(a,b,"b")



#---------------Histogram Grafiği---------------#

# Veri setlerinin istatiksel dağılımı hakkında bilgi veren bir sütun grafiği türüdür.
# Her bir veriyi değil, veri gruplarını temsil eden sütunlardan (bins) oluşur.

x=np.random.randint(0,100,800)
plt.title("Ders Sınav Sonuçları")
plt.xlabel("Notlar")
plt.ylabel("Öğrenci Sayısı")
plt.axis([0,100,0,20])
plt.grid()
n,bins,patches=plt.hist(x,bins=100,facecolor="green",alpha=0.5) # bins değeri değiştirilerek hassasiyet değiştirilebilir.




