# Answer: 6486

hx = 0
hy = 0
tx = 0
ty = 0
visited = set()
visited.add((tx, ty))
with open("input/9.txt", "r") as input:
    for line in input:
        move = line.strip().split(' ')
        if move[0] == 'U':
            for i in range(int(move[1])):
                hy += 1
                if tx == hx and abs(hx - tx) + abs(hy - ty) > 1:
                    ty += 1
                    visited.add((tx, ty))
                elif abs(hx - tx) + abs(hy - ty) > 2:
                    tx = hx
                    ty += 1
                    visited.add((tx, ty))
        elif move[0] == 'D':
            for i in range(int(move[1])):
                hy -= 1
                if tx == hx and abs(hx - tx) + abs(hy - ty) > 1:
                    ty -= 1
                    visited.add((tx, ty))
                elif abs(hx - tx) + abs(hy - ty) > 2:
                    tx = hx
                    ty -= 1
                    visited.add((tx, ty))
        elif move[0] == 'L':
            for i in range(int(move[1])):
                hx -= 1
                if ty == hy and abs(hx - tx) + abs(hy - ty) > 1:
                    tx -= 1
                    visited.add((tx, ty))
                elif abs(hx - tx) + abs(hy - ty) > 2:
                    ty = hy
                    tx -= 1
                    visited.add((tx, ty))
        elif move[0] == 'R':
            for i in range(int(move[1])):
                hx += 1
                if ty == hy and abs(hx - tx) + abs(hy - ty) > 1:
                    tx += 1
                    visited.add((tx, ty))
                elif abs(hx - tx) + abs(hy - ty) > 2:
                    ty = hy
                    tx += 1
                    visited.add((tx, ty))
print(len(visited))
