# any all

sonuc = all([True,True,False])
sonuc = all([True,True,True])
sonuc = any([False,True,True])

# And => True and true => all()
# Or => True or False => any()

sayilar = [1,3,5,7,6,52,0]
sonuc = all([bool(sayi) for sayi in sayilar])
# false

sonuc = any([bool(sayi) for sayi in sayilar])
# true

sonuc = all([sayi % 2 ==0 for sayi in sayilar])
# false

sonuc = any([sayi % 2 ==0 for sayi in sayilar])
# true

users = ["ahmet","ali","orkun"]
sonuc= all([user[0]=='a' for user in users])
# false
sonuc= any([user[0]=='a' for user in users])
# true

print(sonuc)