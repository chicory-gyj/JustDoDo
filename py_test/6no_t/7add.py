#!/usr/bin/python
def add(x,y):
    return x+y
params=(1,3)
print add(*params)


def hello(greeting,name):
    print '%s,%s!' % (greeting,name)
pa={'greeting':'awsome','name':'Fabius'}
hello(**pa)
