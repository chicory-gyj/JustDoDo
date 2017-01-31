#!/usr/bin/python
def power(x,y,*others):
    if others:
        print 'Received redundant parameters:',others
    return pow(x,y)
def interval(start,stop=None,step=1):
    if stop is None:
        start,stop=0,start
    result=[]
    i=start
    while i<stop:
        result.append(i)
        i+=step
    return result

print power(2,3)
print power(3,2)
print power(y=2,x=3)
print power(3,3,'Hello,Mr Fabius')
m=(9,8,3)
print power(4,4,*m)
ff=(4,5)
print power(*ff)
xx=(1,2,3,4,5,6,7)
print power(*xx)

print interval(10)
print interval(1,5)
print interval(3,19,4)
print interval(2,7,2)
print power(*interval(2,7,2))
