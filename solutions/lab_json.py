#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_json` -- JSON Navigation
=========================================

LAB_JSON Learning Objective: Learn to navigate a JSON file and convert to a
                             python object. Practice file IO using with.
::

 a. Load the data/widget.json file using the Python JSON library.

 b. Change the value for the width and height of the window element to be 1/2 their current value.
    Change the size of the text element to be 1/4 it's current value.
    Change the image alignment element to 'justified'.

 c. Save your updated object to widget_updated.json using Python's JSON library.

"""

import json
import sys

# step a
with open('data/widget.json', 'r') as widget:
    w_json = json.load(widget)

# step b
w_json['widget']['window']['width'] = int(w_json['widget']['window']['width'] / 2)
w_json['widget']['window']['height'] = int(w_json['widget']['window']['width'] / 2)
w_json['widget']['text']['size'] = int(w_json['widget']['text']['size'] / 4)
w_json['widget']['image']['alignment'] = 'justified'

# step c
with open('widget_updated.json', 'w') as widget:
    json.dump(w_json, widget, sort_keys=True, indent=4)
