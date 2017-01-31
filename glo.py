#!/usr/bin/python

def ff():
    #global x
    globals()['x']+=1
x=10
ff()
print x
