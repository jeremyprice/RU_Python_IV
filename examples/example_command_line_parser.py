#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-p", "--process", help="Use multiprocessing",
                   action="store_true", default=False)
group.add_argument("-t", "--thread", help="use threading", action="store_true",
                   default=False)
parser.add_argument("-w", "--workers", help="number of workers to spawn",
                    type=int, default=5)
parser.add_argument("-i", "--items", help="number of items to process",
                    type=int, default=20)
config = parser.parse_args()

print(config)
print(config.process, config.thread, config.workers, config.items)
