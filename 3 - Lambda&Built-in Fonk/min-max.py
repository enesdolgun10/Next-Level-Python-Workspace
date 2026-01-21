sayilar = [1,4,6,32,23,12]
harfler = ['a','c','v','z']
isimler = ['ahmet','ali','sena','yiğit']

sonuc= min(sayilar) #1
sonuc= max(sayilar) #32
sonuc=min(harfler) #a
sonuc=max(harfler) #z

sonuc= max(isimler) # yiğit
sonuc= min(isimler) # ali

sonuc = min([len(isim) for isim in isimler]) # 3
sonuc = max([len(isim) for isim in isimler]) # 5

sonuc= max(isimler,key=lambda isim:len(isim)) # ahmet
sonuc= min(isimler,key=lambda isim:len(isim)) # ali

urunler = [
    {"title":"samsung s23","price":50000},
    {"title":"samsung s24","price":70000},
    {"title":"samsung s25","price":90000},
]

sonuc = min(urunler,key=lambda urun:urun["price"]) #{'title': 'samsung s23', 'price': 50000}

sonuc = max(urunler,key=lambda urun:urun["price"])["title"] # samsung s25

max = 0
for urun in urunler:
    if(urun["price"]>max):
        max = urun["price"]

print(max)

print(sonuc)