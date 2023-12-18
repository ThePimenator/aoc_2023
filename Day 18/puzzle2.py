import queue
import numpy as np
from shapely import Polygon

input = open('input.txt', 'r')
inputLines = np.array([x.split(" ") for x in [s.strip() for s in input.readlines()]])

coords = [(0,0)]

count = 0

for i in inputLines: 
    steps = int(i[2][2:7],16)
    count += steps

    match i[2][7]:
        case "0": #R
            coords.append((coords[-1][0],coords[-1][1]+steps))
        case "2": #L
            coords.append((coords[-1][0],coords[-1][1]-steps))
        case "3": #U
            coords.append((coords[-1][0]-steps,coords[-1][1]))
        case "1": #D
            coords.append((coords[-1][0]+steps,coords[-1][1]))

polygon = Polygon(coords)
print(int(polygon.area + count /2 + 1))