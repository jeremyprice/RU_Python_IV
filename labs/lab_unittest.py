#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""

:mod:`lab_unittest` --- Module unittest
========================================

a. Create a series of unittest tests to verify the classes below.

"""

import math
class InvalidShape(Exception):
    pass


class shape(object):
    def __init__(self):
        self.name = "generic shape"

    def area(self):
        raise InvalidShape

    def perimeter(self):
        raise InvalidShape


class circle(shape):
    def __init__(self):
        self.name = "circle"
        self.center = (0.0,0.0)
        self.radius = 1.0

    def area(self):
        return math.pi * r**2

    def circumference(self):
        return math.pi * r * 2.0

    def perimeter(self):
        return self.circumference()


class square(shape):
    def __init__(self):
        self.name = "square"
        self.position = (0.0,0.0)
        self.side = 1.0

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4
