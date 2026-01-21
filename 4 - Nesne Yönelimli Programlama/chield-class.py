class Person:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname=surname
        self.age = age
        print("Person sınıfı türetildi.")
   
    def intro(self):
        print(self.name,self.surname,self.age)

class Student(Person):
    def __init__(self,name,surname,age, number):
        # Person.__init__(self,name,surname,age) bu şekilde de yazılabilir
        super().__init__(name,surname,age)
        self.number = number
        print("student sınıfı türetildi.")
    
    def study(self):
        print(f"{self.name} ders çalışıyor.")

    def intro(self):
        print(self.name,self.surname,self.age, self.number)

class Teacher(Person):
    def __init__(self, name, surname, age,branch):
        super().__init__(name, surname, age)
        self.branch = branch

    def teach(self):
        print(f"{self.name} {self.branch} dersi anlatıyor.")

    def intro(self):
        print(f"{self.name} {self.surname}, {self.age} yaşındaki {self.branch} öğrtemeni.")

p1 = Person("Enes","Dolgun",22)
p1.intro()

s1 = Student("Ahmet","Yılmaz",16,643)
s1.intro()
s1.study()
# print(s1.number)

t1= Teacher("Ali","Korkmaz",35,"Fizik")
t1.intro()
t1.teach()
# print(t1.branch)