#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

:mod:`lab_decorators` --- Decorators practice
========================================

a. Create a decorator that times the function it wraps.  It should start the timer
   before the function starts, and stop it after the wrapped function returns.  Print the
   elapsed time.

An example of timing a function is as follows:
start_time = time.perf_counter()
do_something()
stop_time = time.perf_counter()
elapsed = stop_time - start_time
"""


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
    for step in range(10):
        # run your decorated function instead
        time_me(200)
