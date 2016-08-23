#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""

:mod:`lab_decorators_with_parameters` --- Decorators with parameters practice
========================================

a. Modify the decorator you created in the lab_decorators.py to accept an argument
   that specifies whether to print the timing in seconds or milliseconds.  Make the
   default units seconds.

"""
import sys
import time


def function_timer_units(seconds=True):
    """ This function times another function and prints the elapsed time in
    seconds (seconds=True) or milliseconds (seconds=False)"""
    def function_timer(func):
        def inside(*args, **kwargs):
            start = time.time()
            retval = func(*args, **kwargs)
            stop = time.time()
            elapsed = stop - start
            if seconds:
                label = "sec"
                value = elapsed
            else:
                label = "msec"
                value = elapsed * 1000.0
            print "Function {} took {} {}".format(func.func_name,
                                                  value,
                                                  label)
            return retval
        return inside
    return function_timer


@function_timer_units()
def time_me(item):
    """time this function for various calls"""
    def is_prime(num):
        for j in xrange(2, num):
            if (num % j) == 0:
                return False
        return True

    index = 0
    check = 0
    while index < item:
        check += 1
        if is_prime(check):
            index += 1
    return check

if __name__ == "__main__":
    if len(sys.argv) > 1:
        nth = int(sys.argv[1])
    else:
        nth = 1000
    for step in xrange(10):
        # run your decorated function instead
        time_me(nth)
    print time_me.func_closure
    print time_me.func_code.co_freevars
