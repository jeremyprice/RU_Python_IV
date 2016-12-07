#!/usr/bin/env python3


import threading
import time


def xyz():
    for i in range(10):
        print("thread")
        time.sleep(1.5)


if __name__ == "__main__":
    th = threading.Thread(target=xyz)
    th.start()
    for i in range(10):
        print("main")
        time.sleep(1)
