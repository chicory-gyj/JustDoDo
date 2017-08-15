#!/usr/bin/python
scope={}
exec 'x=10' in scope
print eval('x*x',scope)

