# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tensorflow as tf
import numpy as np
import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt

from tensorflow.keras.models import load_model

# Percetron(Yapay nöron): Kendisine verilen girdilere göre işlem yapıp çıktı veren fonksiyonlardır. 
# Nöronların birleşimiyle oluşan sisteme Artificial Neural Network(ANN) denir.
# Aktivasyon Fonksiyonları?
# Sigmoid, Tanh(hiperbolik tanjant), ReLU(rectified linear unit), Linear
# Gradient Descent?


veriFrame=pd.read_excel("bisiklet_fiyatlari.xlsx")
veriFrame.head(10)
sbn.pairplot(veriFrame) # Verilerin birbirine göre durumlarını gösteren grafikler oluşturur.


# Verileri işlemeden önce eğitim ve test seti olarak ayrılmaları gerekmektedir.
# Eğitim seti adı üstünde modeli eğitmek için kullanılacaktır.
# Test seti ise oluşan modelin doğruluğunun test edilmesi için kullanılacaktır.
# Bu ayırma işlemini scikit kütüphanesi ile kolayca yapabilmekteyiz.

from sklearn.model_selection import train_test_split # Train-Test ayırma sınıfının çağırılması.

# y= wx+b oluşturulacak tahmin modelinin fonksiyonudur.
# y ulaşılmak istenen hedeftir. İngilizce bunun için "label" ifadesi kullanılmaktadır.
y=veriFrame["Fiyat"].values # .values metodu sayesinde pandas serisi bir numpy dizisine çevrilebilmektedir.
x=veriFrame[["BisikletOzellik1","BisikletOzellik2"]].values # x ve y değerlerini değişkenlere verdik.
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.33,random_state=25) 
# Yukardaki değişkenler isimlendirildiği sırada değerler almaktadır. Kafa karışıklığını önlemek için direkt isimler verilmiştir
# ama istenirse train ve test değişkenlerine farklı isimler de verilebilir.
# test_size ile test için ayrılacak verinin yüzdesi belirlenmektedir.
# random_state ile verilerin ayrılması için bir random sayı verilir. İstenen her sayı olabilir bu, önemsizdir.

from sklearn.preprocessing import MinMaxScaler
# Verilerin işlenmesini daha kolay hale getirmek için giriş(x) verilerinin değerlerini daha küçük bir oranda ölçekyeleyebiliriz.
# Matematiksel olarak bir hata oluşturmamaktadır.
scaler=MinMaxScaler() # MinMaxScaler sınıfına ait scaler adında bir nesne tanımladık.
scaler.fit(x_train)   # x_train dizisini ölçeklendirdik. Değerleri 0-1 arasına ölçeklendirdi.
x_train=scaler.transform(x_train)
x_test=scaler.transform(x_test)

from tensorflow.keras.models import Sequential  # Modelin oluşturulacağı sınıf.
from tensorflow.keras.layers import Dense       # Modelin katmanlarının oluşturulacağı sınıf.

model=Sequential()
model.add(Dense(5,activation="relu")) 
model.add(Dense(5,activation="relu"))  # 5'er tane nöron barındıran 3 tane gizli katman oluşturduk.
model.add(Dense(5,activation="relu"))  # Akivasyon fonksiyonu cinsi ise ReLU.

model.add(Dense(1)) # Burda ise 1 adet çıktı nöronu oluşturduk. (Bu örnek için yeterli.)
model.compile(optimizer = "rmsprop",loss = "mse") # Çalıştırmadan önce çalıştırılacak fonksiyonları ve parametreleri derledik.
model.fit(x_train,y_train,epochs=250)

loss = model.history.history["loss"]    # Çıktıyı bir diziye atadık.

sbn.lineplot(x=range(len(loss)),y=loss) # Grafiksel olarak gösterdik.

trainLoss = model.evaluate(x_train,y_train, verbose=0)
# Loss değerlerini değerlendirme işlemini yapmaktadır evaluete.
# Bu iki değerin arasındaki fark ne kadar az olursa o kada iyidir.
testLoss = model.evaluate(x_test,y_test,verbose=0) # evaluate kelime manası olarak değerlendirmek demektir.
# verbose=0 dememizin sebebi arkada yaptığı uzun işlemi görsel olarak vermesini istememiz.

