#!/usr/bin/env python3


import dis


def myFunc():
    x = 1
    y = 2
    z = 'abc'  # noqa
    return x + y


print(myFunc.__name__)
print(myFunc.__code__.co_varnames)
print(myFunc.__code__.co_consts)
print(myFunc.__code__.co_code)

dis.disassemble(myFunc.__code__)
