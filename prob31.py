#-*- coding: utf-8 -*-
"""
In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:
    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:
    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""


# brute force
def coin():
    counter = 0
    for i100 in range(3):
        item100 = 100 * i100
        print "100:", i100
        for i50 in range(5):
            item50 = 50 * i50
            print "50:", i50
            for i20 in range(11):
                item20 = 20 * i20
                for i10 in range(21):
                    item10 = 10 * i10
                    for i5 in range(41):
                        item5 = 5 * i5
                        for i2 in range(101):
                            item2 = 2 * i2
                            for i in range(201):
                                if item100 + item50 + item20 + item10\
                                        + item5 + item2 + i == 200:
                                    counter += 1
                                    #print [i, i2, i5, i10, i20, i50, i100]
    return counter


# brute force 2
def coin2():
    counter = 0
    item200 = 200
    while item200 >= 0:
        item100 = item200
        while item100 >= 0:
            item50 = item100
            while item50 >= 0:
                item20 = item50
                while item20 >= 0:
                    item10 = item20
                    while item10 >= 0:
                        item5 = item10
                        while item5 >= 0:
                            item2 = item5
                            while item2 >= 0:
                                item1 = item2
                                while item1 >= 0:
                                    item1 -= 1
                                if item1 == -1:
                                    counter += 1
                                item2 -= 2
                            item5 -= 5
                        item10 -= 10
                    item20 -= 20
                item50 -= 50
            item100 -= 100
        item200 -= 200
    return counter


# recursion
def coin3(l=[200, 100, 50, 20, 10, 5, 2, 1], target=200):
    counter = 0
    if len(l) == 1:
        while target >= 0:
            target -= l[0]
        if target + l[0] == 0:
            return 1
        else:
            return 0
    while target >= 0:
        counter += coin3(l[1:], target)
        target -= l[0]
    return counter


if __name__ == "__main__":
    print coin3()
