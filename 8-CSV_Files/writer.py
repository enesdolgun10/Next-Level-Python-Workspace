import csv

# with open("arabalar.csv","w",newline="") as file:
#     csv_writer = csv.writer(file)
#     # csv_writer.writerow(["Marka","Model"])
#     # csv_writer.writerow(["Toyota","Corolla"])
#     # csv_writer.writerow(["Mazda","CX-5"])
#     csv_writer.writerows([["Marka","Model"],["Fiat","Egea"],["Toyota","Corolla"]])

# with open("arabalar.csv","a") as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(["Bmw","F30"])

# with open("urunler.csv") as file:
#     csv_reader = csv.reader(file)
#     with open("yeni-urunler.csv","w", newline='') as f:
#         csv_writer = csv.writer(f)
#         for urun in csv_reader:
#             csv_writer.writerow([u.upper() for u in urun])

# OKUMA
with open("urunler.csv", "r", newline="", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # header atla

    urunler = []
    for u in csv_reader:
        urunler.append([
            u[0],                      # Id
            u[1],                      # ProductName
            float(u[2]) * 1.2,         # Price %20 zam
            u[3],                      # IsActive
            u[4],                      # Category
            u[5]                       # Rating
        ])

# YAZMA
with open("yeni-urunler.csv", "w", newline="", encoding="utf-8") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(
        ["Id", "ProductName", "Price", "IsActive", "Category", "Rating"]
    )
    csv_writer.writerows(urunler)