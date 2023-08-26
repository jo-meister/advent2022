# Answer: 952

overlap = 0
with open("input/4.txt", "r") as input:
    for pair in input:
        ranges = pair.split(',')
        first = ranges[0].split('-')
        second = ranges[1].split('-')
        if int(first[0]) <= int(second[1]) and int(first[1]) >= int(second[1]):
            overlap += 1
        elif int(second[0]) <= int(first[1]) and int(second[1]) >= int(first[1]):
            overlap += 1
print(overlap)
