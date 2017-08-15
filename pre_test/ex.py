#!/usr/bin/python

while True:
    try:
        x=input('enter the first number:')
        y=input('enter the second number:')
        print x/y
    except Exception,e:
        print 'Invalid input,',e
        print 'Please try again.'
    else:
        break


