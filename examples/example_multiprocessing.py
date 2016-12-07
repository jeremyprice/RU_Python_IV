#!/usr/bin/env python3


import multiprocessing
import time


def xyz():
    for i in range(10):
        print("thread")
        time.sleep(1)


if __name__ == '__main__':
    proc = multiprocessing.Process(target=xyz)
    proc.start()
    for i in range(10):
        print("main")
        time.sleep(1)
