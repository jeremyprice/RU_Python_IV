#!/usr/bin/python3

"""
    Lab04 - DB-API
"""

from pprint import pformat

from mysql.connector import connect
from mysql.connector.errors import ProgrammingError

class DefineDBError(Exception):
    pass

class PatentData(object):
    """ Patent Data Template """

    def __init__(self,
                 first_name=None,
                 last_name=None,
                 patent_number=None,
                 filing_date=None):
        self.first_name = first_name
        self.last_name = last_name
        self.patent_number = patent_number
        self.filing_date = filing_date
        return

    def get_patent_dict(self):
        """ Returns patent's details in dictionary form """
        return {"first_name":    self.first_name,
                "last_name":     self.last_name,
                "patent_number": self.patent_number,
                "filing_date":   self.filing_date}

class PatentDB(object):
    """ Class for interaction with Patent DB """

    def __init__(self,
                 username="admin",
                 password=None,
                 hostname="localhost",
                 database="patents"):
        self.username = username
        self.password = password
        self.hostname = hostname
        self.database = database

    def _query(self, query, commit=False):

        try:
            conn = connect(user=self.username, passwd=self.password,
                           host=self.hostname, database=self.database)
        except ProgrammingError:
            conn = connect(user=self.username, passwd=self.password,
                           host=self.hostname)
        cursor = conn.cursor()
        if isinstance(query, str):
            cursor.execute(query)
        else:
            cursor.execute(*query)
        if commit:
            result = conn.commit()
        else:
            result = cursor.fetchall()

        return result

    def define_db(self):
        """ Primes database for data entry. Drops if already exists. """

        try:
            print("Dropping old database {}, if it exists.".format(self.database))
            self._query("drop database if exists {}".format(self.database), commit=True)

            print("Creating database {}.".format(self.database))
            self._query("create database {}".format(self.database), commit=True)

            print('Creating table "authors" with default field names.')
            self._query("create table authors (firstname varchar(255) null, "
                                              "lastname  varchar(255) null, "
                                              "patentnumber varchar(255) null, "
                                              "filingdate date null)", commit=True)

            print("Initialization complete:")
            data = self._query("describe authors")
            print("Describe Authors Table:\n{}".format(pformat(data)))

        except Exception as e:
            raise DefineDBError(e)

        return

    def find_by_filing_date(self, filing_date):
        """ Find data based on filing date """

        query = ("select firstname, lastname, patentnumber, filingdate"
                 "from authors where filingdate = %s", (filing_date,))

        return self._query(query)

    def find_by_last_name(self, last_name):
        """ Find data based on patent author """

        query = ("select firstname, lastname, patentnumber, filingdate "
                 "from authors where lastname = %s", (last_name,))

        return self._query(query)

    def find_by_patent_number(self, patent_number):
        """ Find data based on patent number """

        query = ("select firstname, lastname, patentnumber, filingdate "
                 "from authors where patentnumber = %s", (patent_number,))

        return self._query(query)

    def load_db(self, patent_data):
        """ Load data into database """

        print("Starting to load patent_data into the authors database...")
        for patent in patent_data:
            query = ("insert into authors values (%s, %s, %s, %s)",
                     (patent["first_name"],
                      patent["last_name"],
                      patent["patent_number"],
                      patent["filing_date"]))
            try:
                self._query(query, commit=True)
            except Exception as e:
                raise LoadError(e.args)
        print("Loading of data complete.")

        return

class PatentNotFoundError(Exception):
    pass

class LoadError(Exception):
    pass

def load_patent_data(filename):
    patent_data = list()

    re_patent_start = re.compile(r"<PATDOC.+")
    re_patent_stop = re.compile(r"</PATDOC.+")
    re_patent_first_name = re.compile(r"<NAM><FNM><PDAT>\s*(\w+)\s*.+")
    re_patent_last_name = re.compile(r"<NAM><SNM><STEXT><PDAT>\s*(\w+)\s*.+")
    # NEED TO FIX
    re_patent_number = re.compile(r"<DATE><PDAT>\s*(.+)\s*</PDAT.+")
    re_patent_filing_date = re.compile(r"<DATE><PDAT>\s*(.*)\s*</PDAT.+")

    with open(filename, "r") as patent_file:
        for line in patent_file:
            if re_patent_start.match(line):
                patent = PatentData()
            elif re_patent_stop.match(line):
                patent_data.append(patent.get_patent_dict())
            else:
                match = re_patent_first_name.match(line)
                if match:
                    patent.first_name = match.group(1) or None
                    continue
                
                match = re_patent_last_name.match(line)
                if match:
                    patent.last_name = match.group(1) or None
                    continue

                match = re_patent_number.match(line)
                if match:
                    patent.patent_number = match.group(1) or None

                match = re_patent_filing_date.match(line)
                if match:
                    patent.filing_date = match.group(1) or None

    return patent_data


if __name__ == "__main__":
    from argparse import ArgumentParser
    from getpass import getpass
    from pprint import pprint
    import re
    from sys import exit

    parser = ArgumentParser()
    parser.add_argument("-u", "--username",
                        help="Username for DB access", 
                        required=True)
    parser.add_argument("-s", "--server",
                        help="Hostname where database resides",
                        required=True)
    parser.add_argument("-d", "--database",
                        help="Database Name",
                        default="mytestdb")
    args = parser.parse_args()

    db_password = getpass("Enter the password: ")

    patent_db = PatentDB(username=args.username,
                         password=db_password,
                         hostname=args.server,
                         database=args.database)
    patent_db.define_db()
    patent_data = load_patent_data("../labs/patent_data.sgm")
    patent_db.load_db(patent_data)

    pprint(patent_db.find_by_patent_number(20010100))
