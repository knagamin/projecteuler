#!/usr/bin/env pytho3
"""Smallest multiple"""


def gcd(x, y):
    """Get greatest common divisor of two numbers
       You can use gcd function in math module instead.
    """
    if(y == 0):
        return x
    return gcd(y, x % y)


def lcm(x, y):
    """Get least common multiple of two numbers"""

    gcd_num = gcd(x, y)

    # correclty : lcm = gcd * (x / gcd) * (y / gcd)
    return x * y / gcd_num


def main():
    """Use the law: lcm(a,b,c) -> lcm(lcm(a, b) c)"""
    lcm_n = 1
    for x in range(1, 21):
        lcm_n = lcm(lcm_n, x)

    print(lcm_n)


if __name__ == "__main__":
    main()
