import sys

if len(sys.argv) == 2:
	filename = sys.argv[1] + ".txt"
else:
	filename = "input.txt"

with open (filename, "r") as f:
    content = f.readlines()

niceStringCount = 0

vowels = ['a', 'e', 'i', 'o', 'u']
badStrings = ['ab', 'cd', 'pq', 'xy']

def isNiceString(string):
	
	numVowels = 0
	for char in string:
		if char in vowels:
			numVowels += 1
	if numVowels < 3:
		return False
	
	
	
	hasMatch = False
	for i in range(0, (len(string) - 1)):
		if string[i] == string[i+1]:
			hasMatch = True
	if not hasMatch:
		return False
		
	numVowels = 0
	for char in string:
		if char in vowels:
			numVowels += 1
	if numVowels < 3:
		return False
		
		
	for badString in badStrings:
		if badString in string:
			return False
	
	return True

for i in range(0, len(content)):
	line = content[i]
	line = line.replace('\n', '')
	
	if isNiceString(line):
		niceStringCount += 1
		
print niceStringCount