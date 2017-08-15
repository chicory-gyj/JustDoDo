#!/usr/bin/python
from random import randrange
n=input('How many dice?')
side=input('How many sides of each dice?')
sum=0
for i in range(n):
    sum+=randrange(side)+1
print 'The result is',sum
