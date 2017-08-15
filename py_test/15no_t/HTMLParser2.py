#!/usr/bin/python
from urllib import urlopen
from HTMLParser import HTMLParser
text=urlopen('http://python.org/community/jobs').read()
parser=HTMLParser()
parser.handle_starttag(tag='li')
parser.feed(text)
print attrs
parser.close()
