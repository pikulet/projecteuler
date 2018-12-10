# Problem 7


def is_coprime(n,primes):
    for i in primes:
        if n%i ==0: return False
    return True


primes = [2,3,5,7,11,13]
i = 13

while len(primes) < 10001:
    if is_coprime(i, primes):
        primes.append(i)
    i += 2

result = primes[-1]
print(result)

