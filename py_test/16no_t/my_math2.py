#!/usr/bin/python
def product(x,y):
    if x==7 and y==9:
        return 'An insidious bug has surfaced!'
    else:
        return x*y

import unittest,my_math2
class ProductTestcase(unittest.TestCase):
    def testInteger(self):
        for x in xrange(-10,10):
            for y in xrange(-10,10):
                p=my_math2.product(x,y)
                self.failUnless(p==x*y,'Integer Multiplication failed')
    def testFloats(self):
        for x in xrange(-10,10):
            for y in xrange(-10,10):
                x=x/10.0
                y=y/10.0
                p=my_math2.product(x,y)
                self.failUnless(p==x*y,'Float multiplication failed')
if __name__=='__main__':
    unittest.main()


