#!/usr/bin/python
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

m=input('enter the number you want:')
print fac(m)
