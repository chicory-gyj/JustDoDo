#!/usr/bin/python
import fileinput,random
fortunes=list(fileinput.input())
print random.choice(fortunes)
