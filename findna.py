#!/usr/bin/python
people={'Alice':{'phone':'1123','addr':'guangnan'},'Chicory':{'phone':'4456','addr':'jianchuan'},'Fabius':{'phone':'7810','addr':'minhang'}}
labels={'phone':'phonenumber','addr':'address'}
name=raw_input('Please enter your name:')
request=raw_input('Phonenumber(p) or address(a)?')
if request=='p': key='phone'
if request=='a': key='addr'
NAME=people.get(name,{})
LABELS=labels.get(key,request)
PEOPLE=people[name].get(key,'not availabe')
if name in people: print '%-s\'s %s is %s' % (name,LABELS,PEOPLE)
                                                    
                                                    
