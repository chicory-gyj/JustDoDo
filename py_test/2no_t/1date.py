#!/usr/bin/python
months=['January','February','March','April','May','June','July','Auguest','September','October','November','December']
ending=['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']
year=raw_input('the year is:')
month=input('the month is(1~12):')
day=input('the day is(1~31):')
M=months[month-1]
date=`day`+ending[day-1]+' '+M+','+year
print date
