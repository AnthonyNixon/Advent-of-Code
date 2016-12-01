import sys
import itertools
import re
import json

if len(sys.argv) == 2:
	filename = sys.argv[1] + ".txt"
else:
	filename = "input.txt"

with open (filename, "r") as f:
    content = f.readlines()

addedName = False


addNames = ['ajn0592']
names = []

if len(addNames) > 0:
    addedNames = True


deltaLookup = {}

def evalTable(seating):
    # seating.insert(0, seating[-1])
    numPeople = len(seating)
    happiness = 0

    for i in range(0, numPeople):
        happiness += deltaLookup[seating[i]][seating[i-1]]
        if i < (numPeople - 1):
            happiness += deltaLookup[seating[i]][seating[i+1]]
        else:
            happiness += deltaLookup[seating[i]][seating[0]]

    return happiness


for line in content:
    matchObj = re.match(r'(.+) would (.+) (\d+) happiness units by sitting next to (.+)\.', line)
    name = matchObj.group(1)
    effect = matchObj.group(2)
    amount = int(matchObj.group(3))
    affectingName = matchObj.group(4)

    print matchObj.group(1) + " + " + matchObj.group(4) + " = " + matchObj.group(2) + " " + matchObj.group(3)

    if name not in names:
        names.append(name)

    if name not in deltaLookup:
        deltaLookup[name] = {}


    if effect == 'gain':
	    deltaLookup[name][affectingName] = amount
    elif effect == 'lose':
        deltaLookup[name][affectingName] = -1 * amount

if addedNames:
    for name in names:
        for addName in addNames:
            if addName not in deltaLookup:
                deltaLookup[addName] = {}

            deltaLookup[name][addName] = 0
            deltaLookup[addName][name] = 0

    for name in addNames:
        names.append(name)

print names
print deltaLookup

bestHappiness = 0
bestSeatingChart = []
tableHappiness = 0


permutations = list(itertools.permutations(names))
for seatingChart in permutations:
    tableHappiness = evalTable(list(seatingChart))
    if tableHappiness > bestHappiness:
        bestHappiness = tableHappiness
        bestSeatingChart = list(seatingChart)

print "Best: " + str(bestSeatingChart) + ": " + str(bestHappiness)
