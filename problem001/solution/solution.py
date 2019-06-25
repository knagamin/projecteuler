#!/usr/bin/env python3
"""Multiples of 3 and 5"""

from solution.multiple import gen_multiples_set


def solution():
    return sum(list(gen_multiples_set(3) | gen_multiples_set(5)))


if __name__ == "__main__":
    solution()
