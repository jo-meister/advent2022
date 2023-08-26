# Answer: 197301

first = 0
second = 0
third = 0
current_calories = 0
with open("input/1.txt", "r") as input:
    for calories in input:
        if calories == '\n':
            if current_calories > first:
                third = second
                second = first
                first = current_calories
            elif current_calories > second:
                third = second
                second = current_calories
            elif current_calories > third:
                third = current_calories
            current_calories = 0
        else:
            current_calories += int(calories)
print(first + second + third)
