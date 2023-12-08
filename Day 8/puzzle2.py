input = open('input.txt', 'r')
inputLines = input.readlines()

directions = inputLines[0].strip()
nodes = [s.strip() for s in inputLines[2:]]
nodes_c = [s.replace("=", "").replace("(", "").replace(")", "").replace(",", "").split(" ") for s in nodes]
table_nodes = {c[0] + "L":c[2] for c in nodes_c}
table_nodes.update({c[0] + "R":c[3] for c in nodes_c})

current_nodes = [c[0] for c in nodes_c if c[0][2] == "A"]

p = 0
steps = 0
last_steps = [0,0,0,0,0,0]

while True:
    for i in range(len(current_nodes)):
        current_nodes[i] =  table_nodes[current_nodes[i] + directions[p]]
    # print(directions[p])
        if current_nodes[i][2] == "Z":
            print("i = " + str(i) + " -- " + str(steps - last_steps[i]))
            last_steps[i] = steps
    if p == len(directions)-1:
        p = 0
    else: 
        p += 1
    steps += 1
    
# just take LCM from print result nodes
# i = 0 -- 19631
# i = 2 -- 21389
# i = 1 -- 13771
# i = 3 -- 17287
# i = 5 -- 20803
# i = 4 -- 23147

