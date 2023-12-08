input = open('input.txt', 'r')
inputLines = input.readlines()

directions = inputLines[0].strip()
nodes = [s.strip() for s in inputLines[2:]]
nodes_c = [s.replace("=", "").replace("(", "").replace(")", "").replace(",", "").split(" ") for s in nodes]
table_nodes = {c[0] + "L":c[2] for c in nodes_c}
table_nodes.update({c[0] + "R":c[3] for c in nodes_c})
print(table_nodes)

current_node = "AAA"
p = 0
steps = 0

while current_node != "ZZZ":
    current_node =  table_nodes[current_node + directions[p]]
    print(directions[p])
    if p == len(directions)-1:
        p = 0
    else: 
        p += 1
    steps += 1
    print(current_node)


print(steps)