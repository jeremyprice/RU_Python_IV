#!/usr/bin/python3

"""
    Lab01_pyreview
"""


from argparse import ArgumentParser
from random import choice


parser = ArgumentParser("Patent database search engine")
parser.add_argument('-a', '--author', help="Last Name, First Name")
parser.add_argument('-p', '--patent_num', help="Patent Number")
parser.add_argument('-f', '--filing_date', help="Date of Filing")
args = parser.parse_args()

def find_by_author():
    """ Do nothing """
    print("Running find_by_author")

def find_by_filing_date():
    """ Do nothing """
    print("Running find_by_filing_date")

def find_by_patent_number():
    """ Do nothing """
    print("Runnning find_by_patent_number")

def test_db_load():
    funs = [find_by_author,
            find_by_filing_date,
            find_by_patent_number]
    while True:
        yield choice(funs)

if __name__ == "__main__":
    next(test_db_load())()

