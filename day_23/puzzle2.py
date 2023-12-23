import queue
import numpy as np
from sortedcontainers import SortedSet
import sys
np.set_printoptions(threshold=sys.maxsize)

input = open('input.txt', 'r')
output = open('output.txt', 'w')
inputLines = np.array([list(x) for x in [s.strip() for s in input.readlines()]])

print(len(inputLines[0]))

Q = queue.PriorityQueue()
Q.put((0,(0,1), set()))


# def solve(l, y,x visited):
#     print(l, y,x, visited, inputLines[y][x])
#     assert len(visited) == l
#     if y == 140 and x == 139:
#         print(l)
#         print(len(visited))
#         if l > 1000:
#             for v in visited: 
#                 inputLines[v[0]][v[1]] = "O"
#             for i in inputLines:
#                 output.write("".join(i) + "\n")
    



while not Q.empty():
    l, coord, visited = Q.get()
    y,x = coord
    # print(l, y,x, inputLines[y][x])
    assert len(visited) == l
    if y == 140 and x == 139:
        print(l)
    visited_next = set(visited)
    visited_next.add((y,x))
    # print(visited_next)

    if inputLines[y][x] in [".", "<", ">", "v"]:
        for d in [(0,1), (0,-1), (1,0), (-1,0)]:
            if y+d[0] >= 0 and y+d[0] < 141 and x+d[1] >= 0 and x+d[1] < 141 and (not (y+d[0],x+d[1]) in visited) and inputLines[y+d[0]][x+d[1]] in [".", "<", ">", "v"]:
                Q.put((l+1, (y+d[0],x+d[1]), visited_next))

