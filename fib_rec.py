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


def fibonacci_optimized(n):
    return fibonacci_memo(n, {})


def fibonacci_memo(n, cash):
    if n < 0:
        raise ValueError(f"{n = }: must be positive")
    if n in (1, 2):
        return n
    if n in cash:
        return cash[n]
    cash[n] = res = fibonacci_memo(n - 1, cash) + fibonacci_memo(n - 2, cash)
    return res


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


def test_fib_rec():
    for k in range(1, 37):
        assert fib_rec(k) == fibonacci_optimized(k)


if __name__ == "__main__":
    with Timethis("getting fib_rec(N)"):
        fib_rec(37)
    with Timethis("getting fibonacci_optimized(N)"):
        fibonacci_optimized(37)
    # with timethis("getting fib_rec(N)"):
    #     fib_rec(42)
    # print(fib_rec(5), fibonacci_optimized(5))
