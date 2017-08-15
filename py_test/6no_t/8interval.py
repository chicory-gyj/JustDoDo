#!/usr/bin/python
def interval(start,stop=None,step=1):
    if stop is None:
        start,stop=0,start
    result=[]
    i=start
    while i<stop:
        result.append(i)
        i+=step
    return result

print interval(10)
print interval(5,4,1)
print interval(3,4,6)

