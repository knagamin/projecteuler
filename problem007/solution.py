#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""10001st prime"""


def main():
    """Print the 10001st prime number
    """
    cnt_p = 1
    primes = [2]
    x = 2
    while cnt_p <= 10000:
        x += 1
        for prime in primes:
            if x % prime == 0:
                break
            if prime == primes[-1]:
                primes.append(x)
                cnt_p += 1
    print(primes[-1])

if __name__ == "__main__":
    main()
