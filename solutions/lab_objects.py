#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_objects` -- Objects in Python
=========================================

LAB Objects Learning Objective: Explore objects in Python and how everything in Python
                                is an object.

a. Fill in the series of functions below that determine the characteristics of an object.

b. Write a print_object_flags function that uses the is_* functions to find the characteristics
   of the passed in object and print the characteristics (flags).

"""


def is_callable(obj):
    """ returns True if the object is callable """
    return hasattr(obj, '__call__')


def is_with(obj):
    """ returns True if the object can be used in a "with" context """
    return hasattr(obj, '__enter__') and hasattr(obj, '__exit__')


def is_math(obj):
    """ returns True if the object supports +, -, /, and * """
    # __add__, ...
    retval = hasattr(obj, '__add__') and hasattr(obj, '__mul__') and \
        hasattr(obj, '__sub__') and hasattr(obj, '__truediv__')
    return retval


def is_iterable(obj):
    """ returns True if the object is iterable """
    # __iter__
    return hasattr(obj, '__iter__')


def print_object_flags(obj):
    """ assess the object for various characteristics and print them """
    if is_iterable(obj):
        print('ITERABLE', end=' ')
    if is_math(obj):
        print('MATH', end=' ')
    if is_with(obj):
        print('WITH', end=' ')
    if is_callable(obj):
        print('CALLABLE', end=' ')
    print()


if __name__ == "__main__":
    print_object_flags(1)
    print_object_flags("abc")
    print_object_flags(print_object_flags)
    print_object_flags([1, 2, 3])
    print_object_flags(open('test.file.deleteme', 'w'))
