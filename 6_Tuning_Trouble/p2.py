# Answer: 2472

with open("input/6.txt", "r") as input:
    signal = input.readline()
    for i in range(len(signal)):
        if len(set(signal[i:i+14])) == 14:
            print(i+14)
            break
