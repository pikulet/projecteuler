# Problem 24

import math
from string import digits

d = digits
INDEX = 1000000 - 1     # compensate for 0-indexing
permutation = []

for i in range(10):
    i = 9 - i
    permutations_after = math.factorial(i)
    next_digit = INDEX // permutations_after
    permutation.append(d[next_digit])
    d = d[: next_digit] + d[next_digit + 1:]
    INDEX %= permutations_after

result = ''.join([str(x) for x in permutation])
print(result)
