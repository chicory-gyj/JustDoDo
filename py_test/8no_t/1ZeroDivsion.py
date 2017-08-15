#!/usr/bin/python
try:
    x=input('the first number:')
    y=input('the second number:')
    print x/y
except ZeroDivisionError:
    print 'THe second number can not be zero!!!'
except TypeError:
    print 'That was not a number,was it?'
