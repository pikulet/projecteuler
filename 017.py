# Problem 17

LIMIT = 1000

ONES = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3]
TEENS = [0, 6, 6, 8, 8, 7, 7, 9, 8, 8]
TENS = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
HUNDRED = 7
AND = 3
ONE_THOUSAND = 11

def count_length(n):
    if n == 1000:
        return ONE_THOUSAND

    result = 0
    d1 = n // 100
    d2 = n % 100
    
    if d1 >= 1:
        result += ONES[d1] + HUNDRED
        if d2 > 0:
            result += AND

    if d2 <= 10:
        result += ONES[d2]
    elif d2 < 20:
        result += TEENS[d2%10]
    else:
        result += TENS[d2//10]
        result += ONES[d2%10]

    return result
    
result = sum(map(lambda x: count_length(x), range(1, LIMIT + 1)))
print(result)
