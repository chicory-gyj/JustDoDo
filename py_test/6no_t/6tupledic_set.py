#!/usr/bin/python
def print_params(*params):
    print params
print_params(33,45,'dd')

def print_params_1(x,y,z=3,*foryou,**forme):
    print x,y,z
    print foryou
    print forme
print_params_1(19,20,21,5,4,5,4,4,5,fl=89,bar=34)
