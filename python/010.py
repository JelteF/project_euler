from utils.my_math import PrimeList
import time

start = time.time()

pl = PrimeList()
primes = pl.primes_up_to(2000000)

print time.time() - start

print sum(primes)
