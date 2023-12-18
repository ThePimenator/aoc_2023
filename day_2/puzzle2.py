
input = open('input.txt', 'r')
inputLines = input.readlines()

sum = 0 

for line in inputLines:
    # Get the number of the game and the grabs
    number, games = line.split(":")
    gameNr = int(number.split(" ")[1])
    games = games.split(";")
    product = 1

    color_min = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for grab in games:
        colors = grab.split(",")
        for color in colors:
            color = color[1:].split(" ")

            color_min[color[1].rstrip()] = max(color_min[color[1].rstrip()], int(color[0]))

    for c in color_min.items():
        product = product * int(c[1])

    sum += product

print(sum)

