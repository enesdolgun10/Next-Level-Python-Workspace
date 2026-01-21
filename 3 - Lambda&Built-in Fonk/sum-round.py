sayilar = [1,2,3,5,6,32,56]

sonuc = sum(sayilar) # 105
sonuc = sum(sayilar,15) # 120

products = [
    {"title":"iphone 15","price":60000},
    {"title":"iphone 16","price":70000},
    {"title":"iphone 17","price":80000},
    {"title":"iphone 17 pro","price":0},
]

toplamFiyat = sum([urun["price"] for urun in products])
urunAdedi = len([urun for urun in products if urun["price"]>0])

sonuc = toplamFiyat / urunAdedi # urun fiyatları ortalaması 70000

sonuc = round(5.3) # 5
sonuc= round(5.5) # 6
sonuc= round(5.3456, 2) # 5.35


print(sonuc)