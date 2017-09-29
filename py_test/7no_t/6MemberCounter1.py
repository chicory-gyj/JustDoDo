#!/usr/bin/python
class MemberCounter:
    members=0
    def init(self):
        MemberCounter.members+=1

m1=MemberCounter()
m1.init()
print MemberCounter.members
print m1.members
m2=MemberCounter()
m2.init()
print MemberCounter.members
print m2.members
print m1.members
m2.members='chicory'
print m2.members
print m1.members
