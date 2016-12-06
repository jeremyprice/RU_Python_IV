#!/usr/bin/env python3


import multiprocessing
import os


def worker(q):
    process_id = os.getpid()
    while True:
        item = q.get()
        print("Worker %s:" % process_id, item)
        q.task_done()


if __name__ == "__main__":
    num_worker_processes = 5
    num_work_items = 20
    q = multiprocessing.JoinableQueue(num_work_items+1)
    for i in range(num_worker_processes):
        p = multiprocessing.Process(target=worker, args=[q])
        p.daemon = True
        p.start()

    work_items = range(num_work_items)
    for item in work_items:
        q.put(item)

    q.join()       # block until all tasks are done
    print("All done")
