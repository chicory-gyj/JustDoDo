#!/usr/bin/python
def multi(f):
    def multi_2(n):
        return f*n
    return multi_2

print multi(5)(6)

