# class Test():
#     pass

class BaseClass():
    def show(self):
        return "Merhaba"
    
def add_attribute(self):
    self.b = 10

Test = type("Test",(BaseClass,),{"a":5,"add_attribute":add_attribute})
t = Test()

sonuc = Test()  # nesnenin adresi gelir
sonuc = Test    # testin bir class oldugunu söyler
sonuc = type(Test)  # type sınıfı oldugunu soyler (metaclass) 

# sonuc = type(2) # int 
# sonuc = type(int)   # type

# sonuc = type("2")   # str

sonuc = t.show()
sonuc = t.a
t.add_attribute()
sonuc = t.b


print(sonuc)