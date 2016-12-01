import hashlib
import sys

if len(sys.argv) == 2:
	filename = sys.argv[1] + ".txt"
else:
	filename = "input.txt"

with open (filename, "r") as myfile:
    data=myfile.read().replace('\n', '')
	
def numberMatchesRequirements(number):
	m = hashlib.md5()
	m.update(data + str(number))
	hashVal = m.hexdigest()
	return hashVal[0:6] == '000000'
	
number = 0
while not numberMatchesRequirements(number):
	number+=1

print number

