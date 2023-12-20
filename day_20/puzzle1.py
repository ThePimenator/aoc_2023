import queue
import numpy as np
from shapely import Polygon

input = open('input.txt', 'r')
inputLines = np.array([x.split(" -> ") for x in [s.strip() for s in input.readlines()]])

rules = {}

high = 0
low = 0

# print(inputLines)

for i in inputLines:
    if i[0] == "broadcaster":
        rules["broadcaster"] = ["b", [x for x in i[1].split(", ")]]
    elif i[0][0] == "%":
        rules[i[0]] = ["off", [x for x in i[1].split(", ")]]
    elif i[0][0] == "&":
        state = {}
        rules[i[0]] = [state, [x for x in i[1].split(", ")]]

for i in rules:
    for j in rules[i][1]:
        if "&" + j in rules:
            rules["&" + j][0].update({i: 0})
# for i in rules:
#     print(i, rules[i])

# print()

p = 0
Q = queue.PriorityQueue()

for attempt in range(1000):
    Q.put((p, ("button", 0, "broadcaster")))
    p += 1
    low += 1
    
    while not Q.empty():
        prio, (source, signal, dest) = Q.get()

        if dest == "broadcaster":
            for new_dest in rules["broadcaster"][1]:               
                Q.put((p, ("broadcaster", 0, new_dest)))   
                p += 1
                low += 1
        elif "%" + dest in rules:
            if not signal:
                if rules["%" + dest][0] == "off":
                    rules["%" + dest][0] = "on"
                    for new_dest in rules["%" + dest][1]:
                        Q.put((p, ("%" + dest, 1, new_dest)))    
                        p += 1
                        high += 1     
                else:
                    rules["%" + dest][0] = "off"
                    for new_dest in rules["%" + dest][1]:
                        Q.put((p, ("%" + dest, 0, new_dest))) 
                        p += 1
                        low += 1
        elif "&" + dest in rules: 
            rules["&" + dest][0][source] = signal
            highpulse = True
            for j in rules["&" + dest][0]:
                if not rules["&" + dest][0][j]:
                    highpulse = False
                    break
            
            if highpulse: 
                for new_dest in rules["&" + dest][1]:
                        Q.put((p, ("&" + dest, 0, new_dest)))     
                        p += 1
                        low += 1    
            else: 
                for new_dest in rules["&" + dest][1]:
                        Q.put((p, ("&" + dest, 1, new_dest)))        
                        p += 1
                        high += 1 

print(high*low)

