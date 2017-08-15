#!/usr/bin/python
__metaclass__=type
class Bird:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print 'Aaah..'
            self.hungry=False
        else:
            print 'No thanks'

class SongBird(Bird):
    def __init__(self):
        super(SongBird,self).__init__()
        self.sound='Squawk'
    def sing(self):
        print self.sound

bc=SongBird()
bc.sing()
bc.eat()
bc.eat()
