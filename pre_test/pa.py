#!/usr/bin/python

def para(x,y,z=3,*p,**f):
    print x,y,z
    print p
    print f

para(5,6,8,3,4,5,m=3,i='f',u='df')
