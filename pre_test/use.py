#!/usr/bin/python
date=[['susan','113'],['smith','1122'],['fabius','2233'],['chicory','3344']]
name=raw_input('enter the name:')
pin=raw_input('enter the pin:')
if [name,pin] in date: print 'yeah'
else: print 'no'
