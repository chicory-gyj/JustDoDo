#!/usr/bin/python
from ConfigParser import ConfigParser
CONFIGFILE='python.txt'

config=ConfigParser()
config.read(CONFIGFILE)

print config.get('messages','greeting')
radius=input(config.get('messages','question')+' ')
print config.get('messages','result_message'),
print config.getfloat('numbers','pi')*radius**2
