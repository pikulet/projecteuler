# Problem 8

from functools import reduce

with open('008-input.txt', 'r') as f:
    data = f.readlines()
    data = data[0].split("0")

length = len(data)


def count_num_string(s, distance):
    if len(s) < distance:
        return 0

    s = [int(x) for x in s]
    greatest = 0
    for i in range(len(s) - distance + 1):
        product = reduce(lambda x, y: x * y, s[i: i + distance])
        greatest = max(product, greatest)

    return greatest


result = max(map(lambda x: count_num_string(x, 13), data))
print(result)
