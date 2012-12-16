from utils.my_math import Prime
import time

start = time.time()

pl = Prime()
primes = pl.primes_up_to(2000000)

print time.time() - start

print sum(primes)
