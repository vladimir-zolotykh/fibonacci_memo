#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


def fib_rec(n):
    if n < 0:
        raise ValueError(f"{n = }: must be positive")
    if n in (1, 2):
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)
