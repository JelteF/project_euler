from utils.main import main

"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

def find_sum_of_digits(number):
    return sum(map(int, str(number)))


if __name__ == '__main__':
    main(find_sum_of_digits, 2**1000)
