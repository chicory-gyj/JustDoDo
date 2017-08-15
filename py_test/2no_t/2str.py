#!/usr/bin/python
sentence=raw_input('input the sentence you want:')
sc_width=80
se_width=len(sentence)
box_width=30
mar_width=(sc_width-se_width)//2
print '-'*sc_width
print ' '*mar_width+'|'+sentence+'|'
print '_'*sc_width
