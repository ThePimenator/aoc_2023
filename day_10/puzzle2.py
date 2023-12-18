import queue
from matplotlib.path import Path

input = open('input.txt', 'r')
inputLines = [s.strip() for s in input.readlines()]
height = len(inputLines)
width = len(inputLines[0])
distanceM = [["." for i in range(height)] for j in range(width)]
mazeBig = [[" " for i in range(3*height)] for j in range(3*width)]

startingPoint = inputLines[83][25]

verts = [
   (83, 25),  # left, bottom
]

codes = [
    Path.MOVETO,
]

def process(point):
    verts.append(point)
    codes.append(Path.LINETO)
    up = (point[0] - 1, point[1]) if point[0] - 1 >= 0 and inputLines[point[0]][point[1]] in ["S", "|", "J", "L"] else None
    down = (point[0] + 1, point[1]) if point[0] + 1 < height and inputLines[point[0]][point[1]] in ["S", "|", "7", "F"] else None
    left = (point[0], point[1] - 1) if point[1] - 1 >= 0 and inputLines[point[0]][point[1]] in ["S", "-", "J", "7"] else None
    right = (point[0], point[1] + 1) if point[1] + 1 < width and inputLines[point[0]][point[1]] in ["S", "-", "F", "L"] else None
    distanceM[point[0]][point[1]] = inputLines[point[0]][point[1]]

    if (not up is None) and inputLines[up[0]][up[1]] in ["7", "|", "F"] and distanceM[up[0]][up[1]] == ".":
        process(up)
    if (not down is None) and inputLines[down[0]][down[1]] in ["J", "|", "L"] and distanceM[down[0]][down[1]] == ".":
        process(down)
    if (not left is None) and inputLines[left[0]][left[1]] in ["L", "-", "F"] and distanceM[left[0]][left[1]] == ".":
        process(left)
    if (not right is None) and inputLines[right[0]][right[1]] in ["J", "-", "7"] and distanceM[right[0]][right[1]] == ".":
        process(right)

item_next = (83,25)
item = (83,25)
while True:
    item = item_next
    up = (item[0] - 1, item[1]) if item[0] - 1 >= 0 and inputLines[item[0]][item[1]] in ["S", "|", "J", "L"] else None
    down = (item[0] + 1, item[1]) if item[0] + 1 < height and inputLines[item[0]][item[1]] in ["S", "|", "7", "F"] else None
    left = (item[0], item[1] - 1) if item[1] - 1 >= 0 and inputLines[item[0]][item[1]] in ["S", "-", "J", "7"] else None
    right = (item[0], item[1] + 1) if item[1] + 1 < width and inputLines[item[0]][item[1]] in ["S", "-", "F", "L"] else None
    distanceM[item[0]][item[1]] = inputLines[item[0]][item[1]]

    if (not up is None) and inputLines[up[0]][up[1]] in ["7", "|", "F"] and distanceM[up[0]][up[1]] == ".":
        item_next = up
    if (not down is None) and inputLines[down[0]][down[1]] in ["J", "|", "L"] and distanceM[down[0]][down[1]] == ".":
        item_next = down
    if (not left is None) and inputLines[left[0]][left[1]] in ["L", "-", "F"] and distanceM[left[0]][left[1]] == ".":
        item_next = left
    if (not right is None) and inputLines[right[0]][right[1]] in ["J", "-", "7"] and distanceM[right[0]][right[1]] == ".":
        item_next = right

    if item_next == (84, 25):
        break

    print(item_next)

    verts.append(item_next)
    codes.append(Path.LINETO)

verts.append((84, 25))
codes.append(Path.LINETO)
verts.append((83, 25))
codes.append(Path.CLOSEPOLY)

path = Path(verts, codes)

print(path)

countInner = 0

for i in range(width):
    for j in range(height):
        if (not [i, j] in verts) and path.contains_point((i, j)):
            countInner += 1
            print(i,j)




print(countInner)
