#!/usr/bin/python                        #  1 #  1
import fileinput                         #  2 #  2
for line in fileinput.input(inplace=True): #  3 #  3
   # line=line.rstrip()                   #  4 #  4
    num=fileinput.lineno()               #  5 #  5
    print '%-80s # %2i' % (line,num)     #  6 #  6
    print line
