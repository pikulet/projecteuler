# Problem 14

LIMIT = 1000000

chain_length = {}
chain_length[1] = 1
longest = (1, 1)

def process_collatz(n):
    if n in chain_length:
        return chain_length[n]

    if n % 2 == 0:
        result = 1 + process_collatz(n/2)
    else:
        result = 1 + process_collatz(3*n + 1)

    chain_length[n] = result
    return result
    
for i in range(1, LIMIT + 1):
    result = process_collatz(i)
    if result > longest[1]:
        longest = i, result

result = longest[0]
print(result)
