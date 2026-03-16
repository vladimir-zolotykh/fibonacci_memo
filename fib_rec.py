#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from contextlib import contextmanager
import time


def fib_rec(n):
    if n < 0:
        raise ValueError(f"{n = }: must be positive")
    if n in (1, 2):
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print("{}: {}".format(label, end - start))


class Timethis:
    def __init__(self, label: str):
        self.label = label

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print("{}: {}".format(self.label, self.end - self.start))


# $ python fib_rec.py
# getting fib_rec(40): 11.172739028930664
# getting fib_rec(42): 33.33191108703613

if __name__ == "__main__":
    with Timethis("getting fib_rec(N)"):
        fib_rec(37)
    # with timethis("getting fib_rec(N)"):
    #     fib_rec(42)
