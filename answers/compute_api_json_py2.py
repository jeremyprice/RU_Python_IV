#!/usr/bin/env python
#!*-* coding:utf-8 *-*

"""

Utility functions module for Openstack REST API.

"""

import sys
import json
import os
import urllib2
from datetime import datetime, tzinfo, timedelta
import iso8601

class Utc(tzinfo):
    def utcoffset(self, dt): 
        return timedelta(hours=-6)
    def dst(self, dt):
        return timedelta(hours=-6)
    def tzname(self, dt):
        return "UTC"

class Local(tzinfo):
    def utcoffset(self, dt): 
        return timedelta(hours=-0)
    def dst(self, dt):
        return timedelta(hours=-0)
    def tzname(self, dt):
        return "Local"

def isExpired():

    """ Return True if cached token has expired, else False. """

    token_expires = get_expires_ISO_time()
    if token_expires:
        timestamp = iso8601.parse_date(token_expires)
        utc = Utc()
        local = Local()
        now = datetime.now(local)
        #print "expires is", expires, "|now is", now
        if now < timestamp:
            return False

    return True
    

def get_new_auth_response(user, api_key):

    """ Returns an Openstack authentication response object. """

    auth_url = 'https://identity.api.rackspacecloud.com/v2.0/tokens'

    auth_json_creds = '{"auth":{"RAX-KSKEY:apiKeyCredentials":{"username":"%s", "apiKey":"%s"}}}' % (user, api_key)

    auth_headers = {"Content-Type": "application/json"}

    auth_request = urllib2.Request(auth_url, auth_json_creds, auth_headers)

    try:
        auth_fh = urllib2.urlopen(auth_request)
        return json.loads(auth_fh.read())
    
    except (URLError, HTTPError) as e:
        print "Error requesting authorization token:", e
        sys.exit(127)

def get_server_detail(region="DFW"):

    """ Returns response to a server detail list RESTful API call. """

    url = get_compute_public_URL(region) + "/servers/detail" 
    if not url:
        return None

    auth_response = get_cached_auth_response()
    if not auth_response:
        return None

    headers = {"X-Auth-Token": get_token_id()}
    request = urllib2.Request(url, headers = headers)
    
    try:
        fh = urllib2.urlopen(request)
        return fh.read()

    except (URLError, HTTPError) as e:
        print "Error accessing servers detail:", e
        sys.exit(127)

def get_compute_api_info():

    """ Returns the compute_auth_info cache as an object. """

    try:
        with open("compute_api_info",
                   mode="rt",
                 ) as fh:
    
            return json.load(fh)

    except IOError as e:
        print "compute_api_info file not found: ", e
        sys.exit(127)


def update_compute_api_info(object):

    """ Updates the compute_auth_info cache with object. """

    try:
        with open("compute_api_info",
                   mode="w",
                 ) as fh:
            json.dump(object,fh)

    except IOError as e:
        print "Can't update compute_api_info file: ", e
        sys.exit(127)

##################

def get_token_id():

    """  Returns token id from cache. """

    auth_response = get_cached_auth_response()
    if auth_response:
        return auth_response["access"]["token"]["id"]


def get_tenant_id():

    """  Returns tenant id from cache. """

    auth_response = get_cached_auth_response()
    if auth_response:
        return auth_response["access"]["token"]["tenant"]["id"]


def get_compute_public_URL(region):

    """  Returns compute public URL endpoint for given region from cache. """

    compute_api_info = get_compute_api_info()
    if not compute_api_info:
        return None

    for service in compute_api_info["auth_response"]["access"]["serviceCatalog"]:
        if service["name"] == "cloudServersOpenStack":
            for endpoint in service["endpoints"]:
                if endpoint["region"] == region: 
                    return endpoint["publicURL"]


def get_image_ID():

    """ Returns image id to clone (lab_server). """

    return  "6e242b85-4d03-4c02-8198-fec5242d54a1"


def get_flavor_ID():

    """ Returns flavor of server to boot. """

    return 2


def get_cached_auth_response():

    """ Returns existing (cached) auth response object. """

    cai =  get_compute_api_info()
    if cai:
        return cai["auth_response"]

 
def update_cached_auth_response(auth_object):

    """ Updates the compute_api_info cache with auth_object. """

    cai = get_compute_api_info()
    if cai:
        cai["auth_response"] = auth_object
        update_compute_api_info(cai)

#######################

def get_expires_ISO_time():

    """  Returns time the cached token expires in ISO format. """

    auth_response = get_cached_auth_response()
    if auth_response:
        return auth_response["access"]["token"]["expires"]

