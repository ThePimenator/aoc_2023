import queue
import numpy as np

input = open('input.txt', 'r')
output = open('output.txt', 'w')
inputLines = input.readlines()

rules = {}
inputSymbols = []

inputRules = True

for i in inputLines:
    if i == "\n": 
        inputRules = False
    elif inputRules:
        # rule = [i.split("{")[0]]
        # rule.append([x.split(":") for x in i.split("{")[1].split("}")[0].split(",")])
        rule = {i.split("{")[0]:[x.split(":") for x in i.split("{")[1].split("}")[0].split(",")]}
        rules.update(rule)
    else:
        symbol = i[1:-2].split(",")
        symbol = {x[0]:int(x[2:]) for x in symbol}
        inputSymbols.append(symbol)


for i in rules:
    print(i)

sum = 0

for i in inputSymbols:
    state = "in"
    while not state in ["A", "R"]:
        for j in rules[state]:
            if len(j) == 1:
                state = j[0]
            elif j[0][1] == ">":
                if i[j[0][0]] > int(j[0][2:]):
                    state = j[1]
                    break
            elif j[0][1] == "<":
                if i[j[0][0]] < int(j[0][2:]):
                    state = j[1]
                    break
        print(state)
    if state == "A":
        sum += (i["x"]+i["m"]+i["a"]+i["s"])

print(sum)