import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # ipv4  ve tcp protokolu karsılıkları
HOST = socket.gethostbyname(socket.gethostname())
PORT = 12345


server_socket.bind((HOST, PORT))

server_socket.listen()

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Bağlantı yapıldı : {client_address}")
    print(client_socket,client_address)
    client_socket.send("merhaba".encode("utf-8"))
    server_socket.close()
    break