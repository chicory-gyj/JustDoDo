#!/usr/bin/python
def square(x):
    '''
    square a number and returns the result

    square(2)
    4
    square(3)
    9
    '''
    return x*x

if __name__=='__main__':
    import doctest,my_math
    doctest.testmod(my_math)
