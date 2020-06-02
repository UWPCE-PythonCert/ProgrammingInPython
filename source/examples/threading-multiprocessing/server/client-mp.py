#!/usr/bin/env python

import os
import sys
import urllib.request
import multiprocessing

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from decorators.decorators import timer


@timer
def threading_client(number_of_requests=10):

    results = multiprocessing.Queue()
    url = "http://localhost:37337"

    def worker(*args):
        conn = urllib.request.urlopen(url)
        result = conn.read()
        conn.close()
        results.put(result)

    for i in range(number_of_requests):
        proc = multiprocessing.Process(target=worker, args=())
        proc.start()
        print("Process %s started" % proc.name)

    for i in range(number_of_requests):
        print(results.get(timeout=2))

    print("made %d requests" % number_of_requests)


if __name__ == "__main__":

    number_of_requests = 100
    threading_client(number_of_requests=number_of_requests)
