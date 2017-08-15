#!/usr/bin/python
def flatten(n):
    try:n + ''
    except TypeError:pass
    else:raise TypeError
    try:
        for sublist in n :
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield n

nex=[[1,2],[3,[[4],5]],6,7,[[[[8,9],10],11],12]]
print list(flatten(nex))
s=[['bar','foo'],['tomato',['butten']]]
print list(flatten(s))
