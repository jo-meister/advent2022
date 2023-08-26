# Answer: 1835

grid = []

with open('input/8.txt', 'r') as input:

    for line in input:
        row = []
        for char in line.strip():
            row.append(int(char))
        grid.append(row)

num_rows = len(grid)
num_cols = len(grid[0])
visibile = [[0 for i in range(num_cols)] for i in range(num_rows)]

# Look from Left
for i in range(num_rows):
    tallest = -1
    for j in range(num_cols):
        if grid[i][j] > tallest:
            tallest = grid[i][j]
            visibile[i][j] = 1
        else:
            continue

# Look from Right
for i in range(num_rows):
    tallest = -1
    for j in reversed(range(num_cols)):
        if grid[i][j] > tallest:
            tallest = grid[i][j]
            visibile[i][j] = 1
        else:
            continue

# Look from Top
for j in range(num_cols):
    tallest = -1
    for i in range(num_rows):
        if grid[i][j] > tallest:
            tallest = grid[i][j]
            visibile[i][j] = 1
        else:
            continue

# Look from Left
for j in range(num_cols):
    tallest = -1
    for i in reversed(range(num_rows)):
        if grid[i][j] > tallest:
            tallest = grid[i][j]
            visibile[i][j] = 1
        else:
            continue

# Count total visible
num_visible = 0
for i in range(num_rows):
    for j in range(num_cols):
        if visibile[i][j] == 1:
            num_visible += 1

print(num_visible)
