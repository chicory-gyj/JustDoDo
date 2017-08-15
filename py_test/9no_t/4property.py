#!/usr/bin/python
class Rectangle:
    def __init__(self):
        self.height=0
        self.width=0
    def setSize(self,size):
        self.height,self.width=size
    def getSize(self):
        return self.height,self.width
r=Rectangle()
r.height=10
r.width=15
print r.getSize()
r.setSize((100,120))
print r.getSize()
# r.size=(300,40) can't do this
print r.height,r.width
