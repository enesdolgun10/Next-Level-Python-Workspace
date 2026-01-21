class Product:
    def __init__(self, name, price):
        self.name = name
        if price >=0:
            self._price = price
        else:
            raise ValueError("Ürün fiyatı için negatif değer ataması yapılamaz")
        
    
    # def set_price(self, value):
    #     if value >=0:
    #         self._price = value
    #     else:
    #         raise ValueError("Ürün fiyatı için negatif değer ataması yapılamaz")
        
    # def get_price(self):
    #     return self._price


    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value >=0:
            self._price = value
        else:
            raise ValueError("Ürün fiyatı için negatif değer ataması yapılamaz")


p = Product("Iphone 16",80000)

print(p.price)
p.price = 199999
print(p.price)
