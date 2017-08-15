#!/usr/bin/python
while True:
    try:
        x=input('first:')
        y=input('second:')
        print x/y
    except :
        print 'Something wrong happened,please try again:'
    else:
        break
    finally:
        print 'hahah'


