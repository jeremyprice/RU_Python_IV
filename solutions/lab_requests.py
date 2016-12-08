#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_requests` -- interacting with REST
=========================================

LAB_REQUESTS Learning Objective: Learn to interact with RESTful APIs using requests library
::

 a. Using requests, HTTP GET the initial page from the url given to you by the instructor.

 b. Using the JSON you receive from the server, determine the next url you are to open.
    Use HTTP POST to send the `token` you received from the initial page back to the server
    at the next url to load the second page.

    The returned JSON object will be in the form: {'<some_key>': url, 'token': <your_token>}
    where <some_key> will change for each access and <your_token> will be the same token you
    sent to the server.

    Your post JSON should be only one element: {'token': <your_token> }

 c. Continue the pattern from step b until you get a JSON response that contains the element
    called `answer`.  Print out the final object you recieved from the server.

 Note: the token has a short timeout, so you will have to pull all the steps in a loop,
       otherwise the token will invalidate due to timeout

"""

import sys
import requests


def debug_mode():
    import logging
    from http.client import HTTPConnection
    HTTPConnection.debuglevel = 1

    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


# debug_mode()
url = sys.argv[1]

# first request
first_hit = requests.get(url)
first_json = first_hit.json()
token = first_json.pop('token')
title, next_url = first_json.popitem()
print(("My ID is {}".format(token)))

# subsequent requests
done = False
link_titles = [title]
while not done:
    print(("Accessing {}".format(next_url)))
    hit = requests.post(next_url, json={'token': token})
    response = hit.json()
    if 'answer' in response:
        print(response)
        print('Link titles: {}'.format(', '.join(link_titles)))
        done = True
    else:
        token = response.pop('token')
        title, next_url = response.popitem()
        link_titles.append(title)
