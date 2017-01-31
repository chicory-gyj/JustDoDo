#!/usr/bin/python

def combine(par):
    print par+globals()['par']

par='chicory'

combine('fa')
