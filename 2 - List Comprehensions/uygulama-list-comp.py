# 1- (1-100) arasındaki sayılardan 12ye tam bölünebilen sayı listesini oluşturunuz :

uygulama1 = [sayi for sayi in range(100) if sayi%12==0]
# print(uygulama1)

# 2- Verilen text içerisindeki rakamları içeren bir liste oluşturunuz
# text = "Hello 12345 World" => [1,2,3,4,5]

text = "Hello 12345 World"
uygulama2 = [int(karakter) for karakter in text if karakter.isdigit()]
# print(uygulama2)

# 3- Sıcaklıklar listesinde bulunan her hava sıcaklık bilgisine göre 4 derecenin altında buzlanma tehlikesi yazınız.
# sicakliklar = [20,15,0,-5,-2] => [20,15,"Buzlanma Tehlikesi","Buzlanma Tehlikesi","Buzlanma Tehlikesi"]

sicakliklar = [20,15,0,-5,-2]
uygulama3 = [s if s>4  else "Buzlanma Tehlikesi" for s in sicakliklar]
# print(uygulama3)

# 4- ogrenciler ve notlar listelerindeki notu 50den fazla olan kişileri ekrana dict verisinde yazdırınız.
# ogrenciler = ["ali","ahmet","canan"]
# notlar = [50,60,80]
# => "{'ahmet': 60, 'canan': 80}"

ogrenciler = ["ali","ahmet","canan"]
notlar = [50,60,80]

liste = [(ogrenciler[i],notlar[i]) for i in range(0, len(ogrenciler))]
uygulama4 = {key:value for (key,value) in liste if value > 50}
print(uygulama4)


# 5- For döngüsü ile yazılan uygulamayı list comprehension ile yazınız.
sonuc = []
for x in range(3):
    for y in range(3):
        sonuc.append((x,y))
print(sonuc)

uygulama5 = [(x,y) for x in range(3) for y in range(3)]
print(uygulama5)