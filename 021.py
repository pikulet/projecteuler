# Problem 21

LIMIT = 10000

divisor_sum = [None] * LIMIT
amicable = set()

def get_divisor_sum(n):
    return sum(filter(lambda x: n % x == 0, range(1, n)))

for i in range(1, LIMIT):
    divisor_sum[i] = get_divisor_sum(i)

for i in range(1, LIMIT):
    j = divisor_sum[i]
    if j < LIMIT and divisor_sum[j] == i and i != j:
        amicable.add(i)
        amicable.add(j)

result = sum(amicable)
print(result)
