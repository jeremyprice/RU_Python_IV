#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_multi` -- Investigate multiprocessing / multithreading
=========================================

LAB_multi Learning Objective: Learn to use the multiprocessing and multithreading modules
                              to perform parallel tasks.
::

 a. Create set of three functions that perform the following tasks:
    1. Capitalize all strings that come through and pass them along
    2. Count the number of characters in the string and pass along the string and the count as a
       a tuple (string, count).
    3. Check to see if the count is the largest seen so far.  If so, send along a tuple with
       (string, count, True), else send (string, count, False)

 b. Spawn each of those functions into processes (multiprocessing) and wire them together
    with interprocess communications (queues).

 c. Run the entire data/dictionary2.txt file through your processing engine, one word at a time.

 d. In the main process, monitor the results coming from the last stage in the processing engine.
    After all the words have been processed, print the longest word that went through the engine.

 e. If you complete the above tasks, go back and do the same tasks using threads (threading).  Don't
    delete your multiprocessing code, just add the threading code.

"""
