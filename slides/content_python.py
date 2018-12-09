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

if __name__ == '__main__':
    main()


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


# Subprocess - overview
# Python 3.7 version of run()
subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None,
               capture_output=False, shell=False, cwd=None, timeout=None,
               check=False, encoding=None, errors=None, text=None, env=None,
               universal_newlines=None)


# Subprocess examples
import subprocess
subprocess.run(['ls', '-l'])

subprocess.run(['ls', '-l'], stdout=subprocess.DEVNULL)

proc = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
print(proc.stdout.decode())
print(proc.returncode)

proc = subprocess.run('ls -l', shell=True, stdout=subprocess.PIPE)
print(proc.stdout.decode())

# Subprocess - interacting
import subprocess
f = open('file_to_less.txt', 'r')
subprocess.run(['less'], stdin=f)

with open('file_to_less.txt', 'r') as f2:
    data = f2.read()
subprocess.run(['less'], input=data.encode())

with open('output.txt', 'w') as f:
    subprocess.run(['ls', '-l'], stdout=f, stderr=subprocess.STDOUT)


# Subprocess Popen - overview
class subprocess.Popen(args, bufsize=-1, executable=None, stdin=None,
                       stdout=None, stderr=None, preexec_fn=None,
                       close_fds=True, shell=False, cwd=None, env=None,
                       universal_newlines=None, startupinfo=None,
                       creationflags=0, restore_signals=True,
                       start_new_session=False, pass_fds=(), *, encoding=None,
                       errors=None, text=None)


# Subprocess Popen - examples
import subprocess
outfile = open('zip_results.txt', 'w')
fnames = b'file1.txt\nfile2.jpg\nfile3.html'
proc = subprocess.Popen(['zip', '--names-stdin', 'myzip'],
                        stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
(stdout, stderr) = proc.communicate(input=fnames)

import subprocess
outfile = open('zip_results.txt', 'w')
fnames = [b'file1.txt', b'file2.jpg', b'file3.html']
proc = subprocess.Popen(['zip', '--names-stdin', 'myzip'],
                        stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
for fname in fnames:
    proc.stdin.write(fname)
    proc.stdin.write(b'\n')
(stdout, stderr) = proc.communicate()


# Threading module example
import threading

def xyz():
    for i in range(10):
        print("thread")

if __name__ == "__main__":
    th = threading.Thread(target=xyz)
    th.start()
    for i in range(10):
        print("main")

# Threading module more interesting example
import threading
import time

def xyz():
    for i in range(10):
        print("thread")
        time.sleep(1.5)

if __name__ == "__main__":
    th = threading.Thread(target=xyz)
    th.start()
    for i in range(10):
        print("main")
        time.sleep(1)


# Threading module
import threading

def xyz(to_print=None):
    for i in range(10):
        print('Thread {}:{}'.format(i, to_print))

if __name__ == "__main__":
    th = threading.Thread(target=xyz, args=('printme',))
    th.start()
    for i in range(10):
        print('Main {}'.format(i))


# Threading module locks
import threading
mylock = threading.Lock()
with mylock:
    do_protected_stuff()

mylock.acquire()
do_protected_stuff()
mylock.release()


# multiprocessing example
import multiprocessing
import time

def xyz():
    for i in range(10):
        print("process")
        time.sleep(1.5)

if __name__ == '__main__':
    proc = multiprocessing.Process(target=xyz)
    proc.start()
    for i in range(10):
        print("main")
        time.sleep(1)


# command line arguments
import sys
for idx, arg in enumerate(sys.argv):
    print('arg {}: {}'.format(idx,arg)


# YAML in python
# create a python object from yaml txt
yml_txt = open('myfile.yml', 'r').read()
py_obj = yaml.load(yml_txt)

# serialize a python object to yaml txt
yml_txt = yaml.dump(py_obj)
open('myfile.yml', 'w').write(yml_txt)


# YAML Constructs in python
SoS = ['Mark McGwire', 'Sammy Sosa', 'Ken Griffey']

MStSq = {'american': ['Boston Red Sox', 'Detroit Tigers', 'New York Yankees'],
         'national': ['New York Mets', 'Chicago Cubs', 'Atlanta Braves']}

MStSc = {'hr': 65, 'avg': 0.278, 'rbi': 147}

SoM = [{'name': 'Mark McGwire', 'hr': 65, 'avg': 0.278},
       {'name': 'Sammy Sosa', 'hr': 63, 'avg':0.288}]
