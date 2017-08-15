#!/usr/bin/python
while True:
    try:
        x=input('first:')
        y=input('second:')
        print x/y
    except Exception,e:
        print 'invalid input:',e
        print 'Please try again:'
    else:
        break
