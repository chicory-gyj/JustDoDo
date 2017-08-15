#!/usr/bin/python
try:
    1/0
except NameError:
    print 'Wrong'
else:
    print 'Go well'
finally:
    print 'Cleanig up'
