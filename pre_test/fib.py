#!/usr/bin/python
fibs=[0,1]
i=input('how many fibonacci numbers do you want?')
for n in range(i-2):
    fibs.append(fibs[-1]+fibs[-2])
print fibs
