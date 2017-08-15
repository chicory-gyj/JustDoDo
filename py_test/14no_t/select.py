#!/usr/bin/python
import socket,select
s=socket.socket()
host=socket.gethostname()
port=11111
s.bind((host,port))
s.listen(5)

inputs=[s]
while True:
    #rs,ws,es=select.select(inputs,[],[])
    for r in rs:
        if r is s:
            c,addr=s.accept()
            print 'Got connection from',addr
            inputs.append(c)
        else:
            try:
                data=r.recv(1024)
                disconnect=not data
            except socket.error:
                disconnect=True
            
            if disconnect:
                print r.getpeername(),'disconnected'
                inputs.remove(r)
            else:
                print data
