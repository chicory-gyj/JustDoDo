#!/usr/bin/python
class Filter:
    def init(self):
        self.block=[]
    def filter(self,seq):
        return [x for x in seq if x not in self.block]

class SPAMFilter(Filter):
    def init(self):
        self.block=['SPAM']


f=Filter()
f.init()
print f.filter([1,2,3])

s=SPAMFilter()
s.init()
print s.filter(['SPAM','SPAM','EGGS','CHEERS','SPAM'])

print issubclass(SPAMFilter,Filter)
print issubclass(Filter,SPAMFilter)

print SPAMFilter.__bases__
print Filter.__bases__

print isinstance(s,SPAMFilter)
print isinstance(s,Filter)
print isinstance(s,str)
print isinstance(s,list)
print isinstance(s,tuple)

print s.__class__
