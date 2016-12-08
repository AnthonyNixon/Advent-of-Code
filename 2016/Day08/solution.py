# Read in the input file.
with open ("input.txt", "r") as myfile:
    data=myfile.readlines()

screen = []
screenX = 50
screenY = 6

def printScreen():
    count = 0
    for i in range(screenY):
        for j in range(screenX):
            if screen[i][j] == "#":
                count += 1
        print "".join(screen[i])
    print count

def rect(arg):
    x, y = arg.split('x')
    for i in range(int(y)):
        for j in range(int(x)):
            screen[i][j] = '#'

def rotateColumn(col, amount):
    col = col.split('=')
    colIndex = int(col[1])
    updatedCol = []

    for i in range(screenY):
        updatedCol.append(screen[i][colIndex])

    for i in range(int(amount)):
        updatedCol.insert(0, updatedCol.pop(screenY-1))

    for i in range(screenY):
        screen[i][colIndex] = updatedCol[i]

def rotateRow(row, amount):
    row = row.split('=')
    rowIndex = int(row[1])
    updatedRow = []

    for i in range(screenX):
        updatedRow.append(screen[rowIndex][i])

    for i in range(int(amount)):
        updatedRow.insert(0, updatedRow.pop(screenX-1))

    for i in range(screenX):
        screen[rowIndex][i] = updatedRow[i]



for i in range(screenY):
    screen.append([])
    for j in range(screenX):
        screen[i].append('.')

for instruction in data:
    instructionParts = instruction.replace('\n', '').split(' ')
    if instructionParts[0] == 'rect':
        rect(instructionParts[1])
    elif instructionParts[0] == 'rotate':
        if 'x' in instructionParts[2]:
            rotateColumn(instructionParts[2], instructionParts[4])
        elif 'y' in instructionParts[2]:
            rotateRow(instructionParts[2], instructionParts[4])

printScreen()
