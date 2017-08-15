#!/usr/bin/python
class MemberCounter:
    members=0
    def init(self):
        self.members+=1

m1=MemberCounter()
m1.init()
print m1.members
m2=MemberCounter()
m2.init()
print m2.members
print m1.members
MemberCounter.init(m1)
print MemberCounter.members
