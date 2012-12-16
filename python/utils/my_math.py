from math import sqrt

class PrimeList:
    primes = [2, 3]

    def find_next_prime(self):
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
            print 'blaaa'
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

