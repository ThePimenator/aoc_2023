
input = open('input.txt', 'r')
inputLines = [s.strip() for s in input.readlines()]

springLines = []
springNumber = []

times_sat = 0

for i in inputLines:
    inputLines_i = i.split(" ")
    springLines.append(inputLines_i[0])
    springNumber.append([int(s) for s in inputLines_i[1].split(",")])

def satisfySpring(str, numbers):
    sequences = [s for s in str.split(".") if s]
    if not len(sequences) == len(numbers):
        return 0
    for i in range(len(sequences)):
        if not len(sequences[i]) == numbers[i]:
            return 0

    return 1

def recursiveFill(str, numbers, index, output):
    sat = 0
    if index == len(str):
        sat += satisfySpring(output, numbers)
    elif str[index] != "?": 
        sat += recursiveFill(str, numbers, index+1, output + str[index])
    else: 
        sat += recursiveFill(str, numbers, index+1, output + "#")
        sat += recursiveFill(str, numbers, index+1, output + ".")

    return sat
    

for i in range(len(springNumber)):
    print(i)
    print(springLines[i], springNumber[i])
    print(recursiveFill(list(springLines[i]), springNumber[i], 0, ""))
    times_sat += recursiveFill(list(springLines[i]), springNumber[i], 0, "")

print(times_sat)