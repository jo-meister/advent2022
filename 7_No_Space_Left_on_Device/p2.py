# Answer: 7490863


class Dir:
    def __init__(self, parent):
        self.parent_idx = parent
        self.children = []
        self.file_space = 0
        self.visited = False


def dir_space(cd):
    for i in cd.children:
        if not dirs[i].visited:
            dir_space(dirs[i])
            dirs[i].visited = True
        cd.file_space += dirs[i].file_space


cd = Dir(None)
idx = 0
dirs = [cd]
with open("input/7.txt", "r") as input:
    for line in input:
        command = line.strip().split(' ')
        if command[0] == '$':
            if command[1] == 'ls':
                continue
            elif command[2] == '/':
                cd = dirs[0]
            elif command[2] == '..':
                idx = cd.parent_idx
                cd = dirs[cd.parent_idx]
            else:
                cd = Dir(idx)
                dirs.append(cd)
                idx = len(dirs) - 1
                dirs[cd.parent_idx].children.append(idx)
        elif command[0] == 'dir':
            continue
        else:
            cd.file_space += int(command[0])

dir_space(dirs[0])
space_needed = dirs[0].file_space - 40000000
min_delete = dirs[0].file_space
for dir in dirs:
    if dir.file_space >= space_needed and dir.file_space < min_delete:
        min_delete = dir.file_space
print(min_delete)
