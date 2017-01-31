#!/usr/bin/python

def ppow(n,m):
    if m==0:
        return 1
    else:
        return n*ppow(n,m-1)

n=input('enter the number:')
m=input('enter the pow:')
print ppow(n,m)
