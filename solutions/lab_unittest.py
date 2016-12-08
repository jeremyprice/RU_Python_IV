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
import unittest


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


class TestAllThingsCircle(unittest.TestCase):
    def test_name(self):
        c = circle()
        self.assertEqual(c.name, "circle")

    def test_is_a_shape(self):
        self.assertTrue(issubclass(circle, shape))

    def test_circumference(self):
        c = circle()
        c.radius = 1.0
        expected = 6.28318530  # Pi * 2 * 1
        self.assertAlmostEqual(c.circumference(), expected)

    def test_perimeter(self):
        c = circle()
        c.radius = 1.0
        expected = 6.28318530  # Pi * 2 * 1
        self.assertAlmostEqual(c.perimeter(), expected)

    def test_area(self):
        c = circle()
        c.radius = 1.0
        expected = 3.14159265358  # Pi * 1 * 1
        self.assertAlmostEqual(c.area(), expected)


class TestAllThingsSquare(unittest.TestCase):
    def test_name(self):
        s = square()
        self.assertEqual(s.name, "square")

    def test_is_a_shape(self):
        self.assertTrue(issubclass(square, shape))

    def test_perimeter(self):
        s = square()
        s.side = 5.0
        expected = 20.0
        self.assertAlmostEqual(s.perimeter(), expected)

    def test_area(self):
        s = square()
        s.side = 5.0
        expected = 25.0
        self.assertAlmostEqual(s.area(), expected)


class TestAllThingsShape(unittest.TestCase):
    def test_name(self):
        sh = shape()
        self.assertEqual(sh.name, "generic shape")

    def test_perimeter_exception(self):
        sh = shape()
        with self.assertRaises(InvalidShape):
            sh.perimeter()

    def test_area_exception(self):
        sh = shape()
        with self.assertRaises(InvalidShape):
            sh.area()


if __name__ == "__main__":
    unittest.main()
