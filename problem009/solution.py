#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Special Pythagorean triplet"""
from math import sqrt


def main():
    """Main function"""
    b = 2
    while True:
        for a in range(1, b):
            if a + b + sqrt(a**2 + b**2) == 1000:
                print('a: {}, b: {}, c: {}, prod: {}'
                    .format(a, b, sqrt(a**2 + b**2), a * b * sqrt(a**2 + b**2)))
                return
        b += 1


if __name__ == "__main__":
    main()
