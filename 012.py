import math

def find_next_triangle(triangleList):
    triangleList.append(triangleList[-1]+len(triangleList)+1)

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


def primefactors(number, primes):
    factors = [[],[]]
    for a in primes:
        if number % a == 0:
            factors[0].append(a)
            factors[1].append(0)
            while number % a == 0:
                factors[1][-1] += 1
                number /= a
    find_next_prime(primes)
    while primes[-1] <= number:
        if number % primes[-1] == 0:
            factors[0].append(a)
            factors[1].append(0)
            while number % primes[-1] == 0:
                number /= primes[-1]
                factors[-1] += 1
        else:
            find_next_prime(primes)
    return factors


primes = [2,3]
triangles = [1]
divisors = 0
counter = 0
while divisors <500:
    divisors = 1
    find_next_triangle(triangles)
    factors = primefactors(triangles[-1], primes)
    for a in factors[1]:
        divisors *= a+1
    counter += 1
print triangles[-1]
