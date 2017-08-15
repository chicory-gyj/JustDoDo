#!/usr/bin/python
class MuffledCalculator:
    muffled=False
    def calc(self,expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print 'Division by zero is illage!'
            else:
                raise

c=MuffledCalculator()
print c.calc('6*7')
c.muffled=True
c.calc('10/0')

