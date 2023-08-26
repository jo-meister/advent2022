# Answer: WHTLRMZRC

crates = [[] for i in range(9)]
with open("input/5.txt", "r") as input:
    for line in input:
        if line.startswith('move'):
            procedure = line.split(' ')
            for i in range(int(procedure[1])):
                move = crates[int(procedure[3])-1].pop()
                crates[int(procedure[5])-1].append(move)
        elif line == '\n':
            for i in range(len(crates)):
                crates[i].reverse()
            continue
        elif line[1] == '1':
            continue
        else:
            for i in range(9):
                if line[i*4+1] != ' ':
                    x = crates[i]
                    x.append(line[i*4+1])
                    crates[i] = x
top = ""
for stack in crates:
    top += stack.pop()
print(top)
