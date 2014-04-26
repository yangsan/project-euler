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

if __name__ == "__main__":
    print coin()
