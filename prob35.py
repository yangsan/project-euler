# -*- coding: utf-8 -*-
"""
The number, 197, is called a circular prime because all rotations of the digits
:197, 971, and 719, are themselves prime.There are thirteen such primes below
100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.How many circular
primes are there below one million?
"""


def prime_gen_1(upperbuond):
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


def prime_gen_2(upperbound):
    """
    A generator to produce a prime number list using Sieve of Eratosthenes.
    Return a list of prime number under upperbound.
    """
    number = range(2, upperbound)
    boolean = [1 for i in range(2, upperbound)]

    for i, item in enumerate(number):
        if boolean[i]:
            while i + item < len(number):
                i += item
                boolean[i] = 0

    return [a for i, a in enumerate(number) if boolean[i]]


def circular_of_a_number(number):
    number = str(number)
    CircularOfNumber = []
    for i in range(len(number) - 1):
        number = number[1:] + number[0]
        CircularOfNumber.append(int(number))
    return CircularOfNumber


def number_of_circular_primes_under(n):
    CircularPrimes = []
    PrimeNumbers = prime_gen_2(n)
    for prime in PrimeNumbers:
        if prime in CircularPrimes:
            continue
        else:
            CircularOfNumber = circular_of_a_number(prime)
            flag = True
            for number in CircularOfNumber:
                if number not in PrimeNumbers:
                    flag = False
                    break
            if flag:
                CircularOfNumber.append(prime)
                CircularPrimes += CircularOfNumber

    return len(CircularPrimes) - 1 # CircularPrimes will have two 11.

if __name__ == "__main__":
    print number_of_circular_primes_under(1000000)
