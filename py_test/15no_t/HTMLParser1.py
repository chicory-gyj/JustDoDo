#!/usr/bin/python
from urllib import urlopen
from HTMLParser import HTMLParser

class Scraper(HTMLParser):
    in_li=False
    in_link=False
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if tag=='li':
            self.in_li=True
        if tag=='a' and 'href' in attrs:
            self.in_link=True
            self.chunks=[]
            self.url=attrs['href']

    def handle_data(self,data):
        if self.in_link:
            self.chunks.append(data)

    def handle_endtag(self,tag):
        if tag=='li':
            self.in_h3=False
        if tag=='a':
            if self.in_li and self.in_link:
                print '%s (%s)' % (''.join(self.chunks),self.url)
            self.in_link=False

text=urlopen('http://python.org/community/jobs').read()
parser=Scraper()
parser.feed(text)
parser.close()

