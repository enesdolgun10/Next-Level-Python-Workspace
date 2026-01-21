import json

product = {
    "id":2,
    "title":"Hp Victus",
    "price":45000,
    "rating": 4.3,
    "category":"Bilgisayar",
    "colors": ["black","gray","blue"]
}

print(product)
print(type(product)) # dict
print(product["title"])

# sonuc = json.dumps(product)

# print(sonuc)
# print(type(sonuc)) # str
# print(product["title"])   # Hata verir


# dosyaya yazmak istediğimizde
with open("product.json","w", encoding="utf-8") as file:
    json.dump(product,file, ensure_ascii=False, indent=2)

