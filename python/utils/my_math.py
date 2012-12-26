from math import sqrt
from bisect import bisect
from itertools import combinations
from operator import mul

def product(numbers):
    return reduce(mul, numbers)

class OrderedSequence:
    def up_to(self, max_num):
        """ Return all the numbers in the sequence up to (exclusive) a certain
            value
        """
        if self.sequence[-1] > max_num:
            return self.sequence[:bisect(self.sequence, max_num)]

        while self.sequence[-1] < max_num:
            self.find_next()

        return self.sequence[:-1]

    def up_to_element(self, element):
        while len(self.sequence) < element:
            self.find_next()

        return self.sequence[:element]


class Prime(OrderedSequence):
    def __init__(self):
        self.sequence = [2, 3]

    def get_prime_factors(self, n):
        """ Return a list of all the prime factors """
        factors = []

        for p in self.sequence:
            while n % p == 0:
                n /= p
                factors.append(p)


        while self.sequence[-1] <= n:
            while n % self.sequence[-1] == 0:
                n /= self.sequence[-1]
                factors.append(self.sequence[-1])
            self.find_next()

        return factors

    def get_prime_factor_frequency(self, n):
        factors = []
        frequencies = []

        for p in self.sequence:
            if n % p == 0:
                factors.append(p)
                frequencies.append(0)
                while n % p == 0:
                    n /= p
                    frequencies[-1] += 1

        while self.sequence[-1] <= n:
            if n % self.sequence[-1] == 0:
                factors.append(self.sequence[-1])
                frequencies.append(0)
                while n % self.sequence[-1] == 0:
                    n /= self.sequence[-1]
                    frequencies[-1] += 1
            self.find_next()

        return factors, frequencies

    def get_all_divisors(self, n):
        """ Return a list of all (not only prime) divisors """
        prime_factors = self.get_prime_factors(n)
        combis = [(1,)]

        for i in xrange(1, len(prime_factors) + 1):
            combis.extend(list(set(combinations(prime_factors, i))))

        return map(product, combis)

    def get_proper_divisors(self, n):
        return self.get_all_divisors(n)[:-1]

    def find_next(self):
        """ Find the next prime and add it to the primes list """

        i = self.sequence[-1]
        while True:
            i += 2
            if self.is_prime(i):
                self.sequence.append(i)
                return

    def is_prime(self, n):
        """ Return a boolean value to see if a number is a prime """
        if n < 19:
            return n in [2, 3, 5, 7, 11, 13, 17]

        if n > 5:
            m = n % 30
            if m != 1 and m != 7 and m != 11 and m != 13 and m != 17 and \
                    m != 19 and m != 23 and m != 29:
                return False

        if n < 721801:
            return pow(2, n-1, n)==1 and\
                    pow(3, n-1, n)==1 and pow(5, n-1, n)==1

        # Calculate new primes to do sufficient checking
        while sqrt(n) > self.sequence[-1]:
            self.find_next()

        # Check to see if it could already be in the list
        if n <= self.sequence[-1]:
            if n in self.sequence:
                return True
            return False

        # Check against existing primes
        for p in self.sequence:
            if n % p == 0:
                return False

            if p > sqrt(n):
                return True


class Fibonacci(OrderedSequence):
    def __init__(self):
        self.sequence = [1, 1]

    def find_next(self):
        self.sequence.append(self.sequence[-2] + self.sequence[-1])


class Triangle(OrderedSequence):
    def __init__(self):
        self.sequence = [1]

    def find_next(self):
        self.sequence.append(self.sequence[-1] + len(self.sequence) + 1)
