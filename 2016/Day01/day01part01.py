import re

# Read in the input file.
with open ("input.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')

# Split the data read in into a list delimited by commas.
instructions = data.split(',')

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # Direction Vectors for North, South, East, WEst
currentDirectionIndex = 0
currentLocation = [0, 0]

for instruction in instructions:
    # Change the direction based on the instruction
    if 'R' in instruction:
        currentDirectionIndex += 1
    else: currentDirectionIndex -= 1

    # Fix out of bounds issues
    if currentDirectionIndex < 0:
        currentDirectionIndex = 3
    elif currentDirectionIndex > 3:
        currentDirectionIndex = 0


    amount = re.findall(r'\d+', instruction)
    amount = int(amount[0])

    currentLocation[0] += (directions[currentDirectionIndex][0] * amount)
    currentLocation[1] += (directions[currentDirectionIndex][1] * amount)

    print abs(currentLocation[0]) + abs(currentLocation[1])
