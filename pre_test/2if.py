#!/usr/bin/python
name=raw_input('please enter the name:')
if name.endswith('Chicory'):
    if name.startswith('Mr.'):
        print 'hello,Mr. Chicory'
    elif name.startswith('Mrs.'):
        print 'hello,Mrs. Chicory'
    else:
        print 'hello, Chicory'
else:
    print 'hello,stranger'
