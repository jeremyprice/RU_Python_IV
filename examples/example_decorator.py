#!/usr/bin/env python3

def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped


def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped


@make_bold
@make_italic
def hello():
    return "hello world"


print(hello())   # returns <b><i>hello world</i></b> with both decorators
