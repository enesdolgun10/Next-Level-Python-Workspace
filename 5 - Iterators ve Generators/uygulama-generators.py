#  (1 - sonsuz) aralıgındakı her sayının karesını getıren fonksiyon

def sayi_uret():
    sayi = 0
    while True:
        yield sayi **2
        sayi +=1

generator = sayi_uret()

for i in generator:
    print(i)
    

# Fibonacci serisini hem normal fonksiyon hem de generator fonksiyon ile olusturun

def fib_list(max):
    sayilar = []
    a, b = 0, 1

    while len(sayilar)<max:
        sayilar.append(b)
        a, b = b, a+b

    return sayilar

print(fib_list(90))

def fib_gen(max):
    a, b = 0, 1
    count = 0
    while count <= max:
        a, b = b, a+b
        yield b
        count += 1

for i in fib_gen(9000):
    print(i)
    
# Performans testleri yapın

import sys
liste= [i for i in range(10000)]
print(sys.getsizeof(liste)) # 85176

gen = (i for i in range(10000))
print(sys.getsizeof(gen)) # 192

import time

list_start_time = time.time()
sum([i for i in range(9000000)])
list_stop = time.time()-list_start_time

gen_start_time = time.time()
sum((i for i in range(9000000)))
gen_stop= time.time()-gen_start_time

print(list_stop) # 0.33 sn
print(gen_stop) # 0.21 sn


