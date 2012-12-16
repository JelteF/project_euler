import math

def find_next_prime(primeList):
    i = primeList[-1]
    while True:
        i += 2
        for p in primeList:
            if p>math.sqrt(i):
                primeList.append(i)
                return
            if i % p == 0:
                break
        else:
            primeList.append(i)
            return


primes = [2, 3]
primeSum = 2
counter = 0
while primes[-1] < 2000000:
    if counter == 1000:
        print primes[-1]
        counter = 0
    primeSum += primes[-1]
    find_next_prime(primes)
    counter += 1
print primeSum
