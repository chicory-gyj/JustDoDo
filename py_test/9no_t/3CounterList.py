#!/usr/bin/python
class CounterList(list):
    def __init__(self,*args):
        super(CounterList,self).__init__(*args)
        self.counter=0
    def __getitem__(self,index):
        self.counter+=1
        return super(CounterList,self).__getitem__(index)

c1=CounterList(range(0,10))
print c1
print c1.reverse()
print c1
del c1[2:4]
print c1
print c1.counter
print c1[0]+c1[0]+c1[5]+c1[4]
print c1.counter
print c1.pop()
print c1
print c1.counter
        
