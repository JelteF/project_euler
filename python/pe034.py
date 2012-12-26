from utils.main import main
from math import factorial

"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

def is_curious_number(n):
    return n == sum(map(lambda x: factorial(int(x)), str(n)))


def sum_of_curious_numbers(lim):
    curious_numbers = []
    for n in xrange(10, lim):
        if is_curious_number(n):
            curious_numbers.append(n)

    return sum(curious_numbers)



if __name__ == '__main__':
    main(sum_of_curious_numbers, 10**5)
