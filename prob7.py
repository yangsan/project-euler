#-*- coding: utf-8 -*-
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.
What is the 10 001st prime numberl?
"""
import math


def isPrime(n):
    """
    Check if n is a prime number.
    """
    if n <= 1:
        return False
    for i in xrange(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def findprime(nth):
    """
    Find the nth prime number, begin with 2.
    """
    n = 2
    primelist = []
    while True:
        if isPrime(n):
            primelist.append(n)
        if len(primelist) == nth:
            return primelist[-1]
        n += 1

if __name__ == "__main__":
    print findprime(10001)
