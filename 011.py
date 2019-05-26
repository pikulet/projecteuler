# Problem 11

STREAK_LENGTH = 4

with open('011-input.txt', 'r') as f:
    data = f.readlines()
    grid = list(map(lambda x:
                    list(map(lambda y: int(y), x.split())),
                    data))

def rotate_right(grid):
    new_grid = list()
    for i in range(len(grid[0])):
        new_grid.append(list(reversed(list(map(lambda x: x[i], grid)))))
    return new_grid

def get_product(it):
    p = 1
    for x in it:
        if x == 0:
            return 0
        p *= x
    return p
    
def get_max_horizontal(grid):
    return max(map(lambda x: get_max_row(x), grid))

def get_max_row(row):
    max_product = 0
    for i in range(len(row) - STREAK_LENGTH + 1):
        p = get_product(row[i: i + STREAK_LENGTH])
        max_product = max(p, max_product)
    return max_product

def get_max_diagonal(grid):
    max_product = 0
    for i in range(len(grid) - STREAK_LENGTH + 1):
        for j in range(len(grid[0]) - STREAK_LENGTH + 1):
            p = get_product(map(lambda x: grid[i+x][j+x], range(STREAK_LENGTH)))
            max_product = max(p, max_product)
    return max_product

grid_r = rotate_right(grid)
result = max(get_max_horizontal(grid), get_max_diagonal(grid),
             get_max_horizontal(grid_r), get_max_diagonal(grid_r))
print(result)    
