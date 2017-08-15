#!/usr/bin/python
class Calculator:
    def calcu(self,exp):
        self.value=eval(exp)
    def talk(self):
        print 'HAHA,your value is',self.value

class Talker:
    def talk(self):
        print 'Hi,my value is',self.value

class TalkingCalculator(Talker,Calculator):
    pass

s=TalkingCalculator()
s.calcu('66*66/2')
s.talk()

print hasattr(s,'talk')
print hasattr(s,'fornd')

print getattr(s,'talk',None)
print getattr(s,'fornd',None)

print callable(getattr(s,'talk',None))
print callable(getattr(s,'fornd',None))

setattr(s,'name','Grumby')
print s.name

print s.__dict__
