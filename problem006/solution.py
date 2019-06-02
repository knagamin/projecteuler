#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sum square difference"""


def sum_sqr_first(num):
    """Get the sum of the squares of the first <num>"""
    return sum([x*x for x in range(1, num+1)])


def main():
    """Main"""
    max = 100
    sum_sqr = sum_sqr_first(max)
    sqr_sum = pow(sum(list(range(1, max+1))), 2)
    print(sqr_sum - sum_sqr)


if __name__ == "__main__":
    main()
