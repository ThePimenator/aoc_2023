from curses.ascii import isdigit


input = open('input.txt', 'r')
inputLines = input.readlines()

sum = 0
for line in inputLines:

    for i in line:
        if i.isdigit(): 
            digit = i
            break
    
    for i in reversed(line):
        if i.isdigit(): 
            digit += i
            break

    sum += int(digit)

print(sum)

