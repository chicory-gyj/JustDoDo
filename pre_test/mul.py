#!/usr/bin/python

def multi(fac):
    def multi_2(num):
        return fac*num
    return multi_2

sc=multi(2)
print sc(10)

ch=multi(15)
print ch(309)

print multi(3)(5)
