import queue
import numpy as np
from shapely import Polygon

input = open('input.txt', 'r')
inputLines = np.array([x.split(" ") for x in [s.strip() for s in input.readlines()]])

coords = [(0,0)]

count = 0

for i in inputLines: 
    count+= int(i[1])
    match i[0]:
        case "R":
            coords.append((coords[-1][0],coords[-1][1]+int(i[1])))
        case "L":
            coords.append((coords[-1][0],coords[-1][1]-int(i[1])))
        case "U":
            coords.append((coords[-1][0]-int(i[1]),coords[-1][1]))
        case "D":
            coords.append((coords[-1][0]+int(i[1]),coords[-1][1]))


polygon = Polygon(coords)
print(int(polygon.area + count /2 + 1))