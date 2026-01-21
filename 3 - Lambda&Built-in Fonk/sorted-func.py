sayilar = [1,2,53,23,65,4,5]

sonuc = sorted(sayilar)
# sorted yeni liste olusturur orjınel listeyi değiştirmez

sonuc= sorted(sayilar,reverse=True)
# azalan sıralama

users = [
    {"username":"enesd","posts":["post1","post2"],"email":"info@abc.com","phone":"1234"},
    {"username":"ahmetb","posts":["post1"],"email":"info@abcd.com"},
    {"username":"zakkumg","posts":["post1","post2","post3"]},
]

sonuc = sorted(users,key=len)
# key bilgisi en az olandan cok olana sıralar : zakkum ahmet enes
sonuc = sorted(users,key=len,reverse=True)
# tam tersi enes ahmet zakkum

sonuc = sorted(users,key=lambda user:user["username"])
# usernamelerin alfabetik sırasına göre sıralar

sonuc = sorted(users,key=lambda user:len(user["posts"]))
# post sayısına göre sıralar ahmet enes zakkum
sonuc = sorted(users,key=lambda user:len(user["posts"]),reverse=True)
# tam tersi

# en fazla gonderi atan kullanıcı kım dıye sorarsak :
sonuc = list(map(lambda user: user["username"] ,sorted(users,key=lambda user:len(user["posts"]),reverse=True)))
# zakkumg , enesd, ahmetb


kurslar = [
    {"title":"python","count":10000},
    {"title":"web geliştirme","count":20000},
    {"title":"javascript","count":5000},
]

sonuc = sorted(kurslar,key= lambda kurs: kurs["count"])
# bu kurs bilgierini verir
sonuc = list(map(lambda kurs:kurs["title"], sorted(kurslar,key= lambda kurs: kurs["count"])))
# bu da sadece kursun titleını

print(sonuc)