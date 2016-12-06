#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

:mod:`lab_decorators` --- Decorators practice
========================================

a. Create a decorator that times the function it wraps.  It should start the timer
   before the function starts, and stop it after the wrapped function returns.  Print the
   elapsed time.

An example of timing a function is as follows:
start_time = time.time()
do_something()
stop_time = time.time()
elapsed = stop_time - start_time
"""
import sys
import time


def function_timer(func):
    def inside(*args, **kwargs):
        start = time.time()
        retval = func(*args, **kwargs)
        stop = time.time()
        elapsed = stop - start
        print("Function {} took {} sec ({} msec)".format(func.__name__,
                                                         elapsed,
                                                         elapsed*1000.0))
        return retval
    return inside


@function_timer
def time_me(item):
    """time this function for various calls"""
    def is_prime(num):
        for j in range(2, num):
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
    for step in range(10):
        # run your decorated function instead
        time_me(nth)
    print(time_me.__closure__)
    print(time_me.__code__.co_freevars)
