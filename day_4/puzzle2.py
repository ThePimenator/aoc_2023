
input = open('input.txt', 'r')
inputLines = input.readlines()
amount_process = [1]*len(inputLines)

for line in inputLines:
    card_number = int([s for s in line.split(":")[0].split(" ") if s.strip()][1])
    game = line.split(":")[1]
    split_game = game.strip().split("|")
    winning_numbers = [s for s in split_game[0].strip().split(" ") if s.strip()]
    own_numbers = [s for s in split_game[1].strip().split(" ") if s.strip()]
    print("Processing card: " + str(card_number))

    for i in range(amount_process[card_number-1]):
        score = 0
        for c in own_numbers:
            if c in winning_numbers:
                score += 1
        for j in range(score):
            amount_process[card_number + j] += 1
print(sum(amount_process))

