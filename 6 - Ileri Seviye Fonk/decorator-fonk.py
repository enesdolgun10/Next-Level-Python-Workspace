def selamlama(fn):
    def inner(ad):
        print("hoşgeldiniz")
        fn(ad)
        print("görüşmek üzere")
    return inner

@selamlama
def gunaydin(ad):
    print(f"günaydin benim adim {ad}")

@selamlama
def iyigunler(ad):
    print(f"iyi gunler benim adim {ad}")


# g = selamlama(gunaydin)
# i = selamlama(iyigunler)
# g()
# i()

gunaydin("Enes")

iyigunler("Ali")