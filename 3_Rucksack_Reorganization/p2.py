# Answer: 2499

priority = 0
with open("input/3.txt", "r") as input:
    groups = [line.strip() for line in input]
    for i in range(0, len(groups), 3):
        front = set(groups[i])
        middle = set(groups[i+1])
        back = set(groups[i+2])
        group = back.intersection(front.intersection(middle)).pop()
        if group.isupper():
            priority += ord(group) - 38
        else:
            priority += ord(group) - 96
print(priority)
