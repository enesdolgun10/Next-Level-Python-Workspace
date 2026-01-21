sayilar = [1,3,5,-4,-3]

# def negatifSayilar(x):
#     if x<0:
#         return True
#     else:
#         return False

# sonuc = list(filter(negatifSayilar,sayilar))
sonuc = list(filter(lambda x: x<0,sayilar))
sonuc = list(filter(lambda x: x%2 == 1,sayilar))

isimler = ["çınar","ali","enes","ada","yiğit"]

sonuc = list(filter(lambda x:x[0]=='a',isimler))

sonuc = list(map(lambda x:x.upper(),filter(lambda x:x[0]=='a',isimler)))

users = [
    {"username":"enesd","posts":["post1","post2"]},
    {"username":"ishakdlgn","posts":["post1"]},
    {"username":"arda","posts":["post1","post2","post3"]},
]

filterUsers = list(filter(lambda u: len(u["posts"])>2,users))
sonuc = list(map(lambda u:u["username"],filterUsers))

sonuc = [user["username"].upper() for user in users if len(user["posts"])>0]

print(sonuc)