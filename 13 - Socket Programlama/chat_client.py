import socket

PORT = 12345
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER,PORT)
FORMAT = "utf-8"
BYTE_SIZE =  1024
DISCONNECT_MESSAGE = "quit"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

while True:
    message = client.recv(BYTE_SIZE).decode(FORMAT)

    if message == DISCONNECT_MESSAGE:
        client.send("quit".encode(FORMAT))
        print("Çıkış yapılıyor...")
        break
    else:
        print(f"\nKarşınızdaki: {message}\n")
        message = input("Siz: ")
        client.send(message.encode(FORMAT))

client.close()