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
i.numerator
i.denominator
i.bit_length()


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


# Python JSON
import json
obj = {'a':1, 'b':2}
j_str = json.dumps(obj)

with open('output.json', 'w') as outfile:
    json.dump(obj, outfile)

import json
j_str = '{"a": 1, "b": 2}'
obj = json.loads(j_str)

with open('output.json', 'r') as infile:
    obj = json.load(infile)


# Pickle and Shelve
import pickle
obj = {'a':1, 'b':2}
p_str = pickle.dumps(obj)

with open('output.pickle', 'wb') as outfile:
    pickle.dump(obj, outfile)

import pickle
p_str = b'\x80\x03}q\x00(X\x01\x00\x00\x00aq\x01K\x01X\x01\x00\x00\x00bq\x02K\x02u.'
obj = pickle.loads(p_str)

with open('output.pickle', 'rb') as infile:
    obj = pickle.load(infile)


# Shelve example
import shelve

obj1 = {'a':1, 'b':2}
obj2 = ['a', 1, 100]
with shelve.open('mydb') as db:
    db['mydict'] = obj1
    db['mylist'] = obj2

db = shelve.open('mydb')
mydict = db['mydict']
mylist = db['mylist']
db.close()


# urllib GET example
from urllib import request
import json
response = request.urlopen('https://httpbin.org/get')
txt = response.read().decode()
j_obj = json.loads(txt)
hdrs = response.getheaders()


# urllib POST example
from urllib import request, parse
import json
data = parse.urlencode({'param1': 1, 'param2': 'value', 'param3': 10000})
data = data.encode('ascii')
response = request.urlopen('https://httpbin.org/post', data=data)
txt = response.read().decode()
j_obj = json.loads(txt)


# urllib PUT example
from urllib import request, parse
import json
data = parse.urlencode({'param1': 1, 'param2': 'value', 'param3': 10000})
data = data.encode('ascii')
req = request.Request('https://httpbin.org/put', data=data, method='PUT')
response = request.urlopen(req)
txt = response.read().decode()
j_obj = json.loads(txt)


# urllib DELETE example
from urllib import request
import json
req = request.Request('https://httpbin.org/delete', method='DELETE')
response = request.urlopen(req)
txt = response.read().decode()
j_obj = json.loads(txt)


# Requests examples
import requests
response = requests.get("https://httpbin.org/get")
stat = response.status_code
hdrs = response.headers
txt = response.text
j_obj = response.json()

import requests
data = {'user': 'bob', 'pass': 'password'}
response = requests.post("https://httpbin.org/post", data=data)
j_obj = response.json()

import requests
data = {'user': 'bob', 'pass': 'password'}
response = requests.post("https://httpbin.org/post", json=data)
j_obj = response.json()


# more requests examples
import requests

