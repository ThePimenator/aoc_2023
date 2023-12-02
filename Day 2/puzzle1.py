
input = open('input.txt', 'r')
inputLines = input.readlines()

color_max = {
    "red": 12,
    "green": 13,
    "blue": 14

}

sum = 0 

for line in inputLines:
    # Get the number of the game and the grabs
    number, games = line.split(":")
    gameNr = int(number.split(" ")[1])
    games = games.split(";")

    possible = True

    for grab in games:
        colors = grab.split(",")
        for color in colors:
            color = color[1:].split(" ")
            if (color_max[color[1].rstrip()] < int(color[0])):
                possible = False
                break

    if possible: 
        sum += gameNr

print(sum)

