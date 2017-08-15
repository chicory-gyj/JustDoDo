#!/usr/bin/python
class Fibs:
    def __init__(self):
        self.a=0
        self.b=1
    def next(self):
        self.a,self.b=self.b,self.a+self.b
        return self.a
    def __iter__(self):
        return self

fib=Fibs()
for f in fib:
    if f>2000:
        print f
        break

