import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "EnesDolgun",
    database = "shopdb"
)

cursor = db.cursor()

sql = "INSERT INTO products (name,price,imageUrl,description) VALUES(%s,%s,%s,%s)"
# value = ("İphone 16",70000,"3.jpg","Kamerası kaliteli bir telefon")
# cursor.execute(sql,value)

values = [
    ("Samsung S43",80000,"4.jpg","Kamerası kaliteli bir telefon"),
    ("Samsung S33",90000,"5.jpg","Kamerası kaliteli bir telefon"),
    ("İphone 20",95000,"6.jpg","Kamerası kaliteli bir telefon"),
    ]
cursor.executemany(sql,values)

try:
    db.commit()
    print(cursor.rowcount, "Kayıt edildi")
    print(f"son eklenen kaydın id: {cursor.lastrowid}")
except mysql.connector.Error as err:
    print("hata: ",err)
finally:
    cursor.close()
    db.close()
    print("bağlantı kapatıldı")