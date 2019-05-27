# Problem 12

NUM_DIVISORS = 500

base = (0, 1)
gen_next = lambda n, i: (n + i, i + 1)

def count_divisors(n):
    return len(filter(lambda x: n % x == 0, range(1, n + 1)))

while count_divisors(base[0]) <= NUM_DIVISORS:
    base = gen_next(*base)

result = base[0]
print(result)
