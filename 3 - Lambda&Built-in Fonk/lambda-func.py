# lambda arguments : expression

def kareAl(a):
    return a**2

sonuc = kareAl(5) 
# 25

sonuc = (lambda a: a**2)(3)
# 9

kareAl= lambda a: a**2
sonuc= kareAl(4)
# 16

toplama = lambda a,b,c: a + b + c
sonuc=toplama(1,2,3)
# 6

def myFunc(n):
    return lambda a: a*n

carpma2 = myFunc(2)
carpma3 = myFunc(3)

sonuc = myFunc(5)(3)
# 15

sonuc= carpma2(5)
# 10
sonuc=carpma3(5)
# 15


print(sonuc)