# Problem 9

square = lambda x: x**2
is_triplet = lambda x, y, z: square(x) + square(y) == square(z)

for i in range(998):
    a = i + 1
    for j in range(i, 1000 - i):
        b = j + 2
        c = 1000 - a - b
        if is_triplet(a, b, c):
            result = a*b*c

print(result)

