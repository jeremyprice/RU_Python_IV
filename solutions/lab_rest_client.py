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

import requests
import sys

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


if __name__ == '__main__':
    host = sys.argv[1]
    print('part a.')
    token_url = '{}/{}'.format(host, 'get_token')
    token_response = requests.get(token_url).json()
    my_token = token_response['X-Auth-Token']
    headers = {'X-Auth-Token': my_token}
    print('my token: {}'.format(my_token))

    print('part b.')
    cars_url = '/'.join([host, 'cars'])
    new_car = {'Make': 'Honda', 'Model': 'Fit', 'Color': 'Blue', 'Name': "Dad's Car",
               'Year': '2012', 'PrimaryDriver': 'Jeremy'}
    car_response = requests.post(cars_url, json=new_car, headers=headers).json()
    my_car_id = car_response['car']
    print('new car id: {}'.format(my_car_id))

    print('part c.')
    cars_response = requests.get(cars_url, headers=headers).json()
    cars_list = cars_response['cars']
    if not my_car_id in cars_list:
        print('Error: {} not in {}'.format(my_car_id, cars_list))
    else:
        print('{} is in {} as expected'.format(my_car_id, cars_list))

    print('part d.')
    my_car_url = '/'.join([host, 'cars', my_car_id])
    car_change = {'Model': 'Civic'}
    change_response = requests.put(my_car_url, json=car_change, headers=headers).json()
    new_car_info = change_response['car']
    print('Changed car info: {}'.format(new_car_info))

    print('part e.')
    car_info = requests.get(my_car_url, headers=headers).json()
    if car_info['Model'] != 'Civic':
        print('Error: change did not work: {}'.format(car_info))
    else:
        print('Success! Car changed properly: {}'.format(car_info))

    print('part f.')
    del_response = requests.delete(my_car_url, headers=headers).json()
    print(del_response)
