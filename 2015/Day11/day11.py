import sys
import re

if len(sys.argv) == 2:
	filename = sys.argv[1] + ".txt"
else:
	filename = "input.txt"

with open (filename, "r") as f:
    password = f.read().replace("\n", '').lower()

forbiddenLetters = ['i', 'o', 'l']

def nextChar(num):
    num += 1
    if num == 123:
        return 97
    return num

def incrementChar(char):
    nextCharNum = nextChar(ord(char))

    return chr(nextCharNum)

def incrementString(string):
    strList = list(string)
    i = len(string) - 1
    while i > 0:
        strList[i] = incrementChar(strList[i])
        if strList[i] == 'a':
            i -=1
        else:
            i = 0
    return "".join(strList)

def isAStraight(string, debug):
    if debug: print string + ": len " + str(len(string)) + ": ",

    if len(string) < 3:
        return False

    straight = True
    string = list(string)
    previous = ord(string[0])
    for i in range(1, len(string)):
        current = ord(string[i])
        if current - previous != 1:
            straight = False
        previous = current
    if debug: print straight
    return straight

def containsIncreasingStraight(string, amount, debug):
    straight = False
    for i in range(0, len(string)):
        if isAStraight(string[i:i+amount], debug):
            straight = True
    return straight

def noForbiddenLetters(string, debug):
    string = list(string)
    for i in range(0, len(string)):
        if string[i] in forbiddenLetters:
            return False
    return True

def containsTwoDifferentPairs(string, debug):
    results = re.findall(r'((\w)\2{1,})', string)
    return len(results) >= 2

def valid(password):
    if containsIncreasingStraight(password, 3, False):
        if noForbiddenLetters(password, False):
            if containsTwoDifferentPairs(password, False):
                return True
    return False


print "seed: " + password
password = incrementString(password)

while not valid(password):
    password = incrementString(password)

print
print "straight: "
containsIncreasingStraight(password, 3, True)
print "doubles: " + str(containsTwoDifferentPairs(password, True))
print "No forbiddenLetters: " + str(noForbiddenLetters(password, True))
print password
