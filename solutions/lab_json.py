#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_json` -- JSON to YAML and back again
=========================================

LAB_JSON Learning Objective: Learn to navigate a JSON file and convert to a
                             python object.
::

 a. Create a script that expects 3 command line arguments: -j or -y, json_filename, yaml_filename
    The first argument is -j or -y based on whether to convert from JSON to YAML (-j) or
    YAML to JSON (-y)
    The second argument is the name of the json file to parse or save to
    The third argument is the name of the yaml file to parse or save to

 b. Based on the -y/-j selection, parse the contents of the input file using the appropriate
    library.

 c. Using the other library, save the parsed object to the output filename

 d. Test your script using the json and yml files in the data directory.

"""

import json
import yaml
import sys

if len(sys.argv) < 4:
    print('Usage: {} -j/-y <json_filename> <yaml_filename>'.format(sys.argv[0]))
    raise SystemExit(1)

option = sys.argv[1]
if option == '-j':
    json_to_yaml = True
elif option == '-y':
    json_to_yaml = False
else:
    print('Invalid option')
    print('Usage: {} -j/-y <json_filename> <yaml_filename>'.format(sys.argv[0]))
    raise SystemExit(1)

json_fname = sys.argv[2]
yaml_fname = sys.argv[3]

if json_to_yaml: # translate json to yaml
    with open(json_fname, 'r') as infile:
        json_obj = json.load(infile)
    with open(yaml_fname, 'w') as outfile:
        yaml.dump(json_obj, outfile, default_flow_style=False)
else: # translate yaml to json
    with open(yaml_fname, 'r') as infile, open(json_fname, 'w') as outfile:
        yaml_obj = yaml.load(infile)
        json.dump(yaml_obj, outfile)
