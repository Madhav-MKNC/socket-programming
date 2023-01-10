import socket
import sys

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print("Failed to create a socket")
    print("Reason :",str(e))
    sys.exit()
print("Socket Created")

target_host = input("Enter the target_host name to connect : ")
target_port = input("Enter the target_port : ")

try:
    sock.connect((target_host,int(target_port)))
    print("socket connected to",target_host,target_port)
    sock.shutdown(2)
except socket.error as e:
    print("Failed to connect to {} on port {}".format(target_host,target_port))
    print("Reason :",e)
    sys.exit()

# please ignore this
input()