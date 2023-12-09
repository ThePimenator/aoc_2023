input = open('input.txt', 'r')
inputLines = input.readlines()
sequences = [s.strip().split(" ") for s in inputLines]

sum = 0

for s in sequences:
    steps = []
    steps.append([int(c) for c in s])
    while not all(c == 0 for c in steps[-1]):
        new_step = []
        for i in range(len(steps[-1])-1):
            new_step.append(steps[-1][i+1]-steps[-1][i])
        steps.append(new_step)
    
    steps[-1].append(0)

    for i in range(len(steps)-2, -1, -1):
        steps[i].append(steps[i][-1] + steps[i+1][-1])
    
    sum += steps[0][-1]

print(sum)