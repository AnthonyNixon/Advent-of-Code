# Read in the input file.
with open ("input.txt", "r") as myfile:
    data=myfile.readlines()

validCount = 0
for line in data:
    sides = line.split()
    print sides
    valid = ((int(sides[0]) + int(sides[1]) > int(sides[2])) and (int(sides[1]) + int(sides[2]) > int(sides[0])) and (int(sides[0]) + int(sides[2]) > int(sides[1])))
    if valid:
        validCount += 1

print validCount
