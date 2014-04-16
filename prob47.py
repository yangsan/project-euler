#-*- coding: utf-8 -*-
"""
The first two consecutive numbers to have two distinct prime factors are:
    14 = 2 × 7
    15 = 3 × 5
The first three consecutive numbers to have three distinct prime factors are:
    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.
Find the first four consecutive integers to have four distinct prime factors.
What is the first of these numbers?
"""


def factorize(number):
    Factors = []
    k = 2
    while k <= number:
        while number % k == 0:
            number = number / k
            Factors.append(k)
        k += 1
    return Factors


def first_n_consecutive_numbers(n):
    pass


if __name__ == "__main__":
    print factorize(646)
