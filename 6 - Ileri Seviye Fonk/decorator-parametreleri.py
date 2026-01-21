def double(fn):
    def inner(*args,**kwargs):
        fn(*args, **kwargs)
        return fn(*args, **kwargs)
    return inner

@double
def merhaba():
    print("merhaba")

@double
def selam(isim):
    print("selam",isim)

@double
def iyigunler():
    return "İyi günler"

merhaba()
selam("Enes")
print(iyigunler())
