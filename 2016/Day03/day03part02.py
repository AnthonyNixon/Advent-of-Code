# Read in the input file.
with open ("input.txt", "r") as myfile:
    data=myfile.readlines()

validCount = 0
i = 0
while i < len(data):
    line1 = data[i]
    line2 = data[i + 1]
    line3 = data[i + 2]

    sides1 = line1.split()
    sides2 = line2.split()
    sides3 = line3.split()

    valid1 = ((int(sides1[0]) + int(sides2[0]) > int(sides3[0])) and (int(sides1[0]) + int(sides3[0]) > int(sides2[0])) and (int(sides3[0]) + int(sides2[0]) > int(sides1[0])))
    valid2 = ((int(sides1[1]) + int(sides2[1]) > int(sides3[1])) and (int(sides1[1]) + int(sides3[1]) > int(sides2[1])) and (int(sides3[1]) + int(sides2[1]) > int(sides1[1])))
    valid3 = ((int(sides1[2]) + int(sides2[2]) > int(sides3[2])) and (int(sides1[2]) + int(sides3[2]) > int(sides2[2])) and (int(sides3[2]) + int(sides2[2]) > int(sides1[2])))

    if valid1:
        validCount += 1
    if valid2:
        validCount += 1
    if valid3:
        validCount += 1

    i += 3

print validCount
