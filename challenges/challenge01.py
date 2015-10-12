#!/usr/bin/env python2

# Misusing expressions as defaults for function arguments

# What is wrong with the following function?

def foo(bar=[]):
    bar.append('baz')
    return bar

# Try it out to see what is happening:
print "First run"
print foo()
print "Second run"
print foo()
print "Third run"
print foo()












# answer:
# The new list, which is the default value for the argument, gets created at
# when the code is defined/compiled, not when the function is executed.
# A common way to fix this is:
def foo_fixed(bar=None):
    if bar is None:
        bar = []
    bar.append('baz')
    return bar
