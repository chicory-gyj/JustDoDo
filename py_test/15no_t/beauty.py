#!/usr/bin/python
from urllib import urlopen
from BeautifulSoup import BeautifulSoup

#text=urlopen('http://python.org/community/jobs').read()
#soup=BeautifulSoup(text)

text=open('messy.html').read()
soup=BeautifulSoup(text)
print text
print 'x'*50
print soup

