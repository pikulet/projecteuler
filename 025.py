# Problem 25

NUM_DIGITS = 1000

f_1 = 1
f_2 = 1

result = 2
while f_2 // 10**(NUM_DIGITS - 1) == 0:
    f_1, f_2 = f_2, f_1 + f_2
    result += 1

print(result)
