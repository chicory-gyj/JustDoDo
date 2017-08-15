#!/usr/bin/python
class Rectangle:
    def __init__(self):
        self.height=0
        self.width=0
    def __setattr__(self,name,value):
        if name=='size':
            self.height,self.width=value
        else:
            self.__dict__[name]=value
    def __getattr__(self,name):
        if name=='size':
            return self.height,self.width
        else:
            raise AttributeError
m=Rectangle()
m.size=(100,2)
print m.size

print m

m.__setattr__('reat',90)
#print m.__getattr__('reat')
m.__setattr__('size',(2,3))
print m.__getattr__('size')
