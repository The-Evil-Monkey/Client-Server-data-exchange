import socket, random

ip = '' # LocalHost
port = 8090
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
s.listen(1)
a, addr = s.accept()
print "connected to", a, addr
while 1:
    data = a.recv(1024)
    print "Message from Client", data


s.close()
__author__ = 'vishket.shriwas'
