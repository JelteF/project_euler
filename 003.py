def find_next_prime(primeList):
    i = primeList[len(primeList) - 1]
    while True:
        i += 1
        for p in primeList:
            if i % p == 0:
                break
        else:
            primeList.append(i)
            return


def largest_primefactor_of(maximum):
    primes = [2]
    devider = "No primefactor found"
    while primes[-1] <= maximum:
        if maximum % primes[-1] == 0:
            devider = primes[-1]
            maximum /= primes[-1]
        else:
            find_next_prime(primes)
    print devider


largest_primefactor_of(600851475143)
