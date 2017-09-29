#!/usr/bin/python
import sys,re
from util import *
print '<html><head><title>...</title><body>'
title=True
for block in blocks(sys.stdin):
    block=re.sub(r'\*(.+?)\*',r'<i>\1</i>',block)
    if title:
        print '<h1>'
        print block
        print '</h1>'
        title=False
    else:
        print '<p>'
        print block
        print '</p>'
print '</body></html>'
