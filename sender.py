import socket
s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  
#SOCKET LIB = conect kar ke liye # bina connection ke hi connect kisi message ko n code karte h to encript karte h 
ip_add='192.168.1.4'
port=9999
pura_add=(ip_add,port)
message=input("chita hi khh de 😉")
encript_msg=message.encode('ascii')
s.sendto(encript_msg,pura_add)

