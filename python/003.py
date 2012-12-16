from utils.my_math import Prime
from utils.main import main

def largest_primefactor(n):
    ps = Prime()
    return ps.get_prime_factors(n)[-1]


if __name__ == '__main__':
    main(largest_primefactor, 600851475143)
