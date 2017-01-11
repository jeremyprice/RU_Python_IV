#!/usr/bin/env python3

import yaml
import sys

with open(sys.argv[1], 'r') as infile:
    txt = infile.read()

for doc in yaml.load_all(txt):
    print(doc)
