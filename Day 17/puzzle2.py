import queue
import numpy as np

input = open('input.txt', 'r')
inputLines = np.array([[int(x) for x in s if x.strip()] for s in input.readlines()])

Q = queue.PriorityQueue()
Q.put((0, (0,1, (0,1), 1)))
Q.put((0, (1,0, (1,0), 1)))
min = 1e9

seen = set()

while not Q.empty():
    heat, (y,x,dir,distOne) = Q.get()

    print(heat, (y,x,dir,distOne))
    
    if x == 140 and y == 140 and heat < min:
        min = heat
        print(min)
    
    if ((y,x,dir, distOne)) in seen:
        continue
    else:
        seen.add((y,x,dir, distOne))

    if distOne < 10:
        if not (y+dir[0] > 140 or y+dir[0] < 0 or x+dir[1] > 140 or x+dir[1] < 0): 
            Q.put((heat + inputLines[y][x], (y+dir[0],x+dir[1], dir, distOne + 1)))
    if dir in [(1,0), (-1,0)] and distOne > 3:
        if not (x+1 > 140): 
            Q.put((heat + inputLines[y][x], (y,x+1, (0,1), 1)))
        if not (x-1 < 0): 
            Q.put((heat + inputLines[y][x], (y,x-1, (0,-1), 1)))
    if dir in [(0,-1), (0,1)] and distOne > 3:
        if not (y+1 > 140): 
            Q.put((heat + inputLines[y][x], (y+1,x, (1,0), 1)))
        if not (y-1 < 0): 
            Q.put((heat + inputLines[y][x], (y-1,x, (-1,0), 1)))


print(min + 5)