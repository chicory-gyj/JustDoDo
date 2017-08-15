#!/usr/bin/python
x=None
y=None
try:
    x=input('enter the fisrt number:')
    y=input('enter the second number:')
    print x/y
except Exception,e:
    print e
finally:
    print 'clean up...'
    del x
