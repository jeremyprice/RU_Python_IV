#!/usr/bin/python3

"""
    Lab06 - Decorators
"""

import random

names = ["BoB", "BOB", "Susan","Carol","Bob","Jeanette","Larry","John"]

def bouncer(func):
    def kick_bob(attendees):
        print("Looking for Bob...")
        for attendee in attendees:
            if attendee.lower() == "bob":
                attendees.remove(attendee)
        func(attendees)
    return kick_bob

@bouncer
def party(attendees):
    print("List of people going to the party: {}".format(", ".join(attendees)))

print(party)
party(names)

