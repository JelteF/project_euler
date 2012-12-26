from utils.main import main
from pe004 import palindrome

"""
The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def is_double_base_palindrome(n):
    return palindrome(str(n)) and palindrome(bin(n)[2:])

def sum_of_double_base_palindrome(lim):
    double_base_palindromes = []

    for n in xrange(lim):
        if is_double_base_palindrome(n):
            double_base_palindromes.append(n)

    return sum(double_base_palindromes)


if __name__ == '__main__':
    main(sum_of_double_base_palindrome, 10**6)