testTahminleri = model.predict(x_test) # predict kelime manası olarak tahmin etmek demektir.
# x_test dizisinden vereceğimiz özelliklere göre bir fiyat tahmini üretecektir.

# Bu aşamada gerçek y değerleri ile tahmin edilen değerleri yan yana görmek için bir dataframe oluşturuyoruz.
tahminDf = pd.DataFrame(y_test,columns=["Gerçek Y"])
testTahminleri = pd.Series(testTahminleri.reshape(330,))
tahminDf = pd.concat([tahminDf,testTahminleri],axis=1)
tahminDf.columns = ["Gerçek Y", "Tahmin Y"]

# Elde edilen verileri görselleştiriyoruz.
sbn.scatterplot(x = "Gerçek Y", y = "Tahmin Y", data = tahminDf)


from sklearn.metrics import mean_absolute_error, mean_squared_error
mean_absolute_error(tahminDf["Gerçek Y"],tahminDf["Tahmin Y"]) # Bu iki fonksiyon ile sapma miktarlarını öğrendik.
mean_squared_error(tahminDf["Gerçek Y"],tahminDf["Tahmin Y"])
tahminDf.describe() # İstatiksel verilerini listeledik.

# Bu kısımda modele yeni bir özellik verisi girilecek ve ona göre bir fiyat tahmini alınacaktır.
yeniBisikletOzellikleri = [[1751,1750]]
yeniBisikletOzellikleri = scaler.transform(yeniBisikletOzellikleri)
model.predict(yeniBisikletOzellikleri)

# Bu kısımda model daha sonra kullanılabilmesi için kayıt edilecektir.
from tensorflow.keras.models import load_model
model.save("bisiklet_modeli.h5") # Modeli kaydettik.

# Modelin tekrar kullanılması için çağrılması da bu şekilde yapılır.
sonradanCagirilanModel= load_model("bisiklet_modeli.h5") # .h5 dosya uzantısıdır.
sonradanCagirilanModel.predict(yeniBisikletOzellikleri) # Tahmin edilecek veri olarak yine öncekini kullandık 
# ama istediğini verebilirsin.



#--------------------------------------------- ARABA FİYATLARI TAHMİN MODELİ ---------------------------------------------#

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn

#--------------- Verinin Ön İşleme/Anlama Aşaması ---------------#

dataFrame = pd.read_excel("merc.xlsx")
dataFrame.head()
dataFrame.describe()
dataFrame.isnull().sum() # isnull boş verinin olup olmadığını kontol eder. .sum ise hangi kolonda kaç tane olduğunu verir.

plt.figure(figsize=(7,5))
sbn.distplot(dataFrame["price"])  # Fiyat kolonuna ait dağılım grafiği oluşturuldu.

sbn.countplot(dataFrame["year"])  # Hangi üretim yılına ait kaç adet arabanın olduğunun grafiği oluşturuldu.

dataFrame.corr()                  # Öz niteliklerin birbiri ile olan korelasyonuna bakıldı.
dataFrame.corr()["price"].sort_values()  # Fiyat öz niteliğinin diğer öz niteliklerle olan ilişkisi küçükten büyüğe sıralandı.

sbn.scatterplot(x="mileage",y="price",data=dataFrame) # Mil değerlerine göre fiyatın dağılım grafiği oluşturuldu.


dataFrame.sort_values("price",ascending = False).head(10) # En pahalı ilk 10 araç listelendi.
dataFrame.sort_values("price",ascending = True).head(10)  # En ucuz ilk 10 araç listelendi.
# Ascending parametresi True ise küçükten büyüğe, False ise büyükten küçüğe sıralama yapar. (Ascending=Artan)



#--------------- Verinin Temizlenmesi ---------------#

# Fiyatın dağılım grafiği incelendiğinde (line-123) verilerin geneli toplu bir şekilde olmasına rağmen en yüksek fiyat kısmı
# incelendiğinde çok uç noktalarda çok az sayıda veri bulunmaktadır. Veri setinin genel değerlerini etkilememesi için
# bu çok yüksek fiyatlı istisnai araçlar veri setinden çıkarılacaktır. 
# (Duruma göre çıkarılmasa da olur, burda örnek olması için çıkarıyoruz.) 

