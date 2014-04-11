# -*- coding: utf8 -*-


def multiples(n):
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

if __name__ == "__main__":
    print multiples(1000)
