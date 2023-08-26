# Answer: 14620 - 14960

X = 1
cycle = 0
stage = 20
total_strength = 0

with open('input/10.txt', 'r') as input:

    for line in input:
        cycle += 1
        if stage == 260:
            break
        elif cycle == stage:
            print(f'{cycle}*{X}')
            total_strength += cycle * X
            stage += 40
        instruction = line.strip().split(' ')
        if instruction[0] == 'addx':
            cycle += 1
            X += int(instruction[1])
            if cycle == stage:
                print(f'{cycle}*{X}')
                total_strength += cycle * (X)
                stage += 40

print(total_strength)
