#!/usr/bin/python
def search(seq,number,lower=0,upper=None):
    if upper is None:
        upper=len(seq)-1
    if upper==lower:
        assert seq[upper]==number
        return upper
    else:
        middle=(lower+upper)//2
        if number > seq[middle]:
            return search(seq,number,middle+1,upper)
        else:
            return search(seq,number,lower,middle)

print search(range(2,100,4),18)
