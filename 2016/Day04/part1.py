import re

# Read in the input file.
with open ("input.txt", "r") as myfile:
    data=myfile.readlines()

def makeChecksum(countLookup):
    count = max(countLookup.keys(), key=int)
    checksumArray = []
    while count > 0:
        for letter in countLookup[count]:
            checksumArray.append(letter)
        count -= 1
    return "".join(checksumArray[:5])

validSum = 0
for line in data:
    letterDict = {}
    countLookup = {1: []}
    print line
    matchGroup = re.match('(.+?)-(\d+?)\[(.+?)\]', line)
    letters = matchGroup.group(1).replace('-', '')
    numbers = int(matchGroup.group(2))
    checksum = matchGroup.group(3)

    print "letters: " + letters
    print "numbers: " + str(numbers)
    print "checksum: " + checksum

    for letter in letters:
        if letter in letterDict:
            letterDict[letter] += 1
            letterCount = letterDict[letter]
            countLookup[letterCount - 1].remove(letter)
            if letterCount not in countLookup:
                countLookup[letterCount] = []
            countLookup[letterCount].append(letter)
            countLookup[letterCount].sort()
        else:
            letterDict[letter] = 1
            countLookup[1].append(letter)
            countLookup[1].sort()
    print letterDict
    print countLookup
    if makeChecksum(countLookup) == checksum:
        validSum += numbers
print validSum
