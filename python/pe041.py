from utils.main import main
from utils.my_math import Prime
from itertools import permutations

"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""

def get_largest_pandigital_prime():
    pl = Prime()
    combis = []

    for n in xrange(2, 10):
        combis.extend(permutations(range(1, n + 1), n))
    combis = map(lambda x: int(''.join(map(str, x))), combis)

    for n in combis[::-1]:
        if pl.is_prime(n):
            return n


if __name__ == '__main__':
    main(get_largest_pandigital_prime)
