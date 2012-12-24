from utils.main import main

"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def diff_between_sum_of_squares(n):
    sum_of_squares = sum(map(lambda x: x**2, range(n)))
    square_of_sum = sum(range(n))**2

    return square_of_sum - sum_of_squares


if __name__ == '__main__':
    main(diff_between_sum_of_squares, 101)
