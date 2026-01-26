import requests

API_KEY = "AIzaSyBLzUGEMyP2PQWOtH2Mgq0NvZLgeTqh1gw"  
def signUp():
    email = input("email: ")
    password = input("password: ")

    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={API_KEY}"

    data = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }

    r = requests.post(url, json=data)
    result = r.json()

    if "error" in result:
        print("Hata:", result["error"]["message"])
    else:
        print("kullanıcı oluşturuldu ✅")


def login():
    email = input("email: ")
    password = input("password: ")

    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"

    data = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }

    r = requests.post(url, json=data)
    result = r.json()

    if "error" in result:
        print("hatalı email yada parola ❌")
    else:
        print("login yapıldı ✅")
        print("User info:")
        print(result)


# signUp()
login()