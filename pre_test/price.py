#!/usr/bin/python
width=input('Please enter width:')
price_width=10
item_width=width-price_width
header_f='%-*s%*s'
f='%-*s%*.2f'
print '='*width
print header_f % (item_width,'Item',price_width,'Price')
print '-'*width
print f % (item_width,'Apple',price_width,4.22)
print f % (item_width,'Banana',price_width,5.32)
print f % (item_width,'Pears',price_width,6.12)
print f % (item_width,'Prunes(4 lbs.)',price_width,10.12)
print '='*width

