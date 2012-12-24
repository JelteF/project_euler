from utils.main import main

"""
The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even) n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1 It can be seen that this sequence (starting
at 13 and finishing at 1) contains 10 terms. Although it has not been proved
yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def next_collatz_number(n):
    if n % 2 == 0:
        return n/2
    return 3*n + 1


def longest_collatz_chain(n):
    collatz = {1:0}
    longest = 1
    for a in xrange(2, n):
        new = [a]
        while new[-1] not in collatz:
            new.append(next_collatz_number(new[-1]))

        print a, new
        for i, val in enumerate(new[:-1]):
            collatz[val] = collatz[new[-1]] + len(new) - i - 1

        if collatz[a] > collatz[longest]:
            longest = a

    return longest


if __name__ == '__main__':
    main(longest_collatz_chain, 100)
