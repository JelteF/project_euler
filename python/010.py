from utils.my_math import PrimeList

prime_list = PrimeList()
primes = prime_list.primes


while primes[-1] < 2000000:
    prime_list.find_next_prime()

print sum(primes[0:-1])
