#!/usr/bin/python
def repeater(value):
    new=(yield value)
    if new is not None:value=new

m=repeater(42)
#print m
print m.next()
print m.send('haha')
