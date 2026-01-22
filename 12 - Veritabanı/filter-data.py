import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "EnesDolgun",
    database = "shopdb"
)

cursor = db.cursor()

sql = "SELECT * FROM products WHERE id=1"
cursor.execute(sql)

result = cursor.fetchone()

print(result)