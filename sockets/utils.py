# /usr/bin/python

# functions which I don't want to code in the main program are stored in here

def input_client_addr(recv,send):
    inp = str(recv(1024)).split('.')    ##error todo --> recv again n again --> make the client send again n again, until bypassed
    if len(inp)!=4 or not all(inp) in range(0,255+1):
        send('invalid address! enter again : '.encode('utf-8'))
        return input_client(recv, send)
    return ''.join(inp)


