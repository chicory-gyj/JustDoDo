#!/usr/bin/python
def doctor(patient='Chicory',hour=20,minute=15,day=30,month=2,year=2017):
    print '%s is going to see the doctor at the time of %d %d %d %d %d' % (patient,minute,hour,day,month,year)
doctor()
doctor('Anee')
doctor('Bob',day=17,month=7,hour=19,minute=27)
