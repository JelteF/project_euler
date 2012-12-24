from utils.main import main

"""
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def product_of_triplet_with_sum(sum_):
    for a in range(1, sum_ / 3):
        for b in range(a, (sum_ / 3)*2 - a):
            c = sum_ - a - b
            if (a**2 + b**2) == c**2:
                return a*b*c


if __name__ == '__main__':
    main(product_of_triplet_with_sum, 1000)
