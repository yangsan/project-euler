#-*- coding: utf-8 -*-
"""
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
import math


def is_prime(n, PrimeList):
    """
    n is the number to be checked, prime is a primelist generated whose
    elementsare all smaller than n.
    """
    if n <= 1:
        return False
    SqrtOfN = int(math.sqrt(n)) + 1
    for i in PrimeList:
        if i > SqrtOfN:
            break
        if n % i == 0:
            return False
    return True


def check_head_and_tail(number):
    """
    A truncatable number must has one of [2, 3, 5, 7] as fisrt digit, and one
    of [3, 7] as last digit.
    """
    number = str(number)
    return number[0] in ['2', '3', '5', '7'] and number[-1] in ['3', '7']


def check_middle(number, PrimeList):
    string1 = str(number)
    string2 = str(number)
    while len(string1) > 2:
        string1 = string1[1:]
        if int(string1) not in PrimeList:
            return False
    while len(string2) > 2:
        string2 = string2[:-1]
        if int(string2) not in PrimeList:
            return False
    return True


def truncatable():
    PrimeList = [2]
    TruncatableList = []
    number = 3
    while True:
        if is_prime(number, PrimeList):
            PrimeList.append(number)
            #print PrimeList
            if len(str(number)) > 1 and check_head_and_tail(number) and check_middle(number, PrimeList):
                TruncatableList.append(number)
        if len(TruncatableList) == 11:
            return TruncatableList
        number += 2

if __name__ == "__main__":
    #primelist = [2, 3, 5, 7]
    primelist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223]
    #print check_head_and_tail(223)
    number = 223
    #print check_middle(number, primelist)
    TruncatableList =  truncatable()
    print TruncatableList
    print sum(TruncatableList)

