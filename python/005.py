import time
from utils.my_math import Prime
from operator import mul

"""
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""


def divisible_by_all_lower(max_divisor):
    """ Return the number that is divisible by all numbers lower than the
        max_divisor
    """
    smallest = 1
    pl = Prime()
    prime_divisors = pl.primes_up_to(max_divisor)

    for p in prime_divisors:
        temp = p
        while temp <= max_divisor:
            temp *= p
            smallest *= p

    return smallest

if __name__ == '__main__':
    start = time.time()
    answer = divisible_by_all_lower(21)
    print time.time() - start
    print answer
