#!/usr/bin/python
from subprocess import Popen,PIPE

text=open('messy1.html').read()
tidy=Popen('tidy',stdin=PIPE,stdout=PIPE,stderr=PIPE)
tidy.stdin.write(text)
tidy.stdin.close()

print tidy.stdout.read()
