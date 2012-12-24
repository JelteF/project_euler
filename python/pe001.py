from utils.my_math import Prime
from utils.main import main

""" Add all the natural numbers below one thousand
that are multiples of 3 or 5.
"""

def using_union(maximum):
    three = range(3, maximum, 3)
    five = range(5, maximum, 5)
    return sum(set().union(three, five))

def using_iteration(maximum):
    sum_ = 0

    for i in range(3, maximum, 1):
        if i % 3 == 0 or i % 5 == 0:
            sum_ += i

    return sum_


if __name__ == '__main__':
    main(using_union, 1000)
    main(using_iteration, 1000)
