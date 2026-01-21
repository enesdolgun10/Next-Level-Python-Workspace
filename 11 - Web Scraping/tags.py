from bs4 import BeautifulSoup

with open("index.html", encoding="utf-8") as file:
    html = file.read()

obj = BeautifulSoup(html, "html.parser")

sonuc =  obj
sonuc = obj.prettify() #html dokumanı ıcerısındekı baslıkları duzenler
sonuc = obj.title
sonuc = type(obj.title)
sonuc = obj.title.string

sonuc =  obj.body.h1.string
sonuc =  obj.h1.string

print(sonuc)
