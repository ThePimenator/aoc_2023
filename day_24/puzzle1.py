import queue
import numpy as np
from shapely import LineString, intersection, geometry
import sys
np.set_printoptions(threshold=sys.maxsize)

input = open('input.txt', 'r')
inputLines = np.array([x.split(" @ ") for x in [s.strip() for s in input.readlines()]])

hails = set()

for i in inputLines:
    h = tuple([int(x) for x in i[0].split(", ")]), tuple([int(x) for x in i[1].split(", ")]) 
    hails.add(h)

min_xy = 200000000000000
max_xy = 400000000000000

points = 0

def in_area(x,y):
    return x >= min_xy and x <= max_xy and y >= min_xy and y <= max_xy

while len(hails) > 0:
    h1 = hails.pop()
    x1_1,y1_1 = h1[0][0], h1[0][1]
    x1_2,y1_2 = h1[0][0]+4000000000000000*h1[1][0], h1[0][1]+4000000000000000*h1[1][1]

    h1 = LineString([(x1_1,y1_1), (x1_2,y1_2)])

    for h2 in hails: 
        x2_1,y2_1 = h2[0][0], h2[0][1]
        x2_2,y2_2 = h2[0][0]+4000000000000000*h2[1][0], h2[0][1]+4000000000000000*h2[1][1]

        h2 = LineString([(x2_1,y2_1), (x2_2,y2_2)])

        intersec = h1.intersection(h2)

        if not intersec.is_empty and in_area(intersec.x, intersec.y):
            points += 1




print(points)