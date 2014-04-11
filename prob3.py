# -*- coding: utf-8 -*-
"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

# version 1, use isPrime to check if a integer is a prime
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


def largestprimefactor1(number):
    counter = 0
    while counter <= number:
        if isPrime(counter):
            while number % counter == 0:
                number /= counter
        counter += 1
    return counter - 1

if __name__ == "__main__":
    number = 600851475143
    #number = 13195
    print largestprimefactor1(number)
