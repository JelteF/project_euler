from utils.main import main
from itertools import product

def palindrome(sequence):
    return sequence == sequence[::-1]

def palindrome_product(mini, maxi):

    numbers = range(mini, maxi)
    products = list(set(map(lambda x: x[0] * x[1], product(numbers, numbers))))

    for n in sorted(products, reverse=True):
        if palindrome(str(n)):
            return n
    return 0

if __name__ == '__main__':
    main(palindrome_product, 1, 1000)
