#!/usr/bin/python
def combine(para):
    print para + globals()['para']

para='son'
combine('father')

x=10
def change_global():
    global x
    x+=10
change_global()
print x
