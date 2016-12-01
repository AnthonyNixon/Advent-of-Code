import sys
import itertools
import re
import json

if len(sys.argv) == 2:
    filename = sys.argv[1] + ".txt"
    debug = True
else:
    filename = "input.txt"
    debug = False

with open (filename, "r") as f:
    content = f.readlines()


print content[0]
x = int(len(content[0]) - 1) # minus one to account for the newline.
y = int(len(content)) # minus one to account for the trailing newline.
numSimulations = 100

print ({'x': x, 'y': y})

lights = [[content[i][j] for j in range(y)] for i in range(x)]
#PART TWO HERE
lights[0][0] = '#'
lights[0][y-1] = '#'
lights[x-1][0] = '#'
lights[x-1][y-1] = '#'

#END PART TWO

def printLights(array):
    for row in range(0, len(array)):
        print ''.join(array[row])


def countSurroundingLights(col, row, lights):
    numNeighborsOn = 0

    #Top Left
    if (row-1) in range(0, y):
        if (col-1) in range(0, x):
            if lights[row-1][col-1] == '#':
                numNeighborsOn += 1

    #Mid Left
    if (col-1) in range(0, x):
        if lights[row][col-1] == '#':
            numNeighborsOn += 1

    #Bottom Left
    if (row+1) in range(0, y):
        if (col-1) in range(0, x):
            if lights[row+1][col-1] == '#':
                numNeighborsOn += 1


    #Top Middle
    if (row-1) in range(0, y):
        if lights[row-1][col] == '#':
            numNeighborsOn += 1

    #Bottom Middle
    if (row+1) in range(0, y):
        if lights[row+1][col] == '#':
            numNeighborsOn += 1


    #Top Right
    if (row-1) in range(0, y):
        if (col+1) in range(0, x):
            if lights[row-1][col+1] == '#':
                numNeighborsOn += 1

    #Mid Right
    if (col+1) in range(0, x):
        if lights[row][col+1] == '#':
            numNeighborsOn += 1

    #Bottom Right
    if (row+1) in range(0, y):
        if (col+1) in range(0, x):
            if lights[row+1][col+1] == '#':
                numNeighborsOn += 1

    return numNeighborsOn

def calculateNewLightPattern():
    newLights = [['.' for j in range(y)] for i in range(x)]

    for row in range(0, len(lights)):
        for col in range(0, len(lights[row])):
            numNeighbors = countSurroundingLights(col, row, lights)
            if lights[row][col] == '#':
                if numNeighbors == 2 or numNeighbors == 3:
                    newLights[row][col] = '#'
                else:
                    newLights[row][col] = '.'
            else:
                if numNeighbors == 3:
                    newLights[row][col] = '#'

    #PART TWO HERE
    newLights[0][0] = '#'
    newLights[0][y-1] = '#'
    newLights[x-1][0] = '#'
    newLights[x-1][y-1] = '#'

    #END PART TWO

    return newLights

def copyLights(pattern):
    for row in range(0, len(lights)):
        for col in range(0, len(lights[row])):
            lights[row][col] = pattern[row][col]

def countLightsOn():
    numOn = 0
    for row in range(0, len(lights)):
        for col in range(0, len(lights[row])):
            if lights[row][col] == '#':
                numOn += 1
    return numOn


def simulate(num):
    for i in range(num):
        print
        newPattern = calculateNewLightPattern()
        copyLights(newPattern)
        printLights(lights)

print
printLights(lights)

simulate(numSimulations)
print countLightsOn()
