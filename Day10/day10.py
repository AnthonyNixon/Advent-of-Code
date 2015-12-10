import sys
import itertools
import re
import json

if len(sys.argv) == 2:
	filename = sys.argv[1] + ".txt"
else:
	filename = "input.txt"

with open (filename, "r") as f:
    content = f.read().replace("\n", '')


def playGame(string):
    currentChar = string[:1]
    count = 1
    returnString = ""

    if len(string) > 1:
        for i in range(1, (len(string))):
            if not string[i] == currentChar:
                returnString += str(count) + str(currentChar)
                currentChar = string[i]
                count = 1
            else:
                count += 1

    returnString += str(count) + str(currentChar)
    return returnString




numIterations = 50

string = content

for i in range(0, numIterations):
    # print string
    # print
    string = playGame(string)

print string
print len(string)
