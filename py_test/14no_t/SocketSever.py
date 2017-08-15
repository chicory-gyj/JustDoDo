#!/usr/bin/python
from SocketServer import TCPServer,ForkingMixIn,StreamRequestHandler
class Server(ForkingMixIn,TCPServer):
    pass
class Handler(StreamRequestHandler):
    def handle(self):
        addr=self.request.getpeername()
        print 'Got connection to ',addr
        self.wfile.write('Thank you for connecting')
server=Server(('',12345),Handler)
server.serve_forever()
