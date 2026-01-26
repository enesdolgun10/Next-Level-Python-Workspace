import time
import threading

def calculate_square(numbers):
    print("Kareleri hesaplanıyor...")
    for i in numbers:
        time.sleep(0.3)
        print("karesi :", i*i)

def calculate_cube(numbers):
    print("Küpleri hesaplanıyor...")
    for i in numbers:
        time.sleep(0.3)
        print("küpü :", i*i*i)

sayilar = [3,5,8,9,5,25]

t = time.time()

# calculate_square(sayilar)
# calculate_cube(sayilar)

# args bızden tuple bekler o yuzden tek bir değer gireceksek sonunda mutlaka virgülü unutmamalıyız
t1  = threading.Thread(target=calculate_square,args=(sayilar,)) 
t2 = threading.Thread(target=calculate_cube,args=(sayilar,))

t1.start()
t2.start()

t1.join()
t2.join()


print("İşlem tamamlandı : ",time.time()-t)