input = open('input.txt', 'r')
inputLines = input.readlines()

product = 1 

times = [int(s) for s in inputLines[0].rstrip().split(" ")[1:] if s]
distance = [int(s) for s in inputLines[1].rstrip().split(" ")[1:] if s]


for t in range(len(times)):
    sum = 0
    for t_try in range(times[t]+1):
        t_left = times[t] - t_try
        speed = t_try 
        distance_try = speed*t_left

        if distance[t] < distance_try:
            sum += 1
    
    product *= sum
    print(sum)
    sum = 0

print(product)

        



