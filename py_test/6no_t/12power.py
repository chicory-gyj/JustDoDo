#!/usr/bin/python
def power(x,y):
    if y==0:
        return 1
    else:
        return x*power(x,y-1)
m=input('enter the first number:')
n=input('enter the second number:')
print power(m,n)
