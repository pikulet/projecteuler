##Problem 7
##By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
##What is the 10 001st prime number?

def prime_list():
    primes = [2,3,5,7,11,13]
    i = 13
    while len(primes) < 10001:
        if is_coprime(i, primes):   primes.append(i)
        i+=2
    return primes[-1]

def is_coprime(n,primes):
    for i in primes:
        if n%i ==0: return False
    return True
