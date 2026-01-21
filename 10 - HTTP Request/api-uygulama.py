import requests
import json

API_KEY = "7b9d2d1c6b5f4e0ebcf52520262001"
URL = "http://api.weatherapi.com/v1/current.json"

konum = input("Şehir giriniz :")

response = requests.get(URL,params={
    "key" : API_KEY,
    "q" : konum,
    "lang": "tr"
})

sonuc = response.json()
sehir = sonuc["location"]["name"]
havaDurumu = sonuc["current"]["temp_c"]
text = sonuc["current"]["condition"]["text"]

print(f"{sehir} şu anda {havaDurumu} derece ve {text}")