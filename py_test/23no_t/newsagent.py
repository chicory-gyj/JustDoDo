#!/usr/bin/python

from nntplib import NNTP
from time import localtime,strftime,time
from email import message_from_string
from urllib import urlopen
import textwrap
import re

day=24*60*60
def wrap(string,max=70):
    return '\n'.join(textwrap.wrap(string))+'\n'

class NewsAgent:
    def __init__(self):
        self.sources=[]
        self.destinations=[]

    def addSource(self,source):
        self.sources.append(source)
    def addDestination(self,dest):
        self.destinations.append(dest)
    def distribute(self):
        items=[]
        for source in self.sources:
            items.extend(source.getItems())
        for dest in self.destinations:
            dest.receiveItems(items)

class NewsItem:
    def __int__(self):
        self.title=title
        self.body=body

class NNTPSource:
    def __int__(self,servername,group,window):
        self.servername=servername
        self.group=group
        self.window=window

    def getItems(self):
        start=localtime(time()-self.window*day)
        date=strftime('%y%m%d',start)
        hour=strftime('%H%M%S',start)

        server=NNTP(self.servername)
        ids=server.newnews(self.group,date,hour)[1]

        for id in ids:
            lines=server.article(id)[3]
            message=message_from_string('\n'.join(lines))

            title=message['subject']
            body=message.get_payload()
            if message.is_multipart():
                body=body[0]
            yield NewsItem(title,body)

        server.quit()

class SimpleWebSource:
    def __int__(self,url,titlePattern,bodyPattern):
        self.url=url
        self.titlePattern=re.compile(titlePattern)
        self.bodyPattern=re.compile(bodyPattern)
    def getItems(self):
        text=urlopen(self.url).read()
        titles=self.titlePattern.findall(text)
        bodies=self.bodyPattern.findall(text)
        for title,body in zip(titles,bodies):
            yield NewsItem(title,wrap(body))

class PlainDestination:
    def receiveItems(self,items):
        for item in items:
            print item.title
            print '-'*len(item.title)
            print item.body

class HTMLDestination:
    def __int__(self,filename):
        self.filename=filename
    def receiveItems(self,items):
        out=open(self.filename,'w')
        print >>out,"""<html>
        <head>
          <title>Today's News</title>
        </head>
        <body>
        <h1>Hi,Today's News</h1>"""

        print >>out,'<ul>'
        id=0
        for item in items:
            id+=1
            print >>out,'<li><a href="#%i">%s</a></li>' % (id,item.title)
        print >>out,'</ul>'

        id=0
        for item in items:
            id+=1
            print >>out,'<h2><a name="%i">%s</a></h2>' % (id,item.title)
            print >>out,'<pre>%s</pre>' % item.body

        print >>out,"""</body></html>"""
def runDefaultSetup():
    agent=NewsAgent()
    #bbc_url='http://news.bbc.co.uk/text_only.stm'
    #bbc_title=r'(?s)a href="[^"]*">\s*<b>\s*(.*?)\s*</b>'
    #bbc_body=r'(?s)</a>\s*<br />\s*(.*?)\s*<'
    #bbc=SimpleWebSource(bbc_url,bbc_title,bbc_body)
    #agent.addSource(bbc)

    clpa=NNTPSource()
    clpa.servername='web.aioe.org'
    clpa.group='comp.lang.python'
    clpa.window=1
    agent.addSource(clpa)

    #clpa_server='web.aioe.org'
    #clpa_group='comp.lang.python.announce'
    #clpa_window=1
    #clpa=NNTPSource(clpa_server,clpa_group,clpa_window)
    #agent.addSource(clpa)

    agent.addDestination(PlainDestination())
    #agent.addDestination(HTMLDestination('news.html'))
    handler=HTMLDestination()
    handler.filename='news.html'
    agent.addDestination(handler)
    agent.distribute()
if __name__=='__main__':
    runDefaultSetup()