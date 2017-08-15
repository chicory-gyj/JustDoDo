#!/usr/bin/python
class Member:
    member=0
    def init(self):
        Member.member+=1
m1=Member()
m1.init()
print Member.member
print m1.member

m2=Member()
m2.init()
print Member.member
print m2.member

print m1.member

m1.member=5
print m1.member
print m2.member
