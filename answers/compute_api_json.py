#!/usr/bin/python3

"""
    Compute API JSON Module
"""


import json
from urllib import request as Request
from urllib.parse import urlencode


HEADERS = {"Content-type": "application/json",
           "Accept":       "application/json"}


def auth(username,
         password,
         headers=HEADERS,
         url="https://identity.api.rackspacecloud.com/v2.0/tokens"):

    payload = {"auth":
                   {"passwordCredentials":
                        {"username": username,
                         "password": password}}}
    payload = bytes(json.dumps(payload),"utf-8")
    request = Request.Request(url=url, data=payload, headers=headers)
    response = Request.urlopen(request)
    return str(response.read(),"utf-8")

def get_image_id():
    return "9db746f3-c54f-491b-b139-dea4b73bb9cb"

def get_flavor():
    return 2

def get_token_id(auth_response):
    " Pull token from an OpenStack Auth response "
    return auth_response['access']['token']['id']

def get_tenant_id(auth_response):
    " Pull tenant ID from an OpenStack Auth response "
    return auth_response['access']['token']['tenant']['id']

def get_compute_public_URL(auth_response):
    " Pull Compute's Public URL from an OpenStack Auth response "
    endpoints = list()
    services = [service for service in
                    auth_response['access']['serviceCatalog']
                    if service['type'].lower() == "compute"]

    for service in services:
        for endpoint in service['endpoints']:
            endpoints += [value for key,value in endpoint.items() if key == "publicURL"]
    return endpoints

def update_cache(data, file_name="auth_api_info"):
    try:
        with open(file_name, "w") as output:
            json.dump(data, output)
    except IOError as e:
        print("Failed to write to {}! {}".format(file_name, e))

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-u","--username", help="Username for auth with Identity")
    parser.add_argument("-p","--password", help="Password for auth with Identity")
    args = parser.parse_args()

    auth_response = auth(username=args.username,
                         password=args.password)
    print(json.dumps(auth_response))
