#!/bin/false

# these are code snippets for the slides
# they are put in here so we can get a nice screenshot with
# syntax highlighting


# Anatomy of a Python Module
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Line #1 = shebang
# Line #2 = encoding declaration

"""Docstrings"""
# Inline documentation

import module
import library

actual_code_here


# Objects and methods
i = 123
a.numerator
a.denominator
a.bit_length()


# Text, bytes, and Unicode in Python 3
s = 'abc123'
b = b'abc123'
b2 = s.encode() # encode string to bytes with default
s2 = b.decode() # decode bytes to string with default


# Tuple type
tup = (1, "a", 3)
tup = tuple()
tup = (1,) # Comma needed for single element
gen = (x**2 for x in range(1,4)) # Not a tuple!


# List type
lst = [1, "a", 3]
lst = list()
lst = [x for x in range(5)]


# Dictionary type
dic = {"a": 1}
dic = dict(a=1)
dic = {x: chr(x) for x in range(97, 107)}


# Set type
st = {1,2,2,3}
st = set([1,2,2,3])
st = {x for x in range(1,4)}


# Yield statement
def foo(bar=10):
    i = 1
    while i < bar:
        yield i
        i = i + 1

# With statement
with open("foo.txt", "r") as infile:
    all_txt = infile.read()


# Import statement
import sys
from random import randint, randrange


# Subprocess -  using it
import subprocess
subprocess.run(['ls', '-l'])
subprocess.run(['ls', '-l'], stdout=subprocess.DEVNULL)
proc = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
print(proc.stdout.decode())
print(proc.returncode)
proc = subprocess.run('ls -l', shell=True, stdout=subprocess.PIPE)
print(proc.stdout.decode())
