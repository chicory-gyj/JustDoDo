#!/usr/bin/python
from urllib import urlopen
from BeautifulSoup import BeautifulSoup

text=urlopen('http://python.org/community/jobs').read()
soup=BeautifulSoup(text)

jobs=set()
#print soup('h3')
for header in soup('h3'):
    links=header('a','reference')
    if not links:continue
    link=links[0]
    jobs.add('%s (%s)' % (link.string,link['href']))
print '\n'.join(sorted(jobs))

