#!/usr/bin/python
username=[['Fabius','7818'],['Chicory','4456'],['Smith','6677']]
name=raw_input('enter the name:')
number=raw_input('enter the number:')
if [name,number] in username: print 'Find it!'+name+' '+number
else:print 'not find!'
