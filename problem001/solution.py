#!/usr/bin/env python3
"""Multiples of 3 and 5"""


def gen_multiples_set(mul, limit=1000):
    """Return the list of multiples of argument value(mul)"""
    num = (limit-1) // mul
    return set([mul*i for i in range(1, num+1)])


if __name__ == "__main__":
    print(sum(list(gen_multiples_set(3) | gen_multiples_set(5))))
