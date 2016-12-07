#!/usr/bin/env python3


import queue
import threading

num_worker_threads = 5
num_work_items = 20


def worker():
    thread_id = threading.current_thread().name
    while True:
        item = q.get()
        print("Worker %s:" % thread_id, item)
        q.task_done()


if __name__ == '__main__':
    q = queue.Queue()
    for i in range(num_worker_threads):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()

    work_items = range(num_work_items)
    for item in work_items:
        q.put(item)

    q.join()       # block until all tasks are done
