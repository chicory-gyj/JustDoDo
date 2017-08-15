#!/usr/bin/python
class Addone:
    def __init__(self):
        self.value=0
    def next(self):
        self.value+=1
        return self.value
    def __iter__(self):
        return self

it=Addone()
for i in it:
    print i
    if i>120:
        break

