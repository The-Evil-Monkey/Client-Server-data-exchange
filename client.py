import socket

ip = '' # Localhost
port = 8090

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((ip, port))

while 1:
    data = raw_input("enter message to send")
    c.send(data)
    recv = c.recv(1024)
    print "Message from Server", recv


c.close()


__author__ = 'vishket.shriwas'
