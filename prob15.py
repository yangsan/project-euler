#-*- coding: utf-8 -*-
"""
Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""


def routes(n):
    """
    Assume there is a n×n grid, the number of routes are (n+1)*(n+2)...*(2*n)/n!
    """
    return factorial(n + 1, 2 * n) / factorial(1, n)


def factorial(lowerbound, upperbound):
    if upperbound == lowerbound:
        return lowerbound
    return upperbound * factorial(lowerbound, upperbound - 1)

if __name__ == "__main__":
    print routes(20)
