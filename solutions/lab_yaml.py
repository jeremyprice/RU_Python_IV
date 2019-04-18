#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_yaml` -- YAML Parsing
=========================================

LAB_YAML Learning Objective: Learn to parse a YAML file using the PyYAML library
                             and use the information.
::

 a. Load the data/widget.yaml file using the PyYAML library.

 b. Change the value for the width and height of the window element to be 1/2 their current value.
    Change the size of the text element to be 1/4 it's current value.
    Change the image alignment element to 'justified'.

 c. Save your updated object to widget_updated.yml using the PyYAML library.

"""
import yaml

# step a
with open('data/widget.yml', 'r') as widget:
    w_yaml = yaml.safe_load(widget)

# step b
w_yaml['widget']['window']['width'] = int(w_yaml['widget']['window']['width'] / 2)
w_yaml['widget']['window']['height'] = int(w_yaml['widget']['window']['height'] / 2)
w_yaml['widget']['text']['size'] = int(w_yaml['widget']['text']['size'] / 4)
w_yaml['widget']['image']['alignment'] = 'justified'

# step c
with open('widget_updated.yml', 'w') as widget:
    yaml.dump(w_yaml, widget, default_flow_style=False)
