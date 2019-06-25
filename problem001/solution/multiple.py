#!/usr/bin/env python3
"""Multiples"""


def gen_multiples_set(mul, limit=1000):
    """Return the list of multiples of argument value(mul)"""
    num = (limit-1) // mul
    return {mul*i for i in range(1, num+1)}
