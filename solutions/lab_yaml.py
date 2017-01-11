#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_yaml` -- YAML Parsing
=========================================

LAB_YAML Learning Objective: Learn to parse a YAML file using the PyYAML library
                             and use the information.
::

 a. Start with your code (or the solution code) from lab_multi.

 b. Replace the command line config parsing with a YAML config parsing function.  Use the first
    argument to the program as the config file to parse.

 c. Create a YAML file that contains the same config items as the old command line.  Verify you
    can configure the program by changing the config file options.

"""
import queue
import argparse
import multiprocessing
import os
import threading
import time
import yaml
import sys

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

def parse_config(config_file):
    with open(config_file, 'r') as infile:
        cfg_dict = yaml.load(infile.read())
    return cfg_dict

if __name__ == "__main__":
    config = parse_config(sys.argv[1])
    if config['thread']:
        work_q = queue.Queue()
        done_q = queue.Queue()
    if config['process']:
        work_q = multiprocessing.JoinableQueue(config['items']+1)
        done_q = multiprocessing.JoinableQueue(config['items']+1)
    workers = create_workers(config['workers'], config['thread'], config['process'], work_q, done_q)
    work = generate_work(config['items'])
    [w.start() for w in workers]
    start = time.time()
    [work_q.put(w) for w in work]
    returned_items = 0
    while returned_items < config['items']:
        result = done_q.get()
        # print(("Result from {}: {}".format(result[0], result[1])))
        returned_items += 1
    stop = time.time()
    elapsed = stop-start
    print(("Elapsed {} ({} msec)".format(elapsed, elapsed*1000.0)))
    avg = elapsed / config['items']
    print("Avg. time per work item: {} ({} msec)".format(avg, avg*1000.0))
