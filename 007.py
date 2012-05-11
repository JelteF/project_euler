def find_next_prime(primeList):
    i = primeList[len(primeList) - 1]
    while True:
        i += 2
        for p in primeList:
            if i % p == 0:
                break
        else:
            primeList.append(i)
            return


primes = [2, 3]
for a in range(2, 10002):
    find_next_prime(primes)
print primes[10000]
