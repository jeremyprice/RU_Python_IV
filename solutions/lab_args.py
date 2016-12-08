#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_args` -- Arguing with the functions
=========================================

LAB_ARGS Learning Objective: Learn to modify, receive, and work with arguments to function.
::

 a. Create a function that accepts any number of positional arguments and
    keyword arguments and prints the argument values out to the screen.

 b. Create a function that takes in any number of positional arguments, turns
    those arguments into keyword arguments using "arg#" for the keyword names,
    and calls the print function you wrote in a.

 c. Write a validation function that takes in a variable number of positional
    arguments.  Validate that all the arguments passed in are integers and are
    greater than 0.  If the arguments validate, call the print function, if an
    argument doesn't validate raise a ValueError.

"""


def print_args(*args, **kwargs):
    if len(args) > 0:
        print("Positional arguments")
        for (i, arg) in enumerate(args):
            print("{}: {}".format(i, arg))
    else:
        print("No Positional arguments")
    if len(kwargs) > 0:
        print("Keyword arguments")
        for (key, val) in kwargs.items():
            print("{}: {}".format(key, val))
    else:
        print("No Keyword arguments")


print("Part a.")
print_args(1, 2, 3)
print_args(a='1', b=2)


def args_to_kwargs(*args):
    kwargs = {}
    for (i, arg) in enumerate(args):
        kwargs["arg{}".format(i)] = arg
    print_args(**kwargs)


print("Part b.")
args_to_kwargs(1, "a", 3, "xyz")
args_to_kwargs("bob")


def validate(*args):
    for arg in args:
        if not issubclass(arg, int):
            raise ValueError("All arguments must be Integers")
        if arg <= 0:
            raise ValueError("All arguments must be > 0")
    print_args(*args)


print("Part c.")
validate(1, 2, 3)
try:
    validate(3, -1)
except ValueError as e:
    print(e)
try:
    validate("1")
except ValueError as e:
    print(e)
