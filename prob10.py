#-*- coding: utf-8 -*-
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
import math


def isPrime2(n, primelist):
    """
    n is the number to be checked, prime is a primelist generated whose
    elementsare all smaller than n.
    """
    if n <= 1:
        return False
    sqrtofn = int(math.sqrt(n))
    for i in primelist:
        if i > sqrtofn:
            break
        if n % i == 0:
            return False
    return True


def primesum(nth):
    primelist = []
    n = 2
    while True:
        if isPrime2(n, primelist):
            if n > nth:
                return sum(primelist)
            primelist.append(n)
        n += 1


if __name__ == "__main__":
    print primesum(2000000)
