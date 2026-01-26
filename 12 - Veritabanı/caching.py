import mysql.connector
from cachetools import cached,TTLCache
import time

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "EnesDolgun",
    database = "shopdb"
)

#  60 dk bellek üzerinde yer alır
@cached(cache=TTLCache(maxsize=32,ttl=60))
def getProducts():
    cursor = db.cursor()
    sql = "SELECT p.name,c.categoryName FROM products p inner join categories c on  p.categoryId=c.id WHERE c.categoryName='Bilgisayar'"
    cursor.execute(sql)
    print("From Sql") # ilk çağırıldığında sqlden verileri aldığını belirtir 2. ve 3. printte cacheden bellekten verıyı getırır
    return cursor.fetchall()


s = time.time()
print(getProducts())
print("Geçen zaman: ",time.time() - s)
s = time.time()
print(getProducts())
print("Geçen zaman: ",time.time() - s)
s = time.time()
print(getProducts())
print("Geçen zaman: ",time.time() - s)

#  Büyük trafik alan uygulamalarda cacheleme yapılması çok önemlidir !