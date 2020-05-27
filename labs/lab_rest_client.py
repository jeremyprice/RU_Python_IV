#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_rest_client` -- interacting with a RESTful server
=========================================

LAB_REST_CLIENT Learning Objective: Learn to interact with RESTful APIs using requests library
::

 a. Using requests, HTTP GET the /get_token path from the url given to you by the instructor.  Store
    the token for use in the next steps.

    Note: For all the rest of the steps the server requires that you send a header with a key of
    "X-Auth-Token" and the value set to the token received in this step.

 b. Create a new "car" object using a POST to /cars path.  The expected data items for the "car"
    object can be seen by viewing the /formats/car path.  Note: you have to interact with the
    server via JSON, and you have to have values for each of the data items in the format.

 c. Get the list of cars from the server.  Verify that the id for the car you created is in that
    list.

 d. Change the Model of the car you created using the PUT HTTP verb to the proper url /cars/<id>

 e. Verify the change was registered by reading the information for the car id from /cars/<id>

 f. Delete the car you created by sending the http DELETE verb to /cars/<id>

 g. (Optional) Explore the other collections on the server.  Create some appliances or pantry items,
    change them, delete them, and generally mess around with the objects.  Check out /formats for
    the expected data format items.

"""

# Note: if you need to debug your HTTP connection info, call the following
# function before you do any http calls with requests:


def debug_mode():
    import logging
    from http.client import HTTPConnection
    HTTPConnection.debuglevel = 1

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True
