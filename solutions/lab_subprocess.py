#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_subprocess` -- subprocess module
============================================

LAB subprocess Learning Objective: Familiarization with subprocess

::

 a. Use the subprocess run function to run "ls -l" and print the output.

 b. Do the same as a), but don't print anything to the screen.

 c. Do the same as a), but run the command "/bogus/command". What happens?

 d. Use subprocess Popen to run "du -h" and output stdout to a pipe. Read the pipe
    and print the output.

 e. Create a new function commander() which takes in a list of commands to execute
    (as strings) on the arg list, then runs them sequentially printing stdout.

"""
import subprocess
print("step a.")
proc = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE)
print(proc.stdout.decode())

print("step b.")
subprocess.run(["ls", "-l"], stdout=subprocess.DEVNULL)
print('')

print("step c.")
try:
    subprocess.run(["/bogus/command"])
except OSError as e:
    print(e)
print('')

print("step d.")
proc = subprocess.run(["du", "-h"], stdout=subprocess.PIPE)
print(("Output from command:\n{}".format(proc.stdout.decode())))
print('')

print("step e.")
def commander(commands):
    for cmd in commands:
        proc = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
        print("Output from {} :\n{}".format(cmd, proc.stdout.decode()))


commands = ["ls -al",
            "df -h",
            "mount",
            'fortune',
            "who",
            "whoami"]
commander(commands)
