#!/usr/bin/python
from nntplib import NNTP
from time import time,localtime,strftime
day=24*60*60
yesterday=localtime(time()-day)
date=strftime('%y%m%d',yesterday)
t=strftime('%H%M%S',yesterday)
s=NNTP('web.aioe.org')
g='comp.lang.python.announce'
ids=s.newnews(g,date,t)[1]

for id in ids:
    head=s.head(id)[3]
    for line in head:
        if line.lower().startswith('subject:'):
            subject=line[9:]
            break
    body=s.body(id)[3]

    print subject
    print '-'*len(subject)
    print '\n'.join(body)
s.quit()

