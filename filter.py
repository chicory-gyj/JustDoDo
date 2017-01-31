#!/usr/bin/python
class Filter:
    def init(self):
        self.block=[]
    def filter(self,seq):
        return [x for x in seq if x not in self.block]
class sonFilter(Filter):
    def init(self):
        self.block=['son','mother']

m=Filter()
m.init()
m.filter([1,4,6])

n=sonFilter()
n.init()
print n.filter(['son','daugther','mother','father'])
print issubclass(sonFilter,Filter)
print issubclass(Filter,sonFilter)
print sonFilter.__bases__
print Filter.__bases__

print isinstance(m,Filter)
print isinstance(m,type)
print m.__class__
print n.__class__
