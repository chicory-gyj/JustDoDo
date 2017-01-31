#!/usr/bin/python

def search(sq,number,lower=0,upper=None):
    if upper is None:
        upper=len(sq)-1
    elif lower==upper:
        if number==sq[lower]:
            return lower
        else:
            print 'Can\' find it!'
    else:
        middel=(lower+upper)//2
        if number>sq[middel]:
            return search(sq,number,middel+1,upper)
        else:
            return search(sq,number,lower,middel)

my_num=[34,55,578,342,44,12,35,56]
my_num.sort()
number=input('enter the number you want to search:')
print search(my_num,number,0,len(my_num)-1)

