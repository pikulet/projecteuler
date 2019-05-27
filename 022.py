# Problem 22

BASE = ord("a")

with open('022-input.txt', 'r') as f:
    data = f.read().split(",")
    data = set([x[1: -1] for x in data])

sorted_names = sorted(data)
get_name_score = lambda name: sum(map(lambda x: ord(x) - BASE + 1, name.lower()))

result = 0
for i, name in enumerate(sorted_names):
    result += (i + 1) * get_name_score(name)

print(result)
