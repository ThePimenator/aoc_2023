import queue
import numpy as np
from sortedcontainers import SortedSet

input = open('input.txt', 'r')
output = open('output.txt', 'w')
inputLines = np.array([list(x) for x in [s.strip() for s in input.readlines()]])
inputLines[65][65] = "."
copyInputLines = inputLines
# 131 131 (65,65)


Q = SortedSet()
Q.add((0, (65,65)))

while len(Q)>0:
    step, (y,x) = Q.pop(0)
    print(step)
    if step == 64:
        Q.add((step, (y,x)))
        break
    for dir in [(0,1), (0,-1), (1,0), (-1,0)]:
        y_next = y + dir[0]
        x_next = x + dir[1]
        if y_next < 0 or y_next > 130 or x_next < 0 or x_next > 130:
            continue
        elif inputLines[y_next][x_next] == ".":
            Q.add((step+1, (y_next,x_next)))

print(len(Q)) 