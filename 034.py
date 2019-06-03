# Problem 34

fact = [1]
for i in range(1, 11):
    fact.append(fact[-1]*i)

LIMIT = 1
while len(str(LIMIT * fact[9])) >= LIMIT:
    LIMIT += 1
LIMIT -= 1

def is_curious(n):
    num = [int(x) for x in str(n)]
    return n == sum(map(lambda x: fact[x], num))

result = sum(filter(lambda x: is_curious(x), range(10, 10**LIMIT)))
print(result)
