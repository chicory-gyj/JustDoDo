#!/usr/bin/python
__metaclass__=type
class MyClass:
    def smeth():
        print 'This is a static method'
    smeth=staticmethod(smeth)
    
    def cmeth(cls):
        print 'This is a class method of',cls
    cmeth=classmethod(cmeth)

MyClass.smeth()
MyClass.cmeth()
