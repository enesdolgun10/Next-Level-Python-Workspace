import csv

urunler_path = r"C:\GitHub_Folders\Next-Level-Python-Workspace\8-CSV_Files\urunler.csv"

with open(urunler_path) as file:
    csv_reader = csv.DictReader(file)
    for i in csv_reader:
        if i["Category"] == "Telefon" and float(i["Rating"]) > 4.5:
            print(i["ProductName"],i["Price"])
            