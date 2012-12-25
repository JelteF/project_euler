from utils.main import main
from utils.my_math import Prime

"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def d(n, pl):
    return sum(pl.get_proper_divisors(n))


def sum_of_amicable_numbers(n):
    pl = Prime()
    amicable_sum = 0

    for i in xrange(2, n):
        divisor_sum = d(i, pl)
        if divisor_sum < i and divisor_sum > 0 and d(divisor_sum, pl) == i:
            amicable_sum += divisor_sum + i

    return amicable_sum


if __name__ == '__main__':
    main(sum_of_amicable_numbers, 10000)
