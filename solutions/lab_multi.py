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

import queue
import multiprocessing
import threading
import time


# Don't change this function


def capitalize(in_q, out_q):
    """Capitalize each word as it comes in on the input queue"""
    while True:
        item = in_q.get()
        cap = item.upper()
        out_q.put(cap)
        in_q.task_done()

def count_chars(in_q, out_q):
    """Count the length of each word as it comes in on the input queue"""
    while True:
        item = in_q.get()
        c = len(item)
        out_q.put((item, c))
        in_q.task_done()

def largest(in_q, out_q):
    """Check if this is the largest so far as it comes in on the input queue"""
    largest_seen = -1
    while True:
        item = in_q.get()
        if item[1] > largest_seen:
            largest_seen = item[1]
            output = (item[0], item[1], True)
        else:
            output = (item[0], item[1], False)
        out_q.put(output)
        in_q.task_done()

if __name__ == "__main__":
    # processes
    qstart = multiprocessing.JoinableQueue()
    q1to2 = multiprocessing.JoinableQueue()
    q2to3 = multiprocessing.JoinableQueue()
    qend = multiprocessing.JoinableQueue()
    cap_worker = multiprocessing.Process(target=capitalize, args=[qstart, q1to2])
    cap_worker.daemon = True
    count_worker = multiprocessing.Process(target=count_chars, args=[q1to2, q2to3])
    count_worker.daemon = True
    larg_worker = multiprocessing.Process(target=largest, args=[q2to3, qend])
    larg_worker.daemon = True
    with open('data/dictionary2.txt', 'r') as infile:
        words = infile.read().splitlines()
    larg_worker.start()
    count_worker.start()
    cap_worker.start()
    start = time.time()
    [qstart.put(word) for word in words]
    largest_so_far = None
    for returned_items in range(len(words)):
        word, count, large = qend.get()
        if large:
            largest_so_far = word
    stop = time.time()
    print('(Processes) Largest: {} in {:.2f} sec'.format(largest_so_far, stop-start))

    # threads
    qstart = queue.Queue()
    q1to2 = queue.Queue()
    q2to3 = queue.Queue()
    qend = queue.Queue()
    cap_worker = threading.Thread(target=capitalize, args=[qstart, q1to2])
    cap_worker.daemon = True
    count_worker = threading.Thread(target=count_chars, args=[q1to2, q2to3])
    count_worker.daemon = True
    larg_worker = threading.Thread(target=largest, args=[q2to3, qend])
    larg_worker.daemon = True
    with open('data/dictionary2.txt', 'r') as infile:
        words = infile.read().splitlines()
    larg_worker.start()
    count_worker.start()
    cap_worker.start()
    start = time.time()
    [qstart.put(word) for word in words]
    largest_so_far = None
    for returned_items in range(len(words)):
        word, count, large = qend.get()
        if large:
            largest_so_far = word
    stop = time.time()
    print('(Threads) Largest: {} in {:.2f} sec'.format(largest_so_far, stop-start))
