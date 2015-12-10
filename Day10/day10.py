import sys

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
    for i in range(1, (len(string))):
        if not string[i] == currentChar:
            returnString += str(count) + str(currentChar)
            currentChar = string[i]
            count = 1
        else:
            count += 1

    returnString += str(count) + str(currentChar)
    return returnString

for i in range(0, 50):
    content = playGame(content)

print len(content)
