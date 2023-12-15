input = open('input.txt', 'r')
inputLines = [s for s in input.readlines()][0].split(",")
boxes = [None]*256

for hash in inputLines:
    if "=" in hash:
        label, value = hash.split("=")
        value = int(value)
    else:
        label = hash[:len(hash)-1]
        value = -1

    labelHash = 0

    for j in label:
        labelHash += ord(j)
        labelHash *= 17
        labelHash %= 256

    if value > 0:
        if boxes[labelHash] == None:
            boxes[labelHash] = [(label, value)]
        else:
            present = -1
            for i in range(len(boxes[labelHash])):
                if boxes[labelHash][i][0] == label:
                    present = i
                    break

            if present >= 0:
                boxes[labelHash][present] = (label, value) 
            else: 
                boxes[labelHash].append((label, value))
    else:
        if boxes[labelHash] != None:
            for (x,y) in boxes[labelHash]:
                if x == label:
                    boxes[labelHash].remove((x,y))
                    break

sum = 0

for b in range(len(boxes)):
    if boxes[b] != None:
        for l in range(len(boxes[b])):
            sum += ((b+1)*(l+1)*boxes[b][l][1])
            
print(sum)
