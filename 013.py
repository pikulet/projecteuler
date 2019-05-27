# Problem 13

with open('013-input.txt', 'r') as f:
    data = f.readlines()

def sum_row(row):
    s = sum([int(x) for x in row.split()])
    return s

total = sum(map(lambda x: sum_row(x), data))
result = str(total)[:10]
print(result)

