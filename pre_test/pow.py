#!/usr/bin/python
def ppow(n,m):
    result=1
    for i in range(m):
        result*=n
    return result
x=input('enter the numeber')
y=input('enter the pow')
print ppow(x,y)
