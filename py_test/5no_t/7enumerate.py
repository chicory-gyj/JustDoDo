#!/usr/bin/python
strings=['we','are','in','a','team','we','are','brave']
for index,string in enumerate(strings):
    if 'we' in string:
        strings[index]='You'
        print strings
