#!/usr/bin/python3

"""
    lab_json Example solution
"""


import json


def get_image_id():
    return "9db746f3-c54f-491b-b139-dea4b73bb9cb"

def get_flavor():
    return 2

def get_token_id(auth_response):
    """ Pull token from an OpenStack Auth response """
    return auth_response['access']['token']['id']

def get_tenant_id(auth_response):
    """ Pull tenant ID from an OpenStack Auth response """
    return auth_response['access']['token']['tenant']['id']

def get_compute_public_URL(auth_response):
    """ Pull Compute's Public URL from an OpenStack Auth response """
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
        print("Failed to write to {}! {}".format(file_name,e))


if __name__ == "__main__":

    with open("auth_sample", "r") as sample:
        auth_response = json.load(sample)

    compute_api_info = {"flavor_id":     None,
                        "image_id":      None}

    update_cache(auth_response, file_name="auth_api_info")
    update_cache(compute_api_info, file_name="compute_api_info")

    print("Token: {}".format(get_token_id(auth_response)))
    print("Tenant: {}".format(get_tenant_id(auth_response)))
    print("Compute URLs: {}".format(get_compute_public_URL(auth_response)))
    print("Image ID: {}".format(get_image_id()))
    print("Flavor ID: {}".format(get_flavor()))
