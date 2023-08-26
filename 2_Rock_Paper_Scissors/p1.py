# Answer: 13536

score = 0
with open("input/2.txt", "r") as input:
    for game in input:
        if game[2] == 'X':
            if game[0] == 'A':
                score += 4
            elif game[0] == 'B':
                score += 1
            elif game[0] == 'C':
                score += 7
        if game[2] == 'Y':
            if game[0] == 'A':
                score += 8
            elif game[0] == 'B':
                score += 5
            elif game[0] == 'C':
                score += 2
        if game[2] == 'Z':
            if game[0] == 'A':
                score += 3
            elif game[0] == 'B':
                score += 9
            elif game[0] == 'C':
                score += 6
print(score)
