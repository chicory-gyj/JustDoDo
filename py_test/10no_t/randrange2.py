#!/usr/bin/python
from random import shuffle
value=range(1,11)+'Jack Queue King'.split()
people='Chicory Fabius Bob Anne'.split()
shuffle(value)
#while value:
    for p in people:
        print '%s to %s' % (value.pop(),p)
