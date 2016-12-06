#!/usr/bin/env python3
import string


def make_boring(fn):
    def wrapped(var):
        return fn(var.strip(string.punctuation).lower())
    return wrapped


@make_boring
def print_me(var):
    print(var)


print_me("HELLO WORLD!!!!!")   # returns "hello world"
