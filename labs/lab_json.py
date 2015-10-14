#!/usr/bin/env python
#!*-* coding:utf-8 *-*

"""

:mod:`lab_json` -- JSON Navigation
=========================================

LAB_JSON Learning Objective: Learn to navigate a JSON file and convert to a
                             python object. Practice file IO using with.
::

 a. Based on a sample Openstack authentication response file, what python
    syntax would you use to access items in the serviceCatalog?

    What path would access the publicURL for the DFW cloudServersOpenStack endpoint?

 b. Provide a new dict called compute_api_info and add keys "image_id"
    and "flavor_id". Use None for values. Dump compute_api_info
    to a file in JSON format (same as function in d.iii below)

 c. Based on analysis of the sample authentication response file, provide
    the following functions in a new module named compute_api_json.py:
     i. get_token_id()
     ii. get_tenant_id()
     iii. get_compute_public_URL(region) # solve this programmatically
                                         # i.e. don't hard code

 d. Also provide these functions:
     NOTE: Feel free to combine functions if easier
     i. get_image_id()  # use an ID of your choosing (Ex. 9db746f3-c54f-491b-b139-dea4b73bb9cb)
     ii. get_flavor_id()  # return 2
     iii. update_cached_compute_api_info(compute_api_info) # Dump to compute_api_info
     iv. update_cached_auth_response(auth_response) # Dump to auth_api_info

"""
