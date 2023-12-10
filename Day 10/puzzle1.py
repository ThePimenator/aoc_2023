import queue

input = open('input.txt', 'r')
inputLines = [s.strip() for s in input.readlines()]
height = len(inputLines)
width = len(inputLines[0])
distanceM = [["." for i in range(height)] for j in range(width)]

startingPoint = inputLines[83][25]
distanceM[83][25] = 0

Q = queue.PriorityQueue();
Q.put((0, (83,25)))
max = 0

while not Q.empty():
    item = Q.get()
    up = (item[1][0] - 1, item[1][1]) if item[1][0] - 1 >= 0 and inputLines[item[1][0]][item[1][1]] in ["S", "|", "J", "L"] else None
    down = (item[1][0] + 1, item[1][1]) if item[1][0] + 1 < height and inputLines[item[1][0]][item[1][1]] in ["S", "|", "7", "F"] else None
    left = (item[1][0], item[1][1] - 1) if item[1][1] - 1 >= 0 and inputLines[item[1][0]][item[1][1]] in ["S", "-", "J", "7"] else None
    right = (item[1][0], item[1][1] + 1) if item[1][1] + 1 < width and inputLines[item[1][0]][item[1][1]] in ["S", "-", "F", "L"] else None
    distanceM[item[1][0]][item[1][1]] = item[0]

    if (not up is None) and inputLines[up[0]][up[1]] in ["7", "|", "F"] and distanceM[up[0]][up[1]] == ".":
        Q.put((item[0] + 1, up))
    if (not down is None) and inputLines[down[0]][down[1]] in ["J", "|", "L"] and distanceM[down[0]][down[1]] == ".":
        Q.put((item[0] + 1, down))
    if (not left is None) and inputLines[left[0]][left[1]] in ["L", "-", "F"] and distanceM[left[0]][left[1]] == ".":
        Q.put((item[0] + 1, left))
    if (not right is None) and inputLines[right[0]][right[1]] in ["J", "-", "7"] and distanceM[right[0]][right[1]] == ".":
        Q.put((item[0] + 1, right))
     
    if item[0] > max:
        max = item[0]


print(max)
