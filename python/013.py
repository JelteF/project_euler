from utils.main import main

"""
Work out the first ten digits of the sum of the following one-hundred 50-digit
numbers*.

* See 013_data.txt for the numbers

"""


def get_first_digits_of_sum(amount, filename):
    f = open(filename, 'r')
    numbers = map(int, f.read().split('\n')[:-1])
    return str(sum(numbers))[:10]


if __name__ == '__main__':
    main(get_first_digits_of_sum, 10, './013_data.txt')
