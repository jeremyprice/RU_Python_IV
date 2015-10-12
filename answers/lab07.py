#!/usr/bin/python3

"""
    Lab07 - Threads
"""

import random
import threading
import time

def boss(*args, **kwargs):
    """ Da boss. Give works to the peons. """
    work_control = kwargs['work_control']
    work_list = kwargs['work_list']
    work_queue = kwargs['work_queue']

    for work in work_list:
        work_control.acquire()
        work_queue.append(work)
        print("Boss is giving out more work! (Oh geez...)")
        work_control.notify_all()
        work_control.release()
        time.sleep(random.randint(0,2))

    time.sleep(3)
    return

def connection_mgr():
    """ """

    return

def random_work():
    """ Random work generator """

    thread = None
    while True:
        num = random.randint(1,100000)
        thread = yield "{}: Ran through {} cycles.".format(thread, num)
        counter = num
        while counter > 0:
            counter -= 1

def worker(*args, **kwargs):
    """ Worker bees. Waits for work, then does the needful. """

    work_control = kwargs['work_control']
    work_queue = kwargs['work_queue']

    while True:
        work_control.acquire()
        while not work_queue:
            work_control.wait()
        work_item = work_queue.pop()
        work_control.release()
        print("{}: Starting work!".format(threading.current_thread().name))   
        print(work_item.send(threading.current_thread().name))

    return

if __name__ == "__main__":

    num_workers = 4
    num_jobs = 10
    work_list = []
    work_queue = []
    work_queue_lock = threading.RLock()
    work_control = threading.Condition(work_queue_lock)

    for job in range(num_jobs):
        job = random_work()
        next(job)
        work_list.append(job)

    for thread in range(num_workers):
        worker_kwargs = {"work_control": work_control,
                         "work_queue":   work_queue}
        worker_thread = threading.Thread(target=worker, kwargs=worker_kwargs)
        # NOTE: daemonized threads are killed at the end of parent process
        worker_thread.daemon = True
        worker_thread.start()

    boss_kwargs = {"work_list": work_list,
                   "work_control": work_control,
                   "work_queue": work_queue}
    boss_thread = threading.Thread(target=boss, kwargs=boss_kwargs)
    boss_thread.start()

    print("Reached end of __main__")
