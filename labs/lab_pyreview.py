#!/usr/bin/env python
#!*-* coding:utf-8 *-*

"""

:mod:`lab_pyreview` -- Python review
=========================================

LAB PyReview Learning Objective: Familiarization with argparse and parsing command line arguments.

a. Review argparse module documentation

b. Build an ArgumentParser object using the following parameters:
   description: "Patent database search engine"

c. Add support for the following arguments and argument attributes:
   -a --author last first
   -p --patent_num
   -f --filing_date

d. Run parse_args() to build arguments objects and print the Namespace

e. Construct a generator called test_db_load() that returns a random function from a list of functions.
   The list will support find_by_author(), find_by_patent_number(), and find_by_filing date()
   Test your generator with stub functions. (HINT: random is a module)

"""
