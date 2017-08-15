#!/usr/bin/python
try:
    x=input('enter the first number:')
    y=input('enter the second number:')
    print x/y
except (ZeroDivisionError,NameError,TypeError):
    print 'Your numbers were bogus...'
