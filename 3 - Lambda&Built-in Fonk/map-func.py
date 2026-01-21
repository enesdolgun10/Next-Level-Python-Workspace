sayilar = [1,2,3,4,5]
# kareleri = []

# for sayi in sayilar:
#     kareleri.append(sayi**2)

# print(kareleri)

# def kareAl(sayi):
#     return sayi ** 2

sonuc = list(map(lambda sayi:sayi**2,sayilar))
print(sonuc)

sayilar_str = ["1","2","3","4","5"]
sonuc2 = list(map(int,sayilar_str))
print(sayilar_str)
print(sonuc2)

isimler = ["ali","hasan","ayşe","zeynep"]
sonuc3 = list(map(str.capitalize,isimler))
print(sonuc3)

kullanicilar = [
    {"ad":"Ali","soyad":"Yılmaz"},
    {"ad":"Ahmet","soyad":"Cengiz"}
]

sonuc4 = list(map(lambda kisi: kisi["ad"],kullanicilar)) 
print(sonuc4)