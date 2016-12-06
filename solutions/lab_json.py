#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_json` -- JSON Navigation
=========================================

LAB_JSON Learning Objective: Learn to navigate a JSON file and convert to a
                             python object. Practice file IO using with.
::

 a. Using urllib2, explore the GitHub JSON API.  Load the initial api page, parse it
    into JSON, and use it for the following tasks.

 b. Load the list of emojis from the GitHub API and print a random one from the list.
    Save the list to emojis.json

 c. Load the information for a GitHub username passed in from the command line, print
    the number of repositories the user has and what organizations they belong to.
    Save the user info to {{username}}.json

"""

# see https://docs.python.org/2/library/urllib2.html for more info on urllib2
# example use of urllib2 to get a web resource:
import json
import random
import sys
import urllib.request
import urllib.error
import urllib.parse

token = open('github_api_key', 'r').read().strip()
url_token = "?access_token={}".format(token)

# step a.
url = "https://api.github.com/" + url_token
data = urllib.request.urlopen(url)
data = data.read().decode()
initial_page = json.loads(data)
json.dump(initial_page, open('initial.json', 'w'), sort_keys=True, indent=4)
print("wrote initial page to initial.json")

# step b.
url = initial_page['emojis_url'] + url_token
data = urllib.request.urlopen(url)
data = data.read().decode()
emojis = json.loads(data)
json.dump(emojis, open('emojis.json', 'w'), sort_keys=True, indent=4)
print("wrote emojis page to emojies.json")
rand_emoji = random.choice(list(emojis.keys()))
print(("A random emoji for you:\n{} - {}".format(rand_emoji, emojis[rand_emoji])))

# step c.
username = sys.argv[1]
# get the user url from the initial api info
url = initial_page["user_url"].replace("{user}", username) + url_token
data = urllib.request.urlopen(url)
data = data.read().decode()
user_info = json.loads(data)
json.dump(user_info, open('{}.json'.format(username), 'w'), sort_keys=True, indent=4)
print(("wrote {0} user info page to {0}.json".format(username)))
print(("{} has {} public repos".format(username, user_info["public_repos"])))
url = user_info["organizations_url"] + url_token
data = urllib.request.urlopen(url)
data = data.read().decode()
org_info = json.loads(data)
print(("{} belongs to {} organization(s)".format(username, len(org_info))))
