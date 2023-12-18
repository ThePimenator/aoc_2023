input = open('input.txt', 'r')
inputLines = [s for s in input.readlines()][0].split(",")

sum = 0 

for hash in inputLines:
    hashValue = 0
    for j in hash:
        hashValue += ord(j)
        hashValue *= 17
        hashValue %= 256
    sum += hashValue

print(sum)