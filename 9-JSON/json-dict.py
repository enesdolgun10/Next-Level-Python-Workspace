data = {
  "2":{
    "title": "Iphone 15",
    "price": 55000
  },
  "3":{
    "title": "Samsung S25",
    "price": 50000
  }
}

import json


with open("products.json") as file:
    products = json.load(file)

print(products["2"])

# ekleme
# products.update({
#     "1": {
#     "title": "Mackbook Pro",
#     "price": 50000
#   }
# })


# güncelleeme
# products.update({
#     "3": {
#     "title": "Samsung S25",
#     "price": 50005
#   }
# })

# silme
# products.pop("1")

with open("products.json","w",encoding="utf-8") as file:
    json.dump(products,file, ensure_ascii=False, indent=2)