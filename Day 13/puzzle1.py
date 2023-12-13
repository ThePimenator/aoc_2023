import numpy as np

with open("input.txt") as file:
    puzzles = file.read().strip().split("\n\n")

# print(puzzles)

def find_mirror(puzzle):
    for i in range(1, len(puzzle)):
        smallRange = min(i, len(puzzle) - i)

        if not True in (puzzle[:i][::-1][:smallRange] ^ puzzle[i:][:smallRange]):
            return i


amount = 0
# This apparently splits on newlines
for p in puzzles:
    a = np.array([[x == "#" for x in l] for l in p.split()])
    row = find_mirror(a)
    
    if not row is None: 
        amount += 100 * row        
    else: 
        amount += find_mirror(a.T)

print(amount)