#!/usr/bin/env python3
# -*- coding: utf_8 -*-

"""Even Fibonacci numbers
"""


def gen_fib(max_val=1000000):
    """
    Generate Fibonacci numbers which are less than max_val argument.

    :param max_val: The value defines the range of numbers which are not beyond
    its.
    """
    num_1 = 1
    num_2 = 2
    while num_1 < max_val:
        ret = num_1
        num_1, num_2 = num_2, num_1+num_2
        yield ret


if __name__ == "__main__":
    sum_even = 0
    for n in gen_fib(4000000):
        if n % 2 == 0:
            sum_even += n
    print(sum_even)
