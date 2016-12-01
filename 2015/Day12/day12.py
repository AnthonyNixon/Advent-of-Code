import sys
import re
import json

if len(sys.argv) == 2:
	filename = sys.argv[1] + ".txt"
else:
	filename = "input.txt"

with open (filename, "r") as f:
    content = f.read().replace("\n", '')

ignoreTerms = []

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def containsIgnoreTerm(content):
    keyType = type(content)

    for term in content:
        if keyType is list:
            if term.lower() in ignoreTerms:
                return True
        if keyType is dict:
            if content[term] in ignoreTerms:
                return True
    return False


def parseList(content):
    for item in content:
        parse(item)

def parseDict(content):
    for item in content:
        if not containsIgnoreTerm(content):
            parse(content[item])


def parse(content):
    keyType = type(content)

    if keyType is list:
        parseList(content)
    elif keyType is dict:
        parseDict(content)
    elif keyType is str:
        if RepresentsInt(content):
            numbers.append(int(content))
    elif keyType is int:
        numbers.append(content)
    else:
        print "IDK WTF this is:" + str(keyType) + "\n\t" + content + "\n"



jsonContent = json.loads(content)
numbers = []

for key in jsonContent:
    parse(jsonContent[key])


print numbers
print sum(numbers)
