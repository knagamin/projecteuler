#!/usr/bin/env python3
"""Largest palindrome product
"""


def is_palindrome_num(num):
    """Check whether the number is palindrome or not"""
    pn_str = str(num)
    for i in range(0, len(pn_str)):
        if pn_str[i] != pn_str[-(i+1)]:
            return False
    return True


def main():
    """Main"""
    max_pn = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            if is_palindrome_num(i*j) and max_pn < i*j:
                max_pn = i*j

    print(max_pn)

if __name__ == "__main__":
    main()
