#!/usr/bin/python
import socket
s=socket.socket()
host=socket.gethostname()
port=12345

s.bind((host,port))
s.listen(5)
while True:
    c,addr=s.accept()
    print c.fileno()
    print 'Got connection to Client\'s Address',addr
    c.send('Thank you for your connection!')
    c.close()

