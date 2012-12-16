from utils.my_math import Prime
from time import time

start = time()

pl = Prime()
primes = pl.up_to(2000000)

print time() - start

print sum(primes)
