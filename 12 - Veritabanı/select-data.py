import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "EnesDolgun",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "SELECT * FROM products"
# cursor.execute(sql)
# products = cursor.fetchall()
# for p in products:
#     print(p[0],p[1])

# sadece tablonun belirli değerlerini cekerız
# sql = "SELECT id,name FROM products"
# cursor.execute(sql)
# products = cursor.fetchall()
# for p in products:
#     print(p[0],p[1])

# tek product dondurur (ilkini)
sql = "SELECT id,name FROM products"
cursor.execute(sql)
product = cursor.fetchone()
print(product)