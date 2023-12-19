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
        rule = {i.split("{")[0]:[x.split(":") for x in i.split("{")[1].split("}")[0].split(",")]}
        rules.update(rule)
    else:
        symbol = i[1:-2].split(",")
        symbol = {x[0]:int(x[2:]) for x in symbol}
        inputSymbols.append(symbol)


for i in rules:
    print(rules[i])


def make_test(op, val):
    if op == '<':
        return lambda n: n < val
    elif op == '>':
        return lambda n: n > val
    else:
        assert(False)

def count_accepted(state, x, m, a, s):
    if state == 'A':
        return len(x) * len(m) * len(a) * len(s)
    if state == 'R':
        return 0

    rule = rules[state]

    c = 0

    for r in rule:
        if len(r) > 1:
            n_state = r[1]
            var = r[0][0]
            greater = r[0][1] == ">"
            val = int(r[0][2:])

            if greater:
                test = lambda x: x > val
            else: 
                test = lambda x: x < val

            match var: 
                case 'x':
                    n_x = tuple(filter(test, x))
                    if len(n_x) > 0:
                        c += count_accepted(n_state, n_x, m, a, s)
                    x = tuple(n for n in x if not test(n))
                case 'm':
                    n_m = tuple(filter(test, m))
                    if len(n_m) > 0:
                        c += count_accepted(n_state, x, n_m, a, s)
                    m = tuple(n for n in m if not test(n))
                case 'a':
                    n_a = tuple(filter(test, a))
                    if len(n_a) > 0:
                        c += count_accepted(n_state, x, m, n_a, s)
                    a = tuple(n for n in a if not test(n))
                case 's':
                    n_s = tuple(filter(test, s))
                    if len(n_s) > 0:
                        c += count_accepted(n_state, x, m, a, n_s)
                    s = tuple(n for n in s if not test(n))
        else:
            c += count_accepted(r[0], x, m, a, s)

    return c

answer = count_accepted('in',tuple(range(1, 4001)),tuple(range(1, 4001)),tuple(range(1, 4001)),tuple(range(1, 4001)))

print(answer)

