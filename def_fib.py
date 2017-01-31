#!/usr/bin/python
def fibs(num):
    result=[0,1]
    for i in range(num-2):
        result.append(result[-1]+result[-2])
    return result
x=input('how many fib numbers do you want?')
print fibs(x)
