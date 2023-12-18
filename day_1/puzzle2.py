# writing to file
from curses.ascii import isdigit


input = open('input.txt', 'r')
inputLines = input.readlines()

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

sum = 0
# Strips the newline character
for line in inputLines:

    digit = ""

    for i in range(len(line)):
        if line[i].isdigit(): 
            if digit == "":
                digit = line[i]
            lastDigit = line[i]
        if i + 3 < len(line):
            if line[i : i + 3] == "one": 
                if digit == "":
                    digit = "1"
                lastDigit = "1"
            if line[i : i + 3] == "two": 
                if digit == "":
                    digit = "2"
                lastDigit = "2"
            if line[i : i + 3] == "six": 
                if digit == "":
                    digit = "6"
                lastDigit = "6"
        if i + 4 < len(line):   
            if line[i : i + 4] == "four": 
                if digit == "":
                    digit = "4"
                lastDigit = "4"
            if line[i : i + 4] == "five": 
                if digit == "":
                    digit = "5"
                lastDigit = "5"
            if line[i : i + 4] == "nine": 
                if digit == "":
                    digit = "9"
                lastDigit = "9"
        if i + 5 < len(line):
            if line[i : i + 5] == "three":     
                if digit == "":
                    digit = "3"       
                lastDigit = "3"            
            if line[i : i + 5] == "seven": 
                if digit == "":
                    digit = "7"
                lastDigit = "7"
            if line[i : i + 5] == "eight": 
                if digit == "":
                    digit = "8"
                lastDigit = "8"

    digit += lastDigit


    sum += int(digit)

print(sum)