len(dataFrame)
len(dataFrame)*0.01 # Verinin %1'lik kısmının kaç veriyi ifade ettiğini(131) buluyoruz.
yuzdeDoksanDokuzDf = dataFrame.sort_values("price",ascending = False).iloc[131:]
# Fiyat kolonunu yüksekten düşüğ doğru sıralayıp, iloc metodu ile 131. satırdan sonraki verileri ayırarak 
# yeni bir değişken oluşturduk. Bu sayede %1'lik çok pahalı arabaların olduğu kısmı filtrelemiş olduk.
# Ana dataframe değişmedi, yeni bir değişkene aktardık filtrelenmiş verileri.

# Burda da görüleceği üzere veride aşırı bir sapma oluşturmadan gereksiz kısımları çıkarmış olduk.
yuzdeDoksanDokuzDf.describe()
plt.figure(figsize=(7,5))
sbn.distplot(yuzdeDoksanDokuzDf["price"])

# Her bir yıla ait araçların ortalama fiyatlarını listeledik.
dataFrame.groupby("year").mean()["price"]
yuzdeDoksanDokuzDf.groupby("year").mean()["price"]
# Burda son olarak 1970 yılında üretilen bir arabanın fiyatının anormal şekilde yüksek olduğunu görmekteyiz.
# Bunun sebebi muhtemelen klasik bir araç olması. Yani yine istisnai bir durum oluşturmakta. O yüzden onu da çıkaracağız.


dataFrame = yuzdeDoksanDokuzDf   # Ana dataframe'i %99'luk filtrelenmiş veri haline getirdik.
dataFrame = dataFrame[dataFrame.year != 1970]  # 1970 model aracı da çıkardık.
dataFrame.groupby("year").mean()["price"]  # Dataframe'i model yıllarına ait ortalama fiyatlarını listeledik.

dataFrame = dataFrame.drop("transmission",axis=1) # Vites çeşidi sözel bir ifade olduğu için çıkarılmaktadır.



#--------------- Modeli Oluşturmak ---------------#

y = dataFrame["price"].values # y oluşturuldu.
x = dataFrame.drop("price",axis=1).values # Fiyat harici her şeyi x olarak alacağımız için direkt fiyatı atıp kalanlara x dedik.

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=31)
# Veriyi test ve eğitim olarak ayırdık.

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)  # x_train'i ölçeklendirip transform ettik. (önceki örnekte iki satırda, burda tek satır.)
x_test = scaler.transform(x_test)        # x_test'i transform ettik.

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
# Bu kısımda modeli oluşturup ara katmanları, nöronları ve kullanılacak aktivasyon fonksiyonunu ayarladık.
model = Sequential()
model.add(Dense(12,activation="relu"))
model.add(Dense(12,activation="relu"))
model.add(Dense(12,activation="relu"))
model.add(Dense(12,activation="relu"))
model.add(Dense(1))
model.compile(optimizer="adam",loss="mse")

# validation_data ile modelde direkt olarak test ve onay işlemlerini yaptırabiliyoruz tek seferde otomatik olarak.
# batch_size ile verileri belirli miktarlara bölerek modelimize veriyoruz ki sorun çıkmasın çok fazla veriden ötürü.
model.fit(x=x_train, y = y_train,validation_data=(x_test,y_test),batch_size=350,epochs=350)

kayipVerisi = pd.DataFrame(model.history.history) # Burda çıktılarımızı görebilmekteyiz.
kayipVerisi.head()
kayipVerisi.plot()


from sklearn.metrics import mean_squared_error, mean_absolute_error
tahminDizisi = model.predict(x_test)
mean_absolute_error(y_test,tahminDizisi)
dataFrame.describe()
plt.scatter(y_test,tahminDizisi)
plt.plot(y_test,y_test,"g-*")

yeniArabaBilgi=[2013,15000,100,25,1.6]
yeniArabaSeries=pd.Series(yeniArabaBilgi) # Tahmin yapılacak bir araba verisi hazırladık.
yeniArabaSeries = scaler.transform(yeniArabaSeries.values.reshape(-1,5)) # Veriyi transform ettik.

