import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server.bind((socket.gethostbyname(socket.gethostname()),12345))
server.bind((input("Enter the host : "),12345))
server.listen(5)
print("Socket is Listening...")

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
# please ignore this
input()
