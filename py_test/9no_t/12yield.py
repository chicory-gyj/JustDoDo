#!/usr/bin/python
def flatten(n):
    for sublist in n:
        for element in sublist:
            yield element

nested=[[1,2,3],[4,5],[6]]
print flatten(nested)
print list(flatten(nested))