model.predict(yeniArabaSeries) # Fiyat tahmini gerçekleştirildi.



#--------------------------------------------- SINIFLANDIRMA ANALİZİ ---------------------------------------------#

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn

# Veri seti alındı.
dataFrame2=pd.read_excel("maliciousornot.xlsx")

# Veri seti hakkında genel bilgi alındı.
dataFrame2.info()
dataFrame2.describe()

# Type özelliğine göre karşılaştırma grafikleri çizildi.
dataFrame2.corr()["Type"].sort_values()
sbn.countplot(x="Type", data = dataFrame2)
dataFrame2.corr()["Type"].sort_values().plot(kind="bar") # Burda .plt kısmı eklenerek korelasyonun grafiği de çizdirildi.

# x ve yoluşturuldu.
y = dataFrame2["Type"].values
x = dataFrame2.drop("Type",axis = 1).values

y = dataFrame2["Type"].values
x = dataFrame2.drop("Type",axis = 1).values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=105)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.callbacks import EarlyStopping

model = Sequential()
model.add(Dense(units=30,activation = "relu")) # İlk katmandaki nöron sayısını kolon sayısına göre belirlemek avantajlı olabilir.
model.add(Dense(units=15,activation = "relu"))
model.add(Dense(units=15,activation = "relu"))
model.add(Dense(units=1,activation = "sigmoid"))  # Çıkış katmanına da bir aktivasyon fonksiyonu verdik sınıflandırma olduğu için.
model.compile(loss="binary_crossentropy",optimizer = "adam") # loss fonksiyonunu sınıflandırmaya daha uygun olanı seçtik.

model.fit(x=x_train, y=y_train, epochs=700,validation_data=(x_test,y_test),verbose=1) # Epochs değeri bilerek yüksek verildi.

modelKaybi = pd.DataFrame(model.history.history)
modelKaybi.plot()


# Modeli tekrar oluşturduk.
model = Sequential()
model.add(Dense(units=30,activation = "relu"))
model.add(Dense(units=15,activation = "relu"))
model.add(Dense(units=15,activation = "relu"))
model.add(Dense(units=1,activation = "sigmoid"))
model.compile(loss="binary_crossentropy",optimizer = "adam")

# Overfitting durumu yaşanmaya başlandığı anda program durdurularak hatanın önüne geçilebilmektedir.
# Bunun için EarlyStopping sınıfı kullanılır. monitor parametresinde izlenecek olan veri belirlenmektedir.
#  patience parametresinde tahammül edilecek iyileşme olmaması durumu belirlenir. O aşıldığında iyileşme olmazsa işlemler durur.
earlyStopping = EarlyStopping(monitor="val_loss",mode="min",verbose=1,patience=20)

# callbacks parametresi bir dizidir. 
model.fit(x=x_train, y=y_train, epochs = 700, validation_data = (x_test,y_test), verbose = 1, callbacks=[earlyStopping])

modelKaybi = pd.DataFrame(model.history.history)
modelKaybi.plot()
# Çok daha iyi bir sonuç verdiği görülmekte açıkça.



# Dropout sınıfı ile bazı layer'lar verilen orana göre açılıp kapatılarak daha düzgün bir sonuç elde edilmesi amaçlanır.
model = Sequential()
model.add(Dense(units=30,activation = "relu"))
model.add(Dropout(0.45))
model.add(Dense(units=15,activation = "relu"))
model.add(Dropout(0.45))
model.add(Dense(units=15,activation = "relu"))
model.add(Dropout(0.45))
model.add(Dense(units=1,activation = "sigmoid"))
model.compile(loss="binary_crossentropy",optimizer = "adam")

model.fit(x=x_train, y=y_train, epochs = 700, validation_data = (x_test,y_test), verbose = 1, callbacks=[earlyStopping])

kayipDf = pd.DataFrame(model.history.history)
kayipDf.plot()

tahminlerimiz =(model.predict(x_test) > 0.5).astype("int32")

from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test,tahminlerimiz))
print(confusion_matrix(y_test,tahminlerimiz))

