#!/usr/bin/python
try:
    x=input('fisrt:')
    y=input('second')
    print x/y
except (ZeroDivisionError,TypeError,SyntaxError),e:
    print e
