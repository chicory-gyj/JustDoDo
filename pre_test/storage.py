#!/usr/bin/python
def init(date):
    date['first']={}
    date['second']={}
    date['last']={}

def lookup(date,label,name):
    return date[label].get(name)

def store(date,full_name):
    names=full_name.split()
    if len(names)==2:
        names.insert(1,'')
    labels='first','second','last'
    for label,name in zip(labels,names):
        people=lookup(date,label,name)
        if people:
            people.append(full_name)
        else:
            date[label][name]=[full_name]

my_name={}
init(my_name)

NAME='me'
while NAME:
    NAME=raw_input('enter the name which need to store:')
    store(my_name,NAME)

lab=input('enter the label(1,2 or 3):')
if lab==1: 
    label='first'
elif lab==2:
    label='second'
else:
    label='last'

print my_name
name=raw_input('the name you want to lookup:')
print lookup(my_name,label,name)
