import threading
import time


def xyz():
    for i in range(10):
        print "thread"
        time.sleep(1.5)

th = threading.Thread(target=xyz)
th.start()
for i in range(10):
    print "main"
    time.sleep(1)
