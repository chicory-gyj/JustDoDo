#!/usr/bin/python
class Secretive:
    def __inaccessible(self):
        print 'Bet you can not see me'
    def accessible(self):
        print 'The secret message is:'
        self.__inaccessible()

s=Secretive()
s.accessible()
s._Secretive__inaccessible()
