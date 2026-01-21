# FONKSIYONDAN FONKSIYON DONDURME

def usAlma(taban):
    def inner(us):
        return taban**us
    
    return inner

# sonuc = usAlma(2)(3) 8

# fn = usAlma(2)
# sonuc = fn(4) 16
 

def yetki_sorgulama(sayfa):
    def inner(role):
        if role == "Admin":
            return f"{role} rolü {sayfa} sayfasına ulaşabilir."
        else:
            return f"{role} rolü {sayfa} sayfasına ulaşamaz."
    return inner

yetki = yetki_sorgulama("Ürün güncelleme")
sonuc = yetki("User") # ulaşamaz
sonuc = yetki("Admin")
# print(sonuc)

def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam +=i
        return toplam

    def carpim(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim    

    if islem_adi == "toplama":
        return toplam
    else:
        return carpim
    

toplama = islem("toplama")
carpma = islem("carpma")

# sonuc = toplama(10,20) # 30
# sonuc = carpma(10,20) #200
# print(sonuc)