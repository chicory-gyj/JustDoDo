#!/usr/bin/python
class Calc:
    def calc(self,expression):
        self.value=eval(expression)
   # def talking(self):
   #     print 'yes,the value is',self.value
class Talk:
    def talking(self):
        print 'hello,my value is ',self.value
class TalkingCalc(Calc,Talk):
    pass

m=TalkingCalc()
m.calc('1+3*5')
m.talking()

n=TalkingCalc()
n.calc('\'ff\'+\'dd\'')
n.talking()

print hasattr(n,'talking')
print hasattr(n,'dfs')

print callable(getattr(n,'talking',None))

setattr(n,'name','Mr Fabius')
print n.name
print hasattr(n,'name')

print getattr(n,'talking')
print getattr(n,'dfad',None)
print m.__dict__
print n.__dict__


print type(m)
print type('talking')

print dir(TalkingCalc)
