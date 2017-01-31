#!/usr/bin/python
class Person:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def greet(self):
        print 'Hello,I\'am %s' % self.name
foo=Person()
bar=Person()

foo.setName('Mr Fabius')
bar.setName('Mrs Chicory')
print foo.getName()
print bar.getName()

Person.greet(foo)
Person.greet(bar)
foo.greet()
bar.greet()

print foo.name
print bar.name

bar.name='Pagge'
print bar.getName()
Person.greet(bar)
