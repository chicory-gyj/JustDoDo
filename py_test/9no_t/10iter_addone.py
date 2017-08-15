#!/usr/bin/python
class Addone:
    def __init__(self):
        self.value=0
    def next(self):
        self.value+=1
        if self.value>100:
            raise StopIteration
        return self.value
    def __iter__(self):
        return self

ti=Addone()
print list(ti)
