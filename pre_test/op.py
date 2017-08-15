#!/usr/bin/python

def describePersion(person):
    print 'Description of ',person['name']
    print 'Age is ',person['age']
    try:
        print 'Occupation: '+person['occupation']
    except:
        pass
m={'name':'Chicory','age':'25','occupation':'engineer'}
describePersion(m)

n={'name':'Fabius','age':'29'}
describePersion(n)
