#!/usr/bin/env python3


class myInt():
    def __init__(self):
        self.value = 0

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


x = myInt()
print(x, id(x))

x_t = (x, x)
print(x_t, id(x_t), id(x_t[0]), id(x_t[1]))

x_t[0] = 999  # exception!

x.value = 999
print(x, id(x))
print(x_t, id(x_t), id(x_t[0]), id(x_t[1]))
