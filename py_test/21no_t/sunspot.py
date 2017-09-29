#!/usr/bin/python
from urllib import urlopen
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF

URL='/Users/gaoyajie/github/JustDoDo/py_test/21no_t/s.txt'
COMMENT_CHARS='#:'

drawing=Drawing(400,200)
data=[]
for line in open(URL).readlines():
    if not line.isspace() and not line[0] in COMMENT_CHARS:
        data.append([float(n) for n in line.split()])

pred=[row[5] for row in data]
high=[row[6] for row in data]
low=[row[7] for row in data]
times=[row[0]+row[1]/12.0 for row in data]

lp=LinePlot()
lp.x=20
lp.y=20
lp.height=125
lp.width=300
lp.data=[zip(times,pred),zip(times,high),zip(times,low)]
lp.lines[0].strokeColor=colors.blue
lp.lines[1].strokeColor=colors.red
lp.lines[2].strokeColor=colors.greenyellow

drawing.add(lp)
drawing.add(String(250,150,'SunSpot',fontSize=14,fillColor=colors.darkblue))

renderPDF.drawToFile(drawing,'report3.pdf','Sunspots')