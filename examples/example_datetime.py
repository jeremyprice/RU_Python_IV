#!/usr/bin/env python3

import datetime
import imp

print(datetime.datetime.now())
print(datetime.datetime.max, datetime.datetime.min)


class PartyTime():
    def __call__(self, *args):
        imp.reload(datetime)
        value = datetime.datetime(*args)
        datetime.datetime = self
        return value

    def __getattr__(self, value):
        if value == 'now':
            return lambda: print('Party Time!')
        else:
            imp.reload(datetime)
            value = getattr(datetime.datetime, value)
            datetime.datetime = self
            return value


datetime.datetime = PartyTime()
print(datetime.datetime.now())
print(datetime.datetime.max, datetime.datetime.min)