r = requests.put('https://httpbin.org/put', data = {'key':'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')

headers = {'X-Auth-Token': '62c0e8d7305c4fd88d3772cde0d06d38'}
r = requests.get("https://httpbin.org/get", headers=headers)


# Minimal Flask Application
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run()


# Routes
dogs = ['Daisy', 'Sparky', 'Bo']
@app.route('/dogs')
def list_dogs():
    # return the full list of dogs
    return str(dogs)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User {}'.format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post {}'.format(post_id)


# Routes continued
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    if name is None:
        return "Hello what's-your-name"
    else:
        return "Hello {}".format(name)


# Templates
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


# Debug mode
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<h1>Hello world!</h1>'
if __name__ == '__main__':
    # either
    app.debug = True
    app.run()
    # or
    app.run(debug=True)


# Function arguments
def func(arg1, arg2, arg3='abc', arg4=123):
    pass


# Args
def argless(*args):
    print(args)

argless()
argless(1,2,3)

def twoargs(x, y, *args):
    print(x, y, args)

twoargs(1, 2, 3)
twoargs('a', 'b')


# Args unrolling
def subtract(x, y):
    return x - y

subtract(10, 5)
lst = [10, 5]
subtract(*lst)


# Kwargs
def kwargless(**kwargs):
    print(kwargs)
kwargless()
kwargless(x=1, y=2)

def subtract(x, y):
    return x - y
values = {'x': 10, 'y': 5}
subtract(**values)


# Since everything is just names bound to objects
import datetime
import importlib

print(datetime.datetime.now())
print(datetime.datetime.max, datetime.datetime.min)

class PartyTime():
    def __call__(self, *args):
        imp.reload(datetime)
        value = datetime.datetime(*args)
        datetime.datetime = self
        return value

    def __getattr__(self, value):
        if value == 'now':
            return lambda: print('Party Time!')
        else:
            importlib.reload(datetime)
            value = getattr(datetime.datetime, value)
            datetime.datetime = self
            return value

datetime.datetime = PartyTime()
print(datetime.datetime.now())
print(datetime.datetime.max, datetime.datetime.min)


# Mutable vs. Immutable

x = 'abc'
print(hex(id(x)))
x += 'def'
print(hex(id(x)))

y = 1.23
print(hex(id(y)))
y += 2.9
print(hex(id(y)))

z = ['abc']
print(hex(id(z)))
z.append(123)
print(hex(id(z)))


# Tuples are immutable, right?
class myInt():
    def __init__(self):
        self.value = 0
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return str(self.value)

x = myInt()
y = myInt()
print(x, hex(id(x)))
print(y, hex(id(y)))

x_tup = (x, y)
print(x_tup, hex(id(x_tup)), hex(id(x_tup[0])), hex(id(x_tup[1])))

try:
    x_tup[0] = 999  # exception!
except TypeError:
    print('Error as expected')

x.value = 999
print(x, hex(id(x)))
print(x_tup, hex(id(x_tup)), hex(id(x_tup[0])), hex(id(x_tup[1])))


# Mutable Lists
def list_widget(in_list):
    in_list[0] = 10

    in_list = list(range(1, 5))
    print(in_list)
    in_list[0] = 10
    print(in_list)

my_list = [9, 9, 9, 9]
list_widget(my_list)
print(my_list)


# Even functions are objects
import dis

def myFunc():
    x = 1
    y = 2
    z = 'abc'
    return x + y

print(myFunc.__name__)
print(myFunc.__code__.co_varnames)
print(myFunc.__code__.co_consts)
print(myFunc.__code__.co_code)

dis.disassemble(myFunc.__code__)


# Let's explore objects
class myobj:
    def __init__(self):
        self.y = 111
z = myobj()
# get all the attributes of an object
dir(z)

# get a specific attribute of an object
# equivalent to: obj.y
x = getattr(z, 'y')

# check if an object has an attribute named 'y'
hasattr(z, 'y')


# Decorators - we all know about functions
def func():
    return "hi"

print(func())


# Scope
info = "hello world"

def localonly():
    print(locals())

print(globals())
localonly()


# Scope (globals)
info = "hello world"

def localonly():
    print(info)

localonly()


# scope (global shadowing)
info = "hello world"

def localonly():
   info = "inside localonly"
   print(info)

localonly()
print(info)


# Lifetime of Identifiers
def localonly():
   info = "inside localonly"
   print(info)

localonly()
print(info)


# function parameters and args
def hello(arg1):
   print(locals())

hello(1)


# Function parameters and args
def hello(arg1, arg2=0):
   print(locals())

hello(1)
hello(1, 3)
hello()
hello(arg2=15, arg1=10)
hello(arg2=99)


# Nested functions
def outer():
    info = 1
    def inner():
        print(info)
    inner()

outer()


# functions are Objects
def func():
    pass

print(type(func))
print(func.__class__)
print(issubclass(func.__class__, object))


# treating functions like the Objects
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def do_math(operation, x, y):
    return operation(x, y)

print(do_math(sub, 10, 5))
print(do_math(add, 2, 2))


# what about those weird inner functions
def outer():
    def inner():
        print("inside the inner function")
    return inner

my_func = outer()
print(my_func)
print(my_func())


# Closures
def outside():
    info = 1
    def inside():
        print(info)
    return inside

my_func = outside()
my_func.__closure__
my_func()


# even function arguments work with Closures
def outside(arg1):
    def inside():
        print(arg1)
    return inside

my_func1 = outside(123)
my_func2 = outside('xyz')
my_func1()
my_func2()


# decorators (finally!)
def wrapper(passed_in_func):
    def inside():
        print("before passed_in_func")
        retval = passed_in_func()
        return retval + 1
    return inside

def constant():
    return 2

decorated = wrapper(constant)
decorated()


# what can decorators do?
def add_two_numbers(x, y):
    return x + y

def ensure_positivity(func):
    def inner(x, y):
        return func(abs(x), abs(y))
    return inner

add_two_numbers(-10, 10)
add_two_numbers = ensure_positivity(add_two_numbers)
add_two_numbers(-10, 10)


# Decorator syntax
def ensure_positivity(func):
    def inner(x, y):
        return func(abs(x), abs(y))
    return inner

@ensure_positivity
def add_two_numbers(x, y):
    return x + y

add_two_numbers(-10, 10)


# Args and Kwargs in decorators
def debug_call(func):
    def inner(*args, **kwargs):
        print("{} called with {} {}".format(func.func_name, args, kwargs))
        return func(*args, **kwargs)
    return inner

@debug_call
def add(x, y=0):
    return x + y

print(add(1, 2))
print(add(y=3, x=5))
print(add(5))


# who are you really?
def ensure_positivity(func):
    def inner(x, y):
        return func(abs(x), abs(y))
    return inner

@ensure_positivity
def add_two_numbers(x, y):
    return x + y

print(add_two_numbers)
print(add_two_numbers.__name__)
help(add_two_numbers)
print(add_two_numbers.__closure__[0].cell_contents.__name__)


# Better debug function args
def debug(func):
    """Print the function signature and return value"""
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print("Calling {}({})".format(func.__name__, signature))
        value = func(*args, **kwargs)
        print("{!r} returned {!r}".format(func.__name__, value))           # 4
        return value
    return wrapper_debug

@debug
def add_two_numbers(x, y):
    return x + y

add_two_numbers(5, 10)
add_two_numbers(x=7, y=16)


# plugin decorator example
import random
PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return "Hello {}".format(name)

@register
def be_awesome(name):
    return "Yo {}, together we are the awesomest!".format(name)

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print("Using {!r}".format(greeter))
    return greeter_func(name)

print(randomly_greet('Jeremy'))
print(randomly_greet('Not Jeremy'))


# walk down memory lane...
@debug_call
def add(x, y=0):
    return x + y

# translates into:
add = debug_call(add)


# Decorators with parameters return ???
@decorator_with_args(arg)
def foo(*args, **kwargs):
    pass

# translates into:
foo = decorator_with_args(arg)(foo)


# Decorator with parameter
def debug_call(enabled=True):
    def real_debug_call(func):
        def inner(*args, **kwargs):
            if enabled:
                print("{} called with {} {}".format(func.__name__,
                                                    args,
                                                    kwargs))
            return func(*args, **kwargs)
        return inner
    return real_debug_call

@debug_call()
def add(x, y=0):
    return x + y

@debug_call(enabled=False)
def sub(x, y):
    return x - y

print(add(1, 2))
print(sub(3, 4))
