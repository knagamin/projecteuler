#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Largest product in a series"""
from functools import reduce
WINDOW_SIZE = 13


def main():
    """Main function"""
    digits = ""
    with open("./digits.txt") as file:
        for line in file:
            digits += line.rstrip()

    max_product = 0
    for idx in range(0, len(digits) - WINDOW_SIZE + 1):
        four_digits = digits[idx:idx+WINDOW_SIZE]
        if '0' in four_digits:
            continue

        product = reduce(lambda x, y: x*y, map(int, four_digits))
        if max_product < product:
            max_product = product

    print(max_product)


if __name__ == "__main__":
    main()
