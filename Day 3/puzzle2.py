
input = open('input.txt', 'r')
inputLines = input.readlines()

sum = 0 

lineNr = 0

def checkGear(x,y):
    numbers = []
    for i in range(x-1,x+2):
        for j in range(y-1, y+2):
            if inputLines[j][i].isdigit():
                l = i
                r = i

                while True:
                    if l - 1 < 0:
                        break
                    if not (inputLines[j][l-1].isdigit()):
                        break
                    l = l - 1

                while True:
                    if r + 1 >= 140 :
                        break
                    if not (inputLines[j][r+1].isdigit()):
                        break
                    r = r + 1
                nr = ""
                for ii in range(l,r+1):
                    nr += inputLines[j][ii]
                if (int(nr) not in numbers):
                    numbers.append(int(nr))
                
    if len(numbers) == 2:
        print(str(numbers[0]) + " x " + str(numbers[1]) + " = " + str(numbers[0]*numbers[1]) )
        return (numbers[0]*numbers[1])
    else:
        # print(j, i, numbers)
        return 0

for i in range(len(inputLines)):
    # Get the number of the game and the grabs
    for j in range(len(inputLines[i].rstrip())):
        if inputLines[i][j] == "*":
            sum += checkGear(j,i)


print(sum)


    