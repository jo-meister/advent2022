# Answer: 1034

with open("input/6.txt", "r") as input:
    signal = input.readline()
    for i in range(len(signal)):
        if len(set(signal[i:i+4])) == 4:
            print(i+4)
            break
