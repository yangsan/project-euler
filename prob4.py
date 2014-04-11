#-*- coding: utf-8 -*-
"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

import sys


def ifPalin(n):
    if len(n) <= 1:
        return True
    if n[0] == n[-1]:
        return True and ifPalin(n[1:-1])
    return False

if __name__ == "__main__":
    print ifPalin(sys.argv[1])
