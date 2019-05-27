# Problem 20

LIMIT  = 100

total = 1
for i in range(1, LIMIT + 1):
    if i % 10 == 0:
        i //= 10
    total *= i

result = sum(map(lambda x: int(x), str(total)))
print(result)
