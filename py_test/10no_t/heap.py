#!/usr/bin/python
from heapq import *
from random import shuffle
date=range(10)
#shuffle(date)
heap=[]
for n in date:
    heappush(heap,n)
print heap
heappush(heap,0.5)
print heap
print heappop(heap)
print heap
print heappop(heap)
print heap
