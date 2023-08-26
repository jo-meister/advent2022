# Answer: 595

containers = 0
with open("input/4.txt", "r") as input:
    for pair in input:
        ranges = pair.split(',')
        first = ranges[0].split('-')
        second = ranges[1].split('-')
        if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]):
            containers += 1
        elif int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1]):
            containers += 1
print(containers)
