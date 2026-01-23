import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "EnesDolgun",
    database = "shopdb"
)

cursor = db.cursor()

def updateProduct(id,name,price):
    sql = "UPDATE products SET name=%s, price=%s WHERE id=%s"
    params = (name,price,id)
    cursor.execute(sql,params)

    try:
        db.commit()
        print(f"{cursor.rowcount} tane kayıt guncellendi")
    except mysql.connector.Error as e:
        print("Hata : " ,e)
    finally:
        cursor.close()
        db.close()

updateProduct(3,"updatedProduct",55999)