#!/usr/bin/python
class Secretive():
    def __inaccess(self):
        print 'you can\'t see me.'
    def access(self):
        print 'There is one way:'
        self.__inaccess()

M=Secretive()
M.access()
M._Secretive__inaccess()

class M():
    print 'yiyayiy'
