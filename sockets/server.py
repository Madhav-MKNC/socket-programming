import socket
from variables import Host,Port
import utils

import os,sys,time 

# creating a socket
try:
    print('creating a TCP Socket')
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.gaierror as err:
    print('[-] failed to create a TCP Socket. REASON: ')
    sys.exit()    
print('[+] socket created\t')

# hosting
host = Host().localhost
port = Port().default

# binding and listening 
server.bind((host,port))
print(f"Listening... on '{host}:{port}'")
server.listen(5)

# connection with client
while True:
    try:
        client1,addr1 = server.accept()
        print("\n[+] Client 1 connected from : ",addr1)

        client2,addr2 = server.accept()
        print("[+] Client 2 connected from : ",addr2)

        try:
            while True:
                c1 = client1.recv(1024).decode('utf-8')
                c2 = client2.recv(1024).decode('utf-8')
                client2.send(str(c1).encode('utf-8'))
                client1.send(str(c2).encode('utf-8'))
        except: print("Exited by the user")
        client1.close()
        client2.close()

    except Exception as e:
        print(str(e))

server.close()
input('\n[-] Program Stopped! (press any key) ')