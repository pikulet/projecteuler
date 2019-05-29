# Problem 28

DIMENSION = 1001
mid = DIMENSION//2

def corner_sum(n):
    result = 0
    length = 2*n - 1
    top_sum = length**2
    for i in range(4):
        result += top_sum
        top_sum -= (length - 1)
    return result

result = 1 # middle value
result += sum(map(lambda x: corner_sum(x + 2), range(mid)))
print(result)
