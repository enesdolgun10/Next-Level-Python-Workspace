# 1- Online yemek siparişi veren kaç kişi var

import csv
with open("onlinefoods.csv") as file:
    csv_reader = csv.reader(file)
    liste = list(csv_reader)
    print(f"Online yemek siparişi veren kişi sayısı : {len(liste)-1}") # ilk satırı çıkartmamız önemli (header)


# 2- Online yemek siparişi veren öğrencileri listeleyin

with open("onlinefoods.csv") as file:
    csv_reader = csv.DictReader(file)
    users = [user for user in csv_reader if user["Occupation"] == "Student"]
    print(f"Online yemek siparişi veren öğrencilerin listesi : \n{users}")

    # for i in csv_reader:
    #     if(i["Occupation"] == "Student"):
    #         print(i)

# 3- 20-30 yaş aralığındaki kişilerin konum listesini hazırlayınız

with open("onlinefoods.csv") as file:
    csv_reader = csv.DictReader(file)
    filteredUsers = (user for user in csv_reader if int(user["Age"]) >= 20 and int(user["Age"]) <= 30)
    print(f"20-30 yaş aralığındaki kişilerin konum listesi:")
    for i in users:
        print(f"{i["latitude"]} - {i["longitude"]}")