from utils.my_math import Prime
from utils.main import main

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def sum_of_primes_up_to(n):
    pl = Prime()
    return sum(pl.up_to(n))


if __name__ == '__main__':
    main(sum_of_primes_up_to, 2000000)
