#!/usr/bin/env python
#!*-* coding:utf-8 *-*

"""

:mod:`lab03_urllib2_REST` -- urllib2 and REST
=============================================

LAB03 Learning Objective: Familiarization with urllib2 module and client REST
      API usage.

 a. Use argparse to accept the following parameters:

     -c --creds  takes (2) arguments: username and APIkey
     or
     -u --username  takes (1) argument:  username, and use getpass module for the password/api-key

 b. Run the following curl to verify operation, then convert into a urllib2 call:

   curl -s https://identity.api.rackspacecloud.com/v2.0/tokens -X 'POST' \
     -d '{"auth":{"RAX-KSKEY:apiKeyCredentials":{"username":"USERID","apiKey":"APIKEY"}}}' \
     -H "Content-Type: application/json"

   using the userid and APIkey given in class

 c. Call your LAB_json update_auth_response() to update the compute_ap_info cache file.

 d. Run the following curl, then convert into a urllib2 call:

   curl -s https://dfw.servers.api.rackspacecloud.com/v2/TENANT/servers/detail \
     -H "X-Auth-Token: TOKEN"

   where TOKEN is from get_token_id() and TENANT is from get_tenant_id()

 e. Run your program and print the results.

"""

import compute_api_json_py2 as caj
import sys
import argparse
import json
import getpass


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Credential client for Openstack API V2')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-c', '--creds', nargs=2, dest='creds',
                       help='Please enter username and APIkey for your account')
    group.add_argument('-u', '--username', dest='username',
                       help='Please enter username for your account')
    args = parser.parse_args()

    # if auth token expired, get another
    if caj.isExpired():
        if args.username: # user gave the username
            passwd = getpass.getpass("Enter the password for user {}:".format(args.username))
            auth_response = caj.get_new_auth_response_passwd(args.username, passwd)
        else: # user gave username and APIkey
            auth_response = caj.get_new_auth_response_api_key(args.creds[0], args.creds[1])
        # update the cached auth response
        caj.update_cached_auth_response(auth_response)

    print "\nList servers response:\n", caj.get_server_detail()
