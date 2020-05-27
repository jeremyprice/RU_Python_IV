#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_rest_server` -- RESTful serving
=========================================

LAB_REST_SERVER Learning Objective: Learn to serve a RESTful API using the Flask library
::

 a. Using Flask create a simple server that serves a JSON greeting for the root route ('/')

 b. Add a route for a GET on "/phones" that returns a JSON list of all the phones on the server.

 c. Add a route for a POST on "/phones" that creates a phone on the server.  Return the id of the
    new phone to the client use a simple data structure like a dictionary to track your phones.
    Your phone object should have the following information: Manufacturer, Model, Date Purchased

 d. Add a route for a GET on "/phones/<phone_id>" that will return the information for the requested
    phone id.

 e. Add a route for a PUT on "/phones/<phone_id>" that allows the user to change some or all of the
    information for the given phone.

 f. Add a route for a DELETE on "/phones/<phone_id>" that deletes the phone with phone_id from the
    server.

"""
