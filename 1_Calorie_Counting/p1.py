# Answer: 66487

most_calories = 0
current_calories = 0
with open("input/1.txt", "r") as input:
    for calories in input:
        if calories == '\n':
            if current_calories > most_calories:
                most_calories = current_calories
            current_calories = 0
        else:
            current_calories += int(calories)
print(most_calories)
