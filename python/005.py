import time
from utils.my_math import PrimeList
from operator import mul

def divisible_by_all_lower(max_divisor):
    smallest = 1
    pl = PrimeList()
    prime_divisors = pl.primes_up_to(max_divisor + 1)

    for p in prime_divisors:
        temp = p
        while temp <= max_divisor:
            temp *= p
            smallest *= p

    return smallest

if __name__ == '__main__':
    start = time.time()
    answer = divisible_by_all_lower(20)
    print time.time() - start
    print answer
