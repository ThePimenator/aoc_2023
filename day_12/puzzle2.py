from functools import lru_cache

input = open('input.txt', 'r')
inputLines = [s.strip() for s in input.readlines()]

springLines = []
springNumber = []

times_sat = 0

for i in inputLines:
    inputLines_i = i.split(" ")
    springLines.append(inputLines_i[0])
    springNumber.append([int(s) for s in inputLines_i[1].split(",")])

@lru_cache
def recursiveFill(str, numbers):
    if len(str) == 0:
        if len(numbers) == 0:
            return 1
        else: 
            return 0
    
    # irrelevant information 
    if str.startswith("."):
        return recursiveFill(str.strip("."), numbers)
    
    # recurse on both sides for ?
    if str.startswith("?"):
        return recursiveFill(str.replace("?", ".", 1), numbers) + recursiveFill(str.replace("?", "#", 1), numbers)

    # This can be deciding
    if str.startswith("#"):
        # not possible 
        if len(numbers) == 0 or len(str) < numbers[0]:
            return 0
        if "." in str[0:numbers[0]]:
            return 0
        if len(numbers) > 1:
            if len(str) < numbers[0] + 1 or str[numbers[0]] == "#":
                return 0
            return recursiveFill(str[numbers[0] + 1:], numbers[1:])
        else:
            return recursiveFill(str[numbers[0]:], numbers[1:])
    

for i in range(len(springNumber)):
    springLines[i] = '?'.join([springLines[i]] * 5)
    springNumber[i] = 5*springNumber[i]

    print(i)
    times_sat += recursiveFill(springLines[i], tuple(springNumber[i]))

print(times_sat)