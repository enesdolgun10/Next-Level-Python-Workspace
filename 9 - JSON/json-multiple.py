db = {
    "users":{
        "enesdolgun":{
            "firstname":"Enes",
            "lastname":"Dolgun"
        },
        "ishakdolgun":{
            "firstname":"İshak",
            "lastname":"Dolgun"
        },
    },
    "products":{
        "1":{
            "title":"Mackbook Air",
            "price":70000,
        },
        "2":{
            "title":"Samsung S23",
            "price":30000,
        },
    }
}

import json

#  db nesnesini json dosyasına yazdırdık
# with open("db.json","w",encoding="utf-8") as file:
#     json.dump(db,file, ensure_ascii=False, indent=2)

with open("db.json") as file:
    data = json.load(file)

print(data["users"],"\n")
print(data["users"]["enesdolgun"],"\n")
print(data["products"]["1"]["title"],"\n")

data["products"].update({
    "4":{
        "title":"Samsung S21",
        "price":20000
    }
})

data["users"].update({
    "mustafadolgun":{
            "firstname":"Mustafa",
            "lastname":"Dolgun",
            "age": 41
        },
})

with open("db.json", "w", encoding="utf-8") as file:
    json.dump(data,file,ensure_ascii=False,indent=2)