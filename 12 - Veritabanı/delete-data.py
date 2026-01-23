import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "EnesDolgun",
    database = "shopdb"
)

cursor = db.cursor()

def deleteProducts(id):
    sql = "DELETE FROM products WHERE id=%s"
    # sql = "DELETE FROM products WHERE name LIKE '%s23%'"
    params = (id,)
    cursor.execute(sql,params)

    try:
        db.commit()
        print(f"{cursor.rowcount} tane kayıt silindi")
    except mysql.connector.Error as e:
        print("Hata :",e)
    finally:
        cursor.close()
        db.close()

deleteProducts(3)