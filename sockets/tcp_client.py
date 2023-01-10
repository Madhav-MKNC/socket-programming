import socket
from addresses import host, port

host = host
port = port

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

try:
    while True:
        client_message = input("You: ")
        client.send(client_message.encode('utf-8'))
        data = client.recv(1024)
        print("Server :",str(data))
except KeyboardInterrupt: print("You Exited")

client.close()
input("you are OFFLINE")