#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_multi` -- Investigate multiprocessing / multithreading
=========================================

LAB_multi Learning Objective: Learn to use the multiprocessing and multithreading modules
                              to perform parallel tasks.
::

 a. Write a command line parser that accepts the following args:
    -p --process : use multiprocessing
    -t --thread  : use threading
    -w --workers : number of workers to spawn
    -i --items   : number of work items to process

 b. In the main process, create a Queue for all the workers to use for their input work items,
    and a Queue for the workers to use to send their processed items back.  Make sure to share
    the Queue with the workers when they are created.

 c. Write a worker function.  The workers should take items from the Queue, process them,
    and put the results in the output queue.

 d. Write a function called create_workers() that creates the workers based on the
    multiprocessing or threading module as requested by the command line arguments.

 e. Write the main loop to process command line args, create the Queues, build the workers,
    start the workers, generate the work tasks, feed the work tasks to the workers, and print the
    results coming back in the results Queue.

Note: add args as necessary to the skeleton functions below
"""

import queue
import argparse
import multiprocessing
import os
import threading
import time


# Don't change this function


def work_task(item):
    """This is the work to be done on each input item"""
    def is_prime(num):
        for j in range(2, num):
            if (num % j) == 0:
                return False
        return True

    index = 0
    check = 0
    while index < item:
        check += 1
        if is_prime(check):
            index += 1
    return check

# Don't change this function


def generate_work(num_items):
    # import random
    return [300]*num_items
    # return [random.randint(1, 2000) for x in xrange(num_items)]

# Add your code down here


def worker(work_q, done_q):
    """This is the thread/process main function that will implement c. above"""
    process_id = os.getpid()
    thread_id = threading.current_thread().name
    my_id = "{}-{}".format(process_id, thread_id)
    while True:
        item = work_q.get()
        result = work_task(item)
        done_q.put((my_id, result))
        work_q.task_done()


def create_workers(num_workers, use_threads, use_processes, work_q, done_q):
    """This function creates workers of the requested type and wires them into the queues,
    per step d. above"""
    if use_threads:
        object_create = threading.Thread
    if use_processes:
        object_create = multiprocessing.Process
    workers = []
    for i in range(num_workers):
        processor = object_create(target=worker, args=[work_q, done_q])
        processor.daemon = True
        workers.append(processor)
    return workers


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-p", "--process", help="Use multiprocessing",
                       action="store_true", default=False)
    group.add_argument("-t", "--thread", help="use threading",
                       action="store_true", default=False)
    parser.add_argument("-w", "--workers", help="number of workers to spawn",
                        type=int, default=5)
    parser.add_argument("-i", "--items", help="number of items to process",
                        type=int, default=20)
    config = parser.parse_args()

    if config.thread:
        work_q = queue.Queue()
        done_q = queue.Queue()
    if config.process:
        work_q = multiprocessing.JoinableQueue(config.items+1)
        done_q = multiprocessing.JoinableQueue(config.items+1)
    workers = create_workers(config.workers, config.thread, config.process, work_q, done_q)
    work = generate_work(config.items)
    [w.start() for w in workers]
    start = time.time()
    [work_q.put(w) for w in work]
    returned_items = 0
    while returned_items < config.items:
        result = done_q.get()
        # print(("Result from {}: {}".format(result[0], result[1])))
        returned_items += 1
    stop = time.time()
    elapsed = stop-start
    print(("Elapsed {} ({} msec)".format(elapsed, elapsed*1000.0)))
    avg = elapsed / config.items
    print("Avg. time per work item: {} ({} msec)".format(avg, avg*1000.0))
