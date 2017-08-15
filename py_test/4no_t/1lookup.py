#!/usr/bin/python
people={'Chicory':{'phone':'1615','addr':'SH'},'Fabius':{'phone':'8931','addr':'SH2'},'GaoChun':{'phone':'0825','addr':'JS'}}
fin=raw_input('enter the name you want to know:')
info=raw_input('enter the information you want to know(phone or addr):')
if fin in people:print '%s\'s %s is %s' % (fin,info,people[fin][info])
else:print 'no find!'
