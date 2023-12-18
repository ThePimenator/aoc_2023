input = open('input.txt', 'r')
inputLines = [[x.strip() for x in s if x.strip()] for s in input.readlines()]

last_pos = -1
index = 0
load = 0

for j in range(len(inputLines[0])):
    while index < len(inputLines):
        match inputLines[index][j]:
            case ".":        
                if last_pos < 0:
                    last_pos = index 
                    if j == 5:
                        print("last_pos = " + str(index))
            case "#":
                last_pos = -1
                if j == 5:
                    print("last_pos = -1")
            case "O":
                if last_pos >= 0:
                    inputLines[index][j] = "."
                    inputLines[last_pos][j] = "O"
                    index = last_pos
                    last_pos = -1
                    if j == 5:
                        print("last_pos = " + str(index))


        index += 1
    index = 0
    last_pos = -1

for i in inputLines:
    print("".join(i))

for j in range(len(inputLines[0])):
    for i in range(len(inputLines)):
        if inputLines[i][j] == "O":
            load += len(inputLines) - i

print(load)