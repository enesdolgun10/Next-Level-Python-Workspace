urunler_path = r"C:\GitHub_Folders\Next-Level-Python-Workspace\8-CSV_Files\urunler.csv"

# with open (urunler_path) as file:
#     print(file.read())


import csv

with open(urunler_path) as file:
    csv_reader = csv.reader(file)
    print(csv_reader)
    # liste = list(csv_reader)
    # print(liste[1])
    next(csv_reader)

    for i in csv_reader:
        if i[3] == "True":
            print(f"id: {i[0]}, ürün adı: {i[1]}")
    