import json

# Serialize   -> encode
# Deserialize -> decode

# with open("product.json") as file:
#     data = json.load(file)

jsonStingData = """
    {
        "id":1,
        "title":"Hp Victus",
        "price":45000,
        "rating": 4.3,
        "category":"Bilgisayar",
        "colors": ["black","gray","blue"]
    }
"""
data = json.loads(jsonStingData)

print(data)
print(type(data))
print(data["title"])


