import requests

response = requests.post("https://jsonplaceholder.typicode.com/posts", data={
    "userId": 1,
    "title": "Yeni Gönderi",
    "body": "Yeni Gönderi Açıklaması"
})

sonuc = response

sonuc = response.text
sonuc = response.json()
sonuc = response.headers

print(sonuc)