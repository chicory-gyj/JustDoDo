#!/usr/bin/python

class Calc:
    buf=False
    def calculate(self,expression):
        try:
            return eval(expression)
        except ZeroDivisionError:
            if self.buf:
                print 'Division by zero is illage'
            else:
                raise

m=Calc()
m.buf=True
print m.calculate('1/0')
exp=input('enter the exp:')
print m.calculate('exp')

