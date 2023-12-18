import queue
import numpy as np

input = open('input.txt', 'r')
inputLines = np.array([[x.strip() for x in s if x.strip()] for s in input.readlines()])
energizeMap = np.array([["."]*110]*110)
energizeMap_left = np.array([["."]*110]*110)
energizeMap_right = np.array([["."]*110]*110)
energizeMap_down = np.array([["."]*110]*110)
energizeMap_up = np.array([["."]*110]*110)


Q = queue.PriorityQueue();

max = 0

for l in range(110):
    for i in ["right", "down", "up", "left"]:
        energizeMap = np.array([["."]*110]*110)
        energizeMap_left = np.array([["."]*110]*110)
        energizeMap_right = np.array([["."]*110]*110)
        energizeMap_down = np.array([["."]*110]*110)
        energizeMap_up = np.array([["."]*110]*110)
        match i:
            case "up":
                Q.put((0, (109,l, i)))
            case "down":
                Q.put((0, (0,l, i)))
            case "left":
                Q.put((0, (l,109, i)))
            case "right":
                Q.put((0, (l,0, i)))

        while not Q.empty():
            item = Q.get()

            if item[1][0] > 109 or item[1][0] < 0 or item[1][1] > 109 or item[1][1] < 0:
                continue



            dir = item[1][2]

            # print(inputLines[item[1][0]][item[1][1]])

            energizeMap[item[1][0]][item[1][1]] = "#"

            match dir:
                case "right":
                    energizeMap_right[item[1][0]][item[1][1]] = "#"
                case "left":
                    energizeMap_left[item[1][0]][item[1][1]] = "#"
                case "down":
                    energizeMap_down[item[1][0]][item[1][1]] = "#"
                case "up":
                    energizeMap_up[item[1][0]][item[1][1]] = "#"

            match inputLines[item[1][0]][item[1][1]]:
                case ".":
                    match dir:
                        case "right":
                            if not (item[1][1]+1 < 109 and energizeMap_right[item[1][0]][item[1][1]+1] == "#"):
                                Q.put((item[0]+1, (item[1][0], item[1][1]+1, dir)))
                        case "left":
                            if not (item[1][1]-1 > 0 and energizeMap_left[item[1][0]][item[1][1]-1] == "#"):
                                Q.put((item[0]+1, (item[1][0], item[1][1]-1, dir)))
                        case "down":
                            if not (item[1][0]+1 < 109 and energizeMap_down[item[1][0]+1][item[1][1]] == "#"):
                                Q.put((item[0]+1, (item[1][0]+1, item[1][1], dir)))
                        case "up":
                            if not (item[1][0]-1 > 0 and energizeMap_up[item[1][0]-1][item[1][1]] == "#"):
                                Q.put((item[0]+1, (item[1][0]-1, item[1][1], dir)))
                case "/":
                    match dir:
                        case "right":
                            if not (item[1][0]-1 > 0 and energizeMap_up[item[1][0]-1][item[1][1]] == "#"):
                                Q.put((item[0]+1, (item[1][0]-1, item[1][1], "up")))
                        case "left":
                            if not (item[1][0]+1 < 109 and energizeMap_down[item[1][0]+1][item[1][1]] == "#"):
                                Q.put((item[0]+1, (item[1][0]+1, item[1][1], "down")))
                        case "down":
                            if not (item[1][1]-1 > 0 and energizeMap_left[item[1][0]][item[1][1]-1] == "#"):
                                Q.put((item[0]+1, (item[1][0], item[1][1]-1, "left")))
                        case "up":
                            if not (item[1][1]+1 < 109 and energizeMap_right[item[1][0]][item[1][1]+1] == "#"):
                                Q.put((item[0]+1, (item[1][0], item[1][1]+1, "right")))
                case '\\':
                    match dir:
                        case "right":
                            if not (item[1][0]+1 < 109 and energizeMap_down[item[1][0]+1][item[1][1]] == "#"):
                                Q.put((item[0]+1, (item[1][0]+1, item[1][1], "down")))
                        case "left":
                            if not (item[1][0]-1 > 0 and energizeMap_up[item[1][0]-1][item[1][1]] == "#"):
                                Q.put((item[0]+1, (item[1][0]-1, item[1][1], "up")))
                        case "down":
                            if not (item[1][1]+1 < 109 and energizeMap_right[item[1][0]][item[1][1]+1] == "#"):
                                Q.put((item[0]+1, (item[1][0], item[1][1]+1, "right")))
                        case "up":
                            if not (item[1][1]-1 > 0 and energizeMap_left[item[1][0]][item[1][1]-1] == "#"):
                                Q.put((item[0]+1, (item[1][0], item[1][1]-1, "left")))
                
                case "-":
                    match dir:
                        case "right":
                            if not (item[1][1]+1 < 109 and energizeMap_right[item[1][0]][item[1][1]+1] == "#"):
                                Q.put((item[0]+1, (item[1][0], item[1][1]+1, dir)))
                        case "left":
                            if not (item[1][1]-1 > 0 and energizeMap_left[item[1][0]][item[1][1]-1] == "#"):
                                Q.put((item[0]+1, (item[1][0], item[1][1]-1, dir)))
                        case "down":
                            if not (item[1][1]-1 > 0 and energizeMap_left[item[1][0]][item[1][1]-1] == "#"):
                                Q.put((item[0]+1, (item[1][0], item[1][1]-1, "left")))
                            if not (item[1][1]+1 < 109 and energizeMap_right[item[1][0]][item[1][1]+1] == "#"):
                                Q.put((item[0]+1, (item[1][0], item[1][1]+1, "right")))
                        case "up":
                            if not (item[1][1]-1 > 0 and energizeMap_left[item[1][0]][item[1][1]-1] == "#"):
                                Q.put((item[0]+1, (item[1][0], item[1][1]-1, "left")))
                            if not (item[1][1]+1 < 109 and energizeMap_right[item[1][0]][item[1][1]+1] == "#"):
                                Q.put((item[0]+1, (item[1][0], item[1][1]+1, "right")))

                case "|":
                    match dir:
                        case "right":
                            if not (item[1][0]+1 < 109 and energizeMap_down[item[1][0]+1][item[1][1]] == "#"):
                                Q.put((item[0]+1, (item[1][0]+1, item[1][1], "down")))
                            if not (item[1][0]-1 > 0 and energizeMap_up[item[1][0]-1][item[1][1]] == "#"):
                                Q.put((item[0]+1, (item[1][0]-1, item[1][1], "up")))
                        case "left":
                            if not (item[1][0]+1 < 109 and energizeMap_down[item[1][0]+1][item[1][1]] == "#"):
                                Q.put((item[0]+1, (item[1][0]+1, item[1][1], "down")))
                            if not (item[1][0]-1 > 0 and energizeMap_up[item[1][0]-1][item[1][1]] == "#"):    
                                Q.put((item[0]+1, (item[1][0]-1, item[1][1], "up")))
                        case "down":
                            if not (item[1][0]+1 < 109 and energizeMap_down[item[1][0]+1][item[1][1]] == "#"):
                                Q.put((item[0]+1, (item[1][0]+1, item[1][1], dir)))
                        case "up":
                            if not (item[1][0]-1 > 0 and energizeMap_up[item[1][0]-1][item[1][1]] == "#"):
                                Q.put((item[0]+1, (item[1][0]-1, item[1][1], dir)))

        count = 0

        for i in energizeMap:
            for j in i: 
                if j == "#":
                    count += 1

        if count > max:
            max = count
            print(max)
