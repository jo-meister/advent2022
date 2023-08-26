# Answer: 1926


class Knot():
    def __init__(self):
        self.x = 0
        self.y = 0


rope = []
for i in range(10):
    rope.append(Knot())
visited = set()
visited.add((rope[9].x, rope[9].y))
with open("input/9.txt", "r") as input:
    for line in input:
        move = line.strip().split(' ')
        if move[0] == 'U':
            for i in range(int(move[1])):
                rope[0].y += 1
                for i in range(9):
                    if rope[i+1].x == rope[i].x and abs(rope[i].x - rope[i+1].x) + abs(rope[i].y - rope[i+1].y) > 1:
                        rope[i+1].y += 1
                    elif abs(rope[i].x - rope[i+1].x) + abs(rope[i].y - rope[i+1].y) > 2:
                        rope[i+1].x = rope[i].x
                        rope[i+1].y += 1
                visited.add((rope[9].x, rope[9].y))
        elif move[0] == 'D':
            for i in range(int(move[1])):
                rope[0].y -= 1
                for i in range(9):
                    if rope[i+1].x == rope[i].x and abs(rope[i].x - rope[i+1].x) + abs(rope[i].y - rope[i+1].y) > 1:
                        rope[i+1].y -= 1
                    elif abs(rope[i].x - rope[i+1].x) + abs(rope[i].y - rope[i+1].y) > 2:
                        rope[i+1].x = rope[i].x
                        rope[i+1].y -= 1
                visited.add((rope[9].x, rope[9].y))
        elif move[0] == 'L':
            for i in range(int(move[1])):
                rope[0].x -= 1
                for i in range(9):
                    if rope[i+1].y == rope[i].y and abs(rope[i].x - rope[i+1].x) + abs(rope[i].y - rope[i+1].y) > 1:
                        rope[i+1].x -= 1
                    elif abs(rope[i].x - rope[i+1].x) + abs(rope[i].y - rope[i+1].y) > 2:
                        rope[i+1].y = rope[i].y
                        rope[i+1].x -= 1
                visited.add((rope[9].x, rope[9].y))
        elif move[0] == 'R':
            for i in range(int(move[1])):
                rope[0].x += 1
                for i in range(9):
                    if rope[i+1].y == rope[i].y and abs(rope[i].x - rope[i+1].x) + abs(rope[i].y - rope[i+1].y) > 1:
                        rope[i+1].x += 1
                    elif abs(rope[i].x - rope[i+1].x) + abs(rope[i].y - rope[i+1].y) > 2:
                        rope[i+1].y = rope[i].y
                        rope[i+1].x += 1
                visited.add((rope[9].x, rope[9].y))
print(len(visited))
