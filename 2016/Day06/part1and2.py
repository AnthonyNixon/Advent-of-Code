# Read in the input file.
with open ("input.txt", "r") as myfile:
    data=myfile.readlines()

lineLen = 0
positionLookup = {}

for line in data:
    line = line.replace('\n', '')
    lineLen = len(line)
    print line
    for i in range(lineLen):
        if i not in positionLookup:
            positionLookup[i] = {line[i]: 1}
        elif line[i] not in positionLookup[i]:
            positionLookup[i][line[i]] = 1
        else:
            positionLookup[i][line[i]] += 1
            
string1 = []
string2 = []
for i in range(lineLen):
    string1.append(str(max(positionLookup[i], key=positionLookup[i].get)))
    string2.append(str(min(positionLookup[i], key=positionLookup[i].get)))
print "".join(string1)
print "".join(string2)
