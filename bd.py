#!/usr/bin/python
names=['chicory','fabius','page']
ages=['25','28','1']
# for i in range(len(names)):
#    print names[i],'is',ages[i],'years old'
for name,age in zip(names,ages):
    print name,'is',age,'years old'
