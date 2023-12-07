from functools import cmp_to_key
from itertools import product

input = open('input.txt', 'r')
inputLines = input.readlines()

hands = [s.rstrip().split(" ") for s in inputLines]
input_list = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

def jokerSortValue(hand):
    value = 0 

    jokers = hand[0].count("J")
    hand_cards = hand[0].replace("J", "")
    
    if jokers == 0:
        value = sortValue(hand)
    else:
        for combo in product(input_list, repeat=jokers):
            hand_cards_new = hand_cards + "".join(combo)
            value = max(value, sortValue([hand_cards_new, hand[1]]))
    return value


def sortValue(hand): 
    hand_cards = hand[0]
    value = 0 
    table = {e:hand_cards.count(e) for e in set(hand_cards)}
    for c in table:
        match table[c]:
            case 5:
                value = 500
                break
            case 4:
                value = 400
                break
            case 3:
                for c2 in table:
                    if table[c2] == 2:
                        value = 300
                if value == 0: 
                    value = 200
            case 2: 
                for c2 in table:
                    if table[c2] == 2 and not c2 == c:
                        value = 100
                if value == 0: 
                    value = 50
    return value

def number(stringNumber):
    match stringNumber:
        case "A":
            return 14
        case "K":
            return 13
        case "Q":
            return 12
        case "J":
            return 1
        case "T": 
            return 10 
        case _:
            return int(stringNumber) 

def compare(hand1, hand2):
    if jokerSortValue(hand1) > jokerSortValue(hand2):
        return -1
    elif jokerSortValue(hand1) < jokerSortValue(hand2): 
        return 1
    else: 
        for i in range(5):
            if number(hand1[0][i]) > number(hand2[0][i]):
                return -1
            elif number(hand1[0][i]) < number(hand2[0][i]):
                return 1
    return 0    

hands = sorted(hands, key=cmp_to_key(compare))

sum = 0

for i in range(len(hands)):
    sum += int(hands[i][1])*(len(hands)-i)

print(sum)
        



