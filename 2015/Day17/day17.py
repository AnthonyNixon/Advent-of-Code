import sys
import itertools
import re
import json

if len(sys.argv) == 2:
    numLiters = int(sys.argv[1])
    filename = "input.txt"
elif len(sys.argv) == 3:
    numLiters = int(sys.argv[1])
    filename = sys.argv[2] + ".txt"
else:
    numLiters = 150
    filename = "input.txt"

with open (filename, "r") as f:
    # content = f.readlines()
    content = f.read().splitlines()
    for line in content:
        line = int(line),

print "Num Liters: " + str(numLiters)
print "Content: " + str(content)
content = sorted(content, key=int, reverse=True)
print "Sorted Content: " + str(content)
count = 0
contentWithKeys = []
for line in content:
    contentWithKeys.append((count, line))
    count += 1
content = contentWithKeys
print "With keys: " + str(content)

numCombinations = 0
goodCombos = []
usedContainers = []
minContainers = len(content)
minCount = 1

def getBestComboInfo(array):
    minContainers = len(content)
    minCount = 1

    for element in array:
        numContainers = len(element['used'])
        if numContainers < minContainers:
            minContainers = numContainers
            minCount = 1
        elif numContainers == minContainers:
            minCount += 1
    return (minContainers, minCount)

def convert(numList):
    s = ''.join(map(str, numList))
    return int(s)

def removeDuplicates(array):
    alreadySeen = []
    returnArray = []
    for element in array:
        indexes = sorted(element['indexes'], key=int, reverse=True)
        idNumber = convert(indexes)
        if idNumber not in alreadySeen:
            alreadySeen.append(idNumber)
            returnArray.append(element)
    return returnArray

def addNext(containers, usedContainers, usedIndexes):
    for i  in range(len(containers)):
        container = containers[i][1]
        containerId = containers[i][0]

        usedContainers.append(int(container))
        usedIndexes.append(containerId)

        if sum([int(container[1]) for container in containers]) >= (numLiters - sum(usedContainers)):
            if sum(usedContainers) < numLiters:
                addNext(containers[i+1 :], usedContainers, usedIndexes)
            elif sum(usedContainers) == numLiters:
                # print "done. " + str(usedContainers) + "\t" + str(usedIndexes)
                goodCombos.append({"used": list(usedContainers), "indexes": list(usedIndexes)})

        usedContainers.pop()
        usedIndexes.pop()

addNext(content, [], [])

print "\nResult (" + str(len(goodCombos)) + "):"
for combo in goodCombos:
    print combo

goodCombos = removeDuplicates(goodCombos)

print "\nDuplicates Removed (" + str(len(goodCombos)) + "):"
for combo in goodCombos:
    print combo

print len(goodCombos)
print getBestComboInfo(goodCombos)
