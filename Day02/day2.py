import itertools

with open("input.txt") as f:
    content = f.readlines()
	
totalNeeded = 0
totalRibbon = 0

for i in range(0, len(content)):
	line = content[i]
	line = line.replace('\n', '')
	
	print str(i) + ": " + line,
	parts = sorted([int(n) for n in line.split('x')])
	print parts
	combinations = list(itertools.combinations(parts, 2))
	
	comboNeeded = 0
	for combination in combinations:
		print "2*" + str(combination[0] * combination[1]) + " (" + str(combination[0]) + "*" + str(combination[1]) + ")\t",
		comboNeeded += 2 * combination[0] * combination[1]
	comboNeeded += combinations[0][0] * combinations[0][1]
	
	ribbonNeeded = ((parts[0] * 2) + (parts[1] * 2))
	ribbonNeeded += (parts[0] * parts[1] * parts[2])
	
	print "\t=" + str(comboNeeded) + "\tRibbon=" + str(ribbonNeeded) + "\n"
	totalNeeded += comboNeeded
	totalRibbon += ribbonNeeded

print str(totalNeeded) + ", ribbon = " + str(totalRibbon)