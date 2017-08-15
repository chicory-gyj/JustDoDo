#!/usr/bin/python
from math import sqrt
for n in range(99,0,-1):
    m=sqrt(n)
    if m==int(m):
        print n
        break
