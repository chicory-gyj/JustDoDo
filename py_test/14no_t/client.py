#!/usr/bin/python
import socket
s=socket.socket()
host=socket.gethostname()
port=11111

s.connect((host,port))
#print s.recv(1024)

