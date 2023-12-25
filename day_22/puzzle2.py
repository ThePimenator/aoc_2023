import queue
import sys
import numpy as np

input = open('input.txt', 'r')
output = open('output.txt', 'w')
inputLines = np.array([x.split("~") for x in [s.strip() for s in input.readlines()]])

inputChanged = []

Q = queue.PriorityQueue()
placed = set()

for i in range(len(inputLines)):
    Q.put((int(inputLines[i][0].split(",")[2]), [tuple([int(x) for x in inputLines[i][0].split(",")]), tuple([int(x) for x in inputLines[i][1].split(",")])]))

field = np.full((10,10), 0) 

while not Q.empty():
    z_low, coord = Q.get()
    output.write(str(z_low) + " - " + str(coord) + "\n")
    max_height = float("-inf")
    for x in range(coord[0][0], coord[1][0]+1):
        for y in range(coord[0][1], coord[1][1]+1):
            max_height = max(max_height, field[x][y]+1)

    difference = z_low - max_height
    placed.add(tuple([tuple([coord[0][0], coord[0][1], coord[0][2] - difference]), tuple([coord[1][0], coord[1][1], coord[1][2] - difference])]))

    for x in range(coord[0][0], coord[1][0]+1):
        for y in range(coord[0][1], coord[1][1]+1):
            assert coord[1][2] - difference > field[x][y]
            field[x][y] = coord[1][2] - difference

    output.write(str(coord[0][0]) + ", " + str(coord[0][1]) + ", " + str(coord[0][2] - difference) + 
                 " - " + str(coord[1][0]) + ", " + str(coord[1][1]) + ", " + str(coord[1][2] - difference)+"\n\n")
    
    for i in field: 
        output.write(str(i)+"\n")
    output.write("\n")

fieldPlace = np.full((200,10,10), -1) 

for x in range(10):
        for y in range(10):
            fieldPlace[0][x][y] = 0

blockNr = 1
for block in placed: 
    for x in range(block[0][0], block[1][0]+1):
        for y in range(block[0][1], block[1][1]+1):
            for z in range(block[0][2], block[1][2]+1):
                assert fieldPlace[z][x][y] == -1
                fieldPlace[z][x][y] = blockNr
    blockNr += 1

np.set_printoptions(threshold=sys.maxsize)
for i in range(200):
    output.write(np.array2string(fieldPlace[i]))
    output.write("\n\n")

links = {}

for block in placed:
    blocks_below = set()
    for x in range(block[0][0], block[1][0]+1):
        for y in range(block[0][1], block[1][1]+1):
            if fieldPlace[block[0][2]-1][x][y] not in blocks_below and fieldPlace[block[0][2]-1][x][y] != -1:
                blocks_below.add(fieldPlace[block[0][2]-1][x][y])

    assert len(blocks_below) > 0
    links[fieldPlace[block[0][2]][x][y]] = blocks_below

for i in links:
    removedBlocks = set()
    for j in links:
        if i in links[j]:
            links[j].remove(i)
    removedBlocks.add(i) 
    print(removedBlocks)

# werkt niet helemaal 
# print(links)