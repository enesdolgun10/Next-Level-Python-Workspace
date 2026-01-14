data = [

    {
        "id":1,
        "title":"Iphone 14",
        "price":50000
    },
    {
        "id":2,
        "title":"Iphone 15",
        "price":55000
    }
]

import json

# dosya içerisine yeni urun ekleme

product = {
    "id":3,
    "title":"Samsung S25",
    "price":50000
}

with open("products.json") as file:
    products = json.load(file)

# veriyi ekleme
# products.append(product)


# veri guncelleme
for p in products:
    if p["title"] == "Samsung S24":
        p["title"] = "Samsung S25"


# veri silme
products.remove(products[0])


with open("products.json","w", encoding="utf-8") as file:
    json.dump(products,file, ensure_ascii=False, indent=2)


