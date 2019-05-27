# Problem 15

import math

WIDTH = 20
HEIGHT = 20

f = math.factorial
choose = lambda n, r: f(n)/(f(r)*f(n - r))

result = int(choose(WIDTH + HEIGHT, WIDTH))
print(result)
