from utils.my_math import Prime, Triangle
from utils.main import main

def get_amount_of_divisors(pl, n):
    factors, frequencies = pl.get_prime_factor_frequency(n)
    possible_combinations = 1
    for f in frequencies:
        possible_combinations *= f + 1

    return possible_combinations


def first_triangle_divisors(n):
    tri = Triangle()
    pl = Prime()
    while get_amount_of_divisors(pl, tri.sequence[-1]) < n:
        tri.find_next()
    return tri.sequence[-1]


if __name__ == '__main__':
    main(first_triangle_divisors, 500)
