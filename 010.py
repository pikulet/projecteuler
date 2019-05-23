# Problem 10
import math

LIMIT = 2000000
primes = [2,3,5,7,11,13]
i = 13

def is_coprime(n, primes):
    SQRT_LIMIT = math.floor(n)
    for i in primes:
        if i > SQRT_LIMIT: return True
        if n % i == 0: return False
    return True

while i < LIMIT:
    if is_coprime(i, primes):
        primes.append(i)
    i += 2

result = sum(primes)
print(result)
