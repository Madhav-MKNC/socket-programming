import socket

host = 'localhost' # input('enter a host : ')
port = int(input('enter port : '))
host = socket.gethostbyname(host)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port)) 

try:
    while True:
        client_message = input("You: ")
        client.send(client_message.encode('utf-8'))
        data = client.recv(1024)
        client.settimeout(3)
        if not data: continue
        print("Server :",str(data))
except KeyboardInterrupt: print("You Exited")

client.close()
input()
