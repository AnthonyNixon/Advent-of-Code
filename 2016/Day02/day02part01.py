# Read in the input file.
with open ("input.txt", "r") as myfile:
    instructions=myfile.readlines()

keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
directionLookup = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

for instruction in instructions:
    currentKey = [1, 1]
    instruction = instruction.replace('\n', '')
    for letter in instruction:
        currentKey[0] += directionLookup[letter][0]
        currentKey[1] += directionLookup[letter][1]
        if currentKey[0] < 0:
            currentKey[0] = 0
        if currentKey[0] > 2:
            currentKey[0] = 2

        if currentKey[1] < 0:
            currentKey[1] = 0
        if currentKey[1] > 2:
            currentKey[1] = 2
        # print "[" + letter + " " + str(keypad[currentKey[0]][currentKey[1]]) + "]",

    print keypad[currentKey[0]][currentKey[1]]
