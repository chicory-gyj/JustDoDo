#!/usr/bin/python

try:
    x=input('enter the first number:')
    y=input('enter the second number:')
    print x/y
except (ZeroDivisionError,TypeError,NameError),e:
    print e
print 'ddd'

try:
    x=input('enter the first number:')
    y=input('enter the second number:')
    print x/y
except:
    print 'Someting must be wrong'
