# iterable
# iterator

sayilar = [1,2,3,4,5] # iterable nesne: elemanları üstünde tek tek dolaşabiliriz

iterator = iter(sayilar)

print(next(iterator)) #1
print(next(iterator)) #2
print(next(iterator)) #3

while True:
    try:
        sayi = next(iterator)
        print(sayi)
    except StopIteration:
        break

# s = "BTK AKADEMİ"
# a = 10

# for i in a:
#     print(i) i burada iterator elemanıdır

# print(dir(a)) # hata verir : a yani int objesi iterable değildir