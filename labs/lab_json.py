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
