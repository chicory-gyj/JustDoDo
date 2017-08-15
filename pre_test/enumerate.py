#!/usr/bin/python
g=['chicory','fabius','pagge']
t=enumerate(g)
#print list(t)
for index,string in list(t):
    if 'chicory' in string:
        print t
        print list(t)
        g[index]='[gyj]'
        print g
        print list(t)
