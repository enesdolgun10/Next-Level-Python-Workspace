from bs4 import BeautifulSoup

with open("index.html", encoding="utf-8") as file:
    html = file.read()

obj = BeautifulSoup(html, "html.parser")

sonuc = obj.find(id="item1")
sonuc = obj.find(id="header")
sonuc = obj.find(class_="item") # burada class dan sonra  _ koymayı unutma ÖNEMLİ ! class_ 

sonuc = obj.find_all(class_="item")
sonuc = obj.find_all(class_="item")[1]

sonuc = obj.select("#header") # id aramak istediğimizde başına # işareti gelir , select liste döner
sonuc = obj.select("#item1") # find_all a benzer 
sonuc = obj.select(".item") # class aramak istiyorsak başına . getirmemiz lazım , dizi döner yine

sonuc = obj.select_one(".item") # kritere uyan ilk seceneği getirir bu find gibidir
sonuc = obj.select_one("#item1")

sonuc = obj.div.attrs["id"]    # cağırdığımız objenin id veya class isimlerini verir
sonuc = obj.div.attrs["class"] 

sonuc = obj.ul.get_text(strip=True, separator="-")

print(sonuc)


for a in obj.div.find_all("a"):
    # print(a.get("href"))
    print(a["href"])
