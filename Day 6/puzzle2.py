input = open('input.txt', 'r')
inputLines = input.readlines()

product = 1 

times_concat = int("".join([s for s in inputLines[0].rstrip().split(" ")[1:] if s]))
distance_concat = int("".join([s for s in inputLines[1].rstrip().split(" ")[1:] if s]))

sum = 0
for t in range(times_concat+1):
    t_left = times_concat - t
    speed = t 
    distance_try = speed*t_left

    if distance_concat < distance_try:
        sum += 1

print(sum)

        



