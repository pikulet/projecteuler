MAX_INDEX = 100
MIN_FOUND = 23
THRESHOLD = 1000000

def gen_fact():
    fact = [1]*101
    k = 1
    for i in range(2, MAX_INDEX + 1):
        k *= i
        fact[i] = k
    return fact

choose = lambda n, r: fact[n]/fact[r]/fact[n-r]

def binary_find_r(n):
    left = 1
    right = n
    while left < right:
        r = ( left + right ) // 2
        r_val = choose(n, r)
        if r_val > THRESHOLD:
            right = r
        elif r_val < THRESHOLD:
            left = r + 1
        else:
            return r + 1
    return left
        
fact = gen_fact()
result = sum(map(lambda x: x + 1 - 2 * binary_find_r(x), range(MIN_FOUND, MAX_INDEX + 1)))
print(result)
