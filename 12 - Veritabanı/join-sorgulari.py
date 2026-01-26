import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "EnesDolgun",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "SELECT name,categoryId FROM products"
# sql = "SELECT categoryName FROM categories"
# sql = "SELECT products.name,categories.categoryName FROM products inner join categories on  products.categoryId=categories.id"
# sql = "SELECT p.name,c.categoryName FROM products p inner join categories c on  p.categoryId=c.id"
# sql = "SELECT p.name,c.categoryName FROM products p inner join categories c on  p.categoryId=c.id WHERE c.id=1"
# sql = "SELECT p.name,c.categoryName FROM products p inner join categories c on  p.categoryId=c.id WHERE c.id=2"
sql = "SELECT p.name,c.categoryName FROM products p inner join categories c on  p.categoryId=c.id WHERE c.categoryName='Telefon'"

cursor.execute(sql)

result = cursor.fetchall()

print(result)