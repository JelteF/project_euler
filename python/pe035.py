from utils.main import main
from utils.my_math import Prime
import re

"""
The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?
"""

def is_circular_prime(p, pl):
    p = str(p)
    circular_p = p
    if not re.match('^[1379]*$', p):
        return False

    for c in p[:-1]:
        circular_p = circular_p[1:] + circular_p[0]

        if not pl.is_prime(int(circular_p)):
            return False

    return True


def amount_of_circular_primes(lim):
    pl = Prime()
    pl.up_to(lim)
    circular_primes = pl.sequence[:4]

    for p in pl.sequence[4:-1]:
        if is_circular_prime(p, pl):
            circular_primes.append(p)

    return len(circular_primes)


if __name__ == '__main__':
    main(amount_of_circular_primes, 10**6)
