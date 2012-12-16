from math import sqrt
from bisect import bisect

class PrimeList:
    primes = [2, 3]

    def primes_up_to(self, max_prime):
        """ Return all the primes up to (inclusive) a certain value """

        if self.primes[-1] > max_prime:
            return self.primes[:bisect(self.primes, max_prime)]

        while self.primes[-1] < max_prime:
            self.find_next_prime()

        return self.primes[:-1]

    def find_next_prime(self):
        """ Find the next prime and add it to the primes list """

        i = self.primes[-1]
        while True:
            i += 2
            if self.is_prime(i):
                self.primes.append(i)
                return


    def is_prime(self, possible_prime):
        """ Return a boolean value to see if a number is a prime """

        # Calculate new primes to do sufficient checking
        while sqrt(possible_prime) > self.primes[-1]:
            self.find_next_prime()

        # Check to see if it could alread be in the list
        if possible_prime <= self.primes[-1]:
            if possible_prime in self.primes:
                return True
            return False

        # Check against existing primes
        for p in self.primes:
            if possible_prime % p == 0:
                return False

            if p > sqrt(possible_prime):
                return True

