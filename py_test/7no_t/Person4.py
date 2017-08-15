#!/usr/bin/python
class Person:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def greet(self):
        print'Hello,world.I\'am %s' % self.name

#foo=Person()
#bar=Person()
#foo.setName('Luck')
#bar.setName('Anne')
#print foo.getName()
#print bar.getName()
#bar.greet()
#foo.greet()
#print bar.name
#print foo.name
#foo.name='CHicory'
#foo.greet()
#Person.greet(foo)
