from math import sqrt
from bisect import bisect


class OrderedSequence:
    sequence = []

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
    sequence = [2, 3]

    def get_prime_factors(self, n):
        """ Return a list of all the prime factors """
        factors = []
        if self.is_prime(n):
            return [n]

        for p in self.sequence:
            while n % p == 0:
                n /= p
                factors.append(p)

            if n == 1:
                return factors

    def find_next(self):
        """ Find the next prime and add it to the primes list """

        i = self.sequence[-1]
        while True:
            i += 2
            if self.is_prime(i):
                self.sequence.append(i)
                return

    def is_prime(self, possible_prime):
        """ Return a boolean value to see if a number is a prime """

        # Calculate new primes to do sufficient checking
        while sqrt(possible_prime) > self.sequence[-1]:
            self.find_next()

        # Check to see if it could already be in the list
        if possible_prime <= self.sequence[-1]:
            if possible_prime in self.sequence:
                return True
            return False

        # Check against existing primes
        for p in self.sequence:
            if possible_prime % p == 0:
                return False

            if p > sqrt(possible_prime):
                return True


class Fibonacci(OrderedSequence):
    sequence = [1, 1]

    def find_next(self):
        self.sequence.append(self.sequence[-2] + self.sequence[-1])

