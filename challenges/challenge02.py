#!/usr/bin/env python2

# Using class variables incorrectly

# What do you expect in the print statements below?


class A(object):
    x = 1  # class variable


class B(A):
    pass


class C(A):
    pass


print(A.x, B.x, C.x)

B.x = 2
print(A.x, B.x, C.x)

A.x = 3
print(A.x, B.x, C.x)

#
#
#
#
#
#
#
#
#
#
#
#
# answer:
# The class variable x is looked up by Python in the dictionary of the
# subclass, and each superclass, until it is found.  In the case of the last
# line of the example code, class C doesn't have its own copy of x, so Python
# looks to class A for x.  Thus, when you change the base class value at
# runtime, it will change the value for all the subclasses that haven't
# changed it.
