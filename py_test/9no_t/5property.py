#!/usr/bin/python
__metaclass__=type
class Rectangle:
    def __init__(self):
        self.height=0
        self.width=0
    def setSize(self,size):
        self.height,self.width=size
    def getSize(self):
        return self.height,self.width
    size=property(getSize,setSize)


r=Rectangle()
print r.size
