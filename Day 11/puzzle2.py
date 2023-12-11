input = open('input.txt', 'r')
inputLines = [s.strip() for s in input.readlines()]

rowCount = [0]*len(inputLines[0])
columnCount = [0]*len(inputLines)
distanceRow = [1]*len(inputLines[0])
distanceCol = [1]*len(inputLines)
countNr = 0



def findcoor(number):
    for i in range(len(inputLines)):
        for j in range(len(inputLines[i])):
            if inputLines[i][j] == number:
                return i,j
    return None

# Create unique number and count
for i in range(len(inputLines)):
    inputLines[i] = list(inputLines[i])
    for j in range(len(inputLines[i])):
        if inputLines[i][j] == "#":
            rowCount[i] += 1
            columnCount[j] += 1
            countNr += 1
            inputLines[i][j] = countNr

# expand
for i in range(len(rowCount)-1, -1, -1):
    if rowCount[i] == 0:
        distanceRow[i] = 1000000
    if columnCount[i] == 0:
        distanceCol[i] = 1000000

print(distanceCol)
print(distanceRow)


coords = []

i = 1
while not findcoor(i) is None:
    coords.append(findcoor(i)) 
    i += 1

distance = 0

print(coords)

for c2 in range(len(coords)):
    for c1 in range(len(coords)):
        if c2 > c1:
            y1, x1 = coords[c1]
            y2, x2 = coords[c2]
            xi = x1 + 1 if x1 <= x2 else x2 + 1
            yi = y1 + 1 if y1 <= y1 else y2 + 1

            while xi <= max(x1,x2):
                distance += distanceCol[xi]
                xi += 1
            
            while yi <= max(y1,y2):
                distance += distanceRow[yi]
                yi += 1

            print(distance)