##Problem 3
##The prime factors of 13195 are 5, 7, 13 and 29.
##What is the largest prime factor of the number 600851475143?

def largest_prime_factor(n):
    factors = []
    while n%2==0:     n//=2
    while n%3==0:     n//=3
    print(n)
    i = 5
    while n>1:
        if n%i == 0:
            factors.append(i)
            n//=i
        i+=2

    return factors[-1]
