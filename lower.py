#!/usr/bin/python
name=raw_input('Please enter your name:')
names=['chicory','fabius','page']
if name.lower()|| name.strip() in names: print 'Yes,you are'
if name.lower() not in names: print 'no,you are not'
