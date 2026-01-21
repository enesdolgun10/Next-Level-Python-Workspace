# class => sınıf
class CartItem:
    # constructor => yapıcı metot
    def __init__(self,name,price,quantity):
        # instance attribues
        self.name = name
        self.price = price
        self.quantity = quantity
    
    # instance methods
    def calculate_total(self):
        return self.price * self.quantity

    def apply_discount(self,rate):
        self.price = self.price * rate

# instance => nesne, örnek
item1 = CartItem("Telefon",50000,2)
item2 = CartItem("Bilgisayar",70000,1)
item3 = CartItem("Kitap",100,3)

print(item1.calculate_total()) # 100.000
print(item3.calculate_total()) # 300

item1.apply_discount(0.5)
print(item1.calculate_total()) # 50.000
print(item1.price) # 25.000