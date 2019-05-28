# Problem 23

LIMIT = 28123

def get_divisor_sum(n):
    return sum(filter(lambda x: n % x == 0, range(1, n)))

abundant = list(filter(lambda x: get_divisor_sum(x) > x, range(1, LIMIT + 1)))

def fulfils_sum(n):
    left = 0
    right = len(abundant) - 1

    while left != right:
        current = abundant[left] + abundant[right]
        if current == n:
            return True
        elif current < n:
            left += 1
        else:
            right -= 1

    if 2 * abundant[left] == n:
        return True
    
    return False

result = sum(filter(lambda x: not fulfils_sum(x), range(1, LIMIT + 1)))
print(result)
