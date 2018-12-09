# Problem 3

n = 600851475143

factors = []
while n % 2 == 0:
    n //= 2
while n % 3 == 0:
    n //= 3

i = 5
while n > 1:
    if n % i == 0:
        factors.append(i)
        n //= i
    i += 2

result = factors[-1]

