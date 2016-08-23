#!/usr/bin/env python
# *-* coding:utf-8 *-*

"""

:mod:`lab_subprocess` -- subprocess module
============================================

LAB subprocess Learning Objective: Familiarization with subprocess

::

 a. Use the subprocess call function to run "ls -l" and print the output.

 b. Do the same as a), but suppress stdout.

 c. Do the same as a), but run the command "/bogus/command". What happens?

 d. Use subprocess Popen to run "du -h" and output stdout to a pipe. Read the pipe
    and print the output.

 e. Create a new function commander() which takes any number of commands to execute
    (as strings) on the arg list, then runs them sequentially printing stdout.

"""
