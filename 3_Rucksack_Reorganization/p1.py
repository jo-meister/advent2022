# Answer: 7793

priority = 0
with open("input/3.txt", "r") as input:
    for rucksack in input:
        n = len(rucksack) // 2
        front = set(rucksack[:n])
        back = set(rucksack[n:])
        in_both = front.intersection(back).pop()
        if in_both.isupper():
            priority += ord(in_both) - 38
        else:
            priority += ord(in_both) - 96
print(priority)
