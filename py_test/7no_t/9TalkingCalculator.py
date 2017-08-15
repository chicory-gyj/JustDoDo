#!/usr/bin/python
class Calculator:
    def calcu(self,expression):
        self.value=eval(expression)

class Talker:
    def talk(self):
        print 'Hi my value is',self.value

class TalkingCalculator(Calculator,Talker):
    pass

s=TalkingCalculator()
s.calcu('78*12+9')
s.talk()
