#!/usr/bin/python
import sys
text=sys.stdin.read()
words=text.split()
Count=len(words)
print 'Wordcount:',Count
