# Problem 67

with open('067-input.txt', 'r') as f:
    data = f.readlines()
    map_int = lambda row: list(map(lambda x: int(x), row.split()))
    data = list(map(map_int, data))

num_rows = len(data)

def process_row(row_num):
    for i, value in enumerate(data[row_num]):
        next_row = data[row_num + 1]
        data[row_num][i] += max(next_row[i], next_row[i + 1])
        
for row_num, row in enumerate(reversed(data)):
    if row_num == 0:
        continue
    process_row(num_rows - row_num - 1)

result = data[0][0]
print(result)
