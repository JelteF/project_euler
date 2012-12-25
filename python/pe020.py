from utils.main import main
from pe016 import find_sum_of_digits
from math import factorial

"""
n! means n  (n  1)  ...  3  2  1

For example, 10! = 10  9  ...  3  2  1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

if __name__ == '__main__':
    main(find_sum_of_digits, factorial(100))
