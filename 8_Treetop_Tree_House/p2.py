# Answer: 263670

grid = []

with open('input/8.txt', 'r') as input:

    for line in input:
        row = []
        for char in line.strip():
            row.append(int(char))
        grid.append(row)

num_rows = len(grid)
num_cols = len(grid[0])
score = [[1 for i in range(num_cols)] for j in range(num_rows)]

for i in range(1, num_rows-1):
    for j in range(1, num_cols-1):
        multiplier = 0
        # Look Right
        for k in range(j+1, num_cols, 1):
            multiplier += 1
            if grid[i][j] <= grid[i][k]:
                break
        score[i][j] *= multiplier
        multiplier = 0
        # Look Left
        for k in range(j-1, -1, -1):
            multiplier += 1
            if grid[i][j] <= grid[i][k]:
                break
        score[i][j] *= multiplier
        multiplier = 0
        # Look Down
        for k in range(i+1, num_cols, 1):
            multiplier += 1
            if grid[i][j] <= grid[k][j]:
                break
        score[i][j] *= multiplier
        multiplier = 0
        # Look Up
        for k in range(i-1, -1, -1):
            multiplier += 1
            if grid[i][j] <= grid[k][j]:
                break
        score[i][j] *= multiplier
        multiplier = 0

# Count total visible
high_score = 0
for i in range(num_rows):
    for j in range(num_cols):
        if score[i][j] > high_score:
            high_score = score[i][j]

print(high_score)
