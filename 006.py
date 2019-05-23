# Problem 6

sum_of_squares = sum(map(lambda x: x**2, range(1,101)))
square_of_sum = sum(range(1,101))**2
result = square_of_sum - sum_of_squares

print(result)
