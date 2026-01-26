import socket

PORT = 12345
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER,PORT)
FORMAT = "utf-8"
BYTE_SIZE =  1024
DISCONNECT_MESSAGE = "quit"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDRESS)

server.listen()
print("Server çalışıyor...\n")

client_socket, client_address = server.accept()
client_socket.send("Server bağlantınız yapıldı.\n".encode(FORMAT))

while True:
    message = client_socket.recv(BYTE_SIZE).decode(FORMAT)

    if message == DISCONNECT_MESSAGE:
        client_socket.send("quit".encode(FORMAT))
        print("Çıkış yapıldı...")
        break
    else:
        print(f"\nKarşınızdaki: {message}\n")
        message = input("Siz: ")
        client_socket.send(message.encode(FORMAT))

server.close()