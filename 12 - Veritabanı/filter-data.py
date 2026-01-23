import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "EnesDolgun",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "SELECT * FROM products WHERE id=1"
# sql = "SELECT * FROM products WHERE id>1"
# sql = "SELECT * FROM products WHERE name='Samsung S25'"
# sql = "SELECT * FROM products WHERE name='Samsung S25' and price=50000"
# sql = "SELECT * FROM products WHERE name='Samsung S25' or price=60000"
# sql = "SELECT * FROM products WHERE name LIKE '%Samsung%'"  #içinde samsung geçen
# sql = "SELECT * FROM products WHERE name LIKE 'Samsung%'"  # samsungla başlayan
sql = "SELECT * FROM products WHERE name LIKE '%Samsung'"  # samsungla biten
# sql = "SELECT * FROM products WHERE name LIKE '%Samsung%' or description LIKE '%iyi%'"

cursor.execute(sql)

# result = cursor.fetchone()
result = cursor.fetchall()

print(result)

# yer tutucu ile dinamik sorgu
def getProductById(id):
    sql = "SELECT * FROM products WHERE id=%s"
    params = (id,)
    cursor.execute(sql,params)
    result = cursor.fetchall()
    print(result)

getProductById(3)