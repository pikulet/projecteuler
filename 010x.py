# Problem 10

LIMIT = 2000000
is_not_prime = [0] * (LIMIT + 1)

is_not_prime[0] = 1
is_not_prime[1] = 1

result = 2

for i in range(3, LIMIT + 1, 2):
    if is_not_prime[i] == 0:
        result += i
        for j in range(int((LIMIT + 1)/i)):
            is_not_prime[i * j] = 1

print(result)
