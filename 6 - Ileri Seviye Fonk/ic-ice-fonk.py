# def selam(isim):
#     return f"selam, {isim}"

# # print(selam("Enes"))
# # print(selam)

# merhaba = selam

# print(selam)
# print(merhaba)

# print(selam("Enes"))
# print(merhaba("Mustafa"))

# del selam
# # print(selam("Enes")) hata verir!

# print(merhaba)



# def outer(number1):
#     def inner(number):
#         print(number)

#     inner(number1)

# outer(10)


def faktoriyel(sayi):

    if not isinstance(sayi, int):
        raise TypeError("number must be an int")
    
    if not sayi >= 0:
        raise ValueError("number must be zero or positive")

    
    def inner_faktoriyel(sayi):
        if sayi <= 1:
            return 1

        return sayi* inner_faktoriyel(sayi-1)
    
    return inner_faktoriyel(sayi)

try: 
    sonuc = faktoriyel(4)
    print(sonuc)
except Exception as ex:
    print(ex)

