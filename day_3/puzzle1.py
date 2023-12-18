
input = open('input.txt', 'r')
inputLines = input.readlines()

sum = 0 

lineNr = 0

def checkPartNr(lineNr, beginNr, endNr):
    for i in range(beginNr-1, endNr + 2):
        for j in range(lineNr-1, lineNr + 2):
            if i < 140 and i >= 0 and j < 140 and j >= 0:
                if not (inputLines[j][i] == ".") and not (inputLines[j][i].isdigit()):
                    return True
            
    return False

for i in range(len(inputLines)):
    # Get the number of the game and the grabs
    nr = ""
    for j in range(len(inputLines[i].rstrip())):
        if inputLines[i][j].isdigit():
            nr += inputLines[i][j]
        elif not inputLines[i][j].isdigit() and not nr == "":
            if checkPartNr(i,j- len(nr) ,j-1):
                sum += int(nr)
            nr = ""
    if (not nr == "") and checkPartNr(i,len(inputLines[i].rstrip())-(1 + len(nr)) ,len(inputLines[i].rstrip())-1):
        sum += int(nr)

print(sum)


    