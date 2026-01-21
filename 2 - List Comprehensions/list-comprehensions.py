sayilar = []

for i in range(5):
    sayilar.append(i)

print(sayilar)


sayilar2 = [i*2 for i in range(5)]

print(sayilar2)

kurum = "Koreli Çeyiz"

for i in kurum:
    print(i.upper())

sonuc = [i.upper() for i in kurum]
print(sonuc)