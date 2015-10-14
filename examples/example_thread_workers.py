import Queue
import threading

num_worker_threads = 5

def worker():
    thread_id = threading.current_thread().name
    while True:
        item = q.get()
        print "Worker %s:" % thread_id, item
        q.task_done()

q = Queue.Queue()
for i in range(num_worker_threads):
     t = threading.Thread(target=worker)
     t.daemon = True
     t.start()

work_items = xrange(20)
for item in work_items:
    q.put(item)

q.join()       # block until all tasks are done
