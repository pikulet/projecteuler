# Problem 26

LIMIT = 1000
num_list = [1] * LIMIT
primes = []

for i in range(2, LIMIT):
    if num_list[i] == 1:
        for j in range(LIMIT // i):
            num_list[j * i] = 0
        primes.append(i)

ten_power = lambda x: 10**x

def is_full_reptand(p):
    for i in range(1, p - 1):
        if ten_power(i) % p != 1:
            continue
        return False
    return ten_power(p - 1) % p == 1 

result = list(filter(lambda x: is_full_reptand(x), primes))[-1]
print(result)
