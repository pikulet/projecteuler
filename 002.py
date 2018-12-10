# Problem 2

fibbo_table = [1,2]

# Generating the fibonacci table
check = 0
i = 2

while check < 4000000:
    next_fibbo = fibbo_table[i-1] + fibbo_table[i-2]
    fibbo_table.append(next_fibbo)
    check = fibbo_table[i]
    i+=1

# Sums the even-valued Fibbonacci numbers
result = 0

for fibbo_number in fibbo_table:
    if fibbo_number%2 == 0:
        result += fibbo_number

print(result)
