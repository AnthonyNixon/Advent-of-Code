# Read in the input file.
with open ("input.txt", "r") as myfile:
    instructions=myfile.readlines()

keypad = [[0, 0, 1, 0, 0], [0, 2, 3, 4, 0], [5, 6, 7, 8, 9], [0, 'A', 'B', 'C', 0], [0, 0, 'D', 0, 0]]
directionLookup = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}
currentKey = [2, 0]
for instruction in instructions:
    instruction = instruction.replace('\n', '')
    for letter in instruction:
        currentKey[0] += directionLookup[letter][0]
        currentKey[1] += directionLookup[letter][1]
        if currentKey[0] < 0:
            currentKey[0] = 0
        if currentKey[0] > 4:
            currentKey[0] = 4

        if currentKey[1] < 0:
            currentKey[1] = 0
        if currentKey[1] > 4:
            currentKey[1] = 4

        if keypad[currentKey[0]][currentKey[1]] == 0:
            currentKey[0] -= directionLookup[letter][0]
            currentKey[1] -= directionLookup[letter][1]
        # print "[" + letter + " " + str(keypad[currentKey[0]][currentKey[1]]) + "]",

    print keypad[currentKey[0]][currentKey[1]]
