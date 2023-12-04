
input = open('input.txt', 'r')
inputLines = input.readlines()

sum = 0 

for line in inputLines:
    game = line.split(":")[1]
    split_game = game.strip().split("|")
    winning_numbers = [s for s in split_game[0].strip().split(" ") if s.strip()]
    own_numbers = [s for s in split_game[1].strip().split(" ") if s.strip()]
    score = 0

    for c in own_numbers:
        if c in winning_numbers and score == 0:
            score = 1
        elif c in winning_numbers:
            score *= 2
    
    sum += score

print(sum)

