#-*- coding: utf-8 -*-
"""
The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.There are thirteen such primes below
100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.How many circular
primes are there below one million?
"""

import math


def primegen1(upperbuond):
    """
    A generator to produce a prime number sequence.
    """
    primenumber = [2]
    n = 3
    while n < upperbuond:
        flag = True
        for i in primenumber:
            if n % i == 0:
                flag = False
                break
        if flag:
            primenumber.append(n)
        n += 2
    return primenumber


def primegen2(upperbound):
    """
    A generator to produce a prime number list using Sieve of Eratosthenes.
    """
    number = range(2,upperbound)
    boolean = [1 for i in range(2,upperbound)]

    for i, item in enumerate(number):
        if boolean[i]:
            #print i,item,boolean[i]
            while i + item < len(number):
                i += item
                boolean[i] = 0

    prime = [a for i, a in enumerate(number) if boolean[i]]
    return prime



if __name__ == "__main__":
    print primegen1(100)
    print primegen2(100)
