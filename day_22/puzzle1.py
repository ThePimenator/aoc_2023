import queue

import numpy as np
from shapely import Polygon

input = open('input.txt', 'r')
inputLines = np.array([x.split(" -> ") for x in [s.strip() for s in input.readlines()]])