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

from flask import Flask, jsonify, request
import json

app = Flask(__name__)
phone_db = {}
expected_info = ['Manufacturer', 'Model', 'Date Purchased']
next_phone_id = 0

@app.route('/', methods=['GET'])
def root():
    output = {'/': 'rules, routes, and description',
              '/phones': 'get a list of all the phones on the server',
              '/phones/<phone_id>': 'information and interaction with a specific phone on the server'}
    return jsonify(output)


@app.route('/phones', methods=['GET', 'POST'])
def phones():
    global next_phone_id
    if request.method == 'GET':
        # Read the list of phones
        return jsonify(phone_db)
    elif request.method == 'POST':
        # Create a new phone
        new_phone = request.get_json()
        # check to see that we have all the required information for a new phone
        for info in expected_info:
            if not info in new_phone:
                return jsonify({'error': 'Must specify {} for a new phone'.format(info)})
        # copy the information and add the phone to our database
        phone_db[next_phone_id] = {k: new_phone[k] for k in expected_info}
        output = {'phone_id': next_phone_id}
        next_phone_id += 1
        return jsonify(output)


@app.route('/phones/<int:phone_id>', methods=['GET', 'PUT', 'DELETE'])
def phone(phone_id):
    if not phone_id in phone_db:
        # invalid phone id
        return jsonify({'error': 'Invalid phone id: {}'.format(phone_id)})
    if request.method == 'GET':
        # Read the info for this phone
        return jsonify(phone_db[phone_id])
    elif request.method == 'PUT':
        # Update the info for this phone
        phone_info = phone_db[phone_id]
        for key, value in request.get_json().items():
            if key in phone_info:
                phone_info[key] = value
        phone_db[phone_id] = phone_info
        return jsonify(phone_info)
    elif request.method == 'DELETE':
        # Delete this phone from the database
        del phone_db[phone_id]
        return jsonify({'success': 'Deleted phone {} from the server'.format(phone_id)})

if __name__ == '__main__':
    app.run()
