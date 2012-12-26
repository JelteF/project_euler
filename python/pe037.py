from utils.main import main
from utils.my_math import Prime
import re

"""
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

def is_truncatable_prime(p, pl):
    str_p = str(p)

    # Early ruling out
    if not re.match('^[1379]*$', str_p[1:]):
        return False

    while p > 9:
        if not pl.is_prime(p / 10):
            return False
        p /= 10

    while len(str_p) > 1:
        if not pl.is_prime(int(str_p[1:])):
            return False
        str_p = str_p[1:]

    return True



def sum_of_truncatable_primes():
    pl = Prime()
    truncatable_primes = []

    pl.up_to(10)

    while len(truncatable_primes) < 11:
        if is_truncatable_prime(pl.sequence[-1], pl):
            print pl.sequence[-1]
            truncatable_primes.append(pl.sequence[-1])
        pl.find_next()

    return sum(truncatable_primes)

if __name__ == '__main__':
    main(sum_of_truncatable_primes)
