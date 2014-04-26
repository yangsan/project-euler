# -*- coding: utf-8 -*-
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


# version 1
def factorize(number):
    Factors = []
    k = 2
    while k <= number:
        while number % k == 0:
            number = number / k
            Factors.append(k)
        k += 1
    return set(Factors)


def first_n_consecutive_numbers(n):
    number = 1
    while number < 1000000:
        Factors = factorize(number)
        if len(Factors) == n:
            flag = True
            for i in range(n - 1):
                if len(factorize(number + i + 1)) != n:
                    flag = False
            if flag:
                return number

        number += 1
        if number % 1000 == 0:
            print number


def first_n_consecutive_numbers_recursively(n):
    number = 1
    while number < 1000000:
        if n_consecutive_numbers(number, n, n):
            return number
        number += 1
        #print number


def n_consecutive_numbers(number, margin, n):
    if margin == 1:
        return len(factorize(number)) == n
    else:
        return len(factorize(number)) == n and\
            n_consecutive_numbers(number + 1, margin - 1, n)


# version 2, found on forum
def first_n_consecutive_numbers2(lim, n):
    L = [0] * (lim + 1)
    for i in xrange(2, lim / 2 + 1):
        if L[i] == 0:
            for j in range(i, lim + 1, i):
                L[j] += 1
    return ''.join(map(str, L)).index(''.join(map(str, [n] * n)))


if __name__ == "__main__":
    #print first_n_consecutive_numbers_recursively2(4)
    print first_n_consecutive_numbers2(1000000, 4)
