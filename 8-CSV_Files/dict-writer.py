import csv

# with open("urunler2.csv","w",newline='') as file:
#     headers = ["Id", "ProductName", "Price", "IsActive", "Category", "Rating"]
#     csv_writer = csv.DictWriter(file,headers)
#     csv_writer.writeheader()

#     # csv_writer.writerow({
#     #     "Id":1,
#     #     "ProductName":"Samsung S24",
#     #     "Price": 35000,
#     #     "IsActive": True,
#     #     "Category":"Telefon",
#     #     "Rating": 3.8
#     # })
#     # csv_writer.writerow({
#     #     "Id":2,
#     #     "ProductName":"Samsung S25",
#     #     "Price": 45000,
#     #     "IsActive": True,
#     #     "Category":"Telefon",
#     #     "Rating": 4.4
#     # })

#     csv_writer.writerows([
#         {
#             "Id":1,
#             "ProductName":"Samsung S24",
#             "Price": 35000,
#             "IsActive": True,
#             "Category":"Telefon",
#             "Rating": 3.8
#         },
#         {
#             "Id":2,
#             "ProductName":"Samsung S25",
#             "Price": 45000,
#             "IsActive": True,
#             "Category":"Telefon",
#             "Rating": 4.4
#         },
#         {
#             "Id":3,
#             "ProductName":"Iphone 15",
#             "Price": 65000,
#             "IsActive": True,
#             "Category":"Telefon",
#             "Rating": 4.8
#         }
#     ])



# Elemanlar üzerine ekleme işlemi
# with open("urunler2.csv","a",newline='') as file:
#     headers = ["Id", "ProductName", "Price", "IsActive", "Category", "Rating"]
#     csv_writer = csv.DictWriter(file,headers)
#     csv_writer.writerow({
#         "Id":4,
#         "ProductName":"Iphone 14 Pro",
#         "Price": 60000,
#         "IsActive": True,
#         "Category":"Telefon",
#         "Rating": 4.5
#     })


# Güncelleme işlemi

def price_tax(price):
    return float(price)*1.20

with open("urunler.csv") as file:
    csv_reader = csv.DictReader(file)
    urunler = list(csv_reader)

    with open("urunler3.csv","w",newline='') as file:
        headers = ["Id", "ProductName", "Price", "IsActive", "Category", "Rating"]
        csv_writer = csv.DictWriter(file,headers)
        csv_writer.writeheader()

        for u in urunler:
            csv_writer.writerow({
                "Id":u["Id"],
                "ProductName":u["ProductName"],
                "Price": price_tax(u["Price"]),
                "IsActive": u["IsActive"],
                "Category":u["Category"],
                "Rating": u["Rating"]
            })
        