import sys
import itertools

if len(sys.argv) == 2:
	filename = sys.argv[1] + ".txt"
else:
	filename = "input.txt"

with open (filename, "r") as f:
    content = f.readlines()

niceStringCount = 0

vowels = ['a', 'e', 'i', 'o', 'u']
badStrings = ['ab', 'cd', 'pq', 'xy']

def isNiceStringV1(string):
	
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

def containsDuplicateTwoLetterCombo(string):
	for i in range(0, (len(string) - 1)):
		testString = (string[i] + string[i+1])
		remainder = string[:i] + "-" + string[(i+2):]
		
		#print testString + "\t" + remainder
		if testString in remainder:
			return testString
	return False
	
def containsDuplicateWithMiddleLetter(string):
	for i in range(0, (len(string) - 2)):
		if string[i] == string[i+2]:
			return string[i:i+3]
	return False
	
def isNiceStringV2(string):
	
	if containsDuplicateTwoLetterCombo(string) and containsDuplicateWithMiddleLetter(string):
		print string + "\t",
		print str(containsDuplicateTwoLetterCombo(string)) + " " + str(containsDuplicateWithMiddleLetter(string))
	return containsDuplicateTwoLetterCombo(string) and containsDuplicateWithMiddleLetter(string)

	

for i in range(0, len(content)):
	line = content[i]
	line = line.replace('\n', '')
	
	if isNiceStringV2(line):
		niceStringCount += 1
		print niceStringCount
		
print niceStringCount