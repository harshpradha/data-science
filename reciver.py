import socket
h=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
ip_add='192.168.1.49'
port=588
pura_add=(ip_add,port)
h.bind(pura_add)
while True:
    message=h.recvfrom(150)
    print(message)
    data_massage=message[0]
    find_ms=data_massage.encode("ascii")
    print(find_ms)
 #port = ghar ka pta ki ye kitna h