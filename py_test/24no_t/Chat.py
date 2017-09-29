#!/usr/bin/python

from asyncore import dispatcher
from asynchat import async_chat
import asyncore,socket

PORT=5006
NAME='TestChat'

class ChatSession(async_chat):
    def __init__(self,server,sock):
        async_chat.__init__(self,sock)
        self.server=server
        self.set_terminator('\r\n')
        self.date=[]
        self.push('Welcome to %s\r\n')                                                                                                                                                                                                                                                                                                                                                                                                                              \n' % self.server.name)

    def collect_incoming_data(self, data):
        self.date.append(data)
    def found_terminator(self):
        line=''.join(self.date)
        self.date=[]
        self.server.broadcast(line)

    def handle_close(self):
        async_chat.handle_close(self)
        self.server.disconnect(self)

class ChatServer(dispatcher):
    def __init__(self,port,name):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('',port))
        self.listen(5)
        self.name=name
        self.sessions=[]
    def disconnect(self,session):
        self.sessions.remove(session)
    def broadcast(self,line):
        for session in self.sessions:
            session.push(line+'\r\n')
    def handle_accept(self):
        conn,addr=self.accept()
        self.sessions.append(ChatSession(self,conn))
if __name__=='__main__':
    s=ChatServer(PORT,NAME)
    try:asyncore.loop()
    except KeyboardInterrupt:print


