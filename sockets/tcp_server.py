import socket
from addresses import host, port

host = host
port = port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen(5)
print(f"Socket is Listening... on {host} as port:{port}")

while True:
    print("server is waiting for connection...")
    client,addr = server.accept()
    print("Client connected from",addr)
    try:
        while True:
            client_message = client.recv(1024)
            print("Client :",client_message.decode('utf-8'))
            server_message = input("Send message: ")
            client.send(server_message.encode('utf-8'))
    except: print("Exited by the user")
    client.close()

server.close()
input("server OFFLINE")