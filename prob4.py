#-*- coding: utf-8 -*-
"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def isPalin(n):
    n = str(n)
    if len(n) <= 1:
        return True
    if n[0] == n[-1]:
        return True and isPalin(n[1:-1])
    return False


def largestPalin(digits):

    upperbound = 10 ** digits - 1
    lowerbound = 10 ** (digits - 1)

    palin = 0

    for i in xrange(upperbound, lowerbound, -1):
        for j in xrange(i, lowerbound, -11):
            number = i * j
            if isPalin(number) and number > palin:
                palin = number
    return palin

if __name__ == "__main__":
    #print isPalin('101')
    print largestPalin(3)
