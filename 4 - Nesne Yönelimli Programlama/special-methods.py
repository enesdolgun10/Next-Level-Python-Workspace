# liste = [1,2,3]
# print(len(liste))
# s = "Merhaba GitHub"
# print(len(s))


class Movie:
    def __init__(self, title, director, year, duration):
        self.title = title
        self.director = director
        self.year = year
        self.duration = duration

    def __repr__(self):
        return f"{self.title}, {self.director} tarafından {self.year} yılında yayınlandı."
    
    def __len__(self):
        return self.duration
    
    def __del__(self):
        print("Film silindi.")

m = Movie("Film Adı","Yönetmen","Yayın Tarihi",120)

print(m.__repr__())
print(len(m))