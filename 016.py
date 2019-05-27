# Problem 16

BASE = 2
POWER = 1000

square = lambda x: x**2

def exp(base, power):
    if power == 1:
        return base
    elif power % 2 == 0:
        return square(exp(base, power//2))
    else:
        return base * exp(base, power - 1)

digits = [int(x) for x in str(exp(BASE, POWER))]
result = sum(digits)
print(result)
