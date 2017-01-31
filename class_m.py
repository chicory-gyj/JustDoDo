#!/usr/bin/python
class Class():
    def method(self):
        print 'My name is Chicory'
def fun():
    print 'This is my cat'
m=Class()
m.method()

m.method=fun
m.method()
