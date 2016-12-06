#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

:mod:`lab_unittest` --- Module unittest
========================================

a. Create a series of unittest tests to verify the classes below.  Create the following tests:
  1. verify exceptions are generated as expected (for invalid shapes)
  2. verify that calculations are done correctly for the shape type
  3. verify names are set as expected
  4. test all the things!

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
        self.center = (0.0, 0.0)
        self.radius = 1.0

    def area(self):
        return math.pi * self.radius**2

    def circumference(self):
        return math.pi * self.radius * 2.0

    def perimeter(self):
        return self.circumference()


class square(shape):
    def __init__(self):
        self.name = "square"
        self.position = (0.0, 0.0)
        self.side = 1.0

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4
