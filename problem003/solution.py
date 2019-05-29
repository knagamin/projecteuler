#!/usr/bin/env python3
"""Largest prime factor
"""


def max_prime_factor(num):
    """Find the maximum prime number"""
    prime = 2
    divided = num
    while prime**2 <= num and prime <= divided:
        if divided % prime == 0:
            divided //= prime
        else:
            prime += 1
    return prime


if __name__ == "__main__":
    print(max_prime_factor(600851475143))
