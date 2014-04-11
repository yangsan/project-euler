# -*- coding: utf8 -*-
"""
Problem 1:
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def multiples1(n):
    sum = 0
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            sum += i
        else:
            if i % 3 == 0:
                sum += i
            if i % 5 == 0:
                sum += i
    return sum


def multiples2(n):
    sum = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


def multiples3(n):
    """
    With generator only use O(1) memory.
    """
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            yield i

if __name__ == "__main__":
    print sum(multiples3(1000))
