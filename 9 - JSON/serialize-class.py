import json

class Product:
    def __init__(self,id,title,price):
        self.id=id
        self.title = title
        self.price=price


# SERİALİZE

# p1 = Product(1,"Samsung S24",50000)
# p2 = Product(2,"Samsung S25",60000)

# # products = [p1.__dict__,p2.__dict__]
# products = {
#     p1.id : p1.__dict__,
#     p2.id : p2.__dict__
# }


# with open("products.json", "w") as file:
#     # json.dump(p1,file) # dosyaya yazdırılabilir değil hata verir
#     json.dump(products,file)


# DESERİALİZE

with open("products.json") as file:
    products = json.load(file)

print(type(products))

urunler = []
for key , value in products.items():
    urunler.append(Product(key, value["title"], value["price"]))

print(type(urunler))

for p in urunler:
    print(p.title)