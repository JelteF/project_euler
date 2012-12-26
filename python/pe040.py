from utils.main import main

"""
An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
"""

def get_product_of_fraction():
    fraction = ''
    count = 1
    total = 1

    while len(fraction) < 10**6:
        fraction += str(count)
        count += 1

    for n in [0, 9, 99, 999, 9999, 99999, 999999]:
        total *= int(fraction[n])

    return total


if __name__ == '__main__':
    main(get_product_of_fraction)
