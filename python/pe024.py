from utils.main import main
from itertools import permutations

"""
A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are
listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?
"""

def element_from_lexicographic_permutation(elems, i):
    return ''.join(map(str, list(permutations(elems, len(elems)))[i]))



if __name__ == '__main__':
    main(element_from_lexicographic_permutation, xrange(10), 10**6)
