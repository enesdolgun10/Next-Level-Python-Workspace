class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)

        a = {}

        for name, val in attrs.items():
            if name.startswith("_"):
                a[name] = val
            else:
                a[name.upper()] = val 

        return type(class_name, bases, a)
    
class Person(metaclass=Meta):
    x = 5
    y = 10
    _age = 25

    def hello(self):
        print("Merhaba")


p = Person()

sonuc = p.X
sonuc= p._age

print(sonuc)