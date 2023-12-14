import numpy as np

input = open('input.txt', 'r')
inputLines = [[x.strip() for x in s if x.strip()] for s in input.readlines()]

inputLines = np.array(inputLines)

def turn(A):
    last_pos = -1
    index = 0
    for j in range(len(inputLines[0])):
        while index < len(inputLines):
            match inputLines[index][j]:
                case ".":        
                    if last_pos < 0:
                        last_pos = index 
                case "#":
                    last_pos = -1
                case "O":
                    if last_pos >= 0:
                        inputLines[index][j] = "."
                        inputLines[last_pos][j] = "O"
                        index = last_pos
                        last_pos = -1


            index += 1
        index = 0
        last_pos = -1
    
    return A


for j in range(1000):
    if j % 100 == 0:
        print(j)
    for i in range(4):
        inputLines = turn(inputLines)
        inputLines = np.rot90(inputLines, axes=(1,0))

load = 0

for j in range(len(inputLines[0])):
    for i in range(len(inputLines)):
        if inputLines[i][j] == "O":
            load += len(inputLines) - i

print(load)