from utils.main import main
from utils.my_math import Prime
from itertools import combinations_with_replacement
from pe021 import d as proper_divisor_sum

"""
A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""

def get_abundant_numbers(n):
    pl = Prime()
    abundant = []

    for i in xrange(12, n):
        if i < proper_divisor_sum(i, pl):
            abundant.append(i)

    return abundant


def sum_of_non_abundant(n):
    abundant = get_abundant_numbers(n)
    abundant_sums = map(sum, combinations_with_replacement(abundant, 2))
    return sum(set(xrange(n)).difference(abundant_sums))


if __name__ == '__main__':
    main(sum_of_non_abundant, 28123)
